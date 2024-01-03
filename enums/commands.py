from enum import Enum


class Commands(Enum):
    """Класс констант для комманд"""

    COMMANDS_GET_STATUS = ("узнать статус пациента", "get status")
    COMMANDS_STATUS_UP = ("повысить статус пациента", "status up")
    COMMANDS_STATUS_DOWN = ("понизить статус пациента", "status down")
    COMMANDS_DISCHARGE = ("выписать пациента", "discharge")
    COMMANDS_CALCULATE_STATISTICS = ("рассчитать статистику", "calculate statistics")
    COMMANDS_STOP = ("стоп", "stop")

    def __init__(self, commands_ru, commands_en):
        self.commands_ru = commands_ru
        self.commands_en = commands_en
