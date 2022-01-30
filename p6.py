height_list = list(eval(input("enter the heights of different ppl: ")))
for i in range(len(height_list)):
    for j in range(len(height_list) - i - 1):
        if height_list[j] > height_list[j+1]:
            temp = height_list[j]
            height_list[j] = height_list[j+1]
            height_list[j+1] = temp
print(height_list)