#function for calender
def calender():
    import calendar
    # Get the year and month from the user
    year = int(input("Enter the year (e.g., 2023): "))
    month = int(input("Enter the month (1-12): "))
    
    # Print the calendar for the specified month and year
    print(calendar.month(year, month))
# Function call
# Input from the user
calender()
