# Ülesanne: Salvestame isikuandmeid ning pärime neid väljavõteteks
# Andmeteks on:
# 1. täisnimi, tuleb salvestada eraldi ees + perenimi
# 2. sünniaeg
# 3. riik

# 1. Luua funktsioon täisnime salvestamiseks, tuleb juurde uus võti 'dict' elementi 'fullname'
# 2. Luua funktsioon täis nime kättesaamiseks
# 3. Funktsioon, mis tagastab isiku vanuse, võtame arvesse sisestud sünniaja
# 4. Printida välja mitu isikut on samast riigist

# Andmete salvestamise kasutama listi
 # List võiks koosneda 'dict' => { fname: '', lname: '', dob: '', country: ''  }
 # YYYY-MM-DD === 2000-01-31

from datetime import datetime

people = [
    { 'fname': 'John', 'lname': 'Smith', 'dob': '1990-01-20', 'country': 'USA'  },
    { 'fname': 'Joe', 'lname': 'Doe', 'dob': '2001-05-21', 'country': 'USA'  },
    { 'fname': 'Mari', 'lname': 'Tamm', 'dob': '2005-06-10', 'country': 'Estonia'  }
]

def get_full_name(person):
    full_name = person['fname'] + ' ' +  person['lname']
    return full_name

def set_full_name(person):
    person['full_name'] = get_full_name(person)

def get_person_age(person):
    current_time = datetime.now()
    age_in_datetime = current_time - datetime.strptime(person['dob'], '%Y-%m-%d')

    return age_in_datetime

countries = {}
for person in people:
    set_full_name(person) # 1. ülesanne

    print(get_full_name(person)) # 2. ülesanne

    print(get_person_age(person)) # 3. ülesanne

    ## Järgnev on 4. ülesande lahendus
    country = person['country']
    if country not in countries:
        countries[country] = 1
    else:
        countries[country] += 1
        # countries[country] = countries[country] + 1

print(countries)


# ÜLESANNE 2: Lisame andmed faili

file = open('people.csv', 'a')
file.truncate(0) # kui failis on midagi, siis see kustutatakse,
# vaja argumendina kaasa panna faili lõppsuurus, milleks on 0

for person in people:
    file.write(
        person['fname'] +
        ',' +
        person['lname'] +
        ',' +
        person['dob'] +
        ',' +
        person['country'] +
        '\n')

file.close()
