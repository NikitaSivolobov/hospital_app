from console import Console
from exceptions_hospital import PatientIDNumberError


class ConsoleDialogWithUser:
    """Класс диалога с пользователем при помощи консольного ввода/вывода"""

    @staticmethod
    def request_command() -> str:
        return Console.input("Введите команду: ").strip().lower()

    def request_patient_id(self) -> int:
        patient_id_text = Console.input("Введите ID пациента: ").strip().lower()
        return self._convert_text_to_patient_id(patient_id_text)

    @staticmethod
    def _convert_text_to_patient_id(patient_id_text):
        try:
            patient_id = int(patient_id_text)
            if patient_id <= 0:
                raise ValueError()
            return patient_id
        except ValueError:
            raise PatientIDNumberError()

    @staticmethod
    def request_confirm_for_patient_discharge() -> bool:
        response = Console.input("Желаете этого клиента выписать? (да/нет): ").strip().lower()
        return response == "да"

    @staticmethod
    def send_message(text):
        Console.print(f"{text}\n")
