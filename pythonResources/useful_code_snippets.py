### Merge two dictionaries
dictionary1 = {"name": "Joy", "age": 25}
dictionary2 = {"name": "Joy", "city": "New York"}
merged_dict = {**dictionary1, **dictionary2}
print("Merged dictionary:", merged_dict)


### Print a String n time
n = 5
string = "Hello!"
print(string * n)


### Retrieve the Last Element of a List
my_list = ['banana', 'apple', 'orange', 'pineapple']
#Using brute force method
last_element = my_list[len(my_list) - 1]
#Using negative indeces
last_element = my_list[-1]
#Using pop method
last_element = my_list.pop()


### Reversing a String
str = "Hello World"
print("Reversed string is:", str[::-1])


### Combining a List of Strings into a Single String
list = ["Hello", "world", "Ok", "Bye!"]
combined_string = " ".join(list)
print(combined_string)


###  Filter values
my_list = [0,1,2,3,6,7,9,11]
result = filter(lambda x: x % 2!=0, my_list)
print(list(result))


### Remove Duplicates From a List
list1 = [1,2,3,3,4,'John', 'Ana', 'Mark', 'John']
    #Method 1
def remove_duplicate(list_value):
    return list(set(list_value))
print(remove_duplicate(list1))

    #Method 2
result = []
[result.append(x) for x in list1 if x not in result]
print(result)
