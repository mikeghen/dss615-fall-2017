from faker import Faker
from random import randint, normalvariate

"""
Writes person records to a text file simulating a file you might
receive from a legacy database system.
"""

fake = Faker()

with open('digestive_illnesses.txt','w') as illnesses_file:
    for i in range(1000):
        first_name     = fake.first_name().ljust(50)
        last_name      = fake.first_name().ljust(50)
        street_address = fake.street_address().ljust(50)
        city           = fake.city().ljust(25)
        birth_date     = fake.date().replace('-','')
        ssn            = fake.ssn().replace('-','')
        icd9           = "%03d"%normalvariate(550, 10)
        identifier     = "%09d"%randint(1, 999999999)

        illness = identifier+ssn+birth_date+first_name+last_name+street_address+city+icd9

        illnesses_file.write(illness+'\n')
