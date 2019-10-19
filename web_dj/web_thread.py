#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import threading
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class webThread(threading.Thread):
    def __init__(self, threadId, name):
        threading.Thread.__init__(self)
        self.threadID = threadId
        self.name = name

    def run(self):
        print("开始django线程：" + self.name)
        self.start_django()
        print("退出django线程：" + self.name)

    def start_django(self):
        print("===========start_django工作目录============", BASE_DIR)
        os.chdir(BASE_DIR + "\\web_dj")
        os.system("E:\\tools\\python_64bit\\python manage.py runserver 0.0.0.0:8000")


def django_service_start():
    # 创建新线程
    django_thread = webThread(1, "django_thread")

    # 开启新线程
    django_thread.start()
    print("退出主线程")

# if __name__ == "__main__":
#     django_service_start()