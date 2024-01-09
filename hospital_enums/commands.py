from enum import Enum


class Commands(Enum):
    """Класс констант для комманд"""

    GET_STATUS = ("узнать статус пациента", "get status")
    STATUS_UP = ("повысить статус пациента", "status up")
    STATUS_DOWN = ("понизить статус пациента", "status down")
    DISCHARGE = ("выписать пациента", "discharge")
    CALCULATE_STATISTICS = ("рассчитать статистику", "calculate statistics")
    STOP = ("стоп", "stop")

    def __init__(self, command_ru, command_en):
        self.command_ru = command_ru
        self.command_en = command_en
