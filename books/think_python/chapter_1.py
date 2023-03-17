""" Exercise 1: checks how many seconds are in 42 minutes and 42 seconds """
minutes_total = 42.42
seconds_per_minute = 60
result = minutes_total * seconds_per_minute
print(f" There are {result} seconds in {minutes_total} minutes.")
check_minutes = result / seconds_per_minute
print(f" This confirms that {result} seconds is equal to {check_minutes} minutes.")

""" Exercise 2: checks how many miles are in 10 kilometers """
total_kilometers = 10
miles_per_km = 0.62
result = total_kilometers * miles_per_km
print(f" There are {result} miles in {total_kilometers} kilometers.")

""" Exercise 3: checks pace and speed for a 10km circuit in 42.42 minutes """
total_kilometers = 10
minutes_total = 42.42
miles_per_km = 0.62
total_miles = total_kilometers * miles_per_km
average_pace = total_miles / minutes_total
average_speed = average_pace * minutes_total
print(f""" 
    The average pace for a {total_kilometers} circuit in {minutes_total} minutes is: 
    Average pace: {average_pace}
    Average speed: {average_speed}
    """)
