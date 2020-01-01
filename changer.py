import pandas as pd
import random
import xlsxwriter

df = pd.read_excel('cha.xlsx')
df = df[['Email', 'Name']]
print(type(df))

dff = df.values.T.tolist()

comb_dict = {i: [dff[1][i], dff[0][i]] for i in range(126)}
print(comb_dict)

rando = []
for _ in range(30):
    rando.append(random.randrange(0, 126))


print(rando)

hello = []
helloo = []
for _ in range(30):
    hello.append(comb_dict[rando[_]][0])
    helloo.append(comb_dict[rando[_]][1])


print(hello, helloo)

workbook = xlsxwriter.Workbook('CodeTalks.xlsx')
worksheet = workbook.add_worksheet()

col = 0
for row, data in enumerate(hello):
    worksheet.write(row + 1, col, data)
col = 1
for row, data in enumerate(helloo):
    worksheet.write(row + 1, col, data)

workbook.close()
