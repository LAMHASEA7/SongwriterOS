from core.workflow.engine import WorkflowEngine

from core.workflow.models import (
    Workflow,
    WorkflowStep
)


def concept():

    print(
        "Concept generation"
    )


def lyric():

    print(
        "Lyric generation"
    )



workflow = Workflow(
    "Song Creation Workflow"
)


workflow.add_step(
    WorkflowStep(
        "Create Concept",
        concept
    )
)


workflow.add_step(
    WorkflowStep(
        "Create Lyrics",
        lyric
    )
)



engine = WorkflowEngine()

engine.execute(
    workflow
)