from unittest.mock import MagicMock

import pytest

from console import Console
from console_dialog_with_user import ConsoleDialogWithUser
from exceptions_hospital import PatientIDNumberError


class TestConvertTextToPatientId:
    """Тестовый класс, проверяющий метод преобразования текста в идентификатор пациента"""

    def test_convert_text_to_patient_id(self):
        self.dialog = ConsoleDialogWithUser()
        patient_id = self.dialog._convert_text_to_patient_id("1")
        assert patient_id == 1

    def test_convert_text_to_patient_id_with_spaces(self):
        self.dialog = ConsoleDialogWithUser()
        patient_id = self.dialog._convert_text_to_patient_id(" 1 ")
        assert patient_id == 1

    @pytest.mark.parametrize("test_name, patient_id_text", [
        ("ввод нуля",                            "0"),
        ("отрицательное число в формате int",    "-2"),
        ("отрицательное число в формате float",  "-4.45"),
        ("положительное число в формате float",  "4.5"),
        ("число, написанное текстом",            "два"),
        ("пустой ввод",                          "")
    ])
    def test_convert_text_to_patient_id_when_invalid_input(self, test_name, patient_id_text):
        self.dialog = ConsoleDialogWithUser()
        with pytest.raises(PatientIDNumberError) as excinfo:
            self.dialog._convert_text_to_patient_id(patient_id_text)
        assert str(excinfo.value) == "Ошибка. ID пациента должно быть числом (целым, положительным)"


class TestRequestPatientIdUsingConsole:
    """Тестовый класс, проверяющий метод запроса идентификатора пациента"""

    def test_request_patient_id(self):
        self.dialog = ConsoleDialogWithUser()
        Console.input = MagicMock(return_value="1")
        patient_id = self.dialog.request_patient_id()
        assert patient_id == 1

    def test_request_patient_id_with_spaces(self):
        self.dialog = ConsoleDialogWithUser()
        Console.input = MagicMock(return_value=" 1 ")
        patient_id = self.dialog.request_patient_id()
        assert patient_id == 1

    @pytest.mark.parametrize("test_name, patient_id_text", [
        ("ввод нуля",                            "0"),
        ("отрицательное число в формате int",    "-2"),
        ("отрицательное число в формате float",  "-4.45"),
        ("положительное число в формате float",  "4.5"),
        ("число, написанное текстом",            "два"),
        ("пустой ввод",                          "")
    ])
    def test_request_patient_id_when_invalid_input(self, test_name, patient_id_text):
        self.dialog = ConsoleDialogWithUser()
        Console.input = MagicMock(return_value=patient_id_text)
        with pytest.raises(PatientIDNumberError) as excinfo:
            self.dialog.request_patient_id()
        assert str(excinfo.value) == "Ошибка. ID пациента должно быть числом (целым, положительным)"


class TestRequestConfirmForPatientDischargeUsingConsole:
    """Тестовый класс, проверяющий метод запроса подтверждения выписки пациента при помощи консоли"""

    def test_request_confirm_for_patient_discharge_when_response_equal_yes(self):
        self.dialog = ConsoleDialogWithUser()
        Console.input = MagicMock(return_value="   Да ")
        assert self.dialog.request_confirm_for_patient_discharge() is True

    def test_request_confirm_for_patient_discharge_when_response_equal_no(self):
        self.dialog = ConsoleDialogWithUser()
        Console.input = MagicMock(return_value="нЕт")
        assert self.dialog.request_confirm_for_patient_discharge() is False

    def test_request_confirm_for_patient_discharge_when_response_with_different_text(self):
        self.dialog = ConsoleDialogWithUser()
        Console.input = MagicMock(return_value=" different text ")
        assert self.dialog.request_confirm_for_patient_discharge() is False

    def test_request_confirm_for_patient_discharge_when_empty_response(self):
        self.dialog = ConsoleDialogWithUser()
        Console.input = MagicMock(return_value="")
        assert self.dialog.request_confirm_for_patient_discharge() is False

    def test_request_confirm_for_patient_discharge_when_empty_response_with_spaces(self):
        self.dialog = ConsoleDialogWithUser()
        Console.input = MagicMock(return_value="       ")
        assert self.dialog.request_confirm_for_patient_discharge() is False
