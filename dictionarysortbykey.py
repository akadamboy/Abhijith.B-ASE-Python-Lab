d = {"Sreejith": 2, "Jeevan": 4, "Akash": 3, "Mohan": 1, "Nikhil": 0}
print('Original dictionary : ',d)
d1 =sorted(d.items())
print('Dictionary in ascending order by value : ',d1)
d1 =sorted(d.items(), reverse=True)
print('Dictionary in descending order by value : ',d1)
