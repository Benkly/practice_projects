import datetime as dt

current_time = dt.datetime.now()

print("\n ---=Age calculator=--- \n")

ask_user_time = str(input("Do you know roughly the time you were born? (Y/N): "))

# Code block executes if user does not know their birth time

if ask_user_time.lower() == "n":
  
  user_birth_date = str(input("\nEnter your birth date (DD/MM/YYYY): "))
  
  birth_date_dt_object = dt.datetime.strptime(user_birth_date, "%d/%m/%Y")
  
  user_age = current_time - birth_date_dt_object
  
  user_age_days = user_age.days + (user_age.seconds / 86400)
  
  user_age_years = user_age_days / 365.25
  
  user_age_months = user_age_years * 12
  
  user_age_weeks = user_age_days / 7
  
  user_age_hours = user_age_days * 24
  
  user_age_minutes = user_age_hours * 60
  
  user_age_seconds = user_age_minutes * 60
  
  
# Code block executes if user knows their birth time
  
elif ask_user_time.lower() == "y":
  
  user_birth_date = str(input("\nEnter your birth date (DD/MM/YYYY): "))
  
  user_birth_time = str(input("\nEnter the time you were born as far as you know (24h format - HH:MM:SS): "))
  
  birth_date_dt_object = dt.datetime.strptime(user_birth_date, "%d/%m/%Y")
  
  birth_time_object = dt.datetime.strptime(user_birth_time, "%H:%M:%S").time()
  
  birth_timedelta = dt.timedelta(hours=birth_time_object.hour, minutes=birth_time_object.minute, seconds=birth_time_object.second)
  
  user_age = current_time - (birth_date_dt_object + birth_timedelta)
  
  user_age_days = user_age.days + (user_age.seconds / 86400)
  
  user_age_years = user_age_days / 365.25
  
  user_age_months = user_age_years * 12
  
  user_age_weeks = user_age_days / 7
  
  user_age_hours = user_age_days * 24
  
  user_age_minutes = user_age_hours * 60
  
  user_age_seconds = user_age_minutes * 60
  
  
# Check to see if current date is your birthday, if so, return birthday message
  
if (birth_date_dt_object.day, birth_date_dt_object.month) == (current_time.day, current_time.month):
  print("\n\U0001F973 \U0001F389 HAPPY BIRTHDAY!!!\U0001F389 \U0001F973") 
  
current_time_formatted = current_time.strftime("%d/%m/%Y %H:%M:%S")
# Print out results

print(f"""\n---------------------------\nAs of {current_time_formatted}, 
      \nYou are {user_age_years:.2f} years old!
-------------------------\nThis is equivalent to: 
      \n * {user_age_months:.2f} months 
      \n * {user_age_weeks:.2f} weeks 
      \n * {user_age_days:,.2f} days 
      \n * {user_age_hours:,.2f} hours 
      \n * {user_age_minutes:,.2f} minutes 
      \n * {user_age_seconds:,.0f} seconds""")




