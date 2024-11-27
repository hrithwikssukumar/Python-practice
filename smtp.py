import smtplib

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('hrithwikssukumar@gmail.com', 'wiwf zdqg foge cipo')  # Replace with app password
    print("Login successful!")
    server.quit()
except smtplib.SMTPAuthenticationError as e:
    print(f"SMTPAuthenticationError: {e}")