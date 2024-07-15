from fastapi import Depends, HTTPException, status
from fastapi.routing import APIRouter
from punq import Container

from application.api.claims.schemas import (
    CreateClaimRequestSchema,
    CreateClaimResponseSchema,
)
from application.api.schemas import ErrorSchema
from domain.exceptions.base import ApplicationException
from logic.commands.claims import CreateClaimCommand
from logic.init import init_container
from logic.mediator import Mediator


router = APIRouter(tags=["Claim"])


@router.post(
    "/",
    response_model=CreateClaimResponseSchema,
    status_code=status.HTTP_201_CREATED,
    description="Create new claim",
    responses={
        status.HTTP_201_CREATED: {"model": CreateClaimResponseSchema},
        status.HTTP_400_BAD_REQUEST: {"model": ErrorSchema},
    },
)
async def create_claim_handler(
    schema: CreateClaimRequestSchema, container: Container = Depends(init_container)
):
    """Create new claim"""
    mediator = container.resolve(Mediator)

    try:
        claim, *_ = await mediator.handle_command(
            CreateClaimCommand(
                title=schema.title,
                message=schema.message,
                username=schema.username,
                email=schema.email,
                status=schema.email,
            )
        )
    except ApplicationException as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail={"error": exc.message}
        )

    return CreateClaimResponseSchema.from_entity(claim=claim)
