#!/usr/bin/python3
sum = 0
count = 0
print("please input 10 number,use , split: ")
str = input()
arr = str.split(",")
for num in arr:
    sum = sum + float(num)
    count = count + 1
average = sum / count
print("N = {},Sum = {}".format(count,sum))
print("Average = {:.2f}".format(average)) 
