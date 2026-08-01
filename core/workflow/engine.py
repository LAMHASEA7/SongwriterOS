from datetime import datetime

from core.application import WorkflowResult

from .models import WorkflowExecution

from core.events.models import (
    WorkflowStartedEvent,
    WorkflowStepStartedEvent,
    WorkflowStepCompletedEvent,
    WorkflowCompletedEvent
)



class WorkflowEngine:
    """
    Executes creative workflows.
    """



    def _get_project_id(
        self,
        execution
    ):

        if execution.context:

            return execution.context.project_id


        return None




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



        #
        # Workflow Started Event
        #

        if workflow.event_bus:


            workflow.event_bus.publish(

                WorkflowStartedEvent(

                    workflow_name=workflow.name,

                    project_id=self._get_project_id(
                        execution
                    ),

                    created_at=datetime.utcnow()

                )

            )



        try:


            for step in workflow.steps:


                execution.current_step = step.name



                history_item = {

                    "step": step.name,

                    "status": "RUNNING",

                    "started_at":
                        datetime.utcnow().isoformat()

                }



                execution.history.append(
                    history_item
                )



                print(
                    f"Executing step: {step.name}"
                )



                #
                # Workflow Step Started Event
                #

                if workflow.event_bus:


                    workflow.event_bus.publish(

                        WorkflowStepStartedEvent(

                            workflow_name=workflow.name,

                            step_name=step.name,

                            created_at=datetime.utcnow()

                        )

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




                    #
                    # Workflow Step Completed Event
                    #

                    if workflow.event_bus:


                        workflow.event_bus.publish(

                            WorkflowStepCompletedEvent(

                                workflow_name=workflow.name,

                                step_name=step.name,

                                status="SUCCESS",

                                created_at=datetime.utcnow()

                            )

                        )




                except Exception as error:


                    history_item["status"] = "FAILED"


                    history_item[
                        "finished_at"
                    ] = datetime.utcnow().isoformat()



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



        #
        # Workflow Completed Event
        #

        if workflow.event_bus:


            workflow.event_bus.publish(

                WorkflowCompletedEvent(

                    workflow_name=workflow.name,

                    project_id=self._get_project_id(
                        execution
                    ),

                    status=execution.status,

                    created_at=datetime.utcnow()

                )

            )




        project_id = self._get_project_id(
            execution
        )




        return WorkflowResult(

            status=execution.status,

            project_id=project_id,


            message=(

                "Workflow completed successfully"

                if execution.status == "SUCCESS"

                else "Workflow failed"

            ),


            context=execution.context,


            history=execution.history

        )