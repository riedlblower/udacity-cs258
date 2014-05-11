
def is_luhn_valid(n):
    length = len(str(n))
    checksum = int(str(n)[length-1:length])   # i.e. the last digit
    total = checksum
    i=1
    for l in range (0,length-1):
        digit = int(str(n)[length-(i+1):length-i])   # working back from the 2nd last digit
        if (i%2!=0):
            digit = digit * 2
            if digit > 9:
                digit = digit-9
        total = total + digit
        i = i + 1
    return total%10 == 0

print is_luhn_valid(352361060023017)
