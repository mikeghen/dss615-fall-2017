## Analyze caffeine absorption.
amount = 130
hrs = 0
print("CAFFEINE VALUES")
while amount > (130 / 2):
    amount = 0.87 * amount
    hrs += 1
print("One cup:", "less than 65 mg. will remain after", hrs, "hours.")
amount = 130
for i in range(24):
    amount = 0.87 * amount
print("One cup: {0:.2f} mg. will remain after 24 hours.".format(amount))
amount = 0
for i in range(25):
    amount = 0.87 * amount + 130
print("One cup: {0:.2f} mg. will remain after 24 hours.".format(amount))
