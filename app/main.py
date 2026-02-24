from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.database import create_tables_database
from app.routes import user_routes

@asynccontextmanager
async def lifespan(app:FastAPI):
    create_tables_database()
    yield

app = FastAPI(lifespan = lifespan)
app.include_router(user_routes.router)





