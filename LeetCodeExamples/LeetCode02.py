def PalindromeNumber(number:int)-> bool:
    result = str(number)
    return result == result[::-1]
    


number = 222
print(PalindromeNumber(number))