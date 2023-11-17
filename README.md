# Badger
Work in progress..

This repository includes an executable (.exe) and the code for a Raspberry Pico-based Badger RFID app. The app is designed for reading RFID tags and logging the readings into a file in Windows.
https://github.com/micropython/micropython/blob/master/docs/library/pyb.USB_VCP.rst
https://github.com/openmv/openmv/blob/300331a8daca16d2a895126aff2fee9b48897535/src/omv/templates/main_py.h#L5
https://docs.micropython.org/en/latest/library/pyb.USB_VCP.html


from datetime import datetime

str_d1="10-20 18:19"
str_d2="10-20 19:40"

d1 = datetime.strptime(str_d1, "%m-%d %H:%M")
d2 = datetime.strptime(str_d2, "%m-%d %H:%M")

delta = d2 - d1 

diff_in_hours = delta.total_seconds() / 3600
print('Difference between two datetimes in hours:')
print(diff_in_hours)
