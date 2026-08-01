from core.ai.factory import ProviderFactory
from core.ai.models import Prompt


provider = ProviderFactory.create("openai")

prompt = Prompt(
    system="You are a creative songwriter.",
    user="Create a song concept about memories."
)

response = provider.generate(prompt)

print(response.text)
print(response.model)
print(response.provider)