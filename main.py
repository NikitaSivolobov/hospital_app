from application import Application
from hospital import Hospital
from console_dialog_with_user import ConsoleDialogWithUser
from commands_hospital import CommandsHospital


def main():
    """Конфигурирование разных реализаций"""

    hospital = Hospital([1]*200)
    dialog_with_user = ConsoleDialogWithUser()
    commands_hospital = CommandsHospital(hospital, dialog_with_user)
    app = Application(commands_hospital, dialog_with_user)
    app.main()


if __name__ == '__main__':
    # Запуск программы

    try:
        main()
    except KeyboardInterrupt:
        print("\nПользователь принудительно остановил программу \nОшибка KeyboardInterrupt")
    # input("Нажмите Enter для выхода...")
