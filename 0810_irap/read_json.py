import json

with open('test.json', "r") as f:
    j = json.load(f)
    f.close()
print(j)
print(type(j))

print(j['method_dict'])
print(j['meta_dict'])