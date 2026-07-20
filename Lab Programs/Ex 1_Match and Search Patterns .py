import re

text = "My phone number is 9876543210 and my email is test@gmail.com"

# Search for phone number
phone = re.search(r"\d{10}", text)

# Search for email
email = re.search(r"\S+@\S+", text)

if phone:
    print("Phone Number Found:", phone.group())

if email:
    print("Email Found:", email.group())