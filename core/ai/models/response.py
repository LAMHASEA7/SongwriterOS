from dataclasses import dataclass, field


@dataclass
class AIResponse:

    text: str = ""

    model: str = ""

    provider: str = ""


    usage: dict = field(
        default_factory=dict
    )


    latency: float = 0.0


    success: bool = True


    error: str = ""