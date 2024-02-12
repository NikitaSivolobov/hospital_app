from hospital import Hospital


class TestCanStatusUpInHospital:
    """Тестовый класс, проверяющий метод возможности повышения статуса пациента в больнице"""

    def test_can_status_up_when_not_highest_status_code(self):
        self.hospital = Hospital([0])
        actual_is_status_up = self.hospital.can_status_up(1)
        assert actual_is_status_up is True

    def test_can_status_up_when_highest_status_code(self):
        self.hospital = Hospital([3])
        actual_is_status_up = self.hospital.can_status_up(1)
        assert actual_is_status_up is False
