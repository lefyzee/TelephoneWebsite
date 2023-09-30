#Brandon Dudas
#Answer Machine

# Define a function for the answering machine
def answering_machine():
    print("Welcome to the answering machine!")
    caller_name = input("Please state your name: ")
    message = input("Leave a message: ")

    # Save the message to a file
    with open(f"{caller_name}_message.txt", "w") as file:
        file.write(message)

    print(f"Thank you, {caller_name}! Your message has been recorded.")

# Call the function to run the answering machine
answering_machine()

from twilio.rest import Client

# Replace these with your own credentials
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
twilio_phone_number = 'your_twilio_phone_number'
recipient_phone_number = 'recipient_phone_number'

# Create a Twilio client
client = Client(account_sid, auth_token)

# Send a text message
message = client.messages.create(
    body="Hello from your Python script!",
    from_=twilio_phone_number,
    to=recipient_phone_number
)

print(f"Message sent with SID: {message.sid}")

