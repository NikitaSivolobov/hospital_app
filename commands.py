COMMANDS = {
    "GET_STATUS": ("узнать статус пациента", "get status"),
    "STATUS_UP": ("повысить статус пациента", "status up"),
    "STATUS_DOWN": ("понизить статус пациента", "status down"),
    "DISCHARGE": ("выписать пациента", "discharge"),
    "CALCULATE_STATISTICS": ("рассчитать статистику", "calculate statistics"),
    "STOP": ("стоп", "stop"),
}

COMMAND_MAP = {cmd[0]: key for key, cmd in COMMANDS.items()}
COMMAND_MAP.update({cmd[1]: key for key, cmd in COMMANDS.items()})
