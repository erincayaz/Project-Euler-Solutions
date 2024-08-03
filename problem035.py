import helper

def circular_shifts(number):
    number_str = str(number)
    length = len(number_str)
    shifts = []
    
    for i in range(length):
        shifted_str = number_str[-i:] + number_str[:-i]
        shifts.append(int(shifted_str))
    
    return shifts

def is_all_shifts_prime(n):
    all_sihfts = circular_shifts(n)

    for i in all_sihfts:
        if helper.isPrime(i) == False:
            return False
        
    return True

count = 1
for i in range(3, 1000000, 2):
    if is_all_shifts_prime(i):
        count += 1

print(count)