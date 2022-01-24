word_in = input()
list_out = ''
for i in word_in:
    if i.islower():
        list_out += i
    else:
        list_out += "_" + i.lower()
print(list_out)

# import re
#
# name = input()
# name = re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()
# print(name)  # camel_case_name


