# project/app/api/crud.py


from app.models.pydantic import SummaryPayloadSchema
from app.models.tortoise import TextSummary


async def post(payload: SummaryPayloadSchema) -> int:
    summary = TextSummary(url=payload.url, summary="")
    await summary.save()
    return summary.id


async def get(id: int) -> dict | None:
    summary = await TextSummary.filter(id=id).first().values()
    if summary:
        return summary


async def get_all() -> list:
    return await TextSummary.all().values()


async def delete(id: int) -> int:
    return await TextSummary.filter(id=id).first().delete()


async def put(id: int, payload: SummaryPayloadSchema) -> dict | None:
    summary = await (
        TextSummary.filter(id=id).update(url=payload.url, summary=payload.summary)
    )

    if summary:
        return await TextSummary.filter(id=id).first().values()
