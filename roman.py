# Alex Wassel
# Integer to Roman Numerals

num = int(input("Enter an integer: "))
if num < 1 or num > 3999:
    print("Input must be between 1 and 3999")

ans = ""
m = num // 1000
ans += m * "M"
num -= m * 1000

c = num // 100
if c == 4:
    ans += "CD"
elif c == 9:
    ans += "CM"
elif c > 4:
    ans += "D" + (c - 5) * "C"
else:
    ans += c * "C"

num -= c * 100

x = num // 10
if x == 4:
    ans += "XL"
elif x == 9:
    ans += "XC"
elif x > 4:
    ans += "L" + (x - 5) * "X"
else:
    ans += x * "X"

num -= x * 10

i = num // 1
if i == 4:
    ans += "IV"
elif i == 9:
    ans += "IX"
elif i > 4:
    ans += "V" + (i - 5) * "I"
else:
    ans += i * "I"

print(ans)
