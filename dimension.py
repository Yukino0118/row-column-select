dimension = []
import pandas as pd
while True:
    A = list()
    B = list()
    try:
        Width,Space = input('Input dimension, input 0/0 quit:').split('/')
        D = [Width,Space]
        if Width == '0' and Space == '0':
            break
        df = pd.read_csv('dimension.csv', header = 2, index_col = 0)
        A = df.loc[Width,Space].tolist()
        C = D + A
        dimension.append(C)
        D = list()
    except:
        print('type error')
    else:
        continue
with open('new.csv', 'w') as f:
    f.write('Width,Space,TCD,BCD,THK,SB,BB'+'\n')
    for d in dimension:
        f.write(d[0]+','+d[1]+','+str(d[2])+','+str(d[3])+','+str(d[4])+','+str(d[5])+','+str(d[6])+'\n')
        
        