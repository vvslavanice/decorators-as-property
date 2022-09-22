'''
Create a class method named `validate`, which should be called from the `__init__` method to validate parameter email,
passed to the constructor. The logic inside the `validate` method could be to check if the passed email
parameter is a valid email string.
'''



class Contact_email:
    def __init__(self, emailofusers):
        self.email_adr = emailofusers
        self.validate(emailofusers)


    @classmethod
    def validate(cls, emailofusers):
        if "@" and "." in emailofusers:
            return True
        return False

if __name__ == '__main__':
    slavaemail = Contact_email("vverbytskyi2018@gmail.com")
    print(slavaemail.validate("mail.com"))
    print(Contact_email.validate("4"))
