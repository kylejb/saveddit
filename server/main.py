import uvicorn

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.api_v1.routers.auth import auth_router
from api.api_v1.routers.users import users_router
from core.auth import get_current_user

# temporary mechanism for migrations
# models.Base.metadata.create_all(bind=engine)


def get_application() -> FastAPI:
    application = FastAPI(
        title="saveddit", version="0.1.0", docs_url="/api/docs", openapi_url="/api"
    )

    origins = ["http://localhost:3000", "http://localhost"]

    application.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return application


app = get_application()


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
