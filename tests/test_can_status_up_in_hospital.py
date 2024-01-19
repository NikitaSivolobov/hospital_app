import pytest

from hospital import Hospital


class TestCanStatusUpInHospital:
    """Тестовый класс, проверяющий метод возможности повышения статуса пациента в больнице"""

    hospital = Hospital()
    hospital._patients_list = [0, 1, 2, 3]

    @pytest.mark.parametrize("patient_id, expected_is_status_up", [
        (1, True),
        (2, True),
        (3, True),
        (4, False)
    ])
    def test_can_status_up(self, patient_id, expected_is_status_up):
        actual_is_status_up = self.hospital.can_status_up(patient_id)
        assert actual_is_status_up == expected_is_status_up
