from dataclasses import dataclass


@dataclass(slots=True)
class Agent:
    name: str
    provider: str
    model: str

    async def respond(self, prompt: str) -> str:
        # Placeholder for LLM call integration.
        return f"[{self.name}] response stub for prompt: {prompt}"


@dataclass(slots=True)
class PersonalAgent(Agent):
    persona: str
    goals: list[str]

    async def respond(self, prompt: str) -> str:
        # Placeholder for a personal agent response strategy.
        return (
            f"[{self.name}] ({self.persona}) goals={self.goals} "
            f"prompt={prompt}"
        )


def default_personal_agent() -> PersonalAgent:
    return PersonalAgent(
        name="I-Only",
        provider="openai-or-local",
        model="gpt-4o-mini",
        persona="Personal debate coach",
        goals=["summarize", "challenge assumptions", "propose next steps"],
    )
