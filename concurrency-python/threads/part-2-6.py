"""Барьеры (threading.Barrier)

Последний инструмент для синхронизации работы потоков,
который мы рассмотрим является Barrier.
Он позволяет реализовать алгоритм, когда необходимо
дождаться завершения работы группы потоков,
прежде чем продолжить выполнение задачи.

Параметры:

parties
Количество потоков, которые будут работать в рамках барьера.
action
Определяет функцию, которая будет вызвана, когда потоки будут освобождены (достигнут барьера).
timeout
Таймаут, который будет использовать как значение по умолчанию для методов wait().

Свойства и методы класса:

wait(timeout=None)
Блокирует работу потока до тех пор, пока не будет получено уведомление либо не пройдет время указанное в timeout.
reset()
Переводит Barrier в исходное (пустое) состояние. Потокам, ожидающим уведомления, будет передано исключение BrokenBarrierError.
abort()
Останавливает работу барьера, переводит его в состояние “разрушен” (broken). Все текущие и последующие вызовы метода wait() будут завершены с ошибкой с выбросом исключения BrokenBarrierError.
parties
Количество потоков, которое нужно для достижения барьера.
n_waiting
Количество потоков, которое ожидает срабатывания барьера.
broken
Значение флага равное True указывает на то, что барьер находится в “разрушенном” состоянии.
"""
from threading import Barrier, Thread
from time import sleep, time

br = Barrier(3)
store = []


def f1(x):
    print("Calc part1")
    store.append(x ** 2)
    sleep(0.5)
    br.wait()


def f2(x):
    print("Calc part2")
    store.append(x * 2)
    sleep(1)
    br.wait()


Thread(target=f1, args=(3,)).start()
Thread(target=f2, args=(7,)).start()

br.wait()

print("Result: ", sum(store))