def isPanditigal(n):
  s = str(n)
  hs = {-1}
  for i in range(len(s)):
    if s[i] in hs:
      return False
    
    if s[i] != "0":
      hs.add(s[i])

  return len(hs) == 10

maxNumber = 1
maxFormedNumber = 1
i = 2
while i < 9999:
  num = ""
  for j in range(1, 9):
    if len(num) >= 9:
      break

    num += str(i * j)

  if len(num) == 9 and isPanditigal(num):
    maxNumber = i
    maxFormedNumber = num

  i += 1

print("Max pandigital number is:", maxFormedNumber)