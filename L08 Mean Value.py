mean1 = 38
correct_num = 56 
wrong_number = 36
total_nums = 40

#Current sum
Sum = mean1 * total_nums
print(f"The current sum is {Sum}")

#Actual Sum
Sum = (Sum - wrong_number) + correct_num
print(f"The correct sum is {Sum}")

#Correct mean
mean2 = Sum / total_nums
print(f"The correct mean is {mean2}")
