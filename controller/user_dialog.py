class UserDialog:
    """Класс диалога с пользователем (консольное приложение)"""

    def __init__(self, command_service):
        self.command_service = command_service

    def command_input(self) -> str:
        return input("Введите команду: ").strip().lower()

    def command_output(self, output):
        print(f"{output}\n")

    def _patient_id_input(self):
        patient_id_str = input("Введите ID пациента: ").strip().lower()

        try:
            patient_id = int(patient_id_str)
            if patient_id <= 0:
                raise ValueError
        except ValueError:
            return "Ошибка. ID пациента должно быть числом (целым, положительным)"

        return patient_id - 1

    def get_calculate_statistics_from_commands(self):
        return self.command_output(self.command_service.command_calculate_statistics())

    def get_status_from_commands(self):
        patient_id = self._patient_id_input()
        if isinstance(patient_id, str):
            return self.command_output(patient_id)

        status = self.command_service.command_get_status(patient_id)
        try:
            status_name = status.status_name
            return self.command_output(f"Статус пациента: \"{status_name}\"")
        except AttributeError:
            return self.command_output(status)

    def get_discharge_from_commands(self):
        patient_id = self._patient_id_input()
        if isinstance(patient_id, str):
            return self.command_output(patient_id)
        return self.command_output(self.command_service.command_discharge(patient_id))

    def status_down_from_commands(self):
        patient_id = self._patient_id_input()
        if isinstance(patient_id, str):
            return self.command_output(patient_id)
        output = self.command_service.command_status_down(patient_id)
        if not output:
            output = "Ошибка. Нельзя понизить самый низкий статус (наши пациенты не умирают)"
        return self.command_output(output)

    def status_up_from_commands(self):
        patient_id = self._patient_id_input()
        if isinstance(patient_id, str):
            return self.command_output(patient_id)
        return self.command_output(self.command_service.command_status_up(patient_id))
