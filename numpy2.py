import numpy as np
arr = np.array([2, 55, 32, 76, 34, 99])
re = True
for i in arr:
    if i>100:
        re = False
        break
if re:
    print("Test case passed , none of the element is found greater than 100")
else:
    print("Test case failed, value more than 100 found")
