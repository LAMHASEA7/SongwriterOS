class WorkflowEngine:
    """
    Executes creative workflows.
    """


    def execute(self, workflow):

        print(
            f"Workflow: {workflow.name}"
        )


        for step in workflow.steps:

            print(
                f"Executing step: {step.name}"
            )


            if step.handler:

                step.handler()