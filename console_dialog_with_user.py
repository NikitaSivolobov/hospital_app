from exceptions_hospital import PatientIDNumberError


class ConsoleDialogWithUser:
    """Класс диалога с пользователем при помощи консольного ввода/вывода"""

    @staticmethod
    def get_command_from_user() -> str:
        return input("Введите команду: ").strip().lower()

    def get_patient_id_from_user(self) -> int:
        patient_id = input("Введите ID пациента: ").strip().lower()
        return self._check_patient_id(patient_id)

    @staticmethod
    def _check_patient_id(patient_id):
        try:
            patient_id = int(patient_id)
            if patient_id <= 0:
                raise PatientIDNumberError("ID пациента должно быть числом (целым, положительным)")
        except ValueError:
            raise PatientIDNumberError("ID пациента должно быть числом (целым, положительным)")
        return patient_id

    @staticmethod
    def patient_discharge_request() -> bool:
        discharge_input = input("Желаете этого клиента выписать? (да/нет): ").strip().lower()
        if discharge_input == 'да':
            return True
        else:
            return False

    @staticmethod
    def output_to_user(value):
        print(f"{value}\n")
