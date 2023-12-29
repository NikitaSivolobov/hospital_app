from enums.status import Status


class Patient:
    def __init__(self, status=Status.STATUS_01):
        self.status = status
