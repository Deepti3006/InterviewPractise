def romanToInt(string1):
    return sum(string1.count(r) * v for r, v in [('I', 1), ('V', 5)])

sum1 = romanToInt("IV")
print(sum1)