import pytest

from exceptions_hospital import PatientNotExistsError
from hospital import Hospital


class TestVerifyPatientIdInHospital:
    """Тестовый класс, проверяющий наличие/отсутствие patient_id
                   в hospital (отсутствие/выброс исключения)"""

    hospital = Hospital()

    @pytest.mark.parametrize("test_name, patient_id", [
        # выбраны такие граничные условия, так как на начало сеанса в больнице содержится 200 пациентов (patients)
        ("проверка граничного значения", 201),
        ("проверка в диапозоне значений", 2000)
    ])
    def test_verify_invalid_patient_id(self, test_name, patient_id):
        with pytest.raises(PatientNotExistsError) as excinfo:
            self.hospital.get_status_name_by_patient_id(patient_id)
        assert str(excinfo.value) == "Ошибка. В больнице нет пациента с таким ID", (f"В тест кейсе \"{test_name}\" "
                                                                                    "не совпадает текст ошибки "
                                                                                    "исключения")

    @pytest.mark.parametrize("patient_id", [
        # выбраны такие граничные условия, так как на начало сеанса в больнице содержится 200 пациентов (patients)
        -2000, -1, 0, 99, 101.123, 2, 199, 200
    ])
    def test_verify_valid_patient_id(self, patient_id):
        self.hospital._verify_patient_id(patient_id)
