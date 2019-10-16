#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'界面定义类'

import sys
from multiprocessing.dummy import Pool as ThreadPool
from PyQt5.QtWidgets import QDialog, QLabel, QPushButton, QLineEdit, QListWidget, QGridLayout, QComboBox, QMessageBox, \
    QApplication, QMenuBar, QAction, QMainWindow, QWidget, QVBoxLayout
from PyQt5.QtCore import pyqtSlot, QThread, QObject
from PyQt5.QtGui import QIcon, QPixmap, QImage
from common import config as config


class Sniper:
    def __init__(self):
        self.__pool = ThreadPool(8)

    def test(self, param):
        print('hello world', param)

    def start(self):
        app = QApplication(sys.argv)
        dialog = LayoutDialog()
        dialog.show()
        app.exec_()


class LayoutDialog(QMainWindow):
    __slots__ = ['word', 'movie_name_label', 'movie_name_line_edit', 'movie_source_label', 'movie_source_combobox',
                 'search_push_button', 'tip_label', 'search_content_label', 'search_content_text_list']

    def __init__(self):
        super().__init__()
        self.left = 300
        self.top = 300
        self.width = 400
        self.height = 450

        # self.work = WorkThread()
        self.init_widgets()
        self.init_layout()
        self.init_event()
        # self.init_widgets().init_layout().init_event()

    def init_widgets(self):
        self.setWindowTitle(self.tr("Sniper"))  # 设置窗体名称
        self.setGeometry(config.Main_Window_LEFT,
                         config.Main_Window_TOP,
                         config.Main_Window_WIDTH,
                         config.Main_Window_HEIGHT)  # 设置窗体位置及大小

        # 输入框
        self.address_label = QLabel(self.tr("请输入地址"))
        self.address_edit = QLineEdit()
        # 下拉框
        self.operate_select_option_label = QLabel(self.tr("请选择操作类型"))
        self.operate_select_option_combobox = QComboBox()
        self.operate_select_option_combobox.addItem(self.tr("接口读取"))
        self.operate_select_option_combobox.addItem(self.tr("接口调用"))
        self.operate_select_option_combobox.addItem(self.tr("文档生成"))
        # 开始按钮
        self.search_push_button = QPushButton(self.tr("开始"))
        # 控制台输出
        self.tip_label = QLabel(self.tr("准备就绪..."))
        # 菜单栏
        self.menu_bar = self.menuBar()

        return self

    def init_layout(self):
        top_layout = QGridLayout()

        # 输入框
        top_layout.addWidget(self.address_label, 0, 0)
        top_layout.addWidget(self.address_edit, 0, 1)
        # 下拉框
        top_layout.addWidget(self.operate_select_option_label, 0, 2)
        top_layout.addWidget(self.operate_select_option_combobox, 0, 3)
        # 开始按钮
        top_layout.addWidget(self.search_push_button, 0, 4)

        main_frame = QWidget()
        self.setCentralWidget(main_frame)
        main_frame.setLayout(top_layout)

        return self

    def init_event(self):
        reward_action = QAction('点击试试', self)
        reward_action.triggered.connect(self.click_event)

        # 工具栏菜单
        menu_list = self.menu_bar.addMenu("菜单项")
        menu_list.addAction(reward_action)

    def click_event(self):
        print("---------")
