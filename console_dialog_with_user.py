import console
from exceptions_hospital import PatientIDNumberError


def request_command() -> str:
    return console.input_("Введите команду: ").strip().lower()

def request_patient_id() -> int:
    patient_id_text = console.input_("Введите ID пациента: ").strip().lower()
    return _convert_text_to_patient_id(patient_id_text)

def _convert_text_to_patient_id(patient_id_text):
    try:
        patient_id = int(patient_id_text)
        if patient_id <= 0:
            raise ValueError()
        return patient_id
    except ValueError:
        raise PatientIDNumberError()

def request_confirm_for_patient_discharge() -> bool:
    response = console.input_("Желаете этого клиента выписать? (да/нет): ").strip().lower()
    return response == "да"


def send_message(text):
    console.print_(f"{text}\n")
