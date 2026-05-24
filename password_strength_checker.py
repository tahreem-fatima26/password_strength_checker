
# Password Strength Checker

import re

print("\n========== PASSWORD STRENGTH CHECKER ==========\n")

# User Input
password = input("Enter your password: ")

# Initial Score
score = 0

# Conditions
length = len(password)

# Length Check
if length >= 8:
    score += 1

# Uppercase Check
if re.search(r"[A-Z]", password):
    score += 1

# Lowercase Check
if re.search(r"[a-z]", password):
    score += 1

# Digit Check
if re.search(r"[0-9]", password):
    score += 1

# Special Character Check
if re.search(r"[@$!%*?&#]", password):
    score += 1


# Password Strength Logic
print("\n========== PASSWORD ANALYSIS ==========\n")

print(f"Password Length : {length}")

if re.search(r"[A-Z]", password):
    print("Uppercase Letter : Present")
else:
    print("Uppercase Letter : Missing")

if re.search(r"[a-z]", password):
    print("Lowercase Letter : Present")
else:
    print("Lowercase Letter : Missing")

if re.search(r"[0-9]", password):
    print("Numbers           : Present")
else:
    print("Numbers           : Missing")

if re.search(r"[@$!%*?&#]", password):
    print("Special Character : Present")
else:
    print("Special Character : Missing")


# Final Result
print("\n========== RESULT ==========\n")

if score == 5:
    print("Password Strength : STRONG")
    print("Security Level    : HIGH")

elif score >= 3:
    print("Password Strength : MEDIUM")
    print("Security Level    : MODERATE")

else:
    print("Password Strength : WEAK")
    print("Security Level    : LOW")


print("\n=======================================\n")
print("Thank you for using Password Checker!")