from abc import ABC, abstractmethod
from datetime import datetime
import uuid


class CloudStorage(ABC):
    def __init__(self, name):
        self._id = str(uuid.uuid4())
        self._name = name
        self._created_at = datetime.now()

    @abstractmethod
    def upload(self, file_name: str, content: str):
        pass

    @abstractmethod
    def delete(self, file_name: str):
        pass

    @abstractmethod
    def list_files(self):
        pass

    def metadata(self):
        return {
            'id': self._id,
            'name': self._name,
            'created_at': self._created_at.strftime("%Y-%m-%d %H:%M:%S")
        }

    def __str__(self):
        return f"{self.__class__.__name__}<{self._name}, {self._id}>"


class S3Bucket(CloudStorage):
    def __init__(self, name, region='us-east-1'):
        super().__init__(name)
        self.__region = region
        self.__files = {}

    def upload(self, file_name, content):
        if not self.validate_file_name(file_name):
            raise ValueError("Invalid file name format.")
        self.__files[file_name] = {
            'content': content,
            'timestamp': datetime.now()
        }
        print(f"Uploaded '{file_name}' to bucket '{self._name}'.")

    def delete(self, file_name):
        if file_name not in self.__files:
            raise FileNotFoundError(f"'{file_name}' not found in bucket.")
        del self.__files[file_name]
        print(f"Deleted '{file_name}' from bucket '{self._name}'.")

    def list_files(self):
        return list(self.__files.keys())

    def get_file_content(self, file_name):
        return self.__files[file_name]['content'] if file_name in self.__files else None

    @staticmethod
    def validate_file_name(file_name):
        return '.' in file_name and not file_name.startswith('.')

    @classmethod
    def from_config(cls, config: dict):
        return cls(name=config['name'], region=config.get('region', 'us-east-1'))

    def __repr__(self):
        return f"S3Bucket(name={self._name}, region={self.__region}, files={len(self.__files)})"


class S3Manager:
    def __init__(self):
        self.buckets = []

    def create_bucket(self, name, region='us-east-1'):
        bucket = S3Bucket(name, region)
        self.buckets.append(bucket)
        print(f"Created bucket: {bucket}")
        return bucket

    def list_buckets(self):
        return [bucket.metadata() for bucket in self.buckets]

    def find_bucket(self, name):
        for bucket in self.buckets:
            if bucket._name == name:
                return bucket
        raise LookupError(f"Bucket '{name}' not found.")

    @staticmethod
    def help():
        print("Use `create_bucket`, `upload`, `delete`, `list_files`, and `list_buckets` to simulate S3 operations.")


# Example usage (can move to test_s3_simulator.py)
if __name__ == "__main__":
    manager = S3Manager()
    b1 = manager.create_bucket("my-logs")
    b1.upload("log1.txt", "Log file content here...")
    b1.upload("readme.md", "This is a markdown file.")

    print("Files in bucket:", b1.list_files())
    b1.delete("log1.txt")
    print("Remaining files:", b1.list_files())

    print("All buckets:", manager.list_buckets())
    S3Manager.help()
