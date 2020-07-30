import math
priorities = [2,9,3,2,3]
unsort_pri = priorities.copy()
priorities.sort()
levels =[]

mylist = list(dict.fromkeys(priorities))
print(len(mylist))

for y in range(1,len(mylist)+1):
    levels.append(y)
levels.sort()
print("levels:",levels)


end_dic = dict(zip(mylist, levels))
print(end_dic)

result =[]
for x in unsort_pri:
    print(x)
    result.append(end_dic.get(x))

" ".join(str(x) for x in result)
print(result)

