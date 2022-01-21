

from_year = int(input('Sisest aasta alates, millest soovid liigaastaid kuvada: '))

# Liigaasta def:
# 1. jagub täpselt 100ga ja 400ga
# 2. jagub täpselt 4ga ja ei jagu täpselt 100ga
for year in range(from_year, 2021):
    if (year % 400 == 0) and (year % 100 == 0):
        print(str(year) + ' on liigaaasta')
    if (year % 4 == 0) and (year % 100 != 0):
        print(str(year) + ' on liigaaasta')
    else:
        continue