
from sklearn.preprocessing import StandardScaler
data = [[10, 90], [12, 96], [9, 120], [13, 112], [8, 88]]

total = 0
for i in data:
    total += i[0]
average = total/len(data)
print(average) # 10.4

scaler = StandardScaler()
data = scaler.fit_transform(data)
print(data)

total = 0
for i in data:
    total += i[0]
average = total/len(data)

print(average) # very close to zero