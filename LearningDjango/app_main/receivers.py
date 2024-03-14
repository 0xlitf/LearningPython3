# receivers.py
from django.dispatch import receiver
from .signals import my_signal

@receiver(my_signal)
def my_signal_receiver(sender, **kwargs):
    arg1 = kwargs.get('arg1')
    arg2 = kwargs.get('arg2')
    print(f"Received signal from {sender} with arg1={arg1} and arg2={arg2}")
