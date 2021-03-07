import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def get_application() -> FastAPI:
    application = FastAPI(title="saveddit", debug=True, version="0.1.0")

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


@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Hello API Endpoint"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
