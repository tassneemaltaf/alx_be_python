from datetime import datetime, timedelta, date

def display_current_datetime():    
    c = datetime.now()
    current_date_time = c.strftime('%Y-%m-%d %H:%M:%S')
    print("Current date and time: ", current_date_time)

def calculate_future_date(number_of_days):
    future_date = date.today() + timedelta(number_of_days)
    print(future_date)

def main():
    display_current_datetime()
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    calculate_future_date(number_of_days)


if __name__ == "__main__":
    main()
