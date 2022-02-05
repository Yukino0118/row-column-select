dimension = []
import pandas as pd
while True:
    A = list()
    B = list()
    Width,Space = map(eval,input('Input dimension:').split('/'))
    D = [Width,Space]
    if Width == 0 and Space == 0:
        break
    df = pd.read_excel('dimension.xlsx', header = 2 ,index_col = 0)
    A = (df.loc[Width,Space].values.tolist())
    C = D + A 
    dimension.append(C)
    D = list()
with open('new.csv', 'w') as f:
    f.write('Width,Space,TCD,BCD,THK,SB,BB'+'\n')
    for d in dimension:
        f.write(str(d[0])+','+str(d[1])+','+str(d[2])+','+str(d[3])+','+str(d[4])+','+str(d[5])+','+str(d[6])+'\n')
        
    
