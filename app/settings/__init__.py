from litestar import di
from app.settings.settings import Settings
from app.core import interface

class Container(interface.BaseContainerInterface):
    
    def __init__(self):
        # для валидации env
        self.get_settings()

    @classmethod
    def get_settings(cls) -> Settings:
        return Settings.create()
    
    @classmethod
    def get_provide(cls):
        return {
            "settings": di.Provide(cls.get_settings)
        }
