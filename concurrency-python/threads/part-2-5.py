"""Таймеры (threading.Timer)

Модуль threading предоставляет удобный инструмент для запуска задач по таймеру
– класс Timer. При создании таймера указывается функция,
которая будет выполнена, когда он сработает.
Timer реализован как поток, является наследником от Thread,
поэтому для его запуска необходимо вызвать start(),
если необходимо остановить работу таймера, то вызовите cancel().
"""
from threading import Timer

timer = Timer(interval=3, function=lambda: print("Message from Timer!"))
timer.start()
