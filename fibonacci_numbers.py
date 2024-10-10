# # For Loop
# prev1 = 1
# prev2 = 0
# fibList = [0,1]
# for i in range(18):
#     newFib = prev1 + prev2
#     fibList.append(newFib)
#     prev1 = newFib
#     prev2 = fibList[-2]
# print (fibList)


# Recursion
# print("starting now")


# print (0)
# print (1)
# count = 2
# def fibonacci(prev1,prev2):
#     global count
#     if count <= 19:
#         newFib = prev1 + prev2
#         print(newFib)
#         prev2 = prev1
#         prev1 = newFib
#         count += 1
#         fibonacci(prev1,prev2)
#     else:
#         print('all done')


# fibonacci(1,0)


# Finding The nth Fibonacci Number Using Recursion
def F(n):
    if n <=1:
        return n
    else:
        return(F(n-1) + F(n-2))

print(F(18))