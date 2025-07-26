from abc import ABC, abstractmethod
from datetime import datetime
import uuid

class CloudResource(ABC):
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
    def terminate(self):
        pass

    def info(self):
        return {
            "id": self._id,
            "name": self._name,
            "created_at": self._created_at.strftime("%Y-%m-%d %H:%M:%S")
        }

    def __str__(self):
        return f"{self.__class__.__name__}<{self._name}, {self._id}>"

class EC2Instance(CloudResource):
    def __init__(self, name, instance_type='t2.micro'):
        super().__init__(name)
        self.__instance_type = instance_type
        self.__state = 'stopped'

    def start(self):
        if self.__state == 'running':
            raise RuntimeError(f"{self._name} is already running.")
        self.__state = 'running'
        print(f"{self._name} is starting...")

    def stop(self):
        if self.__state == 'stopped':
            raise RuntimeError(f"{self._name} is already stopped.")
        self.__state = 'stopped'
        print(f"{self._name} is stopping...")

    def terminate(self):
        self.__state = 'terminated'
        print(f"{self._name} has been terminated.")

    def get_state(self):
        return self.__state

    def set_instance_type(self, instance_type):
        if self.__state == 'running':
            raise ValueError("Cannot change instance type while running.")
        self.__instance_type = instance_type

    def get_instance_type(self):
        return self.__instance_type

    def __repr__(self):
        return f"EC2Instance(name={self._name}, type={self.__instance_type}, state={self.__state})"

class EC2Manager:
    def __init__(self):
        self.instances = []

    def create_instance(self, name, instance_type='t2.micro'):
        instance = EC2Instance(name, instance_type)
        self.instances.append(instance)
        print(f"Created instance: {instance}")
        return instance

    def list_instances(self):
        return [i.info() for i in self.instances if i.get_state() != 'terminated']

    @staticmethod
    def help():
        print("Use `create_instance`, `start`, `stop`, `terminate`, and `list_instances` methods.")

# Usage example (You can move this to test_ec2_manager.py)
if __name__ == "__main__":
    manager = EC2Manager()
    i1 = manager.create_instance("web-server")
    i2 = manager.create_instance("db-server", instance_type="t2.large")

    i1.start()
    print(i1.get_state())

    i1.stop()
    print(i1.get_state())

    print(manager.list_instances())
    EC2Manager.help()