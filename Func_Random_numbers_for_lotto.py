import random

def get_numbers_ticket(min, max, quantity):
    # Перевіряємо, чи мінімальне число не менше 1
    if min < 1:
        return []
    
    # Перевіряємо, чи максимальне число не більше 1000
    if max > 1000:
        return []
    
    # Перевіряємо, чи мінімальне число не більше максимального
    if min > max:
        return []
    
    # Перевіряємо, чи кількість чисел знаходиться в допустимому діапазоні, оскільки кількість чисел на виході може бути різна
    if quantity < min or quantity > max:
        return []
    
    # Генеруємо унікальні випадкові числа додаючи 1, для уникнення випадку отримання 0
    numbers = random.sample(range(min, max + 1), quantity)
    
    # Повертаємо відсортований список чисел
    return sorted(numbers)

# Приклад виклику функції
lottery_numbers = get_numbers_ticket(1, 1000, 6)
print("Ваші лотерейні числа:", lottery_numbers)