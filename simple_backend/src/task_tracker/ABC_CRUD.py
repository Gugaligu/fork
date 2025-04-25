from abc import ABC, abstractmethod


class BaseCRUD(ABC):
    @abstractmethod
    def get(self,*args,**kwargs):
        pass

    @abstractmethod
    def create(self,*args,**kwargs):
        pass

    @abstractmethod
    def update(self,*args,**kwargs):
        pass

    @abstractmethod
    def delete(self,*args,**kwargs):
        pass
