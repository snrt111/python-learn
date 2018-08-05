#!/usr/bin/python3
fahrenheit = 0
print("华氏温度 摄氏温度")
while fahrenheit <= 250:
    celsius = (fahrenheit - 32) / 1.8 # 转换为摄氏度
    print("{:8d} {:8.2f}".format(fahrenheit , celsius))
    fahrenheit = fahrenheit + 20
