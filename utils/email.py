import string, random, threading
from django.utils.text import slugify
from django.template.loader import render_to_string 
from django.core.mail import EmailMultiAlternatives

# Email Sending using Thread 
class EmailThread(threading.Thread):
    
    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()

class EmailUtil:   
    @staticmethod
    def send_mail(to, subject, body_context, template_name=None, from_email=None):
        html_version = template_name
        html_message = render_to_string(html_version, body_context).strip()   
        if from_email:
            email = EmailMultiAlternatives(subject=subject, body=html_message, from_email=from_email, to=to)
        else:
            email = EmailMultiAlternatives(subject=subject, body=html_message, to=to)
        email.content_subtype = 'html'
        email.mixed_subtype = 'related'
        # email.send()

        EmailThread(email).start()