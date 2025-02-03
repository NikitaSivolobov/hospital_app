import pytest

import hospital
from exceptions_hospital import PatientNotExistsError

"""метод повышения статуса пациента в больнице"""


def test_status_up():
    patients_list = [1, 1]
    hospital.status_up(1, patients_list)
    assert hospital._patients_list == [2, 1]


def test_status_up_when_patient_id_above_range_patient_list():
    patients_list = [1]
    with pytest.raises(PatientNotExistsError) as excinfo:
        hospital.status_up(2, patients_list)
    assert str(excinfo.value) == "Ошибка. В больнице нет пациента с таким ID", ("Не совпадает текст ошибки "
                                                                                "исключения")
