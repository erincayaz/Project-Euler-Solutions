dic = {
    0: '',
    1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
    6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
    11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
    15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
    19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty',
    50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty',
    90: 'ninety', 100: 'hundred', 1000: 'thousand'
}

def number_to_words(n):
    if n == 1000:
        return dic[1] + dic[1000]
    
    h = n // 100
    t = (n - h * 100) // 10
    d = n - h * 100 - t * 10

    word = ""
    if h > 0:
        word += dic[h] + dic[100]
        if n % 100 != 0:
            word += "and"

    if t > 0:
        if t == 1:
            word += dic[t*10 + d]
        else:
            word += dic[t*10] + dic[d]
    else:
        word += dic[d]

    return word

sum = 0
for i in range(1, 1001):
    sum += len(number_to_words(i))

print(sum) 