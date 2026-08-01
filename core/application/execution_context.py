from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4
from core.domain.song_project import SongProject



@dataclass
class ExecutionContext:


    project_id: str


    id: UUID = field(
        default_factory=uuid4
    )


    created_at: datetime = field(
        default_factory=datetime.utcnow
    )


    agents: list[str] = field(
        default_factory=list
    )


    ai_calls: int = 0



    concepts: list[dict] = field(
        default_factory=list
    )


    works: list[dict] = field(
        default_factory=list
    )


    melodies: list[dict] = field(
        default_factory=list
    )


    arrangements: list[dict] = field(
        default_factory=list
    )


    events: list[str] = field(
        default_factory=list
    )


    metadata: dict = field(
        default_factory=dict
    )
    song_project: SongProject = None


    def register_agent(
        self,
        agent_name: str
    ):


        if agent_name not in self.agents:

            self.agents.append(
                agent_name
            )



    def register_ai_call(
        self
    ):

        self.ai_calls += 1




    def register_concept(
        self,
        concept
    ):


        self.concepts.append(

            {
                "id": str(concept.id),

                "theme": concept.theme,

                "emotion": concept.emotion,

                "message": concept.message

            }

        )




    def register_work(
        self,
        work
    ):


        self.works.append(

            {
                "id": str(work.id),

                "title": work.title,

                "type": work.work_type

            }

        )




    def register_melody(
        self,
        melody
    ):


        self.melodies.append(

            {
                "key": melody.key,

                "tempo": melody.tempo,

                "mood": melody.mood,

                "description": melody.description

            }

        )




    def register_arrangement(
        self,
        arrangement
    ):


        self.arrangements.append(

            {
                "instruments": arrangement.instruments,

                "structure": arrangement.structure,

                "atmosphere": arrangement.atmosphere

            }

        )




    def register_event(
        self,
        event_name: str
    ):


        self.events.append(
            event_name
        )




    def add_metadata(
        self,
        key,
        value
    ):


        self.metadata[key] = value

    def attach_project(
    self,
    project
):

        self.song_project = project



    def summary(
        self
    ):


        return {


            "id": str(self.id),


            "project_id": self.project_id,


            "created_at": self.created_at.isoformat(),


            "agents": self.agents,


            "ai_calls": self.ai_calls,


            "concepts": self.concepts,


            "works": self.works,


            "melodies": self.melodies,


            "arrangements": self.arrangements,


            "events": self.events,


            "metadata": self.metadata

        }