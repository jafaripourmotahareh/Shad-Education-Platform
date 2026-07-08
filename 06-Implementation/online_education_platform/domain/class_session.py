from .base_entity import BaseEntity


class ClassSession(BaseEntity):
    def __init__(
        self,
        title,
        courseId,
        teacherId,
        startTime,
        endTime,
        meetingUrl,
        entity_id=None,
    ):
        super().__init__(entity_id)
        self.title = title
        self.courseId = courseId
        self.teacherId = teacherId
        self.startTime = startTime
        self.endTime = endTime
        self.meetingUrl = meetingUrl
        self.status = "scheduled"
        self.recordingUrl = None
        self._recordingEnabled = False

    def startSession(self):
        self.status = "active"

    def endSession(self):
        self.status = "ended"

    def toggleRecording(self):
        self._recordingEnabled = not self._recordingEnabled

        if self._recordingEnabled:
            self.recordingUrl = f"{self.meetingUrl}/recording"
        else:
            self.recordingUrl = None