from core.domain.models import CreativeWork

from core.infrastructure.repositories import (
    SQLiteWorkRepository
)


repository = SQLiteWorkRepository(
    "database/songwriteros.db"
)


work = CreativeWork(

    title="Memory Song",

    work_type="Lyrics",

    content="A song about Memory"

)


repository.save(work)


print("Saved:")
print(work)


loaded = repository.find(
    work.id
)


print("Loaded:")
print(loaded)