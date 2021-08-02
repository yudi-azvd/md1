
# n = 10
# partial_sum = 0

# # \Sigma 4i-3 = n(2n-1)
# for i in range(1, n+1):
#   partial_sum += 4*i-3

# print(f'partial sum = {partial_sum}')
# print(f'    n(2n-1) = {n*(2*n-1)}')

n = 998
partial_sum = 0

# \Sigma 4i-3 = n(2n-1)
for i in range(1, n+1):
  print(2*i-1)
  partial_sum += 2*i-1

print(f'partial sum = {partial_sum}')
print(f'         n² = {n**2}')

