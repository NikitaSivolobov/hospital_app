import hospital
import console_dialog_with_user as dialog
from exceptions_hospital import PatientIDNumberError, PatientNotExistsError


def _convert_hospital_data_to_calculate_statistics(total_patients: int, status_counts: dict) -> str:
    calculate_statistics = f"В больнице на данный момент находится {total_patients} чел., из них:\n"
    for status, count in status_counts.items():
        if count != 0:
            calculate_statistics += f"\t- в статусе \"{status}\": {count} чел.\n"
    return calculate_statistics.rstrip("\n")


def calculate_hospital_statistics(patients_list):
    total_patients = hospital.get_total_patients(patients_list)
    status_count = hospital.get_status_counts(patients_list)
    calculate_statistics = _convert_hospital_data_to_calculate_statistics(total_patients, status_count)
    dialog.send_message(calculate_statistics)


def get_status_patient(patients_list):
    """Получает статус пациента по ID и отправляет сообщение."""
    try:
        patient_id = dialog.request_patient_id()
        status_name = hospital.get_status_name_by_patient_id(patient_id, patients_list)
        dialog.send_message(f"Статус пациента: \"{status_name}\"")
    except (PatientIDNumberError, PatientNotExistsError) as err:
        dialog.send_message(str(err))

def patient_status_up(patients_list):
    """Повышает статус пациента по ID."""
    try:
        patient_id = dialog.request_patient_id()
        if hospital.can_status_up(patient_id, patients_list):
            hospital.status_up(patient_id, patients_list)
            status_name = hospital.get_status_name_by_patient_id(patient_id, patients_list)
            dialog.send_message(f"Новый статус пациента: \"{status_name}\"")
        else:
            if dialog.request_confirm_for_patient_discharge():
                hospital.discharge(patient_id, patients_list)
                dialog.send_message("Пациент выписан из больницы")
            else:
                status_name = hospital.get_status_name_by_patient_id(patient_id, patients_list)
                dialog.send_message(f"Пациент остался в статусе \"{status_name}\"")
    except (PatientIDNumberError, PatientNotExistsError) as err:
        dialog.send_message(str(err))

def discharge_patient(patients_list):
    """Выписывает пациента по ID."""
    try:
        patient_id = dialog.request_patient_id()
        hospital.discharge(patient_id, patients_list)
        dialog.send_message("Пациент выписан из больницы")
    except (PatientIDNumberError, PatientNotExistsError) as err:
        dialog.send_message(str(err))

def patient_status_down(patients_list):
    """Понижает статус пациента по ID."""
    try:
        patient_id = dialog.request_patient_id()
        if hospital.can_status_down(patient_id, patients_list):
            hospital.status_down(patient_id, patients_list)
            status_name = hospital.get_status_name_by_patient_id(patient_id, patients_list)
            dialog.send_message(f"Новый статус пациента: \"{status_name}\"")
        else:
            dialog.send_message("Ошибка. Нельзя понизить самый низкий статус (наши пациенты не умирают)")
    except (PatientIDNumberError, PatientNotExistsError) as err:
        dialog.send_message(str(err))