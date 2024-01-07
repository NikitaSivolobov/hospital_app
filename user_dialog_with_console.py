class UserDialogWithConsole:
    """Класс диалога с пользователем при помощи консольного ввода/вывода"""

    @staticmethod
    def get_input_from_user() -> str:
        return input("Введите команду: ").strip().lower()

    @staticmethod
    def get_patient_id_from_user() -> str:
        return input("Введите ID пациента: ").strip().lower()

    def process_discharge_request(self) -> str:
        while True:
            discharge_input = input("Желаете этого клиента выписать? (да/нет): ").strip().lower()
            if discharge_input == 'да':
                return True
            elif discharge_input == 'нет':
                return False  # Status.STATUS_03.status_code
            else:
                self.output_to_user("Некорректный ввод. Пожалуйста, ответьте (да) или (нет).")

    @staticmethod
    def output_to_user(output):
        print(f"{output}\n")
