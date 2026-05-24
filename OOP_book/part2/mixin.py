from typing import Protocol

class Emailable(Protocol):
    email: str

class Contact:
    def __init__(self, name:str, email:str):
        self.name = name
        self.email = email 

class Table:
    def __init__(self, size):
        self.size = size
    
class MailSender:
    def send_notification(self, target: Emailable, message: str):
        print(f"Отправка сообщения на {target.email}: {message}")

class EmailableContact(Contact, MailSender):
    pass

e_contact = EmailableContact("Joe", "joe@mail.com")
e_contact.send_notification(e_contact, "Hello")


# table = Table(33)
# contact = Contact("joe", "joe@mail.com")
# sender = MailSender()
# sender.send_notification(contact, "Why are you gay?")
# sender.send_notification(table, "Why are you gay?")

