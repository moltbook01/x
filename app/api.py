from fastapi import APIRouter

from app.agents import default_personal_agent

router = APIRouter()


@router.get("/health")
async def health_check() -> dict[str, str]:
    return {"status": "ok"}


@router.get("/agents/personal")
async def get_personal_agent() -> dict[str, str | list[str]]:
    agent = default_personal_agent()
    return {
        "name": agent.name,
        "provider": agent.provider,
        "model": agent.model,
        "persona": agent.persona,
        "goals": agent.goals,
    }
