
test_list = [1, 2, 3, 4, 5]
  
test_list.sort()
mid = len(test_list) // 2
res = (test_list[mid] + test_list[~mid]) / 2
  
print("Median of list is : " + str(res))


