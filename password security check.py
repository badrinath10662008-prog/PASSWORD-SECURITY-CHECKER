print("=" * 45)
print("       PASSWORD SECURITY ANALYZER")
print("=" * 45)

print("Welcome to Password Security Analyzer!")
print("This tool checks your password strength.")

print("=" * 45)

password = input("\nEnter your password: ")

uppercase = False
lowercase = False
number = False
special = False

for char in password:

    if char.isupper():
        uppercase = True

    elif char.islower():
        lowercase = True

    elif char.isdigit():
        number = True

    else:
        special = True

print("\nPassword Analysis:")
print("Uppercase:", uppercase)
print("Lowercase:", lowercase)
print("Numbers:", number)
print("Special Characters:", special)

score = 0

if len(password) >= 8:
    score = score + 1

if uppercase:
    score = score + 1

if lowercase:
    score = score + 1

if number:
    score = score + 1

if special:
    score = score + 1

print("\nPassword Score:", score, "/ 5")

if score <= 2:
    print("Password Strength: WEAK")

elif score <= 4:
    print("Password Strength: MEDIUM")

else:
    print("Password Strength: STRONG")

print("\nSuggestions:")

if len(password) < 8:
    print("- Use at least 8 characters.")

if not uppercase:
    print("- Add an uppercase letter.")

if not lowercase:
    print("- Add a lowercase letter.")

if not number:
    print("- Add a number.")

if not special:
    print("- Add a special character.")

print("\nThank you for using Password Security Analyzer!")