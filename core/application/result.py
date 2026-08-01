from dataclasses import dataclass, field
from typing import Any
import json
from datetime import datetime
from uuid import UUID



@dataclass
class WorkflowResult:


    status: str

    project_id: str

    message: str

    context: Any = None

    song: Any = None

    history: list = field(
        default_factory=list
    )



    def song_to_dict(self):


        if not self.context:
            return None


        song = getattr(
            self.context,
            "song_project",
            None
        )


        if not song:
            return None



        data = {

            "id": str(song.id),

            "title": song.title

        }



        if song.concept:

            data["concept"] = {

                "theme": song.concept.theme,

                "emotion": song.concept.emotion,

                "message": song.concept.message

            }



        if song.lyrics:

            data["lyrics"] = {

                "title": song.lyrics.title,

                "content": song.lyrics.content

            }



        if song.melody:

            data["melody"] = {

                "key": song.melody.key,

                "tempo": song.melody.tempo,

                "mood": song.melody.mood,

                "description": song.melody.description

            }



        if song.arrangement:

            data["arrangement"] = {

                "instruments": song.arrangement.instruments,

                "structure": song.arrangement.structure,

                "atmosphere": song.arrangement.atmosphere

            }


        return data




    def to_dict(self):

        return {

            "status": self.status,

            "project_id": self.project_id,

            "message": self.message,

            "song": self.song_to_dict(),

            "history": self.history

        }




    def to_json(self):


        return json.dumps(

            self.to_dict(),

            indent=4,

            ensure_ascii=False,

            default=self.json_serializer

        )



    @staticmethod
    def json_serializer(obj):

        if isinstance(obj, (datetime, UUID)):

            return str(obj)


        return str(obj)