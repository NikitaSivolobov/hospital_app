# Консольное приложение: "Автоматизация работы больницы (hospital)"


## Установка и использование
* Установить python3 (например, 3.8) и pip
* Установить виртуальное окружение:
```console
                      python -m venv venv
```
* Активировать виртуальное окружение:
```
                      venv/Scripts/activate.bat
```

* Установить все нужные пакеты, если есть файл requirements.txt:
```console
                      pip install -r requirements.txt
```
* Деактивировать виртуальное окружение, если необходимо:
```
                      venv/Scripts/deactivate.bat
```

### Запуск
* Запустить **main.py**:
```console
                      python main.py
```

* Имеется возможность запуска с помощью start.bat (если активировано виртуальное окружение)

## Перечень команд для работы с приложением

 Команда RU                   | Команда EN              |
|------------------------------|-------------------------|
| узнать статус пациента       | get status              |
| повысить статус пациента     | status up               |
| понизить статус пациента     | status down             |
| выписать пациента            | discharge               |
| рассчитать статистику        | calculate statistics    |
| стоп                         | stop                    |

* Если необходимо, чтобы терминал не закрывался при выходе из программы, то необходимо раскомментировать последнюю строчку в main.py: 

                      # input("Нажмите Enter для выхода...")

## Схема приложения
```mermaid
classDiagram
    Hospital --|> Patient
    Hospital --|> Status
    Patient --|> Status
    Hospital <|-- CommandsService
    UserDialog --|> CommandsService
    Application --|> UserDialog
    Application --|> Commands
    Application <|-- Main
    
    class Hospital{
      -patients_count
      -patient
      -patients_list
      -_create_hospital_patients_with_list()
      -get_status(patient_id)
      -discharge(patient_id)
      -calculate_statistics()
      -status_patient_id_change()
      -process_discharge_request()
      -status_up(patient_id)
      -status_down(patient_id)
    }
    class Patient{
      -status
    }
    
    class Status{
      -STATUS_00
      -STATUS_01
      -STATUS_02
      -STATUS_03
      -get_last_status()
      -get_first_status()
      -get_status_by_code()
    }
    class Commands{
      -COMMANDS_GET_STATUS
      -COMMANDS_STATUS_UP
      -COMMANDS_STATUS_DOWN
      -COMMANDS_DISCHARGE
      -COMMANDS_CALCULATE_STATISTICS
      -COMMANDS_STOP

      -commands_ru
      -commands_en
    }
    class UserDialog{
        command_service
        command_input()
        command_output()
        _patient_id_input()
        get_calculate_statistics_from_commands()
        get_status_from_commands()
        get_discharge_from_commands()
        status_down_from_commands()
        status_up_from_commands()
    }
    class CommandsService{
      -hospital
    
      -__validate_patient_id()
      -command_calculate_statistics()
      -command_get_status(patient_id)
      -command_discharge(patient_id)
      -command_status_down(patient_id)
      -command_status_up(patient_id)
    }
    class Application{
        user_dialog
        Commands
    }
    class Main{
        конфигурирует:
        -Hospital()
        -CommandsService(hospital)
        -UserDialog(commands_service)
        -Application(hospital)
        -Application(user_dialog)
        запускает: main()
    }
```
