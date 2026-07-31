class ProviderRegistry:

    def __init__(self):

        self.providers = {}


    def register(
        self,
        provider
    ):

        self.providers[
            provider.name.lower()
        ] = provider


    def get(
        self,
        name
    ):

        return self.providers.get(
            name.lower()
        )


    def exists(
        self,
        name
    ):

        return (
            name.lower()
            in self.providers
        )


    def all(self):

        return list(
            self.providers.values()
        )