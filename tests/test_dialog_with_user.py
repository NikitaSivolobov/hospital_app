from unittest.mock import MagicMock

import pytest

import console
import console_dialog_with_user as dialog
from exceptions_hospital import PatientIDNumberError

"""Тестовый модуль, проверяющий метод преобразования текста в идентификатор пациента"""


def test_convert_text_to_patient_id():
    patient_id = dialog._convert_text_to_patient_id("1")
    assert patient_id == 1


def test_convert_text_to_patient_id_with_spaces():
    patient_id = dialog._convert_text_to_patient_id(" 1 ")
    assert patient_id == 1


@pytest.mark.parametrize("test_name, patient_id_text", [
    ("ввод нуля", "0"),
    ("отрицательное число в формате int", "-2"),
    ("отрицательное число в формате float", "-4.45"),
    ("положительное число в формате float", "4.5"),
    ("число, написанное текстом", "два"),
    ("пустой ввод", "")
])
def test_convert_text_to_patient_id_when_invalid_input(test_name, patient_id_text):
    with pytest.raises(PatientIDNumberError) as excinfo:
        dialog._convert_text_to_patient_id(patient_id_text)
    assert str(excinfo.value) == "Ошибка. ID пациента должно быть числом (целым, положительным)"


"""Тестовый модуль, проверяющий метод запроса идентификатора пациента"""


def test_request_patient_id():
    console.input_ = MagicMock(return_value="1")
    patient_id = dialog.request_patient_id()
    assert patient_id == 1


def test_request_patient_id_with_spaces():
    console.input_ = MagicMock(return_value=" 1 ")
    patient_id = dialog.request_patient_id()
    assert patient_id == 1


@pytest.mark.parametrize("test_name, patient_id_text", [
    ("ввод нуля", "0"),
    ("отрицательное число в формате int", "-2"),
    ("отрицательное число в формате float", "-4.45"),
    ("положительное число в формате float", "4.5"),
    ("число, написанное текстом", "два"),
    ("пустой ввод", "")
])
def test_request_patient_id_when_invalid_input(test_name, patient_id_text):
    console.input_ = MagicMock(return_value=patient_id_text)
    with pytest.raises(PatientIDNumberError) as excinfo:
        dialog.request_patient_id()
    assert str(excinfo.value) == "Ошибка. ID пациента должно быть числом (целым, положительным)"


"""Тестовый класс, проверяющий метод запроса подтверждения выписки пациента при помощи консоли"""


def test_request_confirm_for_patient_discharge_when_response_equal_yes():
    console.input_ = MagicMock(return_value="   Да ")
    assert dialog.request_confirm_for_patient_discharge() is True


def test_request_confirm_for_patient_discharge_when_response_equal_no():
    console.input_ = MagicMock(return_value="нЕт")
    assert dialog.request_confirm_for_patient_discharge() is False


def test_request_confirm_for_patient_discharge_when_response_with_different_text():
    console.input_ = MagicMock(return_value=" different text ")
    assert dialog.request_confirm_for_patient_discharge() is False


def test_request_confirm_for_patient_discharge_when_empty_response():
    console.input_ = MagicMock(return_value="")
    assert dialog.request_confirm_for_patient_discharge() is False


def test_request_confirm_for_patient_discharge_when_empty_response_with_spaces():
    console.input_ = MagicMock(return_value="       ")
    assert dialog.request_confirm_for_patient_discharge() is False
