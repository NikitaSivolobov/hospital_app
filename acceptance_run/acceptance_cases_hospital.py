from acceptance_run.application_mock import ApplicationMock
from acceptance_run.user_dialog_mock import UserDialogMock, UserDialogMockNegativeVar, \
    UserDialogMockConstYes, UserDialogMockConstNo
from entities.hospital import Hospital
from use_cases.use_cases_commands import UseCasesCommands


def main_acceptance_first():
    """Конфигурирование Приёмочного теста № 1 (базовый сценарий)"""
    hospital = Hospital()
    commands_service = UseCasesCommands(hospital)
    user_dialog = UserDialogMock(commands_service)
    app = ApplicationMock(user_dialog)
    app.main_first()


def main_acceptance_second():
    """Конфигурирование Приёмочного теста № 2 (неизвестная команда)"""
    hospital = Hospital()
    commands_service = UseCasesCommands(hospital)
    user_dialog = UserDialogMock(commands_service)
    app = ApplicationMock(user_dialog)
    app.main_second()


def main_acceptance_three():
    """Конфигурирование Приёмочного теста № 3 (случаи ввода пользователем некорректных данных)"""
    hospital = Hospital()
    commands_service = UseCasesCommands(hospital)
    user_dialog = UserDialogMockNegativeVar(commands_service)
    app = ApplicationMock(user_dialog)
    app.main_third()


def main_acceptance_four():
    """Конфигурирование Приёмочного теста № 4 (попытка повысить самый высокий статус,"
              " которая приводит к выписке пациента)"""
    hospital = Hospital()
    commands_service = UseCasesCommands(hospital)
    user_dialog = UserDialogMockConstYes(commands_service)
    app = ApplicationMock(user_dialog)
    app.main_fourth()


def main_acceptance_five():
    """Конфигурирование Приёмочного теста № 5 (попытка повысить самый высокий статус,
     которая ни к чему не приводит)"""
    hospital = Hospital()
    commands_service = UseCasesCommands(hospital)
    user_dialog = UserDialogMockConstNo(commands_service)
    app = ApplicationMock(user_dialog)
    app.main_fourth()


def main_acceptance_six():
    """Конфигурирование Приёмочного теста № 6 (неудачная попытка понизить самый низкий статус)"""
    hospital = Hospital()
    commands_service = UseCasesCommands(hospital)
    user_dialog = UserDialogMockConstYes(commands_service)
    app = ApplicationMock(user_dialog)
    app.main_sixth()


if __name__ == '__main__':
    # Запуск приёмочный тестов консольного приложения: "Автоматизация работы больницы (hospital)"
    try:
        print("=== Приёмочный тест № 1 (базовый сценарий) ===")
        main_acceptance_first()
        print()
        print("=== Приёмочный тест № 2 (неизвестная команда) ===")
        print()
        main_acceptance_second()
        print()
        print("=== Приёмочный тест № 3 (случаи ввода пользователем некорректных данных) ===")
        print()
        main_acceptance_three()
        print()
        print("=== Приёмочный тест № 4 (попытка повысить самый высокий статус,"
              " которая приводит к выписке пациента) ===")
        print()
        main_acceptance_four()
        print()
        print("=== Приёмочный тест № 5 (попытка повысить самый высокий статус, которая ни к чему не приводит) ===")
        print()
        main_acceptance_five()
        print()
        print("=== Приёмочный тест № 6 (неудачная попытка понизить самый низкий статус) ===")
        print()
        main_acceptance_six()
        print()
        print("Если вы дошли до этого места, то вы великолепны :-) !!")
    except KeyboardInterrupt:
        print("\nПользователь принудительно остановил программу \nОшибка KeyboardInterrupt")
    finally:
        print("Сеанс успешно завершён ;-) .")
    # input("Нажмите Enter для выхода...")
