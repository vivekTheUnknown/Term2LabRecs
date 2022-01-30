input_list = list(eval(input("enter a series of nos: ")))
output_list = []
for i in input_list:
    if i % 2 == 0:
        output_list.append(i + 10)
    else:
        output_list.append(i + 5)

print(output_list)