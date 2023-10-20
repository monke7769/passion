import pandas as pd

df=pd.read_csv('Emotion_final.csv')
# print(df['Text'])
divisions=[]
# ciphers ceaser, rsa, vinegar, binary, hexadecimal
# print(len(df['Text']))
ciphers={'ceaser':[],'rsa':[],'vinegar':[],'binary':[],'hexadecimal':[]}
names=['ceaser','rsa','vinegar','binary','hexadecimal']
index=-1
for i in range(len(df['Text'])):
    ciphers[names[index]].append(df['Text'][i])
    if(i%4291==0):
        index+=1
    if(index>4):
        break

import csv

new_row = [["leggings", 22.99, 483]]

with open('product_sales.csv', 'a', newline='') as file:
    
    writer = csv.writer(file)
    writer.writerows(new_row)
