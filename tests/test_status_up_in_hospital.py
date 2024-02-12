import pytest

from exceptions_hospital import PatientNotExistsError
from hospital import Hospital


class TestStatusUpInHospital:
    """Тестовый класс, проверяющий метод повышения статуса пациента в больнице"""

    def test_status_up(self):
        self.hospital = Hospital([1, 1])
        self.hospital.status_up(1)
        assert self.hospital._patients_list == [2, 1]

    def test_status_up_when_patient_id_above_range_patient_list(self):
        self.hospital = Hospital([1])
        with pytest.raises(PatientNotExistsError) as excinfo:
            self.hospital.status_up(2)
        assert str(excinfo.value) == "Ошибка. В больнице нет пациента с таким ID", ("Не совпадает текст ошибки "
                                                                                    "исключения")
