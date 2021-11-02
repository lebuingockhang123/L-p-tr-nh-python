"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Program:  Assume that the variable data refers to the dictionary {'b':20, 'a':35}. Write the
values of the following expressions:
a. data['a']
b. data.get('c', None)
c. len(data)
d. data.keys()
e. data.values()
f. data.pop('b')
g. data # After the pop above

Solution:
    a. 35
    b. None
    c. 2
    d. dict_keys(['b', 'a'])
    e. dict_values([20, 35])
    f. 20
    g. {'a': 35}

"""
data = {'b': 20, 'a': 35}
print(data['a'])
print(data.get('c', None))
print(len(data))
print(data.keys())
print(data.values())
print(data.pop('b'))
print(data)