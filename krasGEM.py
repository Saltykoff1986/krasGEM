import math

T = []
W = []
with open('input.csv','r') as f:
    n = 0
    param = []
    for line in f:
        a = line.split(';')
        p = []
        w = []
        for i in range(1,len(a)):
            if n < 3:
                a[i].replace(',','.')
                p.append(a[i])
            else:                    
                w.append(float(a[i].replace(',','.')))
        if n > 2:
            W.append(w)
            T.append(int(a[0]))
        else:
            param.append(p)
        n += 1
k = []
L0 = []
dT = []
for i in range(len(param[0])):
    k.append(float(param[0][i]))
    L0.append(float(param[1][i]))
    dT.append(int(param[2][i]))
T0 = T[0]
Tend = T[len(T)-1]
CH4 = []
for n in range(Tend-T0):
    ch4 = []
    
    for ii in range(len(param[0])):
        c = 0
        for i in range(n):
            for j in range(dT[ii]):
                dt = dT[ii]
                c += k[ii]*L0[ii]*(W[i][ii]/dt)*math.exp(-k[ii]*(n-i+j/dt))
        ch4.append(c)
    CH4.append(ch4)

with open('results.csv','w') as f:
    for i in range(Tend-T0):
        strin = str(T[i])+';'
        print(i)
        for j in range(len(CH4[0])):
            strin += str(CH4[i][j]).replace('.',',') + ';'
        f.write(strin+'\n')
    