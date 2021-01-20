lunch = {
    '20층' : '111-111',
    '양자강' : '222-222',
    '백수산' : '333-333'
}
# print(lunch.items())
# dict_items([('20층', '111-111'), ('양자강', '222-222'), ('백수산', '333-333')])



# 1. String formatting
with open('lunch.csv', 'w', encoding='utf-8') as f:
    for item in lunch.items():
        f.write(f'{item[0]},{item[1]} \n')




# 2. join method 활용
with open('lunch2.csv', 'w', encoding='utf-8') as f:
    for item in lunch.items():
        f.write(','.join(item) + '\n')



# 3. csv.writer
import csv

with open('lunch3.csv', 'w', newline='', encoding='utf-8') as f:
    csv_writer = csv.writer(f)
    for item in lunch.items():
        csv_writer.writerow(item)
