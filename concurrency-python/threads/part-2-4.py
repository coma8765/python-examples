"""События (threading.Event)

Методы класса Event:

is_set()
Возвращает True если флаг находится в взведенном состоянии.
set()
Переводит флаг в взведенное состояние.
clear()
Переводит флаг в сброшенное состояние.
wait(timeout=None)
Блокирует вызвавший данный метод поток если флаг соответствующего Event-объекта находится в сброшенном состоянии. Время нахождения в состоянии блокировки можно задать через параметр timeout.

"""
from threading import Thread, Event
from time import sleep, time

event = Event()


def worker(name: str):
    event.wait()
    print(f"Worker: {name}")


# Clear event
event.clear()

# Create and start workers
workers = [Thread(target=worker, args=(f"wrk {i}",)) for i in range(5)]
for w in workers:
    w.start()

print("Main thread")

event.set()
