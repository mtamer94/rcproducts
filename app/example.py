import pandas as pd

catalogue = pd.read_csv('data/catalogue.csv')

list = catalogue['MPNs'].to_list()

for value in list:
    if '08G-P5-3767-KL' == value:
        print('yes')

if '08G-P5-3767-KL' in list:
    print('yes')
else: print('no')