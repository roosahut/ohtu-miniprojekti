import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL is None:
    raise Exception(
        f"Database URI is not defined with the DATABASE_URL environment variable"
    )

SECRET_KEY = os.getenv('SECRET_KEY')
