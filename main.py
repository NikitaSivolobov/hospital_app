import application

if __name__ == '__main__':
    # Запуск программы

    try:
        hospital_patients_list = [1] * 200
        application.main_loop(hospital_patients_list)
    except KeyboardInterrupt:
        print("\nПользователь принудительно остановил программу"
              "\nОшибка KeyboardInterrupt")
    # input("Нажмите Enter для выхода...")
