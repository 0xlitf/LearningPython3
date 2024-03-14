# signals.py
from django.dispatch import Signal

# 定义一个带有两个参数的信号
my_signal = Signal(providing_args=["arg1", "arg2"])
