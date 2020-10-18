class Email:
    def __init__(self, sender, receiver, content, is_sent=False):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = is_sent

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []
while True:
    input_line = input()
    if input_line == "Stop":
        break
    else:
        sender = input_line.split()[0]
        receiver = input_line.split()[1]
        content = input_line.split()[2]
        email = Email(sender, receiver, content)
        emails.append(email)

emails_to_send = list(map(lambda x: int(x), input().split(", ")))

for index in emails_to_send:
    emails[index].send()

for email in emails:
    print(email.get_info())