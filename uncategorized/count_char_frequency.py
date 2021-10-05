#  Write a Python program to count the number of characters (character frequency) in a string.

# initializing string 
string = "google.com"
  
# create empty dict, will contain frequency later
frequency = {}
  
# for in loop. read each character(index) on provided string
for index in string:
    if index in frequency:
        frequency[index] += 1
    else:
        frequency[index] = 1
        
# print dict to console
print(frequency)