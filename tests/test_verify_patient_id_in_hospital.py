import pytest

from exceptions_hospital import PatientNotExistsError
from hospital import Hospital


class TestVerifyPatientIdInHospital:
    """Тестовый класс, проверяющий наличие/отсутствие patient_id
                   в hospital (отсутствие/выброс исключения)"""

    hospital = Hospital()

    def test_verify_patient_id(self):
        self.hospital._patients_list = [0, 1]
        self.hospital._verify_patient_id(1)

    def test_verify_patient_id_when_patient_id_above_range_default_patient_list(self):
        with pytest.raises(PatientNotExistsError) as excinfo:
            self.hospital._verify_patient_id(201)
        assert str(excinfo.value) == "Ошибка. В больнице нет пациента с таким ID", ("Не совпадает текст ошибки "
                                                                                    "исключения")
