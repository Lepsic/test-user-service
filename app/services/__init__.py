import typing
from litestar import di
from app.core.interface import BaseContainerInterface
from app.services import user_service




class Container(BaseContainerInterface):

    @classmethod 
    def get_user_service(cls):
        return user_service.UserService()

    @classmethod 
    def get_provide(cls) -> typing.Dict[str, di.Provide]:
        return {
            "user_service": di.Provide(cls.get_user_service),
        }

