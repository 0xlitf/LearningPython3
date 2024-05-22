# myapp/management/commands/run_gui.py
from django.core.management.base import BaseCommand
from app_main.gui import main

class Command(BaseCommand):
    help = 'Run the PySide6 GUI application'

    def handle(self, *args, **kwargs):
        main()
