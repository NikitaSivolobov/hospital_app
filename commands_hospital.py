class CommandsHospital:
    def __init__(self, hospital, user_dialog):
        self.hospital = hospital
        self.dialog = user_dialog

    def get_command_from_user(self):
        return self.dialog.get_input_from_user()

    def output_to_user_from_app(self, value):
        self.dialog.output_to_user(value)

    def command_calculate_hospital_statistics(self):
        total_patients = self.hospital.get_total_patients()
        status_counts = self.hospital.get_status_counts()
        calculate_statistics = f"В больнице на данный момент находится {total_patients} чел., из них:\n"
        for status, count in status_counts.items():
            if count != 0:
                calculate_statistics += f"\t- в статусе \"{status}\": {count} чел.\n"
        self.dialog.output_to_user(calculate_statistics.rstrip("\n"))

    def command_get_status_patient(self):
        patient_id = self.dialog.get_patient_id_from_user()
        is_valid_patient_id = self.hospital.is_valid_patient_id(patient_id)
        if isinstance(is_valid_patient_id, str):
            self.dialog.output_to_user(is_valid_patient_id)
        else:
            status_name_patient = self.hospital.get_status_name(is_valid_patient_id)
            self.dialog.output_to_user(f"Статус пациента: \"{status_name_patient}\"")

    def command_patient_status_up(self):
        patient_id = self.dialog.get_patient_id_from_user()
        is_valid_patient_id = self.hospital.is_valid_patient_id(patient_id)
        if isinstance(is_valid_patient_id, str):
            self.dialog.output_to_user(is_valid_patient_id)
        else:
            self._process_patient_status_up(is_valid_patient_id)

    def _process_patient_status_up(self, valid_patient_id):
        is_valid_patient_status_for_up = self.hospital.check_status_patient_for_up(valid_patient_id)
        if is_valid_patient_status_for_up:
            self.hospital.status_up(valid_patient_id)
            new_status_name_patient = self.hospital.get_status_name(valid_patient_id)
            self.dialog.output_to_user(f"Новый статус пациента: \"{new_status_name_patient}\"")
        else:
            self._process_patient_discharge(valid_patient_id)

    def _process_patient_discharge(self, valid_patient_id):
        is_discharge_patient = self.dialog.process_discharge_request()
        if is_discharge_patient:
            self.hospital.discharge(valid_patient_id)
            self.dialog.output_to_user("Пациент выписан из больницы")
        else:
            status_name_patient = self.hospital.get_status_name(valid_patient_id)
            self.dialog.output_to_user(f"Пациент остался в статусе \"{status_name_patient}\"")

    # TODO: Реализовать метод для команды "выписать пациента" / "discharge"
    def command_discharge(self, patient_id):
        pass

    # TODO: Реализовать метод для команды "понизить статус пациента" / "status down"
    def command_patient_status_down(self, patient_id):
        pass
