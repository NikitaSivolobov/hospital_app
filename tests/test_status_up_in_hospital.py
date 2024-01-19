import pytest

from hospital import Hospital


class TestStatusUpInHospital:
    """Тестовый класс, проверяющий метод повышения статуса пациента в больнице"""

    hospital = Hospital()
    hospital._patients_list = [0, 1, 2, 3]

    @pytest.mark.parametrize("patient_id, expected_old_status_name, expected_new_status_name", [
        (1, "Тяжело болен", "Болен"),
        (2, "Болен", "Слегка болен"),
        (3, "Слегка болен", "Готов к выписке")
    ])
    def test_status_up(self, patient_id, expected_old_status_name, expected_new_status_name):
        old_status_name = self.hospital.get_status_name_by_patient_id(patient_id)
        assert old_status_name == expected_old_status_name

        self.hospital.status_up(patient_id)
        actual_status_name = self.hospital.get_status_name_by_patient_id(patient_id)

        assert old_status_name != actual_status_name
        assert actual_status_name == expected_new_status_name
