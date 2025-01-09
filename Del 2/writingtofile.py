# # Sample list of data
# my_list = ["item1", "item2", "item3", "item4"]

# # Specify the file path
file_path = "D:\SKOLE\Programmer - IT2\Del 2\main.txt"

# # Using "with open" syntax to automatically close the file
# with open(file_path, 'w') as file:
#     # Join the list elements into a single string with a newline character
#     data_to_write = ' '.join(my_list)
    
#     # Write the data to the file
#     file.write(data_to_write)

# print(f"The list has been written to {file_path}.")

# open file in read mode
f = open(file_path, 'r')

# display content of the file
#print(f.read())
x = f.read()
print(x)

# close the file
f.close()

size_y = 6
size_x = 13

dict = {}
x = x.replace('\n','')
t = 0
for i in range(size_y):
    list = []
    for j in range(size_x):
        list.append(x[t])
        t += 1
    dict[i] = list
print(dict)

print("lessago"[2])