import datetime as dt

current_time = dt.datetime.now()

print("\n ---=Age calculator=--- \n")
user_birth_date = str(input("Enter your birth date (DD/MM/YYYY): "))

birth_date_dt_object = dt.datetime.strptime(user_birth_date, "%d/%m/%Y")

user_age = current_time - birth_date_dt_object

user_age_days = user_age.days + (user_age.seconds / 86400)

user_age_years = user_age_days / 365.25

user_age_months = user_age_years * 12

user_age_weeks = user_age_days / 7

user_age_hours = user_age_days * 24

user_age_minutes = user_age_hours * 60

user_age_seconds = user_age_minutes * 60

if (birth_date_dt_object.day, birth_date_dt_object.month) == (current_time.day, current_time.month):
  print("\n\U0001F973 \U0001F389 HAPPY BIRTHDAY!!!\U0001F389 \U0001F973") 

print(f"""\nYou are {user_age_years:.2f} years old. 
      \n\nThis is equivalent to: 
      \n\n  * {user_age_months:.2f} months 
      \n\n  * {user_age_weeks:.2f} weeks 
      \n\n  * {user_age_days:,.2f} days 
      \n\n  * {user_age_hours:,.2f} hours 
      \n\n  * {user_age_minutes:,.2f} minutes 
      \n\n  * {user_age_seconds:,.2f} seconds""")




