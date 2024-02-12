from unittest.mock import MagicMock

from commands_hospital import CommandsHospital
from hospital import Hospital


class TestCommandGetStatusPatient:
    """Тестовый класс, проверяющий метод команды получения статуса пациента"""

    def test_get_status_patient(self):
        self.command = CommandsHospital(Hospital([0, 0]), MagicMock())
        self.command.dialog.request_patient_id = MagicMock(return_value=2)
        self.command.dialog.send_message = MagicMock()

        self.command.get_status_patient()

        assert self.command.hospital._patients_list == [0, 0]
        self.command.dialog.send_message.assert_called_with("Статус пациента: \"Тяжело болен\"")

    def test_get_status_patient_when_patient_id_above_range_patient_list(self):
        self.command = CommandsHospital(Hospital([0]), MagicMock())
        self.command.dialog.request_patient_id = MagicMock(return_value=2)
        self.command.dialog.send_message = MagicMock()

        self.command.get_status_patient()

        assert self.command.hospital._patients_list == [0]
        self.command.dialog.send_message.assert_called_with("Ошибка. В больнице нет пациента с таким ID")

    def test_get_status_patient_when_empty_patient_list(self):
        self.command = CommandsHospital(Hospital([]), MagicMock())
        self.command.dialog.request_patient_id = MagicMock(return_value=2)
        self.command.dialog.send_message = MagicMock()

        self.command.get_status_patient()

        assert self.command.hospital._patients_list == []
        self.command.dialog.send_message.assert_called_with("Ошибка. В больнице нет пациента с таким ID")


class TestCommandPatientStatusUp:
    """Тестовый класс, проверяющий метод команды повышения статуса пациента"""

    def test_status_up(self):
        self.command = CommandsHospital(Hospital([0, 0]), MagicMock())
        self.command.dialog.request_patient_id = MagicMock(return_value=2)
        self.command.dialog.send_message = MagicMock()

        self.command.patient_status_up()

        assert self.command.hospital._patients_list == [0, 1]
        self.command.dialog.send_message.assert_called_with("Новый статус пациента: \"Болен\"")

    def test_status_up_when_discharge_patient(self):
        self.command = CommandsHospital(Hospital([0, 3]), MagicMock())
        self.command.dialog.request_patient_id = MagicMock(return_value=2)
        self.command.dialog.request_confirm_for_patient_discharge = MagicMock(return_value=True)
        self.command.dialog.send_message = MagicMock()

        self.command.patient_status_up()

        assert self.command.hospital._patients_list == [0]
        self.command.dialog.send_message.assert_called_with("Пациент выписан из больницы")

    def test_status_up_when_discharge_patient_false(self):
        self.command = CommandsHospital(Hospital([0, 3]), MagicMock())
        self.command.dialog.request_patient_id = MagicMock(return_value=2)
        self.command.dialog.request_confirm_for_patient_discharge = MagicMock(return_value=False)
        self.command.dialog.send_message = MagicMock()

        self.command.patient_status_up()

        assert self.command.hospital._patients_list == [0, 3]
        self.command.dialog.send_message.assert_called_with("Пациент остался в статусе \"Готов к выписке\"")

    def test_status_up_when_patient_id_above_range_patient_list(self):
        self.command = CommandsHospital(Hospital([0]), MagicMock())
        self.command.dialog.request_patient_id = MagicMock(return_value=2)
        self.command.dialog.send_message = MagicMock()

        self.command.patient_status_up()

        assert self.command.hospital._patients_list == [0]
        self.command.dialog.send_message.assert_called_with("Ошибка. В больнице нет пациента с таким ID")

    def test_status_up_patient_when_empty_patient_list(self):
        self.command = CommandsHospital(Hospital([]), MagicMock())
        self.command.dialog.request_patient_id = MagicMock(return_value=2)
        self.command.dialog.send_message = MagicMock()

        self.command.patient_status_up()

        assert self.command.hospital._patients_list == []
        self.command.dialog.send_message.assert_called_with("Ошибка. В больнице нет пациента с таким ID")
