from enums.status import Status
from models.patient import Patient
from config.config import Config


class Hospital:
    """Класс корневой бизнес логики (hospital)"""

    def __init__(self, patients_count=Config.PATIENTS_COUNT, patient=Patient(Status.STATUS_01)):
        self.patients_count = patients_count
        self.patient = patient
        self.patients_list = None
        self._create_hospital_patients_with_list()

    def _create_hospital_patients_with_list(self):
        self.patients_list = [self.patient.status.status_code for _ in range(self.patients_count)]

    def __str__(self):
        total_patients = len(self.patients_list)
        status_counts = {}
        for status in Status:
            status_counts[status.status_name] = self.patients_list.count(status.status_code)

        output = f"В больнице на данный момент находится {total_patients} чел., из них:\n"
        for status, count in status_counts.items():
            if count != 0:
                output += f"\t- в статусе \"{status}\": {count} чел.\n"
        return output.rstrip("\n")

    def get_status(self, patient_id):
        status_code_in_list = self.patients_list[patient_id]
        status_name_in_list = Status.get_status_by_code(status_code_in_list)
        return status_name_in_list

    def discharge(self, patient_id):
        del self.patients_list[patient_id]
        output = "Пациент выписан из больницы"
        return output

    def calculate_statistics(self):
        return self

    def status_patient_id_change(self, patient_id):
        status, is_discharge = self.process_discharge_request()
        if is_discharge:
            del self.patients_list[patient_id]
            return "Пациент выписан из больницы"
        else:
            return f"Пациент остался в статусе \"{status.status_name}\""

    @staticmethod
    def process_discharge_request():
        while True:
            discharge_input = input("Желаете этого клиента выписать? (да/нет): ").strip().lower()
            if discharge_input == 'да':
                return Status.get_last_status(), True
            elif discharge_input == 'нет':
                return Status.get_last_status(), False  # Status.STATUS_03.status_code
            else:
                print("Некорректный ввод. Пожалуйста, ответьте (да) или (нет)."), False

    def status_up(self, patient_id):
        status_patient_id = self.patients_list[patient_id]
        status_patient_id += 1
        self.patients_list[patient_id] = status_patient_id
        status_name_in_list = Status.get_status_by_code(status_patient_id).status_name
        return f"Новый статус пациента: \"{status_name_in_list}\""

    def status_down(self, patient_id):
        status_patient_id = self.patients_list[patient_id]
        status_patient_id -= 1
        self.patients_list[patient_id] = status_patient_id
        status_name_in_list = Status.get_status_by_code(status_patient_id).status_name
        return f"Новый статус пациента: \"{status_name_in_list}\""
