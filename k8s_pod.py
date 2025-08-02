from abc import ABC, abstractmethod
from datetime import datetime
import uuid


class K8sResource(ABC):
    def __init__(self, name):
        self._id = str(uuid.uuid4())
        self._name = name
        self._created_at = datetime.now()

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    def metadata(self):
        return {
            "id": self._id,
            "name": self._name,
            "created_at": self._created_at.strftime("%Y-%m-%d %H:%M:%S")
        }

    def __str__(self):
        return f"{self.__class__.__name__}<{self._name}, {self._id}>"


class Pod(K8sResource):
    def __init__(self, name, containers=None, namespace="default"):
        super().__init__(name)
        self.__namespace = namespace
        self.__containers = containers if containers else []
        self.__status = "Pending"

    def start(self):
        if self.__status == "Running":
            raise RuntimeError(f"Pod '{self._name}' is already running.")
        self.__status = "Running"
        print(f"Pod '{self._name}' is now Running with containers: {self.__containers}")

    def stop(self):
        if self.__status != "Running":
            raise RuntimeError(f"Pod '{self._name}' is not running.")
        self.__status = "Stopped"
        print(f"Pod '{self._name}' has been Stopped.")

    def delete(self):
        self.__status = "Deleted"
        print(f"Pod '{self._name}' has been Deleted.")

    def add_container(self, container_name):
        if not self.validate_container_name(container_name):
            raise ValueError("Invalid container name.")
        self.__containers.append(container_name)
        print(f"Added container '{container_name}' to Pod '{self._name}'.")

    def list_containers(self):
        return self.__containers

    def get_status(self):
        return self.__status

    @staticmethod
    def validate_container_name(name):
        return name.isidentifier()

    @classmethod
    def from_config(cls, config: dict):
        return cls(
            name=config["name"],
            containers=config.get("containers", []),
            namespace=config.get("namespace", "default")
        )

    def __repr__(self):
        return f"Pod(name={self._name}, namespace={self.__namespace}, status={self.__status}, containers={self.__containers})"


class K8sCluster:
    def __init__(self):
        self.pods = []

    def create_pod(self, name, containers=None, namespace="default"):
        pod = Pod(name, containers, namespace)
        self.pods.append(pod)
        print(f"Created Pod: {pod}")
        return pod

    def list_pods(self):
        return [pod.metadata() for pod in self.pods if pod.get_status() != "Deleted"]

    def find_pod(self, name):
        for pod in self.pods:
            if pod._name == name and pod.get_status() != "Deleted":
                return pod
        raise LookupError(f"Pod '{name}' not found.")

    def delete_pod(self, name):
        pod = self.find_pod(name)
        pod.delete()

    @staticmethod
    def help():
        print("Use `create_pod`, `start`, `stop`, `delete_pod`, and `list_pods` to simulate Kubernetes pod operations.")


# Example usage (can be moved to test_k8s_pod_simulator.py)
if __name__ == "__main__":
    cluster = K8sCluster()

    pod1 = cluster.create_pod("nginx-pod", ["nginx", "sidecar"])
    pod1.start()
    pod1.add_container("metrics-exporter")

    pod2 = cluster.create_pod("db-pod", ["postgres"])
    pod2.start()

    print("List of Pods:", cluster.list_pods())
    pod1.stop()
    cluster.delete_pod("db-pod")

    print("Remaining Pods:", cluster.list_pods())
    K8sCluster.help()