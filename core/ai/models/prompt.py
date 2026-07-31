from dataclasses import dataclass


@dataclass
class Prompt:

    system: str = ""

    user: str = ""

    temperature: float = 0.7

    max_tokens: int = 1000