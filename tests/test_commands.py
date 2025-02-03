from unittest.mock import MagicMock

import commands_hospital as command
import hospital


"""метод команды получения статуса пациента"""

def test_get_status_patient():
    command.dialog.request_patient_id = MagicMock(return_value=2)
    command.dialog.send_message = MagicMock()
    command.get_status_patient([0, 0])
    command.dialog.send_message.assert_called_with("Статус пациента: \"Тяжело болен\"")

def test_get_status_patient_when_patient_id_above_range_patient_list():
    command.dialog.request_patient_id = MagicMock(return_value=2)
    command.dialog.send_message = MagicMock()
    command.get_status_patient([0])
    command.dialog.send_message.assert_called_with("Ошибка. В больнице нет пациента с таким ID")

def test_get_status_patient_when_empty_patient_list():
    command.dialog.request_patient_id = MagicMock(return_value=2)
    command.dialog.send_message = MagicMock()
    command.get_status_patient([])
    command.dialog.send_message.assert_called_with("Ошибка. В больнице нет пациента с таким ID")



"""метод команды повышения статуса пациента"""

def test_status_up():
    command.dialog.request_patient_id = MagicMock(return_value=2)
    command.dialog.send_message = MagicMock()

    command.patient_status_up([0, 0])

    assert command.hospital._patients_list == [0, 1]
    command.dialog.send_message.assert_called_with("Новый статус пациента: \"Болен\"")

def test_status_up_when_discharge_patient():
    command.dialog.request_patient_id = MagicMock(return_value=2)
    command.dialog.request_confirm_for_patient_discharge = MagicMock(return_value=True)
    command.dialog.send_message = MagicMock()
    command.patient_status_up([0, 3])

    assert command.hospital._patients_list == [0]
    command.dialog.send_message.assert_called_with("Пациент выписан из больницы")

def test_status_up_when_discharge_patient_false():
    command.hospital._patients_list = [0, 3]
    command.dialog.request_patient_id = MagicMock(return_value=2)
    command.dialog.request_confirm_for_patient_discharge = MagicMock(return_value=False)
    command.dialog.send_message = MagicMock()

    command.patient_status_up([0, 3])

    assert command.hospital._patients_list == [0, 3]
    command.dialog.send_message.assert_called_with("Пациент остался в статусе \"Готов к выписке\"")

def test_status_up_when_patient_id_above_range_patient_list():
    command.hospital._patients_list = [0]
    command.dialog.request_patient_id = MagicMock(return_value=2)
    command.dialog.send_message = MagicMock()

    command.patient_status_up([0])

    assert command.hospital._patients_list == [0]
    command.dialog.send_message.assert_called_with("Ошибка. В больнице нет пациента с таким ID")

def test_status_up_patient_when_empty_patient_list():
    command.hospital._patients_list = []
    command.dialog.request_patient_id = MagicMock(return_value=2)
    command.dialog.send_message = MagicMock()

    command.patient_status_up([])

    assert command.hospital._patients_list == []
    command.dialog.send_message.assert_called_with("Ошибка. В больнице нет пациента с таким ID")
