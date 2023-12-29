password = input('Enter new password: ')

result = {}  # dictionary

if len(password) >= 8:
    result["Length"] = True
else:
    result["Length"] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True

result["digits"] = digit

uppercase = False
for i in password:
    if i.upper():
        uppercase = True

result["upper-case"] = uppercase

print(result)

if all(result.values()):
    print("Strong password")
else:
    print("Weak password")
