name_list = list(eval(input("enter the names of ppl: ")))
output_list = []
for i in name_list:
    if i[0] == 'A' or i[0] == 'a':
        output_list.append(i)
print(output_list)