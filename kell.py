from datetime import datetime
from time import sleep

# tsüklite liigid:
#  1. while, 2. for, 3. for in
while True:
    praegu_aeg = datetime.now()
    print(praegu_aeg.strftime("%H:%M:%S")) # aja kuvamise formaat - "%H:%M:%S" - veel formaate: https://www.geeksforgeeks.org/python-strftime-function/
    sleep(1)

