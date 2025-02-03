import commands_hospital

import hospital

"""методы получения данных из больницы"""


def test_get_total_patients():
    actual_total_patients = hospital.get_total_patients([0, 1, 2])
    assert actual_total_patients == 3


def test_get_total_patients_when_empty_patient_list():
    actual_total_patients = hospital.get_total_patients([])
    assert actual_total_patients == 0


def test_get_total_patients_when_default_patient_list():
    total_patients = hospital.get_total_patients([1] * 200)
    assert total_patients == 200


def test_get_status_counts():
    actual_status_counts = hospital.get_status_counts([1, 2, 1, 3, 2, 1])
    assert actual_status_counts == {"Болен": 3, "Слегка болен": 2, "Готов к выписке": 1, "Тяжело болен": 0}


def test_get_status_counts_when_empty_patient_list():
    actual_total_patients = hospital.get_status_counts([])
    assert actual_total_patients == {"Болен": 0, "Слегка болен": 0, "Готов к выписке": 0, "Тяжело болен": 0}


def test_get_status_counts_when_default_patient_list():
    status_counts = hospital.get_status_counts([1] * 200)
    assert status_counts == {"Болен": 200, "Слегка болен": 0, "Готов к выписке": 0, "Тяжело болен": 0}


"""методы формирования расчёта статистики из данных полученных из больницы"""


def test_convert_hospital_data_to_calculate_statistics():
    total_patients = 6
    status_count = {"Болен": 3, "Слегка болен": 2, "Готов к выписке": 1, "Тяжело болен": 0}
    actual_calculate_statistics = (commands_hospital
                                   ._convert_hospital_data_to_calculate_statistics(total_patients, status_count))

    assert actual_calculate_statistics == ("В больнице на данный момент находится 6 чел., из них:\n"
                                           "\t- в статусе \"Болен\": 3 чел.\n"
                                           "\t- в статусе \"Слегка болен\": 2 чел.\n"
                                           "\t- в статусе \"Готов к выписке\": 1 чел.")


def test_convert_hospital_data_to_calculate_statistics_when_empty_patient_list():
    total_patients = 0
    status_count = {"Болен": 0, "Слегка болен": 0, "Готов к выписке": 0, "Тяжело болен": 0}
    actual_calculate_statistics = (commands_hospital
                                   ._convert_hospital_data_to_calculate_statistics(total_patients, status_count))

    assert actual_calculate_statistics == "В больнице на данный момент находится 0 чел., из них:"


def test_convert_hospital_data_to_calculate_statistics_when_default_patient_list():
    total_patients = 200
    status_count = {"Болен": 200, "Слегка болен": 0, "Готов к выписке": 0, "Тяжело болен": 0}
    calculate_statistics = (commands_hospital
                            ._convert_hospital_data_to_calculate_statistics(total_patients, status_count))

    assert calculate_statistics == "В больнице на данный момент находится 200 чел., из них:\n" \
                                   "\t- в статусе \"Болен\": 200 чел."
