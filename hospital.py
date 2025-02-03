import status
from exceptions_hospital import PatientNotExistsError
from status import STATUS, get_status_by_code, get_lowest_status

_patients_list = []


def _verify_patient_id(patient_id, patients_list):
    if patient_id > len(patients_list):
        raise PatientNotExistsError()


def get_total_patients(patients_list):
    return len(patients_list)


def get_status_counts(patients_list):
    status_counts = {}
    for status_ in STATUS.keys():
        status_counts[STATUS[status_]] = patients_list.count(status_)
    return status_counts


def get_status_name_by_patient_id(patient_id, patients_list):
    _verify_patient_id(patient_id, patients_list)
    patient_index = patient_id - 1
    status_code = patients_list[patient_index]
    return get_status_by_code(status_code)


def can_status_up(patient_id, patients_list):
    _verify_patient_id(patient_id, patients_list)
    patient_index = patient_id - 1
    status_code = patients_list[patient_index]
    return status_code < status.get_highest_status()


def can_status_down(patient_id, patients_list) -> bool:
    _verify_patient_id(patient_id, patients_list)
    patient_index = patient_id - 1
    status_code = patients_list[patient_index]
    return status_code > get_lowest_status()


def status_up(patient_id, patients_list):
    _verify_patient_id(patient_id, patients_list)
    patient_index = patient_id - 1
    status_code = patients_list[patient_index]
    patients_list[patient_index] = status_code + 1
    global _patients_list
    _patients_list = patients_list


def status_down(patient_id, patients_list) -> bool:
    _verify_patient_id(patient_id, patients_list)
    patient_index = patient_id - 1
    status_code = patients_list[patient_index]
    patients_list[patient_index] = status_code - 1
    global _patients_list
    _patients_list = patients_list


def discharge(patient_id, patients_list):
    _verify_patient_id(patient_id, patients_list)
    patient_index = patient_id - 1
    del patients_list[patient_index]
    global _patients_list
    _patients_list = patients_list
