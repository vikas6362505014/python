print("Vikas gm, USN:1AY24AI115, SEC:O")
from datetime import datetime, timedelta
def current_day_of_week():
    today = datetime.today()
    print("Today's date:", today.strftime("%Y-%m-%d"))
    print("Day of the week:", today.strftime("%A"))
def birthday_info():
    bday_str = input("Enter your birthday (YYYY-MM-DD): ")
    bday = datetime.strptime(bday_str, "%Y-%m-%d")
    now = datetime.now()
    age = now.year - bday.year
    if (now.month, now.day) < (bday.month, bday.day):
        age -= 1
    print(f"You are {age} years old.")
    next_birthday = datetime(now.year, bday.month, bday.day)
    if next_birthday < now:
        next_birthday = datetime(now.year + 1, bday.month, bday.day)
    time_left = next_birthday - now
    print(f"Time until next birthday: {time_left.days} days, "
          f"{time_left.seconds // 3600} hours, "
          f"{(time_left.seconds % 3600) // 60} minutes,"
          f"{time_left.seconds % 60} seconds.")
def double_day(birth1_str, birth2_str):
    birth1 = datetime.strptime(birth1_str, "%Y-%m-%d")
    birth2 = datetime.strptime(birth2_str, "%Y-%m-%d")
    if birth1 > birth2:
        older, younger = birth2, birth1
    else:
        older, younger = birth1, birth2
    diff = younger - older
    double_day = younger + diff
    print("Double Day (when older is twice as old):", double_day.date())
def n_times_day(birth1_str, birth2_str, n):
    birth1 = datetime.strptime(birth1_str, "%Y-%m-%d")
    birth2 = datetime.strptime(birth2_str, "%Y-%m-%d")
    if birth1 > birth2:
        older, younger = birth2, birth1
    else:
        older, younger = birth1, birth2
    diff = younger - older
    target_day = younger + diff / (n - 1)
    print(f"{n}-Times Day:", target_day.date())

# ----------- Run Example --------
if __name__ == "__main__":
    print("1. Current day of the week:")
    current_day_of_week()
    print("\n2. Birthday info:")
    birthday_info()
    print("\n3. Double Day Example:")
    double_day("1990-01-01", "2000-01-01")
    print("\n4. n-Times Day Example (n=3):")
    n_times_day("1990-01-01", "2000-01-01", 3)
