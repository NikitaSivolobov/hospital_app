STATUS = {
    0: "Тяжело болен",
    1: "Болен",
    2: "Слегка болен",
    3: "Готов к выписке"
}

def get_highest_status():
    return max(STATUS.keys())

def get_lowest_status():
    return min(STATUS.keys())

def get_status_by_code(status_code):
    return STATUS.get(status_code, None)
