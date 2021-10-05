# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string. 
# refer to the image below: python-data-type-string-image-exercise-3.png
# Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Sample String : 'w3'
# Expected Result : 'w3w3'
# Sample String : ' w'
# Expected Result : Empty String

# create function
def first_two_last_two(str):
    # if str input is less than two return empty string
  if len(str) < 2:
    return ''
	# else return first 2 and last 2 chars from string
  return str[0:2] + str[-2:]

print(first_two_last_two('w3resource'))
print(first_two_last_two('w3'))
print(first_two_last_two('w'))