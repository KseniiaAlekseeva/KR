arr = ["dlcd", "kuk", "-dxko", "sa", "s"]
print(arr)
res = []
for i in range(len(arr)):
    if len(arr[i]) <= 3:
        res.append(arr[i])
print(res)
