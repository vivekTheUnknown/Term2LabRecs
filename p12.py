months = {
    "jan": 31,
    "feb": 29,
    "mar": 31,
    "apr": 30,
    "may": 31,
    "jun": 30,
    "jul": 31,
    "aug": 31,
    "sept": 30,
    "oct": 31,
    "nov": 30,
    "dec": 31
}
#PART 1:
month_input = str(input("enter the 3-letter abbriviation for the month u want the no of days for: "))
month_input.lower()
print(months[month_input])

#PART 2:
all_months = list(months.keys())
all_months.sort()
for i in all_months:
    print(i)

print("###########################################################")

#PART 3:
for i in months:
    if months[i] == 31:
        print(i)

print("###########################################################")

#PART 4:
all_months1 = list(months.keys())
all_days_of_months = list(months.values())
merged_list = []
for i in all_months1:
    i_index = all_months1.index(i)
    merged_list.append([i, all_days_of_months[i_index]])

for j in range(len(merged_list)):
    for k in range(len(merged_list) - j - 1):
        if merged_list[k][-1] < merged_list[k+1][-1]:
            temp = merged_list[k+1]
            merged_list[k+1] = merged_list[k]
            merged_list[k] = temp

final_dict = {x[0]: x[1] for x in merged_list}
print(final_dict)