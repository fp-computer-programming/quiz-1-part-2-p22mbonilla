# Author MB 10/19/2021

m = int(input("what is the month of the date: "))
d = int(input("what is the day of the date: "))
y = int(input("what is the year of the date: "))

j = y // 100
k = y % 100

h = (d + (26 * (m + 1) // 10) + k + (k // 4) + (j // 4) + j * 5) % 7

if h == 6:
    h = str("Friday")
elif h == 5:
    h = str("Thursday")
elif h == 4:
    h = str("Wednesday")
elif h == 3:
    h = str("Tuesday")
elif h == 2:
    h = str("Monday")
elif h == 1:
    h = str("Sunday")
else:
    h = str("Saturday")

if m == 1:
    m = str("January")
elif m == 2:
    m = str("February")
elif m == 3:
    m = str("March")
elif m == 4:
    m = str("April")
elif m == 5:
    m = str("May")
elif m == 6:
    m = str("June")
elif m == 7:
    m = str("July")
elif m == 8:
    m = str("August")
elif m == 9:
    m = str("September")
elif m == 10:
    m = str("October")
elif m == 11:
    m = str("November")
else:
    m = str("December")

d = str(d)
y = str(y)

print(m + " " + d + "/" + y + " was a " + h)
