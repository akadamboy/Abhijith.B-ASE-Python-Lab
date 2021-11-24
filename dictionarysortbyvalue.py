import operator
d = {"Sreejith": 2, "Jeevan": 4, "Akash": 3, "Mohan": 1, "Nikhil": 0}
print('Original dictionary : ',d)
d1 =sorted(d.items(), key=operator.itemgetter(1))
print('Dictionary in ascending order by value : ',d1)
d1 =sorted(d.items(), key=operator.itemgetter(1),reverse=True)
print('Dictionary in descending order by value : ',d1)
