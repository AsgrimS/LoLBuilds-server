Simple website for creating and accessing builds for LoL (league of legends).   
The main goal is to create fast, esay-to-use website where users can create/save and access builds without the hustle of scrolling through tons of content.  

I want to achieve that using FastAPI with PostgresSQL

1. To create migration run:  
`PYTHONPATH=. alembic revision --autogenerate`

2. To migrate run:  
`PYTHONPATH=. alembic upgrade head`

3. Create .env file with:  
`DB_URL = {driver}://{user}:{pass}@{localhost:PORT}/{dbname}`
