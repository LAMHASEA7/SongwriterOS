from core.events.bus.event_bus import EventBus
from core.events.models import ProjectCreatedEvent


def handler(event):

    print(
        "Received Project Event:",
        event.project_id
    )


bus = EventBus()


bus.subscribe(
    ProjectCreatedEvent,
    handler
)


event = ProjectCreatedEvent(
    "project-001"
)


bus.publish(event)