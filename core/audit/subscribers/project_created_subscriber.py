from core.audit.models import AuditRecord


class ProjectCreatedSubscriber:


    def __init__(self):

        self.records = []


    def handle(self, event):

        record = AuditRecord(

            event_type=type(event).__name__,

            entity_id=str(
                event.project_id
            )

        )


        self.records.append(
            record
        )


        print(
            "AUDIT:",
            record
        )