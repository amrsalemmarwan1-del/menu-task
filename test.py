def seconds_to_hms(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours:02}:{minutes:02}:{seconds:02}"



def celsius_to_fahrenheit(celsius):
    fahrenheit= celsius * 9/5 + 32
    return round(fahrenheit, 2)



def split_evenly(total,people):
    money = total // people
    remainder = total % people
    return money, remainder



def initials(full_name):
    words = full_name.split()
    result = ""
    i = 0
    while i < len(words):
        result += words[i][0].upper()
        i += 1
    return result



def is_palindrome(word):
    word = word.strip().lower()
    return word == word[::-1]



def mask_email(email):
    at_index = email.index('@')
    username = email[:at_index]
    domain = email[at_index:]
    
    if len(username) <= 2:
        masked_user = username[0] + '*'
    else:
        masked_user = username[0] + '*' * (len(username) - 2) + username[-1]
        
    return masked_user + domain



def middle(values):
    n = len(values)
    mid = n // 2
    if n % 2 != 0:
        return values[mid : mid + 1]
    return values[mid - 1 : mid + 1]



def rotate_left(values,k):
    n = len(values)
    k = k % n
    return values[k:] + values[:k]



def fib_list(n):
    result = []
    a, b = 0, 1
    while len(result) < n:
        result.append(a)
        a, b = b, a + b
    return result



def collatz_steps(n):
    steps = 0
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps 