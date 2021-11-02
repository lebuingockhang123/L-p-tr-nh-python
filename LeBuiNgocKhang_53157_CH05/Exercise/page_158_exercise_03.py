"""
Author: Le Bui Ngoc Khang
Date: 12/07/1997
Program:  Assume that the variable data refers to the dictionary {'b':20, 'a':35}. Write the
expressions that perform the following tasks:
a. Replace the value at the key 'b' in data with that value’s negation.
b. Add the key/value pair 'c':40 to data.
c. Remove the value at key 'b' in data, safely.
d. Print the keys in data in alphabetical order.

Solution:
a. {'b': -20, 'a': 35}
b. {'b': -20, 'a': 35, 'c': 40}
c. {'b': -20, 'a': 35, 'c': 40}
d.      a 35
        b -20
        c 40

"""
data = {'b': 20, 'a': 35}

value = data.get("b")
data["b"] = -value
print(data)


data.update({'c': 40})
print(data)


# data.pop('b')
print(data)


theKeys = list(data.keys())
theKeys.sort()
for key in theKeys:
    print(key, data[key])