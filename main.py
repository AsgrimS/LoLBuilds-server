from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from builds.routes import router as builds_router
from items.routes import router as items_router
from users.routes import router as users_router

app = FastAPI()

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(builds_router, tags=["builds"])
app.include_router(items_router, prefix="/items", tags=["items"])
app.include_router(users_router, prefix="/users", tags=["users"])
