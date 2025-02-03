import pytest

import hospital
from exceptions_hospital import PatientNotExistsError

"""Тестовый модуль, проверяющий наличие/отсутствие patient_id
               в hospital (отсутствие/выброс исключения)"""


def test_verify_patient_id():
    patients_list = [0, 1]
    hospital._verify_patient_id(1, patients_list)


def test_verify_patient_id_when_patient_id_above_range_default_patient_list():
    patients_list = [1, 1]
    with pytest.raises(PatientNotExistsError) as excinfo:
        hospital._verify_patient_id(3, patients_list)
    assert str(excinfo.value) == "Ошибка. В больнице нет пациента с таким ID", ("Не совпадает текст ошибки "
                                                                                "исключения")
