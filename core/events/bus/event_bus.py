class EventBus:


    def __init__(self):

        self.listeners = {}



    def subscribe(
        self,
        event_type,
        handler
    ):

        if event_type not in self.listeners:

            self.listeners[event_type] = []


        self.listeners[event_type].append(
            handler
        )



    def publish(
        self,
        event
    ):

        event_type = type(event)


        handlers = self.listeners.get(
            event_type,
            []
        )


        for handler in handlers:

            try:

                handler(event)


            except Exception as error:

                print(
                    f"Event handler failed: {handler.__name__}"
                )

                print(
                    error
                )