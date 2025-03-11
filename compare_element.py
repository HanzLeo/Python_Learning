def find_differences(list1,list2):
    #找出在1不在list2 的元素
    unique_to_list1 = [x for x in list1 if x not in list2]
    #找出在list2不在list1中的元素
    unique_to_list2 = [x for x in list2 if x not in list1]
    return unique_to_list1, unique_to_list2

#测试数据
a = [1,2,3,4,5]
b = [4,5,6,7,8]
diff_a, diff_b = find_differences(a,b)

print(f"仅在列表a中：{diff_a}")
print(f"仅在列表b中：{diff_b}")
