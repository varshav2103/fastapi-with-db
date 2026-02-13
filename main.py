from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.user_routes import router as user_router
from routes.ai_response_routes import router as ai_response_router
from routes.email_routes import router as email_router
from db import get_db, DATABASE_URL
from sqlalchemy import create_engine
from models import Base

app = FastAPI()

# ✅ ADD CORS HERE (IMPORTANT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # React frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Include Routers
app.include_router(user_router)
app.include_router(ai_response_router)
app.include_router(email_router)

# ✅ Create Database Tables
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

# ✅ Test Route
@app.get("/")
def read_root():
    return {"Hello": "World"}



