import dotenv
import dataclasses



@dataclasses.dataclass
class Settings:
    POSTGRES_HOST: str
    POSTGRES_PORT: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DATABASE: str

    @staticmethod
    def create(file_name: str = ".env") -> "Settings":
        data = dotenv.dotenv_values(file_name)

        return Settings(**data)  # type: ignore[arg-type]

        

