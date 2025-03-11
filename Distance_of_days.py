from datetime import datetime

now = datetime.today() # or datetime.now()
#print(now)

while True:
    some_date = input("Enter some date here (YYYY-MM-DD): ") 
    try:
        s_d = datetime.strptime(some_date, "%Y-%m-%d") # the same essential of the name s_d, like some_date
        if s_d < now:
            
            distance_of_days = (now - s_d).days
            print(f"{distance_of_days} day/days the distance between your date and today.")

            break

        else:
            distance_of_days = - ((s_d - now).days)
            print(f"Your date is bigger than today, so the distance between today and your date {distance_of_days} day/days")
            
            break

    except ValueError:
        print("Incorrect format. Please enter the date in YYYY-MM-DD format.")