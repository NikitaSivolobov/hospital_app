from application import Application
from enums.status import Status
from models.patient import Patient
from repository.hospital import Hospital
from service.commands_service import CommandsService
from controller.user_dialog import UserDialog


def main():
    """Конфигурирование разных реализаций"""

    hospital = Hospital()
    commands_service = CommandsService(hospital)
    user_dialog = UserDialog(commands_service)
    app = Application(user_dialog)
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
