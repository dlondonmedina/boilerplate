from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str
    echo_sql: bool = True
    test: bool = False
    debug_logs: bool = False
    project_name: str = "My Boilerplate"
    oauth_token_secret: str = "my_dev_secret"


settings = Settings()  # type: ignore
