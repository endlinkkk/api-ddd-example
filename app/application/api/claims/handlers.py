from fastapi import Depends, HTTPException, status
from fastapi.routing import APIRouter
from punq import Container

from application.api.claims.decorators import handle_exceptions
from application.api.claims.filters import GetClaimsFilters
from application.api.claims.schemas import (
    ClaimDetailSchema,
    CreateClaimRequestSchema,
    CreateClaimResponseSchema,
    GetClaimsResponseSchema,
)
from application.api.schemas import ErrorSchema
from domain.exceptions.base import ApplicationException
from logic.commands.claims import CreateClaimCommand
from logic.init import init_container
from logic.mediator.base import Mediator
from logic.queries.claims import GetClaimQuery, GetClaimsQuery


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
@handle_exceptions
async def create_claim_handler(
    schema: CreateClaimRequestSchema, container: Container = Depends(init_container)
) -> CreateClaimResponseSchema:
    """Create new claim"""
    mediator = container.resolve(Mediator)

    claim, *_ = await mediator.handle_command(
        CreateClaimCommand(
            title=schema.title,
            message=schema.message,
            username=schema.username,
            email=schema.email,
            status=schema.status,
        )
    )

    return CreateClaimResponseSchema.from_entity(claim=claim)


@router.get(
    "/",
    response_model=GetClaimsResponseSchema,
    status_code=status.HTTP_200_OK,
    description="Get all claims",
    responses={
        status.HTTP_200_OK: {"model": GetClaimsResponseSchema},
        status.HTTP_400_BAD_REQUEST: {"model": ErrorSchema},
    },
)
@handle_exceptions
async def get_claims_handler(
    filters: GetClaimsFilters = Depends(),
    container: Container = Depends(init_container),
) -> GetClaimsResponseSchema:
    """Get all claims"""
    mediator = container.resolve(Mediator)

    claims, count = await mediator.handle_query(
        GetClaimsQuery(filters=filters.to_infra())
    )

    return GetClaimsResponseSchema(
        count=count,
        limit=filters.limit,
        offset=filters.offset,
        items=[ClaimDetailSchema.from_entity(claim) for claim in claims],
    )


@router.get(
    "/{claim_oid}",
    response_model=ClaimDetailSchema,
    status_code=status.HTTP_200_OK,
    description="Get claim by claim_id",
    responses={
        status.HTTP_200_OK: {"model": ClaimDetailSchema},
        status.HTTP_400_BAD_REQUEST: {"model": ErrorSchema},
    },
)
@handle_exceptions
async def get_claim_detail_handler(
    claim_oid: str,
    container: Container = Depends(init_container),
) -> ClaimDetailSchema:
    """Get all claims"""
    mediator = container.resolve(Mediator)

    claim = await mediator.handle_query(GetClaimQuery(claim_oid=claim_oid))

    return ClaimDetailSchema.from_entity(claim)
