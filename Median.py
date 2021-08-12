
test_list = [1, 3, 2, 4, 0]
test_list.sort()

mid = len(test_list) // 2
median = (test_list[mid] + test_list[~mid]) / 2
  
print("Median of list is : " + str(res))


