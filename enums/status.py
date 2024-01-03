from enum import Enum


class Status(Enum):
    """Класс констант для статусов пациента"""

    STATUS_00 = (0, "Тяжело болен")
    STATUS_01 = (1, "Болен")
    STATUS_02 = (2, "Слегка болен")
    STATUS_03 = (3, "Готов к выписке")

    def __init__(self, status_code, status_name):
        self.status_code = status_code
        self.status_name = status_name

    @classmethod
    def get_last_status(cls):
        last_status = None
        for status in cls:
            last_status = status
        return last_status

    @classmethod
    def get_first_status(cls):
        return next(iter(cls))

    @classmethod
    def get_status_by_code(cls, code):
        for status in cls:
            if status.status_code == code:
                return status
        return None
