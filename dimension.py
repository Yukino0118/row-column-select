dimension = []
WS = []
import pandas as pd
count = int(input('column numbers:'))
while True:
    A = list()
    B = list()
    Width,Space = map(eval,input('Input dimension:').split('/'))
    D = [Width,Space]
    if Width == 0 and Space == 0:
        break
    df = pd.read_excel('dimension.xlsx', header = 2)
    A.append(df.loc[Width,Space])
    for i in range(1,5):
        df2 = pd.read_excel('dimension.xlsx', header = (count + 6 + (i-1) * (count+4)))
        B.append(df2.loc[Width,Space])
    C = D + A + B
    dimension.append(C)
    D = list()
with open('new.csv', 'w') as f:
    f.write('Width,Space,TCD,BCD,THK,SB,BB'+'\n')
    for d in dimension:
        f.write(str(d[0])+','+str(d[1])+','+str(d[2])+','+str(d[3])+','+str(d[4])+','+str(d[5])+','+str(d[6])+'\n')
