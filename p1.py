input_list = list(eval(input("enter a series of nos. : ")))
element_to_search = int(input("enter the element to search for: "))
if element_to_search in input_list:
    print("its there")
else:
    print("no its not there")