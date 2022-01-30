import num2words

car_name_list = ('toyota', 'honda', 'GM', 'Ford', 'BMW', 'Volkswagen',
'Mercedes', 'Ferrari', 'Porsche')

names_to_be_printed = car_name_list[2:7]
for i in range(0, len(names_to_be_printed)):
    print(num2words.num2words(i+1, to='ordinal'), names_to_be_printed[i])
