from litestar import di
import typing

import litestar
from app import services
from app import repository
from app import settings 

class App:
    containers = [
        repository.Container(),
        services.Container(),
        settings.Container(),
    ]
    __depends: typing.Dict[str, di.Provide] = {}
    def register_depends(self):
        """Регистрация новой зависимости"""
        for container in self.containers:
            self.__depends.update(container())
    
    def get_application(self):
        self.register_depends()
        app = litestar.Litestar()
        app.dependencies.update(self.__depends)
        return app
    
    def register_resource(self):
        """Добавляет ресурс который нужно запутстить на старте и завершить при окончании работы"""
        pass

