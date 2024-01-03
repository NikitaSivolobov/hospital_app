from enums.status import Status


class CommandsService:
    def __init__(self, hospital):
        self.hospital = hospital

    def __validate_patient_id(self, patient_id):
        if patient_id >= len(self.hospital.patients_list):
            return "Ошибка. В больнице нет пациента с таким ID"
        else:
            return patient_id

    def command_calculate_statistics(self):
        return self.hospital.calculate_statistics()

    def command_get_status(self, patient_id):
        patient_id = self.__validate_patient_id(patient_id)
        if isinstance(patient_id, str):
            return patient_id
        return self.hospital.get_status(patient_id)

    def command_discharge(self, patient_id):
        patient_id = self.__validate_patient_id(patient_id)
        if isinstance(patient_id, str):
            return patient_id
        return self.hospital.discharge(patient_id)

    def command_status_down(self, patient_id):
        patient_id = self.__validate_patient_id(patient_id)
        if isinstance(patient_id, str):
            return patient_id
        status = self.hospital.get_status(patient_id)
        if status.status_code > Status.get_first_status().status_code:
            return self.hospital.status_down(patient_id)
        else:
            return False

    def command_status_up(self, patient_id):
        patient_id = self.__validate_patient_id(patient_id)
        if isinstance(patient_id, str):
            return patient_id

        status = self.hospital.get_status(patient_id)
        if status.status_code < Status.get_last_status().status_code:
            return self.hospital.status_up(patient_id)
        else:
            return self.hospital.status_patient_id_change(patient_id)
