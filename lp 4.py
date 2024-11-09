result = []
def divider(a, b):
    try:
        a < b
        raise ValueError
    except:
        b > 100
        raise IndexError
    return a/b
data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8 : 4}
for key in data:
   try:
       res = divider(key, data[key])
       result.append(res)
   except:
       print("Сталася помилка")

print(result)