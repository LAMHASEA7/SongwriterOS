from core.domain.models.entity import Entity
from core.events.event import Event


def test_core():

    entity = Entity()

    event = Event()

    print(entity)
    print(event)


if __name__ == "__main__":
    test_core()