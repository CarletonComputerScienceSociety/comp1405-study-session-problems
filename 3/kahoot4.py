data = [9, 1, 6, 2, 7, 3, 4, 5, 8, 10]

data.reverse()
data.append(6)
data.pop(2)
value = data.count(6)
data.pop(6)
data.append(value)
data.sort()
data.pop(2)

print(data)

