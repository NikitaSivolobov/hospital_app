import pytest

from exceptions_hospital import PatientNotExistsError
from hospital import Hospital


class TestGetStatusNameByPatientIdInHospital:
    """Тестовый класс, проверяющий получение статуса по patient_id в hospital"""
    hospital = Hospital()

    def test_get_status_name_by_patient_id(self):
        self.hospital._patients_list = [0, 1]
        actual_status_name = self.hospital.get_status_name_by_patient_id(1)
        assert actual_status_name == "Тяжело болен"

    def test_get_status_name_by_patient_id_when_patient_id_above_range_patient_list(self):
        self.hospital._patients_list = [1]
        with pytest.raises(PatientNotExistsError) as excinfo:
            self.hospital.get_status_name_by_patient_id(2)
        assert str(excinfo.value) == "Ошибка. В больнице нет пациента с таким ID", ("Не совпадает текст ошибки "
                                                                                    "исключения")

    @pytest.mark.parametrize("test_name, patients_list, patient_id, expected_status_name", [
        ("проверка статуса \"Тяжело болен\"",       [0], 1, "Тяжело болен"),
        ("проверка статуса \"Болен\"",              [1], 1, "Болен"),
        ("проверка статуса \"Слегка болен\"",       [2], 1, "Слегка болен"),
        ("проверка статуса \"Готов к выписке\"",    [3], 1, "Готов к выписке")
    ])
    def test_status_name_text(self, test_name, patients_list, patient_id, expected_status_name):
        self.hospital._patients_list = patients_list
        actual_status_name = self.hospital.get_status_name_by_patient_id(patient_id)
        assert actual_status_name == expected_status_name, (f"В тест кейсе \"{test_name}\" "
                                                            f"actual_status_name - \"{actual_status_name}\" не "
                                                            f"совпадает со статусом "
                                                            f"expected_status_name - \"{expected_status_name}\"")
