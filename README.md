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

## Схемы приложения
### Слои
<img src="images/hospital.png" alt="hospital application layers" width="408" height="396">

### Связи (1 вариант)

```mermaid
classDiagram
        Hospital --|> Patient
    Hospital --|> Status
    Patient --|> Status
    Hospital <|-- UseCasesCommands
    UseCasesCommands --|> Status
    UserDialogWithConsole --|> UseCasesCommands
    Application --|> UserDialogWithConsole
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
    class UserDialogWithConsole{
        commands_use_cases
        command_input()
        command_output()
        _patient_id_input()
        process_discharge_request()
        get_calculate_statistics_from_commands()
        get_status_from_commands()
        get_discharge_from_commands()
        status_down_from_commands()
        status_up_from_commands()
    }
    class UseCasesCommands{
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
        -UseCasesCommands(hospital)
        -UserDialogWithConsole(commands_use_cases)
        -Application(user_dialog)
        запускает: main()
    }
```
### Связи (2 вариант)
```mermaid
stateDiagram-v2
    Hospital --> Patient
    Hospital --> Status
    Patient --> Status
    UseCasesCommands --> Hospital
    UseCasesCommands --> Status
    UserDialogWithConsole --> UseCasesCommands
    Application --> UserDialogWithConsole
    Application --> Commands
    Main --> Application
``` 
