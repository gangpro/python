# read_csv.py

# 1. split으로 읽어오기
with open('lunch.csv', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        #print(line.strip().split(','))
        pass


# 2. csv.reader로 읽어오기
import csv

with open('lunch.csv', 'r', encoding='utf-8') as f:
    items = csv.reader(f)
    for item in items:
        print(item)