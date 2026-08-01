from dataclasses import dataclass, field
from typing import Any
import json


@dataclass
class WorkflowResult:


    status: str

    project_id: str

    message: str

    context: Any = None

    history: list = field(
        default_factory=list
    )



    def to_dict(self):

        song = None


        if self.context and self.context.song_project:

            project = self.context.song_project


            song = {

                "id": str(project.id),

                "title": project.title,

                "status": project.status,


                "concept":
                    self._serialize(project.concept),


                "lyrics":
                    self._serialize(project.lyrics),


                "melody":
                    self._serialize(project.melody),


                "arrangement":
                    self._serialize(project.arrangement)

            }



        return {


            "status": self.status,


            "project_id":
                self.project_id,


            "message":
                self.message,


            "song":
                song,


            "history":
                self.history

        }



    def to_json(self):

        return json.dumps(

            self.to_dict(),

            indent=4,

            ensure_ascii=False,

            default=str

        )



    def _serialize(
        self,
        obj
    ):

        if obj is None:

            return None


        if hasattr(
            obj,
            "__dict__"
        ):

            data = {}

            for key,value in obj.__dict__.items():

                if key.startswith("_"):

                    continue


                data[key] = value


            return data


        return str(obj)