s = input().lower()
set_list = list(set(s))
result = []

for x in set_list :
    result.append(s.count(x))

if result.count(max(result)) >= 2 :
    print("?")
else : print(set_list[result.index(max(result))].upper())
