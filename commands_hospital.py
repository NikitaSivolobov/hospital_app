from exceptions_hospital import PatientIDNumberError, PatientIDIsNotInHospitalError


class CommandsHospital:
    def __init__(self, hospital, dialog_with_user):
        self.hospital = hospital
        self.dialog = dialog_with_user

    def calculate_hospital_statistics(self):
        total_patients = self.hospital.get_total_patients()
        status_counts = self.hospital.get_status_counts()
        calculate_statistics = f"В больнице на данный момент находится {total_patients} чел., из них:\n"
        for status, count in status_counts.items():
            if count != 0:
                calculate_statistics += f"\t- в статусе \"{status}\": {count} чел.\n"
        self.dialog.output_to_user(calculate_statistics.rstrip("\n"))

    def get_status_patient(self):
        try:
            patient_id = self.dialog.get_patient_id_from_user()
            status_name = self.hospital.get_status_name_by_patient_id(patient_id)
            self.dialog.output_to_user(f"Статус пациента: \"{status_name}\"")
        except (PatientIDNumberError, PatientIDIsNotInHospitalError) as err:
            return self.dialog.output_to_user(err)

    def patient_status_up(self):
        try:
            patient_id = self.dialog.get_patient_id_from_user()
            if self.hospital.can_status_up(patient_id):
                self.hospital.status_up(patient_id)
                status_name = self.hospital.get_status_name_by_patient_id(patient_id)
                self.dialog.output_to_user(f"Новый статус пациента: \"{status_name}\"")
            else:
                if self.dialog.patient_discharge_request():
                    self.hospital.discharge(patient_id)
                    self.dialog.output_to_user("Пациент выписан из больницы")
                else:
                    status_name = self.hospital.get_status_name_by_patient_id(patient_id)
                    self.dialog.output_to_user(f"Пациент остался в статусе \"{status_name}\"")
        except (PatientIDNumberError, PatientIDIsNotInHospitalError) as err:
            return self.dialog.output_to_user(err)

    def discharge_patient(self):
        try:
            patient_id = self.dialog.get_patient_id_from_user()
            self.hospital.discharge(patient_id)
            self.dialog.output_to_user("Пациент выписан из больницы")
        except (PatientIDNumberError, PatientIDIsNotInHospitalError) as err:
            return self.dialog.output_to_user(err)

    def patient_status_down(self):
        try:
            patient_id = self.dialog.get_patient_id_from_user()
            if self.hospital.can_status_down(patient_id):
                self.hospital.status_down(patient_id)
                status_name = self.hospital.get_status_name_by_patient_id(patient_id)
                self.dialog.output_to_user(f"Новый статус пациента: \"{status_name}\"")
            else:
                self.dialog.output_to_user("Ошибка. Нельзя понизить самый низкий статус (наши пациенты не умирают)")
        except (PatientIDNumberError, PatientIDIsNotInHospitalError) as err:
            return self.dialog.output_to_user(err)
