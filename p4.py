input_list = list(eval(input("enter a series of nos. :")))
output_list = []
for i in input_list:
    x = list(str(i))
    if x[-1] == '3':
        output_list.append(i)
print(sum(output_list))