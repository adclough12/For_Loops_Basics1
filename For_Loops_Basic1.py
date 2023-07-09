# Basic
x = 0
while x <= 150:
    print(x)
    x += 1

# Multiples of Five
x = 5
while x <= 1000:
    print(x)
    x += 5

# Counting, the Dojo Way
x = 1
while x <= 100:
    if x %10 == 0:
        print("CodingDojo")
    elif x %5 == 0:
        print("Coding")
    else:
        print(x)
    x += 1

# Whoa. That Sucker's Huge
sum = 0
for x in range (1, 500001, 2):
    sum += x
print(sum)

# Countdown by Fours
x = 2018
while x >= 0:
    print(x)
    x -= 4

# Flexible Counter
low = 2
high = 9
mult = 3
for x in range (low, high + 1):
    if x % mult == 0:
        print(x)