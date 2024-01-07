from hospital_enums.status import Status


class Patient:
    """Класс пациента - entity"""

    def __init__(self, status=Status.STATUS_01):
        self.status = status
