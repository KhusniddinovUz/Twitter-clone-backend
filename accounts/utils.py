from django.core.mail import EmailMessage


class Util:
    @staticmethod
    def send_email(data):
        subject = 'Twitter Clone Uz email verification'
        email = EmailMessage(subject=subject, body=data['message'], to=(data['receiver'],))
        email.send()
