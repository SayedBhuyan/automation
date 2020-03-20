from twilio.rest import Client 
 
account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

def send_msg(arg1, arg2):
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body="This is just a python code",
        to='whatsapp:+19995554444'
    )

    print(message.sid)

