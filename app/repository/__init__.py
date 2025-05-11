from litestar import di
from app.core import interface 
from app.repository import user_repository 


class Container(interface.BaseContainerInterface):

    @classmethod
    def get_user_repository(cls) -> user_repository.UserRepository:
        return user_repository.UserRepository()

    @classmethod
    def get_provide(cls):
        return {
            "user_repository": di.Provide(cls.get_user_repository)
        }
    
