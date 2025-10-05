from pydantic import BaseModel
from pydantic_settings import BaseSettings
from pydantic import Field


class LoggingSettings(BaseModel):
    level: str = Field(alias="LEVEL")
    format: str = Field(alias="FORMAT")

class DataBaseSettings(BaseModel):

    url: str = Field(alias="URL")
    test_url: str = Field(alias="TEST_URL")


class BotSettings(BaseModel):

    name: str = Field(alias="NAME")
    env: str = Field(alias="ENV")
    token: str = Field(alias="TOKEN")


class Settings(BaseSettings):


    version: str = Field(alias="VERSION")
    bot: BotSettings   
    debug: bool = Field(alias="DEBUG")


    log: LoggingSettings
    database: DataBaseSettings


    class Config:
        env_file = ".env"
        env_nested_delimiter = "__"
        case_sensitive = False


settings = Settings()