from datetime import datetime

from core.application import WorkflowResult

from .models import WorkflowExecution


class WorkflowEngine:
    """
    Executes creative workflows.
    """


    def execute(
        self,
        workflow,
        input_event=None
    ):

        execution = WorkflowExecution(
            input_event=input_event
        )
        if workflow.context:

            execution.context = workflow.context

        execution.status = "RUNNING"


        print(
            f"Workflow: {workflow.name}"
        )


        for step in workflow.steps:

            execution.current_step = step.name


            execution.history.append(
                {
                    "step": step.name,
                    "status": "RUNNING"
                }
            )


            print(
                f"Executing step: {step.name}"
            )


            result = step.handler(
                execution
            )


            execution.history[-1]["status"] = "SUCCESS"


            if step.output_key:

                execution.state[
                    step.output_key
                ] = result



        execution.status = "SUCCESS"


        execution.finished_at = datetime.utcnow()



        return WorkflowResult(

            status=execution.status,

            project_id=execution.context.project_id,

            message="Workflow completed successfully",

            context=execution.context,

            history=execution.history

        )