import re

s = "am_a"
mod_s = re.sub(r'[\W_]+', '', s)
str_list = list(mod_s.lower())
flag = 'true'
j = -1
for i in str_list:
    if i != str_list[j]:
        flag = 'false'
        break
    j = j-1
print(flag)
