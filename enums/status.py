from enum import Enum


class Status(Enum):
    STATUS_00 = (0, "Тяжело болен")
    STATUS_01 = (1, "Болен")
    STATUS_02 = (2, "Слегка болен")
    STATUS_03 = (3, "Готов к выписке")

    def __init__(self, status_code, status_name):
        self.status_code = status_code
        self.status_name = status_name

    @classmethod
    def get_last_status(cls):
        last_status = None
        for status in cls:
            last_status = status
        return last_status

    @classmethod
    def get_first_status(cls):
        return next(iter(cls))

    @classmethod
    def get_status_by_code(cls, code):
        for status in cls:
            if status.status_code == code:
                return status
        return None

    @classmethod
    def calculate_statistics(cls, patients_list):
        total_patients = len(patients_list)
        status_counts = {}
        for status in cls:
            status_counts[status.status_name] = patients_list.count(status.status_code)

        print(f"В больнице на данный момент находится {total_patients} чел., из них:")
        for status, count in status_counts.items():
            if count != 0:
                print(f"\t- в статусе \"{status}\": {count} чел.")
