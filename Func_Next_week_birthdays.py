from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
   
    today = datetime.today().date()
    end_date = today + timedelta(days=7)
    upcoming_birthdays = []
    
    for user in users:
        name = user["name"]
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)
        
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        if today <= birthday_this_year <= end_date:
            if birthday_this_year.weekday() in [5, 6]:  # Субота або неділя
                birthday_this_year += timedelta(days=(7 - birthday_this_year.weekday()))
            
            upcoming_birthdays.append({
                "name": name,
                "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")
            })
    
    return upcoming_birthdays

# Приклад використання
users = [
    {"name": "John Doe", "birthday": "1985.03.13"},
    {"name": "Jane Smith", "birthday": "1990.03.17"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
