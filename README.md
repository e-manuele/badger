# Badger
Work in progress..

This repository includes an executable (.exe) and the code for a Raspberry Pico-based Badger RFID app. The app is designed for reading RFID tags and logging the readings into a file in Windows.
https://github.com/micropython/micropython/blob/master/docs/library/pyb.USB_VCP.rst
https://github.com/openmv/openmv/blob/300331a8daca16d2a895126aff2fee9b48897535/src/omv/templates/main_py.h#L5
https://docs.micropython.org/en/latest/library/pyb.USB_VCP.html


from datetime import datetime

# dates in string format
str_d1 = '2021/10/20'
str_d2 = '2022/2/20'

# convert string to date object
d1 = datetime.strptime(str_d1, "%Y/%m/%d")
d2 = datetime.strptime(str_d2, "%Y/%m/%d")

# difference between dates in timedelta
delta = d2 - d1
print(f'Difference is {delta.days} days')