input_list = list(eval(input("enter a series of nos. : ")))
output_list = []
for i in range(0, len(input_list)):
    if i%2 != 0:
        output_list.append(input_list[i] * 2)
    else:
        output_list.append(input_list[i])
print(output_list)