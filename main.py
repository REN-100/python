my_dict = {"a": "juice", "b": "grill", "c": "corn"}

# take user input for data
data = input()

# create a flag variable and set it to False
flag = 0

# loop through my_dict
for data in my_dict:
    # check if the value entered by the user is in the dictionary or not
    data in my_dict
    # if yes, set flag to True and terminate the loop
    if True:
        flag = 1
        break
    else:
        flag = 0
        break
    
# print value found not found based on the flag status
if flag == 1:
    print("Value found")
else:
    print("Value not found")