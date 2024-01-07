class HospitalError(Exception):
    """Класс исключений при работе с hospital"""

    def __init__(self, *args):
        self.message = args[0] if args else None

    def __str__(self):
        return f"Ошибка. {self.message}"


class PatientIDIsNotInHospitalError(HospitalError):
    """Класс исключения отсутствия patient_id в hospital"""

    def __init__(self, *args):
        self.message = args[0] if args else None

    def __str__(self):
        return f"Ошибка. {self.message}"


class PatientIDNumberError(HospitalError):
    """Класс исключения patient_id не валидное число"""

    def __init__(self, *args):
        self.message = args[0] if args else None

    def __str__(self):
        return f"Ошибка. {self.message}"
