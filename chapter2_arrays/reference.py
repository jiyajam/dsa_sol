# 1 2 3 4 5 6 7 8 9 10
#starting address being 100

x=[1,2,3,4,5,6,7,8,9,10]
x[3]=10 #O(1)
print(x[3]) #10 #O(1)
print(x)

# x.append(11) #O(1)
# print(x) #[1, 2, 3, 10, 5, 6, 7, 8, 9, 10, 11]
#
# x.insert(3,29 )     #O(n)
# print(x) #[1, 2, 3, 10, 10, 5, 6, 7, 8, 9, 10, 11]
#
# # val=x.pop(3) #O(1)

del x[3] #O(n)
print(x)
# print(val)