from application import Application
from enums.commands import Commands


class ApplicationMock(Application):
    """Мок класса работы приложения в цикле с командами из списка"""

    def __init__(self, user_dialog):
        super().__init__(user_dialog)
        self.dialog = user_dialog

    def main_first(self):
        while True:
            commands = [" узнать статус пациента ", " sTatUs UP     ", "   status down   ",
                        "discharge   ", "   рассчитать статистику  ", "стоп"]
            for com in commands:
                command = self.dialog.command_input(com)
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
                    print("Сеанс завершён.")
                    return False

                else:
                    self.dialog.command_output("Неизвестная команда! Попробуйте ещё раз")

    def main_second(self):
        while True:
            commands = ["выписать всех пациентов", " STOP "]
            for com in commands:
                command = self.dialog.command_input(com)
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
                    print("Сеанс завершён.")
                    return False

                else:
                    self.dialog.command_output("Неизвестная команда! Попробуйте ещё раз")

    def main_third(self):
        while True:
            commands = ["узнать статус пациента", " пОвЫситЬ СтатуС паЦиента     ", "   понизиТЬ сТАтус Пациента   ",
                        "стоп"]
            for com in commands:
                command = self.dialog.command_input(com)
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
                    print("Сеанс завершён.")
                    return False

                else:
                    self.dialog.command_output("Неизвестная команда! Попробуйте ещё раз")

    def main_fourth(self):
        while True:
            commands = [" повысить статус пациента ", " повысить статус пациента     ",
                        "   повысить статус пациента  ", "   рассчитать статистику  ", "стоп"]
            for com in commands:
                command = self.dialog.command_input(com)
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
                    print("Сеанс завершён.")
                    return False

                else:
                    self.dialog.command_output("Неизвестная команда! Попробуйте ещё раз")

    def main_sixth(self):
        while True:
            commands = [" понизить статус пациента ", " понизить статус пациента     ",
                        "   рассчитать статистику  ", "стоп"]
            for com in commands:
                command = self.dialog.command_input(com)
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
                    print("Сеанс завершён.")
                    return False

                else:
                    self.dialog.command_output("Неизвестная команда! Попробуйте ещё раз")
