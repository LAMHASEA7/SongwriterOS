from core.workflow.models import WorkflowExecution


class WorkflowEngine:
    """
    Executes creative workflows.
    """


    def execute(
        self,
        workflow,
        event
    ):

        execution = WorkflowExecution(
            input_event=event
        )


        print(
            f"Workflow: {workflow.name}"
        )


        for step in workflow.steps:

            execution.current_step = step.name


            print(
                f"Executing step: {step.name}"
            )


            result = step.handler(
                execution
            )


            if step.output_key:

                execution.state[
                    step.output_key
                ] = result


        return execution