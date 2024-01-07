from hospital_enums.commands import Commands


class Application:
    """Класс работы приложения больницы (hospital) в цикле"""

    def __init__(self, commands_hospital):
        self.commands_hospital = commands_hospital

    def main(self):
        while True:
            command = self.commands_hospital.get_command_from_user()
            if command in Commands.COMMANDS_STATUS_UP.value:
                self.commands_hospital.command_patient_status_up()

            # elif command in Commands.COMMANDS_STATUS_DOWN.value:
            #     self.commands_hospital.command_patient_status_down()
            #
            # elif command in Commands.COMMANDS_DISCHARGE.value:
            #     self.commands_hospital.command_discharge()

            elif command in Commands.COMMANDS_CALCULATE_STATISTICS.value:
                self.commands_hospital.command_calculate_hospital_statistics()

            elif command in Commands.COMMANDS_GET_STATUS.value:
                self.commands_hospital.command_get_status_patient()

            elif command in Commands.COMMANDS_STOP.value:
                return False

            else:
                self.commands_hospital.output_to_user_from_app("Неизвестная команда! Попробуйте ещё раз")
