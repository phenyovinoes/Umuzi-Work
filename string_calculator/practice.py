# # print("1\n2,3")

# god="1\n2,3"
# print(god[2])

# for i in "1\n2,3":
#     print(i)


# for i in "//,\n1,2":
#     print(i)

# # god="//;\n1;2"
# # print(god[0]+god[1])

# if '-' in "//,\n-1,2":
#     print('-')



god="//***\n1***2***3"
print(god.index('\n'))
print(str(god[2:god.index('\n')]))
