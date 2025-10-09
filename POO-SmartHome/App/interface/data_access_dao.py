from abc import ABC, abstractmethod

class DataAccessDAO(ABC):
    @abstractmethod
    def get(self, id):
        pass

    @abstractmethod
    def get_all_data(self):
        pass

    @abstractmethod
    def create(self, object):
        pass

    @abstractmethod
    def update(self, object):
        pass

    @abstractmethod
    def delete(self, id):
        pass
    