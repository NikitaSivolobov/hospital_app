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

* Запуск всех тестов в папке /tests с подробным выводом результатов тестирования
```
                      pytest --verbose tests
```

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

### Структура и связи

```mermaid
classDiagram
    Hospital --|> Status
    Hospital <|-- CommandsHospital
    CommandsHospital --|> ConsoleDialogWithUser
    Application --|> CommandsHospital
    Application --|> Commands
    Application --|> ConsoleDialogWithUser
    Application <|-- Main
    
    class Hospital{
      _patients_count
      _patient_status
      _patients_list
      -_create_list_hospital_patients()
      -_verify_patient_id(patient_id)
      -get_total_patients()
      -get_status_counts()
      -get_status_name_by_patient_id(patient_id)
      -can_status_up(patient_id)
      -status_up(patient_id)
      -can_status_down(patient_id)
      -status_down(patient_id)
      -discharge(patient_id)
    }
    
    class Status{
      ID_00
      ID_01
      ID_02
      ID_03
      id_code
      name_value
      -get_highest_status()
      -get_lowest_status()
      -get_status_by_code(code)
    }
    class Commands{
      GET_STATUS
      STATUS_UP
      STATUS_DOWN
      DISCHARGE
      CALCULATE_STATISTICS
      STOP

      command_ru
      command_en
    }
    class ConsoleDialogWithUser{
        -request_command()
        -request_patient_id()
        -_convert_text_to_patient_id(patient_id_text)
        -request_confirm_for_patient_discharge()
        -send_message(text)
    }
    class CommandsHospital{
      hospital
      dialog_with_user
    
      -calculate_hospital_statistics()
      -get_status_patient()
      -patient_status_up()
      -patient_status_down()
      -discharge_patient()
    }
    class Application{
        command_hospital
        dialog_with_user
        -main()
    }
    class Main{
        конфигурирует:
        -Hospital()
        -ConsoleDialogWithUser()
        -CommandsHospital(hospital, dialog_with_user)
        -Application(commands_hospital, dialog_with_user)
        запускает: main()
    }
```
### Связи
```mermaid
stateDiagram-v2
    Hospital --> Status
    CommandsHospital --> Hospital
    CommandsHospital --> ConsoleDialogWithUser
    Application --> CommandsHospital
    Application --> ConsoleDialogWithUser
    Application --> Commands
    Main --> Application
``` 
