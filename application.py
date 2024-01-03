from enums.commands import Commands


class Application:
    """Класс работы приложения в цикле"""

    def __init__(self, user_dialog):
        self.dialog = user_dialog

    def main(self):
        while True:
            command = self.dialog.command_input()
            if command in Commands.COMMANDS_STATUS_UP.value:
                self.dialog.status_up_from_commands()

            elif command in Commands.COMMANDS_STATUS_DOWN.value:
                self.dialog.status_down_from_commands()

            elif command in Commands.COMMANDS_DISCHARGE.value:
                self.dialog.get_discharge_from_commands()

            elif command in Commands.COMMANDS_CALCULATE_STATISTICS.value:
                self.dialog.get_calculate_statistics_from_commands()

            elif command in Commands.COMMANDS_GET_STATUS.value:
                self.dialog.get_status_from_commands()

            elif command in Commands.COMMANDS_STOP.value:
                return False

            else:
                self.dialog.command_output("Неизвестная команда! Попробуйте ещё раз")
