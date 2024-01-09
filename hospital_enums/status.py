from enum import Enum


class Status(Enum):
    """Класс констант для статусов пациента"""

    ID_00 = (0, "Тяжело болен")
    ID_01 = (1, "Болен")
    ID_02 = (2, "Слегка болен")
    ID_03 = (3, "Готов к выписке")

    def __init__(self, status_code, status_name):
        self.id_code = status_code
        self.name_value = status_name

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
            if status.id_code == code:
                return status
        return None
