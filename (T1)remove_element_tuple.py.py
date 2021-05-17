tpl = (2, 5, 9, 11, 'hello', [13, 43])
print(id(tpl))
n = 4  # 4th index element to be removed
lst = list(tpl)
lst.remove(lst[4])
tpl = tuple(lst)
print(tpl)
print(id(tpl))
