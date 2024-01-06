class UserDialogWithConsole:
    """Класс диалога с пользователем при помощи консольного ввода/вывода"""

    def __init__(self, commands_use_cases):
        self.commands_use_cases = commands_use_cases

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

    def process_discharge_request(self):
        while True:
            discharge_input = input("Желаете этого клиента выписать? (да/нет): ").strip().lower()
            if discharge_input == 'да':
                return True
            elif discharge_input == 'нет':
                return False
            else:
                print("Некорректный ввод. Пожалуйста, ответьте (да) или (нет)."), False

    def get_calculate_statistics_from_commands(self):
        total_patients, status_counts = self.commands_use_cases.command_calculate_statistics()
        output = f"В больнице на данный момент находится {total_patients} чел., из них:\n"
        for status, count in status_counts.items():
            if count != 0:
                output += f"\t- в статусе \"{status}\": {count} чел.\n"
        return self.command_output(output.rstrip("\n"))

    def get_status_from_commands(self):
        patient_id = self._patient_id_input()
        if isinstance(patient_id, str):
            return self.command_output(patient_id)

        status = self.commands_use_cases.command_get_status(patient_id)
        try:
            status_name = status.status_name
            return self.command_output(f"Статус пациента: \"{status_name}\"")
        except AttributeError:
            return self.command_output(f"{status}")

    def get_discharge_from_commands(self):
        patient_id = self._patient_id_input()
        if isinstance(patient_id, str):
            return self.command_output(patient_id)
        output = self.commands_use_cases.command_discharge(patient_id)
        if output:
            return self.command_output("Пациент выписан из больницы")
        else:
            raise KeyError("Возникла проблема при выписке пациента из больницы")

    def status_down_from_commands(self):
        patient_id = self._patient_id_input()
        if isinstance(patient_id, str):
            return self.command_output(patient_id)
        status = self.commands_use_cases.command_status_down(patient_id)
        if isinstance(status, str):
            return self.command_output(status)
        try:
            status_name = status.status_name
            return self.command_output(f"Новый статус пациента: \"{status_name}\"")
        except AttributeError:
            return self.command_output("Ошибка. Нельзя понизить самый низкий статус (наши пациенты не умирают)")

    def status_up_from_commands(self):
        patient_id = self._patient_id_input()
        if isinstance(patient_id, str):
            return self.command_output(patient_id)
        status, is_discharge = self.commands_use_cases.command_status_up(patient_id)
        # если статус не превышает максимальный, то идёт стандартное повышение статуса и is_discharge = False
        if not is_discharge:
            try:
                status_name = status.status_name
                return self.command_output(f"Новый статус пациента: \"{status_name}\"")
            except AttributeError:
                return self.command_output(f"{status}")
        else:
            # при повышении максимального запускается процесс запроса выписки пациента
            is_command_discharge = self.process_discharge_request()
            if is_command_discharge:
                output = self.commands_use_cases.command_discharge(patient_id)
                if output:
                    return self.command_output("Пациент выписан из больницы")
                else:
                    raise KeyError("Возникла проблема при выписке пациента из больницы")
            else:
                status = self.commands_use_cases.command_get_status(patient_id)
                try:
                    status_name = status.status_name
                    return self.command_output(f"Пациент остался в статусе \"{status_name}\"")
                except AttributeError:
                    return self.command_output(f"{status}")
