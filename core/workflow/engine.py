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



        try:


            for step in workflow.steps:


                execution.current_step = step.name


                history_item = {

                    "step": step.name,

                    "status": "RUNNING",

                    "started_at": datetime.utcnow().isoformat()

                }


                execution.history.append(
                    history_item
                )



                print(
                    f"Executing step: {step.name}"
                )



                try:


                    result = step.handler(
                        execution
                    )


                    history_item["status"] = "SUCCESS"


                    history_item[
                        "finished_at"
                    ] = datetime.utcnow().isoformat()



                    if step.output_key:


                        execution.state[
                            step.output_key
                        ] = result




                except Exception as error:


                    history_item["status"] = "FAILED"

                    history_item[
                        "error"
                    ] = str(error)



                    execution.status = "FAILED"



                    print(
                        f"Step failed: {step.name}"
                    )


                    print(
                        error
                    )


                    break




            if execution.status != "FAILED":


                execution.status = "SUCCESS"



        except Exception as error:


            execution.status = "FAILED"

            print(
                "Workflow failed:"
            )

            print(
                error
            )




        execution.finished_at = datetime.utcnow()



        return WorkflowResult(

            status=execution.status,

            project_id=execution.context.project_id,

            message=(

                "Workflow completed successfully"

                if execution.status == "SUCCESS"

                else "Workflow failed"

            ),

            context=execution.context,

            history=execution.history

        )