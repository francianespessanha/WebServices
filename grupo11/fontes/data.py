import datetime

#day = datetime.datetime(2003, 8, 4, 12, 30, 45)
#print day
#print day.year, day.month, day.day

lista = []
data = datetime.datetime(2003, 8, 4, 12, 30, 45)
lista = [[1,1,1,data,100], [2,2,1,data,900], [3,2,2,datetime.datetime(2013, 4, 26, 00, 00, 00),17]]
print lista[0][3]
