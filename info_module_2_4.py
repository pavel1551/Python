# list_ = ['one', 'two', 'three']
# for i in list_:
#     print(i)
#     if i == 'three':
#         list_.remove(i)
# print(list_)
###################
# list_ = ['one', 'two', 'three']
# for i in range(len(list_)):
#     print(list_[i])
# print(list_)
###################
# list_ = ['one', 'two', 'three']
# for i in range(len(list_)):
#     list_[i] = ':('
# print(list_)
###################
# list_ = ['one', 'two', 'three']
# list_2 = [2, 3, 5, 4, 1]
# sum_ = 0
# for i in range(len(list_2)):
#     sum_ += list_2[i]
# print(sum_)
###################
for i in range(2, 11): #start, stop, step
    for j in range(1, 11):
        print(f'{i} x {j} = {i * j}')
###################
# dict_ = {'a': 1, 'b': 2, 'c': 3}
# for i in dict_:
#     print(i, dict_[i])
###################
# dict_ = {'a': 1, 'b': 2, 'c': 3}
# for i, k in dict_.items():
#     print(i, k)