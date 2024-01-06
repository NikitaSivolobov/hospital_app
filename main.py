from application import Application
from entities.hospital import Hospital
from use_cases.use_cases_commands import UseCasesCommands
from io_presenters.user_dialog_with_console import UserDialogWithConsole


def main():
    """Конфигурирование разных реализаций"""

    hospital = Hospital()
    commands_use_cases = UseCasesCommands(hospital)
    user_dialog = UserDialogWithConsole(commands_use_cases)
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
