import time

n = 1000
time_start = time.time()


print("This program will give the sum of the number you Inputted. /n")
number  =  int(input("Input any number: "))

sum = 0
for i in range(1,number+1):
    sum = sum + i

print("The sum is: ", sum)

time_end = time.time()
time_total = time_end - time_start
print("The total time of the Program is",time_total)


