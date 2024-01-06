from enums.status import Status
from entities.patient import Patient
from config.config import Config


class Hospital:
    """Класс корневой бизнес логики (hospital) - entity"""

    def __init__(self, patients_count=Config.PATIENTS_COUNT, patient=Patient(Status.STATUS_01)):
        self.patients_count = patients_count
        self.patient = patient
        self.patients_list = None
        self._create_hospital_patients_with_list()

    def _create_hospital_patients_with_list(self):
        try:
            self.patients_list = [self.patient.status.status_code for _ in range(int(self.patients_count))]
        except ValueError:
            raise ValueError("Ошибка: неверный формат patients_count передан в Hospital")

    def get_status(self, patient_id):
        status_code_in_list = self.patients_list[patient_id]
        status_in_list = Status.get_status_by_code(status_code_in_list)
        return status_in_list

    def discharge(self, patient_id):
        try:
            del self.patients_list[patient_id]
            return True
        except KeyError:
            return False

    def calculate_statistics(self):
        total_patients = len(self.patients_list)
        status_counts = {}
        for status in Status:
            status_counts[status.status_name] = self.patients_list.count(status.status_code)

        return total_patients, status_counts

    def status_up(self, patient_id):
        status_patient_id = self.patients_list[patient_id]
        status_patient_id += 1
        self.patients_list[patient_id] = status_patient_id
        status_in_list = Status.get_status_by_code(status_patient_id)
        return status_in_list

    def status_down(self, patient_id):
        status_patient_id = self.patients_list[patient_id]
        status_patient_id -= 1
        self.patients_list[patient_id] = status_patient_id
        status_in_list = Status.get_status_by_code(status_patient_id)
        return status_in_list
