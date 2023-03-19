#!/usr/bin/env python3

import sys
import pytest
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class TestButtons:
    @classmethod
    def setup_class(cls):
        cls.app = QApplication(sys.argv)
        cls.window = QMainWindow()
        cls.window.setGeometry(100, 100, 300, 200)
        cls.button1 = QPushButton("Button 1", cls.window)
        cls.button1.move(50, 50)
        cls.button1.clicked.connect(cls.button1_pressed)
        cls.button2 = QPushButton("Button 2", cls.window)
        cls.button2.move(150, 50)
        cls.button2.clicked.connect(cls.button2_pressed)
        cls.window.show()

    @classmethod
    def teardown_class(cls):
        cls.window.close()
        del cls.app

    @staticmethod
    def button1_pressed():
        print("Button 1 was clicked")

    @staticmethod
    def button2_pressed():
        print("Button 2 was clicked")

    def test_button1_press(self):
        self.button1.clicked.emit()
        assert self.button1.text() == "Button 1"

    def test_button2_press(self):
        self.button2.clicked.emit()
        assert self.button2.text() == "Button 2"
