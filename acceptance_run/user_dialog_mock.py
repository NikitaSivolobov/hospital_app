from io_presenters.user_dialog_with_console import UserDialogWithConsole


class UserDialogMock(UserDialogWithConsole):
    """Мок класса диалога с пользователем для Приёмочного теста № 1 (базовый сценарий)"""
    count = 0

    def __init__(self, command_service):
        super().__init__(command_service)
        self.command_service = command_service

    def command_input(self, value) -> str:
        value = value.strip().lower()
        print(f"Введите команду: {value}")
        return value

    def _patient_id_input(self):
        if self.count == 0:
            id_pat = 199
            self.count += 1
        else:
            self.count += 1
            id_pat = self.count
        try:
            id_pat = int(id_pat)
            if id_pat <= 0:
                raise ValueError
        except ValueError:
            return "Ошибка. ID пациента должно быть числом (целым, положительным)"
        print(f"Введите ID пациента: {id_pat}")
        return id_pat


class UserDialogMockConstYes(UserDialogWithConsole):
    """Мок класса диалога с пользователем для Приёмочного теста № 4 (попытка повысить самый высокий статус,"
              " которая приводит к выписке пациента) с выбором \"Да\" для выписки пациента"""

    def __init__(self, command_service):
        super().__init__(command_service)
        self.command_service = command_service

    def command_input(self, value) -> str:
        value = value.strip().lower()
        print(f"Введите команду: {value}")
        return value

    def _patient_id_input(self):
        self.count = 1
        id_pat = self.count
        print(f"Введите ID пациента: {id_pat}")
        try:
            id_pat = int(id_pat)
            if id_pat <= 0:
                raise ValueError
        except ValueError:
            return "Ошибка. ID пациента должно быть числом (целым, положительным)"

        return id_pat

    def process_discharge_request(self, value):
        value = value.strip().lower()
        print(f"Желаете этого клиента выписать? (да/нет): {value}")
        discharge_input = value
        while True:
            # discharge_input = input("Желаете этого клиента выписать? (да/нет): ").strip().lower()
            if discharge_input == 'да':
                return True
            elif discharge_input == 'нет':
                return False
            else:
                print("Некорректный ввод. Пожалуйста, ответьте (да) или (нет)."), False

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
            is_command_discharge = self.process_discharge_request("   Да")
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


class UserDialogMockConstNo(UserDialogWithConsole):
    """Мок класса диалога с пользователем для Приёмочного теста № 5 (попытка повысить самый высокий статус,
     которая ни к чему не приводит) с выбором \"Нет\" для выписки пациента"""

    def __init__(self, command_service):
        super().__init__(command_service)
        self.command_service = command_service

    def command_input(self, value) -> str:
        value = value.strip().lower()
        print(f"Введите команду: {value}")
        return value

    def _patient_id_input(self):
        self.count = 1
        id_pat = self.count
        print(f"Введите ID пациента: {id_pat}")
        try:
            id_pat = int(id_pat)
            if id_pat <= 0:
                raise ValueError
        except ValueError:
            return "Ошибка. ID пациента должно быть числом (целым, положительным)"

        return id_pat

    def process_discharge_request(self, value):
        value = value.strip().lower()
        print(f"Желаете этого клиента выписать? (да/нет): {value}")
        discharge_input = value
        while True:
            # discharge_input = input("Желаете этого клиента выписать? (да/нет): ").strip().lower()
            if discharge_input == 'да':
                return True
            elif discharge_input == 'нет':
                return False
            else:
                print("Некорректный ввод. Пожалуйста, ответьте (да) или (нет)."), False

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
            is_command_discharge = self.process_discharge_request(" нЕт   ")
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


class UserDialogMockNegativeVar(UserDialogWithConsole):
    """Мок Класса диалога с пользователем для Приёмочного теста № 3 (случаи ввода пользователем некорректных данных)"""
    count = 0

    def __init__(self, command_service):
        super().__init__(command_service)
        self.command_service = command_service

    def command_input(self, value) -> str:
        value = value.strip().lower()
        print(f"Введите команду: {value}")
        return value

    def _patient_id_input(self):
        if self.count == 0:
            id_pat = "два"
            self.count += 1
        elif self.count == 1:
            id_pat = -2
            self.count += 1
        elif self.count == 2:
            id_pat = 201
            self.count += 1
        else:
            id_pat = self.count
            self.count += 1
        try:
            print(f"Введите ID пациента: {id_pat}")
            id_pat = int(id_pat)
            if id_pat <= 0:
                raise ValueError
        except ValueError:
            return "Ошибка. ID пациента должно быть числом (целым, положительным)"

        id_pat -= 1
        return id_pat
