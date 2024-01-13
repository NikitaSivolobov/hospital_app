from hospital_enums.status import Status
from exceptions_hospital import PatientNotExistsError
from config import Config


class Hospital:
    """Класс корневой бизнес логики (hospital) - entity"""

    def __init__(self,
                 patients_count=Config.DEFAULT_PATIENTS_COUNT,
                 patient_status=Config.DEFAULT_PATIENT_STATUS):
        self._patients_count = patients_count
        self._patient_status = patient_status
        self._create_list_hospital_patients()

    def _create_list_hospital_patients(self):
        self.patients_list = [Config.DEFAULT_PATIENT_STATUS.id_code for _ in range(self._patients_count)]

    def _verify_patient_id(self, patient_id):
        if patient_id > len(self.patients_list):
            raise PatientNotExistsError()

    def get_total_patients(self):
        return len(self.patients_list)

    def get_status_counts(self):
        status_counts = {}
        for status in Status:
            status_counts[status.name_value] = self.patients_list.count(status.id_code)
        return status_counts

    def get_status_name_by_patient_id(self, patient_id):
        self._verify_patient_id(patient_id)
        patient_index = patient_id - 1
        status_code = self.patients_list[patient_index]
        status_patient = Status.get_status_by_code(status_code)
        return status_patient.name_value

    def can_status_up(self, patient_id) -> bool:
        self._verify_patient_id(patient_id)
        patient_index = patient_id - 1
        status_code = self.patients_list[patient_index]
        return status_code < Status.get_highest_status().id_code

    def status_up(self, patient_id):
        self._verify_patient_id(patient_id)
        patient_index = patient_id - 1
        status_code = self.patients_list[patient_index]
        self.patients_list[patient_index] = status_code + 1

    def can_status_down(self, patient_id) -> bool:
        self._verify_patient_id(patient_id)
        patient_index = patient_id - 1
        status_code = self.patients_list[patient_index]
        return status_code > Status.get_lowest_status().id_code

    def status_down(self, patient_id):
        self._verify_patient_id(patient_id)
        patient_index = patient_id - 1
        status_code = self.patients_list[patient_index]
        self.patients_list[patient_index] = status_code - 1

    def discharge(self, patient_id):
        self._verify_patient_id(patient_id)
        patient_index = patient_id - 1
        del self.patients_list[patient_index]
