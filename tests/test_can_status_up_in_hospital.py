import hospital

"""метод возможности повышения статуса пациента в больнице"""


def test_can_status_up_when_not_highest_status_code():
    patient_list = [0]
    actual_is_status_up = hospital.can_status_up(1, patient_list)
    assert actual_is_status_up is True


def test_can_status_up_when_highest_status_code():
    patient_list = [3]
    actual_is_status_up = hospital.can_status_up(1, patient_list)
    assert actual_is_status_up is False
