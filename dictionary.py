scores = {'james': 1828, 'thomas': 3628, 'danny': 9310}
print(scores)
scores['bobby'] = 4401
numbers = {1: 'One', 2: 'Two', 3: 'Three'}
print(scores)
print(numbers)

#print some value
print("score=",scores['thomas'])

# การอ่านข้อมูลทั้งหมดของ dictionary
for k,v in scores.items():
    print(k,v)

for a,b in numbers.items():
    print(a,b)

# อ่านเฉพาะ value ทั้งหมด
for v in scores.values():
    print(v)
# อ่านเฉพาะ key ทั้งหมด
for k in scores.keys():
    print(k)

