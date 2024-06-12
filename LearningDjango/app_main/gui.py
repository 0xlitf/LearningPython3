# app_main/gui.py
# from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
import sys
import threading
# class MyApplication(QApplication):
#     def __init__(self, argv):
#         super().__init__(argv)
#         self.main_window = QMainWindow()
#         self.main_window.setWindowTitle('Django PySide6 Integration')
#         self.label = QLabel('Hello from PySide6!', self.main_window)
#         self.main_window.setCentralWidget(self.label)
#         self.main_window.show()


def run_gui_thread():
    gui_thread = threading.Thread(target=main)
    gui_thread.start()


def main():
    # app = MyApplication(sys.argv)
    # sys.exit(app.exec())
    ...
