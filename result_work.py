lst = ["hello", ";-)", "The", "1567"]
res = []
for item in range(len(lst)):
    if len(lst[item]) <= 3:
        res.append(lst[item])
print(res)
