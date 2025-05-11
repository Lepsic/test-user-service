import abc
import typing
from litestar import di


class BaseContainerInterface(abc.ABC):
    
    @abc.abstractclassmethod
    def get_provide(cls) -> typing.Dict[str, di.Provide]:
        """возвращает словарь вида нейминг сервиса - его метод"""
        pass


    @classmethod
    def __call__(cls) -> typing.Dict[str, di.Provide]:
        return cls.get_provide()


class BaseResourceInterface(abc.ABC):

    @abc.abstractmethod
    def _initial_resource(self):
        """Инициализирует ресурс"""
        pass
    def __call__(self):
        self._initial_resource()
         

class BaseAsyncResourceInterface(abc.ABC):
    
    @abc.abstractmethod
    async def _initial_resource(self):
        pass

    async def __call__(self):
        await self._initial_resource()



base_container_interface = typing.TypeVar("base_container_interface", bound=BaseContainerInterface)
