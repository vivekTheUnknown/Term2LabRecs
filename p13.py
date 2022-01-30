input_list = list(eval(input("enter a series of nos.: ")))
one_digit_list = [str(x) for x in input_list]

print(one_digit_list)
for i in range(len(one_digit_list)):
    for j in range(len(one_digit_list) - i - 1):
        if one_digit_list[j][-1] > one_digit_list[j+1][-1]:
            temp = one_digit_list[j]
            one_digit_list[j] = one_digit_list[j+1]
            one_digit_list[j+1] = temp

print(one_digit_list)