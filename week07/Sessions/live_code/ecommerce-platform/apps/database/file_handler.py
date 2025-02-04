import json
import csv
from abc import ABC,abstractmethod
from apps.database.exceptions import CouldNotWriteIntoFileException

class BaseFileHandler(ABC):
    FILE_TYPE = None

    def __init__(self, file_path):
        self._file_path

    @abstractmethod
    def save_user_data(self, data):
        pass

    @abstractmethod
    def read_user_data(self):
        pass


class JsonFileHandler(BaseFileHandler):
    FILE_TYPE = 'json'

    def save_user_data(self, data: dict):
        try:
            serialized_data = json.dumps(data)
            with open(self._file_path, "a") as file:
                file.write(serialized_data)
            return True
        except Exception as e:
            raise CouldNotWriteIntoFileException from e

    def read_user_data(self):
        with open(self._file_path, "r") as file:
            data = file.read
            return json.loads(data)


class CsvFileHandler(BaseException):
    FILE_TYPR = 'csv'

    def save_user_data(self, data):
        with open(self._file_path, "a") as file:
            csv_writer = csv.DictWrite(file, filename = list(data.keys()))
            csv_writer.writerow(data)
            return
    
    def read_user_data(self):
        with open(self._file_path, "r") as file:
            csv_reader = csv.DictReader(list(file))
            return csv_reader