from hospital_enums.status import Status
from exceptions_hospital import PatientIDNumberError, PatientIDIsNotInHospitalError
from hospital_entities.patient import Patient
from config import Config


class Hospital:
    """Класс корневой бизнес логики (hospital) - entity"""

    def __init__(self, patients_count=Config.DEFAULT_PATIENTS_COUNT, patient=Patient(Config.DEFAULT_PATIENT_STATUS)):
        self.patients_count = patients_count
        self.patient = patient
        self.patients_list = None
        self._create_list_hospital_patients()

    def _create_list_hospital_patients(self):
        self.patients_list = [self.patient.status.id_code for _ in range(self.patients_count)]

    def _is_valid_patient_id(self, patient_id):
        try:
            patient_id = int(patient_id)
            if patient_id <= 0:
                raise PatientIDNumberError("ID пациента должно быть числом (целым, положительным)")
            if patient_id > len(self.patients_list):
                raise PatientIDIsNotInHospitalError("В больнице нет пациента с таким ID")
        except ValueError:
            raise PatientIDNumberError("ID пациента должно быть числом (целым, положительным)")

    def get_total_patients(self):
        return len(self.patients_list)

    def get_status_counts(self):
        status_counts = {}
        for status in Status:
            status_counts[status.name_value] = self.patients_list.count(status.id_code)
        return status_counts

    def get_status_name_by_patient_id(self, patient_id):
        self._is_valid_patient_id(patient_id)
        patient_id -= 1
        status_code = self.patients_list[patient_id]
        status = Status.get_status_by_code(status_code)
        return status.name_value

    def can_status_up(self, patient_id):
        self._is_valid_patient_id(patient_id)
        patient_id -= 1
        status_code = self.patients_list[patient_id]
        if status_code < Status.get_last_status().id_code:
            return True
        else:
            return False

    def status_up(self, patient_id):
        self._is_valid_patient_id(patient_id)
        patient_id -= 1
        status_patient = self.patients_list[patient_id]
        status_patient += 1
        self.patients_list[patient_id] = status_patient

    def can_status_down(self, patient_id):
        self._is_valid_patient_id(patient_id)
        patient_id -= 1
        status_code = self.patients_list[patient_id]
        if status_code > Status.get_first_status().id_code:
            return True
        else:
            return False

    def status_down(self, patient_id):
        self._is_valid_patient_id(patient_id)
        patient_id -= 1
        status_patient = self.patients_list[patient_id]
        status_patient -= 1
        self.patients_list[patient_id] = status_patient

    def discharge(self, patient_id):
        self._is_valid_patient_id(patient_id)
        patient_id -= 1
        del self.patients_list[patient_id]
