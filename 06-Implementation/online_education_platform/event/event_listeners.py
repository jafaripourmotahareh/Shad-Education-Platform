from domain.notification import Notification


class NotificationEventListener:

    def __init__(self, notification_service):
        self.notification_service = notification_service

    def handleEvent(self, event):
        notification = self.generateNotificationContent(event)

        if notification.userId:
            self.notification_service.send(notification)

    def generateNotificationContent(self, event):
        user_id = getattr(event, "userId", None)
        event_message = getattr(event, "message", str(event))
        event_title = getattr(event, "title", "New System Event Notification")

        return Notification(
            userId=user_id,
            type="system",
            title=event_title,
            message=event_message,
            targetLink=""
        )


class ExamEventListener:

    def __init__(self, notification_service):
        self.notification_service = notification_service

    def handleEvent(self, event):
        self.sendProctoringAlert(event)

    def sendProctoringAlert(self, event):
        user_id = getattr(event, "userId", None)

        if user_id:
            notification = Notification(
                userId=user_id,
                type="exam",
                title="Proctoring Alert",
                message="Exam focus shift or warning event detected.",
                targetLink=""
            )

            self.notification_service.send(notification)