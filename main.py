import os
from PyQt6.QtWidgets import QApplication, QWidget, QFileDialog, QLabel, QPushButton, QListWidget, QHBoxLayout, \
    QVBoxLayout, QMessageBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PIL import Image
from PIL.ImageFilter import BLUR, DETAIL


class ImageProcessor:
    def __init__(self):
        pass

    def load_image(self, filename):
        pass

    def save_image(self, filename):
        pass

    def b_w(self):
        pass

    def rotate_left(self):
        pass

    def rotate_right(self):
        pass

    def flip(self):
        pass

    def blur(self):
        pass




app = QApplication()
mac = QWidget()
mac.resize(800, 600)
mac.setWindowTitle('SevaShop')

app.exec()


def choose_workdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()


def show_filenames_list():
    extensions = ['JPG', ]


if __name__ == '__main__':
    pass
