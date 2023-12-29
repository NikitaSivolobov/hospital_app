from enums.commands import Commands
from enums.status import Status
from models.hospital import Hospital
from models.patient import Patient


def find_patient(patients_list, patient_id):
    patient_id -= 1
    return patient_id, patients_list[patient_id]


def patient_id_up(patients_list, patient_id, status_patient_id):
    if status_patient_id == 0:
        status_patient_id_new = status_patient_id + 1
        patients_list[patient_id] = status_patient_id_new
        return status_patient_id_new
    elif status_patient_id == 1:
        status_patient_id_new = status_patient_id + 1
        patients_list[patient_id] = status_patient_id_new
        return status_patient_id_new
    elif status_patient_id == 2:
        status_patient_id_new = status_patient_id + 1
        patients_list[patient_id] = status_patient_id_new
        return status_patient_id_new


def patient_id_down(patients_list, patient_id, status_patient_id):
    if status_patient_id == 1:
        status_patient_id_new = status_patient_id - 1
        patients_list[patient_id] = status_patient_id_new
        return status_patient_id_new
    elif status_patient_id == 2:
        status_patient_id_new = status_patient_id - 1
        patients_list[patient_id] = status_patient_id_new
        return status_patient_id_new
    elif status_patient_id == 3:
        status_patient_id_new = status_patient_id - 1
        patients_list[patient_id] = status_patient_id_new
        return status_patient_id_new


def patient_id_input(patients_list):
    patient_id_str = input("Введите ID пациента: ").strip().lower()

    try:
        patient_id = int(patient_id_str)
        if patient_id <= 0:
            raise ValueError
        if patient_id > len(patients_list):
            print("Ошибка. В больнице нет пациента с таким ID")
            return None
    except ValueError:
        print("Ошибка. ID пациента должно быть числом (целым, положительным)")
        return None

    return patient_id


def commands_get_status(patients_list):
    patient_id = patient_id_input(patients_list)
    if patient_id != None:
        patient_id, status_patient_id = find_patient(patients_list, patient_id)
        status_code_in_list = patients_list[patient_id]
        status_name_in_list = Status.get_status_by_code(status_code_in_list)
        print(f"Статус пациента: \"{status_name_in_list.status_name}\"")


def status_patient_id_change(patients_list, patient_id, status_patient_id, is_change_up=True):
    if is_change_up:
        if 0 <= status_patient_id < 3:
            status_patient_id_new = patient_id_up(patients_list, patient_id, status_patient_id)
            return status_patient_id_new, False
        else:
            status_patient_id, is_discharge = process_discharge_request(status_patient_id)
            if is_discharge:
                del patients_list[patient_id]
                print("Пациент выписан из больницы")
                return -1, True
            else:
                return Status.get_last_status().status_code, False
    else:
        if 0 < status_patient_id < 3:
            status_patient_id_new = patient_id_down(patients_list, patient_id, status_patient_id)
            return status_patient_id_new, False
        else:
            print("Ошибка. Нельзя понизить самый низкий статус (наши пациенты не умирают)")
            first_status = Status.get_first_status()
            status_code = first_status.value[0]
            return status_code, False  # Status.STATUS_00.status_code


def process_discharge_request(status_patient_id):
    while True:
        discharge_input = input("Желаете этого клиента выписать? (да/нет): ").strip().lower()
        if discharge_input == 'да':
            return 0, True
        elif discharge_input == 'нет':
            return Status.get_last_status().status_code, False  # Status.STATUS_03.status_code
        else:
            print("Некорректный ввод. Пожалуйста, ответьте (да) или (нет)."), False


def command_status_up(patients_list):
    patient_id = patient_id_input(patients_list)
    if patient_id is not None:
        patient_id, status_patient_id = find_patient(patients_list, patient_id)
        status_patient_id_new, is_discharge = status_patient_id_change(patients_list, patient_id, status_patient_id)
        if status_patient_id != status_patient_id_new and is_discharge == False:
            patients_list[patient_id] = status_patient_id_new
            status_name_in_list = Status.get_status_by_code(status_patient_id_new)
            print(f"Новый статус пациента: \"{status_name_in_list.status_name}\"")
            return patient_id, status_patient_id_new
        elif status_patient_id != status_patient_id_new and is_discharge:
            return None, None
        else:
            get_status_name = Status.get_status_by_code(status_patient_id_new)
            print(f"Пациент остался в статусе \"{get_status_name.status_name}\"")
            return patient_id, status_patient_id_new
    else:
        return patient_id, 0


def command_status_down(patients_list):
    patient_id = patient_id_input(patients_list)
    if patient_id is not None:
        patient_id, status_patient_id = find_patient(patients_list, patient_id)
        status_patient_id_new, _ = status_patient_id_change(patients_list, patient_id, status_patient_id, False)
        if status_patient_id != status_patient_id_new:
            patients_list[patient_id] = status_patient_id_new
            status_name_in_list = Status.get_status_by_code(status_patient_id_new).status_name
            print(f"Новый статус пациента: \"{status_name_in_list}\"")
            return patient_id, status_patient_id_new
        else:
            return patient_id, status_patient_id_new
    else:
        return patient_id, 0


def command_discharge(patients_list):
    patient_id = patient_id_input(patients_list)
    if patient_id is not None:
        patient_id, status_patient_id = find_patient(patients_list, patient_id)
        del patients_list[patient_id]
        print("Пациент выписан из больницы")


def command_calculate_statistics(patients_list):
    Status.calculate_statistics(patients_list)


def app_input() -> str:
    return input("Введите команду: ").strip().lower()


def app(hospital):
    patients_list = hospital.create_hospital_patients_with_list()
    command = app_input()
    while command not in Commands.COMMANDS_STOP.value:
        if command in Commands.COMMANDS_STATUS_UP.value:
            patient_id, status_patient_id_new = command_status_up(patients_list)
            if patient_id is not None:
                patients_list[patient_id] = status_patient_id_new

        elif command in Commands.COMMANDS_STATUS_DOWN.value:
            patient_id, status_patient_id_new = command_status_down(patients_list)
            if patient_id is not None:
                patients_list[patient_id] = status_patient_id_new

        elif command in Commands.COMMANDS_DISCHARGE.value:
            command_discharge(patients_list)

        elif command in Commands.COMMANDS_CALCULATE_STATISTICS.value:
            command_calculate_statistics(patients_list)

        elif command in Commands.COMMANDS_GET_STATUS.value:
            commands_get_status(patients_list)

        else:
            print("Неизвестная команда! Попробуйте ещё раз")

        command = app_input()


def main():
    hospital = Hospital()
    app(hospital)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nПользователь принудительно остановил программу \nОшибка KeyboardInterrupt")
    finally:
        print("Сеанс завершён.")
    # input("Нажмите Enter для выхода...")
