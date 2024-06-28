def isPalindrome(n):
  n = str(n)
  return n[0] == n[-1] and n[1] == n[-2] and n[2] == n[-3]

n = 1
for i in range(100, 999):
  for j in range(100, 999):
    p = i * j
    if isPalindrome(p) and p > n:
      n = p

print(n)