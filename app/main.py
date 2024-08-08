from fastapi import FastAPI
from api import battle, status, listing

app = FastAPI(title="Pokemon Battle", version="0.0.1")

app.include_router(listing.router)
app.include_router(battle.router)
app.include_router(status.router)
