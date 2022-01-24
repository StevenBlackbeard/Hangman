# put your python code here
s = 0
ss = 0
while True:
    x = int(input())
    s += x
    ss += x * x
    if s == 0:
        print(ss)
        break

# sums = 0
# ss = 0
# num_in = int(input())
# sums += num_in
# ss += (num_in**2)
#
# while sums != 0:
#     num_in = int(input())
#     sums += num_in
#     ss += (num_in ** 2)
# else:
#     print(ss)
