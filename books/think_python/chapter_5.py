import time


# Exercise 1: read and print current date and time
def current_date_time():
    date_time = time.strftime("%Y-%m-%d %H:%M:%S")
    print(date_time)


current_date_time()


# Exercise 2: Fermat theorem proof exercise
def check_fermat(a, b, c, n):
    if n < 2 and a**n + b**n == c**n:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn`t work!")


def main():
    a = int(input("Type in the value of a: "))
    b = int(input("Type in the value of b: "))
    c = int(input("Type in the value of c: "))
    n = int(input("Type in the value of n: "))
    check_fermat(a, b, c, n)


if __name__ == "__main__":
    main()


# Exercise 3: create a triangle
def is_triangle(a, b, c):
    if a > b + c or b > c + a or c > a + b:
        print("Yes")
    else:
        print("No")


def main():
    a = int(input("Type in the value of a: "))
    b = int(input("Type in the value of b: "))
    c = int(input("Type in the value of c: "))
    is_triangle(a, b, c)


if __name__ == "__main__":
    main()
