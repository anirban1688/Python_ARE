string='hello'
x=string.capitalize()
print(x)

caps='WELCOME TO PYTHON'
x=caps.casefold()
print(x)

string='convert me to upper case'
x=string.upper()
print(x)
count=len(string)
print(count)
y=string.find('me')
print(y)
z=string.index('me')
print(z)

txt = "For only {price} INR"
print(txt.format(price = 35))

datetoday = ("7", "11", "2022")
x = "-".join(datetoday)
print(x)

s='Monty Python'
print(s[:-1])
print(s[2:-4])

word='gamma'
if(word<'beta'):
    print("true")
else:
    print("false")