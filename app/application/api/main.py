from fastapi import FastAPI
from application.api.claims.handlers import router as claim_router


def create_app() -> FastAPI:
    app = FastAPI(
        title="A Simple Claim API",
        docs_url="/api/docs",
        description="Claim API + DDD + Postgres",
        debug=True,
    )

    app.include_router(prefix="/claim", router=claim_router)
    return app
