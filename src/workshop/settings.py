from pydantic import BaseSettings

class Settings(BaseSettings):
    #зн-я по умолчанию
    server_host: str = '127.0.0.1'
    server_port: int = 9000
    database_url: str = "postgresql://katataolu:132565@localhost/workshop"

settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8',
)