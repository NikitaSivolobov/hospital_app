from hospital_enums.status import Status
from exceptions_hospital import PatientIDNumberError, PatientIDIsNotInHospitalError
from hospital_entities.patient import Patient
from config import Config


class Hospital:
    """Класс корневой бизнес логики (hospital) - entity"""

    def __init__(self, patients_count=Config.PATIENTS_COUNT, patient=Patient(Status.STATUS_01)):
        self.patients_count = patients_count
        self.patient = patient
        self.patients_list = None
        self._create_hospital_patients_with_list()

    def _create_hospital_patients_with_list(self):
        self.patients_list = [self.patient.status.status_code for _ in range(self.patients_count)]

    def _check_patient_id(self, patient_id):
        try:
            check_patient_id = int(patient_id)
            if check_patient_id <= 0:
                raise PatientIDNumberError("Ошибка. ID пациента должно быть числом (целым, положительным)")
            elif check_patient_id - 1 >= len(self.patients_list):
                raise PatientIDIsNotInHospitalError("Ошибка. В больнице нет пациента с таким ID")
            return True
        except ValueError:
            raise PatientIDNumberError("Ошибка. ID пациента должно быть числом (целым, положительным)")

    @staticmethod
    def _get_patient_id(patient_id):
        return patient_id - 1

    def get_total_patients(self):
        return len(self.patients_list)

    def get_status_counts(self):
        status_counts = {}
        for status in Status:
            status_counts[status.status_name] = self.patients_list.count(status.status_code)
        return status_counts

    def is_valid_patient_id(self, value_patient_id_from_command):
        try:
            check_patient_id = self._check_patient_id(value_patient_id_from_command)
            if check_patient_id:
                is_valid_patient_id = self._get_patient_id(int(value_patient_id_from_command))
                return is_valid_patient_id
        except (PatientIDNumberError, PatientIDIsNotInHospitalError) as err:
            return err.args[0]

    def get_status_name(self, patient_id):
        status_code_in_list = self.patients_list[patient_id]
        status_name_in_list = Status.get_status_by_code(status_code_in_list)
        return status_name_in_list.status_name

    def check_status_patient_for_up(self, patient_id):
        status_code_patient_in_hospital = self.patients_list[patient_id]
        if status_code_patient_in_hospital < Status.get_last_status().status_code:
            return True
        else:
            return False

    def status_up(self, patient_id):
        status_patient_id = self.patients_list[patient_id]
        status_patient_id += 1
        self.patients_list[patient_id] = status_patient_id

    def discharge(self, patient_id):
        del self.patients_list[patient_id]
