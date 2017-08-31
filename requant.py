#col0 date1
#col1 date2
#col2 perc amphora
#col3 perc local amphora
#col4 duration

import numpy
#numpy.set_printoptions(threshold=numpy.inf)

table1 = numpy.genfromtxt('carthage.csv', delimiter = ',')


interval = 10 

start = int(-400 / interval)
end = int(50 / interval)

for i in range(start,end):
    print(i)
    
    
table2 = numpy.zeros([end-start,2])

#print(table2)

table2[:,0] = range(start,end)
table2[:,0] = table2[:,0] * 10

for i in range(table2.shape[0]):
    c = 0
    for j in range(table1.shape[0]):
        if (table2[i,0] <= table1[j,1]) and (table2[i,0] >= table1[j,0]):
            table2[i,1] = table2[i,1] + table1[j,2]
            c = c + 1
    table2[i,1] = float(table2[i,1] / c)

print(table2)
