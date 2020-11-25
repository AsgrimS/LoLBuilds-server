To create migration run:
PYTHONPATH=. alembic revision --autogenerate

To migrate run:
PYTHONPATH=. alembic upgrade head

Create .env file with:
DATABASE_URL = {driver}://{user}:{pass}@{localhost:PORT}/{dbname}
