from hospital_enums.commands import Commands


class Application:
    """Класс работы приложения больницы (hospital) в цикле"""

    def __init__(self, commands_hospital, dialog_with_user):
        self.command_hospital = commands_hospital
        self.dialog = dialog_with_user

    def main(self):
        while True:
            command = self.dialog.request_command()
            if command in Commands.STATUS_UP.value:
                self.command_hospital.patient_status_up()

            elif command in Commands.STATUS_DOWN.value:
                self.command_hospital.patient_status_down()

            elif command in Commands.DISCHARGE.value:
                self.command_hospital.discharge_patient()

            elif command in Commands.CALCULATE_STATISTICS.value:
                self.command_hospital.calculate_hospital_statistics()

            elif command in Commands.GET_STATUS.value:
                self.command_hospital.get_status_patient()

            elif command in Commands.STOP.value:
                self.dialog.send_message("Сеанс завершён.")
                break

            else:
                self.dialog.send_message("Неизвестная команда! Попробуйте ещё раз")
