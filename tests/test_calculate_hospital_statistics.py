import pytest

from commands_hospital import CommandsHospital
from console_dialog_with_user import ConsoleDialogWithUser
from hospital import Hospital


class TestGetDataFromHospital:
    """Тестовый класс, проверяющий метод получения данных из больницы"""

    hospital = Hospital()

    def test_get_default_total_patients(self):
        # выбраны такие граничные условия, так как на начало сеанса в больнице содержится 200 пациентов (patients)
        total_patients = self.hospital.get_total_patients()
        assert total_patients == 200

    @pytest.mark.parametrize("patients_list, expected_total_patients", [
        ([0, 1, 2, 3], 4),
        ([1, 2, 1, 3, 2, 1], 6),
        ([2], 1),
        ([], 0),
        ([-30, -1, 4, 30], 4)
    ])
    def test_get_total_patients(self, patients_list, expected_total_patients):
        self.hospital._patients_list = patients_list
        actual_total_patients = self.hospital.get_total_patients()
        assert actual_total_patients == expected_total_patients

    def test_get_default_status_counts(self):
        # выбраны такие граничные условия, так как на начало сеанса в больнице содержится
        # 200 пациентов (patients), все в статусе "Болен".
        self.hospital = Hospital()   # если эту строчку убрать, то почему-то не стабильное поведение
        status_counts = self.hospital.get_status_counts()
        assert status_counts == {"Болен": 200, "Слегка болен": 0, "Готов к выписке": 0, "Тяжело болен": 0}

    @pytest.mark.parametrize("patients_list, expected_status_counts", [
        # проверка разных статусов без повторяющихся значений
        ([0, 1, 2, 3], {'Болен': 1, 'Готов к выписке': 1, 'Слегка болен': 1, 'Тяжело болен': 1}),
        # проверка разных статусов с повторяющимися значениями
        ([1, 2, 1, 3, 2, 1], {"Болен": 3, "Слегка болен": 2, "Готов к выписке": 1, "Тяжело болен": 0}),
        # проверка списка с одним значением
        # (возможно лишняя, так как аналогичен проверке в test_get_default_status_counts)
        ([2], {"Болен": 0, "Слегка болен": 1, "Готов к выписке": 0, "Тяжело болен": 0}),

        # проверка с пустым списком пациентов
        ([], {"Болен": 0, "Слегка болен": 0, "Готов к выписке": 0, "Тяжело болен": 0}),
        # проверка списка с невалидными статусами
        ([-30, -1, 4, 30], {"Болен": 0, "Слегка болен": 0, "Готов к выписке": 0, "Тяжело болен": 0})
    ])
    def test_get_status_counts(self, patients_list, expected_status_counts):
        self.hospital._patients_list = patients_list
        actual_status_counts = self.hospital.get_status_counts()
        assert actual_status_counts == expected_status_counts


class TestCalculateStatisticsFromHospitalData:
    """Тестовый класс, проверяющий метод формирования расчёта статистики из полученных из больницы данных"""

    hospital = Hospital()
    dialog = ConsoleDialogWithUser()
    commands_hospital = CommandsHospital(hospital, dialog)

    def test_default_calculate_hospital_statistics(self):
        total_patients = self.hospital.get_total_patients()
        status_count = self.hospital.get_status_counts()
        calculate_statistics = (self.commands_hospital
                                ._convert_hospital_data_to_calculate_statistics(total_patients, status_count))

        assert calculate_statistics == "В больнице на данный момент находится 200 чел., из них:\n" \
                                       "\t- в статусе \"Болен\": 200 чел."

    @pytest.mark.parametrize("patients_list, expected_calculate_statistics", [
        # проверка разных статусов без повторяющихся значений
        ([0, 1, 2, 3], "В больнице на данный момент находится 4 чел., из них:\n"
                       "\t- в статусе \"Тяжело болен\": 1 чел.\n"
                       "\t- в статусе \"Болен\": 1 чел.\n"
                       "\t- в статусе \"Слегка болен\": 1 чел.\n"
                       "\t- в статусе \"Готов к выписке\": 1 чел."),

        # проверка разных статусов с повторяющимися значениями
        ([1, 2, 1, 3, 2, 1], "В больнице на данный момент находится 6 чел., из них:\n"
                             "\t- в статусе \"Болен\": 3 чел.\n"
                             "\t- в статусе \"Слегка болен\": 2 чел.\n"
                             "\t- в статусе \"Готов к выписке\": 1 чел."),

        # проверка списка с одним значением
        # (возможно лишняя, так как аналогичен проверке в test_default_calculate_hospital_statistics)
        ([2], "В больнице на данный момент находится 1 чел., из них:\n"
              "\t- в статусе \"Слегка болен\": 1 чел."),

        # проверка с пустым списком пациентов
        ([], "В больнице на данный момент находится 0 чел., из них:"),
        # проверка списка с невалидными статусами
        ([-30, -1, 4, 30], "В больнице на данный момент находится 4 чел., из них:")
    ])
    def test_calculate_hospital_statistics(self, patients_list, expected_calculate_statistics):
        self.hospital._patients_list = patients_list
        total_patients = self.hospital.get_total_patients()
        status_count = self.hospital.get_status_counts()
        actual_calculate_statistics = (self.commands_hospital
                                       ._convert_hospital_data_to_calculate_statistics(total_patients, status_count))

        assert actual_calculate_statistics == expected_calculate_statistics
