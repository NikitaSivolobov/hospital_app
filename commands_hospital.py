from exceptions_hospital import PatientIDNumberError, PatientNotExistsError


class CommandsHospital:
    def __init__(self, hospital, dialog_with_user):
        self.hospital = hospital
        self.dialog = dialog_with_user

    @staticmethod
    def _convert_hospital_data_to_calculate_statistics(total_patients: int, status_counts: dict) -> str:
        calculate_statistics = f"В больнице на данный момент находится {total_patients} чел., из них:\n"
        for status, count in status_counts.items():
            if count != 0:
                calculate_statistics += f"\t- в статусе \"{status}\": {count} чел.\n"
        return calculate_statistics.rstrip("\n")

    def calculate_hospital_statistics(self):
        total_patients = self.hospital.get_total_patients()
        status_count = self.hospital.get_status_counts()
        calculate_statistics = self._convert_hospital_data_to_calculate_statistics(total_patients, status_count)
        self.dialog.send_message(calculate_statistics)

    def get_status_patient(self):
        try:
            patient_id = self.dialog.request_patient_id()
            status_name = self.hospital.get_status_name_by_patient_id(patient_id)
            self.dialog.send_message(f"Статус пациента: \"{status_name}\"")
        except (PatientIDNumberError, PatientNotExistsError) as err:
            self.dialog.send_message(str(err))

    def patient_status_up(self):
        try:
            patient_id = self.dialog.request_patient_id()
            if self.hospital.can_status_up(patient_id):
                self.hospital.status_up(patient_id)
                status_name = self.hospital.get_status_name_by_patient_id(patient_id)
                self.dialog.send_message(f"Новый статус пациента: \"{status_name}\"")
            else:
                if self.dialog.request_confirm_for_patient_discharge():
                    self.hospital.discharge(patient_id)
                    self.dialog.send_message("Пациент выписан из больницы")
                else:
                    status_name = self.hospital.get_status_name_by_patient_id(patient_id)
                    self.dialog.send_message(f"Пациент остался в статусе \"{status_name}\"")
        except (PatientIDNumberError, PatientNotExistsError) as err:
            self.dialog.send_message(str(err))

    def discharge_patient(self):
        try:
            patient_id = self.dialog.request_patient_id()
            self.hospital.discharge(patient_id)
            self.dialog.send_message("Пациент выписан из больницы")
        except (PatientIDNumberError, PatientNotExistsError) as err:
            self.dialog.send_message(str(err))

    def patient_status_down(self):
        try:
            patient_id = self.dialog.request_patient_id()
            if self.hospital.can_status_down(patient_id):
                self.hospital.status_down(patient_id)
                status_name = self.hospital.get_status_name_by_patient_id(patient_id)
                self.dialog.send_message(f"Новый статус пациента: \"{status_name}\"")
            else:
                self.dialog.send_message("Ошибка. Нельзя понизить самый низкий статус (наши пациенты не умирают)")
        except (PatientIDNumberError, PatientNotExistsError) as err:
            self.dialog.send_message(str(err))
