from dataclasses import dataclass


@dataclass
class AIResponse:

    text: str = ""

    model: str = ""

    provider: str = ""

    usage: dict = None