### Example
echo_word = lambda word1,echo : word1 * echo
result = echo_word("hey", 5)
print(result)



### Filter() in a lambda function
fellowship = ['frodo', 'samwise', 'merry', 'pippin', 'aragorn', 'boromir', 'legolas', 'gimli', 'gandalf']
result = filter(lambda member: len(member) > 6, fellowship)
result_list = list(result)
print(result_list)
