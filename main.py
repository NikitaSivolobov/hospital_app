from application import Application
from hospital_entities.hospital import Hospital
from user_dialog_with_console import UserDialogWithConsole
from commands_hospital import CommandsHospital


def main():
    """Конфигурирование разных реализаций"""

    hospital = Hospital()
    user_dialog = UserDialogWithConsole()
    commands_hospital = CommandsHospital(hospital, user_dialog)
    app = Application(commands_hospital)
    app.main()


if __name__ == '__main__':
    # Запуск программы

    try:
        main()
    except KeyboardInterrupt:
        print("\nПользователь принудительно остановил программу \nОшибка KeyboardInterrupt")
    finally:
        print("Сеанс завершён.")
    # input("Нажмите Enter для выхода...")
