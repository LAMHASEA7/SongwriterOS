from core.domain.models import (
    CreativeProject,
    CreativeWork,
    Concept,
    Agent
)


def main():

    project = CreativeProject(
        title="First Creative Project",
        project_type="Song"
    )

    concept = Concept(
        theme="Memory",
        emotion="Nostalgia",
        message="Keep the moment"
    )

    agent = Agent(
        name="Lyric Agent",
        capability="Writing"
    )

    print(project)
    print(concept)
    print(agent)


if __name__ == "__main__":
    main()