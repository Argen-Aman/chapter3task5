from decimal import Decimal

your_text = input('Type any text:\n')

def counting_stars (your_text):
    l = 0
    u = 0
    for i in your_text:
        if i in ['.', ',' ,':' ,';' ,'!', '?', '(', ')', '[', ']', '{', '}', '-', '"', "'", ' ', '@', '#', '$', '%', '^', '&', '*', '№', '~', '`', '-', '_', '+', '=', '<', '>', '|', '\n', '/']:
            continue
        elif i.islower():
            l += 1
        elif i.isupper():
            u += 1
    s = l + u
    
    x = Decimal((l/s)*100)
    l_percentage = round(x,2)

    y = Decimal((u/s)*100)
    u_percentage = round(y,2)

    print(f'In the text {u_percentage} % of letters are in upper case and {l_percentage} % of letters are in lower case.')

counting_stars (your_text)
