class PatientNotExistsError(Exception):
    """Класс исключения отсутствия patient_id в hospital"""

    def __init__(self, *args):
        self.message = args[0] if args else None

    def __str__(self):
        return "Ошибка. В больнице нет пациента с таким ID"


class PatientIDNumberError(Exception):
    """Класс исключения patient_id не валидное число"""

    def __init__(self, *args):
        self.message = args[0] if args else None

    def __str__(self):
        return "Ошибка. ID пациента должно быть числом (целым, положительным)"
