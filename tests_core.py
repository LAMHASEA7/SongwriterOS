from core.domain.models.entity import Entity
from core.events.event import Event
from core.workflow.engine import WorkflowEngine


def main():

    print("=== CreativeOS Core Test ===")

    entity = Entity()
    print(entity)

    event = Event()
    print(event)

    engine = WorkflowEngine()
    engine.execute("Song Creation Workflow")


if __name__ == "__main__":
    main()