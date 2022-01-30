no_of_times = int(input("enter how many fibonacci nos. u want: "))
fibonacci_list = [0, 1]
for i in range(0, no_of_times - 2):
    x = fibonacci_list[-1]
    y = fibonacci_list[-2]
    z = x + y
    fibonacci_list.append(z)

print(tuple(fibonacci_list))
