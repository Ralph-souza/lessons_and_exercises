""" Exercise 1: checks the radius of a sphere """
radius = 5.0
pi = 3.14
volume = (4.0/3.0) * pi * radius ** 3
print(f"The volume of a sphere with radius {radius} is: {volume:.2f}")

""" Exercise 2: check the price for 60 copies of a book with a 40% discount """
full_price = 24.95
discount = 0.40
discounted_price = full_price - (full_price * discount)

first_book_shipping = 3.00
remain_books_shipping = 0.75

copies = 59

first_copy = discounted_price + first_book_shipping
remaining_copies = discounted_price + remain_books_shipping

total = (remaining_copies * copies) + first_copy
print(f"""
    Considering that a book costs R${full_price} without discount
    However book stores gains R${discount} per copy ending up costing R${discounted_price:.2f}
    Where the first one has a shipping tax value of R${first_book_shipping}
    And the remaining books has a shipping tax value of R${remain_books_shipping}
    The total to pay for 60 copies is R${total:.2f}.
    """)

""" Exercise 3: checks the time for a complete 5km circuit """
time_1 = 1 * 8 + 15  # 1km at a 8min15s speed, in minutes
time_2 = 3 * 7 + 12  # 3km at a 7min12s speed, in minutes
time_3 = 1 * 8 + 15  # 1km at a 8min15s speed, in minutes
total_time = time_1 + time_2 + time_3

starting_hour = 6 * 60 + 52  # 6 hours and 52 seconds converted in minutes.

arrive_time = starting_hour + total_time

hour = arrive_time // 60  # arrive in hours
minutes = arrive_time % 60  # arrive in minutes

print(f""" 
    If a leave my house at 6:52am for a run
    and the first kilometer i do in 8min/15s per/km
    the next 3 kilometers in 7min/12s per/km
    and the last kilometer i keep the same speed of the first one
    i`ll arrive at home for breakfast at {hour}:{minutes:02d}am
    """)
