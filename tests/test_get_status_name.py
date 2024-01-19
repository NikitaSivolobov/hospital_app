import pytest

from exceptions_hospital import PatientNotExistsError
from hospital import Hospital


class TestGetStatusNameByPatientIdInHospital:
    """Тестовый класс, проверяющий получение статуса по patient_id в hospital"""
    hospital = Hospital()

    @pytest.mark.parametrize("test_name, patients_list, patient_id, expected_status_name", [
        ("проверка списка пациентов с одним статусом",      [1, 1, 1, 1],          1, "Болен"),
        ("проверка списка пациентов с разными статусами",   [0, 1, 2, 3],          1, "Тяжело болен"),
        ("проверка списка пациентов с одним пациентом",     [2],                   1, "Слегка болен"),

        ("проверка получения статуса \"Тяжело болен\"",     [0, 1, 0, 2, 0, 3, 0], 3, "Тяжело болен"),
        ("проверка получения статуса \"Болен\"",            [0, 1, 0, 2, 0, 3, 0], 2, "Болен"),
        ("проверка получения статуса \"Слегка болен\"",     [0, 1, 0, 2, 0, 3, 0], 4, "Слегка болен"),
        ("проверка получения статуса \"Готов к выписке\"",  [0, 1, 0, 2, 0, 3, 0], 6, "Готов к выписке")
    ])
    def test_get_status_name_by_valid_patient_id(self, test_name, patients_list, patient_id, expected_status_name):
        self.hospital._patients_list = patients_list
        actual_status_name = self.hospital.get_status_name_by_patient_id(patient_id)
        assert actual_status_name == expected_status_name, (f"В тест кейсе \"{test_name}\" "
                                                            f"actual_status_name - \"{actual_status_name}\" не "
                                                            f"совпадает со  статусом "
                                                            f"expected_status_name - \"{expected_status_name}\"")

    @pytest.mark.parametrize("test_name, patients_list, patient_id", [
        ("проверка исключения при обращении к граничному значению patient_id в списке пациентов", [0, 1, 2, 3], 5),
        ("проверка исключения при значении patient_id выше диапазона значений в списке пациентов", [0, 1, 2, 3], 100),
        ("проверка исключения при обращении к граничному значению patient_id, когда список пустой", [], 1),
        ("проверка исключения при значении patient_id выше диапазона значений, когда список пустой", [], 10)
    ])
    def test_get_status_name_by_invalid_patient_id_above_range(self, test_name, patients_list, patient_id):
        self.hospital._patients_list = patients_list
        with pytest.raises(PatientNotExistsError) as excinfo:
            self.hospital.get_status_name_by_patient_id(patient_id)
        assert str(excinfo.value) == "Ошибка. В больнице нет пациента с таким ID", (f"В тест кейсе \"{test_name}\" "
                                                                                    "не совпадает текст ошибки "
                                                                                    "исключения")
