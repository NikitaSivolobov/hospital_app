from enums.status import Status
from models.patient import Patient


class Hospital:
    def __init__(self, patients=200, patient=Patient(Status.STATUS_01)):
        self.patients = patients
        self.patient = patient
        self.patients_list = None

    def create_hospital_patients_with_list(self):
        return [self.patient.status.status_code for _ in range(self.patients)]
