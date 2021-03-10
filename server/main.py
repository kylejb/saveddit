from fastapi import Depends, FastAPI
from api.api_v1.routers.auth import auth_router
from api.api_v1.routers.users import users_router
from core.auth import get_current_user
import uvicorn

# temporary mechanism for migrations
# models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="saveddit",
    version="0.1.0",
    docs_url="/api/docs",
    openapi_url="/api",
)


@app.get("/api/v1")
async def root():
    return {"message": "Hellow Root"}


# Routers
app.include_router(
    users_router,
    prefix="/api/v1",
    tags=["users"],
    dependencies=[Depends(get_current_user)],
)
app.include_router(auth_router, prefix="/api", tags=["auth"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8000)
