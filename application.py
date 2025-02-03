import commands_hospital
import console_dialog_with_user as dialog

from commands import COMMAND_MAP


def main_loop(patients_list):
    """Основной цикл обработки команд."""
    while True:
        command_key = COMMAND_MAP.get(dialog.request_command())
        if command_key:
            if command_key == "STATUS_UP":
                commands_hospital.patient_status_up(patients_list)

            elif command_key == "STATUS_DOWN":
                commands_hospital.patient_status_down(patients_list)

            elif command_key == "DISCHARGE":
                commands_hospital.discharge_patient(patients_list)

            elif command_key == "CALCULATE_STATISTICS":
                commands_hospital.calculate_hospital_statistics(patients_list)

            elif command_key == "GET_STATUS":
                commands_hospital.get_status_patient(patients_list)

            elif command_key == "STOP":
                dialog.send_message("Сеанс завершён.")
                break
        else:
            dialog.send_message("Неизвестная команда! Попробуйте ещё раз")
