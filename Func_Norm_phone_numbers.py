import re

def normalize_phone(phone_number: str) -> str:
    
    # Видаляємо всі символи, крім "+" та цифр
    phone_number = re.sub(r"[^\+\d+]", "", phone_number)
    
    # Якщо номер вже починається з "+380", залишаємо його
    if phone_number.startswith("+380"):
        return phone_number
    
    # Якщо номер починається з "380", додаємо "+" на початок
    if phone_number.startswith("380"):
        return "+" + phone_number
    
    # Якщо номер починається з "0", замінюємо його на "+380"
    if phone_number.startswith("0"):
        return "+38" + phone_number
    
    # Якщо номер не містить коду країни, додаємо "+38" на початок
    return "+38" + phone_number

# Тестові номери
raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)