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
    def get_highest_status(cls):
        """Метод получения самого высокого статуса"""
        highest_status = None
        for status in cls:
            highest_status = status
        return highest_status

    @classmethod
    def get_lowest_status(cls):
        """Метод получения самого низкого статуса"""
        return next(iter(cls))

    @classmethod
    def get_status_by_code(cls, status_code):
        """Метод получения статуса по коду (status_code)"""
        for status in cls:
            if status.id_code == status_code:
                return status
        return None
