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
<img src="hospital_layers.png" alt="hospital application layers" width="408" height="396">

### Связи (1 вариант)

```mermaid
classDiagram
    Hospital --|> Patient
    Hospital --|> Status
    Patient --|> Status
    Hospital <|-- CommandsHospital
    CommandsHospital --|> UserDialogWithConsole
    Application --|> CommandsHospital
    Application --|> Commands
    Application <|-- Main
    
    class Hospital{
      -patients_count
      -patient
      -patients_list
      -_create_hospital_patients_with_list()
      -_check_patient_id(patient_id)
      -_get_patient_id(patient_id)
      -get_total_patients()
      -get_status_counts()
      -is_valid_patient_id(value_patient_id_from_command)
      -get_status_name(patient_id)
      -check_status_patient_for_up()
      -status_up(patient_id)
      -discharge(patient_id)
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
        get_input_from_user()
        get_patient_id_from_user()
        process_discharge_request()
        output_to_user(output)
    }
    class CommandsHospital{
      -hospital
      -user_dialog
    
      -_process_patient_status_up(valid_patient_id)
      -_process_patient_discharge(valid_patient_id)
      -get_command_from_user()
      -output_to_user_from_app(value)
      -command_calculate_hospital_statistics()
      -command_get_status_patient()
      -command_patient_status_up()
      -command_discharge(patient_id)
      -command_patient_status_down(patient_id)
    }
    class Application{
        commands_hospital
    }
    class Main{
        конфигурирует:
        -Hospital()
        -UserDialogWithConsole(hospital)
        -CommandsHospital(hospital, user_dialog)
        -Application(commands_hospital)
        запускает: main()
    }
```
### Связи (2 вариант)
```mermaid
stateDiagram-v2
    Hospital --> Patient
    Hospital --> Status
    Patient --> Status
    CommandsHospital --> Hospital
    CommandsHospital --> UserDialogWithConsole
    Application --> CommandsHospital
    Application --> Commands
    Main --> Application
``` 
