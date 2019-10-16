#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'入口类'
from gui.main_window import Sniper as SniperGui
__author__ = 'weixuan.ge'


if __name__ == '__main__':
    sniper = SniperGui()
    sniper.start()