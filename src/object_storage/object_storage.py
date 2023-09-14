from abc import ABC, abstractmethod
from io import StringIO


class ObjectStorage(ABC):
    """
    Object storage "interface"
    """

    @abstractmethod
    def put(self, path: str, bucket: str, body: StringIO) -> None:
        """
        Puts an object in an remote object storage

        Args:
            path (str): The path of the object
            bucket (str): The name of the bucket
            body (StringIO): The file data
        """

        raise NotImplementedError
