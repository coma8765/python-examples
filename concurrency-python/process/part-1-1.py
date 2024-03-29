"""Процессы в Python

Процессы в Python позволяют запустить выполнение нескольких задач
в параллельном режиме. По сути, при старте процесса запускает
еще одна копия интерпретатора Python,
в котором выполняется указанная функция. Таким образом,
если мы запустим пять процессов, то будет запущено пять отдельных
интерпретаторов, в этом случае уже не будет проблем с GIL.
Такой способ позволяет параллельно запускать задачи активно
использующие CPU. Они будут распределяться между несколькими процессами (ядрами),
что значительно увеличит производительность вычислений.

Класс Process
Классом, который отвечает за создание и
управление процессами является Process из пакета multiprocessing.
Он совместим по сигнатурам методов и конструктора с threading. Thread,
это сделано для более простого перехода от многопотокового
приложения к многопроцессному.
Помимо одноименных с Thread методов, класс Process дополнительно предоставляет ряд своих.
Познакомимся поближе с этим классом, конструктор класса выглядит следующим образом:

Параметры конструктора:

group
Параметр всегда равен None, используется для обратной совместимости с Thread.
target
Сallable-объект, который будет вызван методом run() при старте процесса.
name
Имя процесса.
args
kwargs
Параметры объекта, переданного через target.
daemon
Флаг, определяющий является ли данный процесс демоном (True) или нет (False).
Если значение не задано, то оно будет равно свойству daemon родительского процесса.

Помимо методов и свойств, которые совпадают по назначению с аналогичными для класса Thread, класс Process имеет ряд уникальных:

pid
Возвращает ID процесса. Если процесс ещё не запущен, то вернет None.
exitcode
Код возврата. Если процесс ещё не завершил свою работу, то вернет None.
authkey
Ключ аутентификации процесса. При инициализации multiprocessing, с главным процессом связывается специальная строка, которая генерируется с помощью  os.urandom(). Это значение наследуют процессы-потомки, но его можно изменить, задав новое значение, через данное свойство.
sentinel
Числовой идентификатор, который может использоваться для синхронизации. Подробно об этом будет написано в одном из следующих уроков.
close()
Освобождает все ресурсы, связанные с процессом. Если процесс еще работает, то вызов метода приведет к выбросу исключения ValueError.
"""
from multiprocessing import Process


def func():
    print("Hello from child Process")


if __name__ == "__main__":
    proc = Process(target=func)
    print("Hello from main Process")
    proc.start()

    # print("Hello from main Process")
    # proc = Process(target=func)
    # proc.start()
    # proc.join()
    # print("Goodbye")

    # print("Hello from main Process")
    # proc = Process(target=func)
    # proc.start()
    # print(f"Proc is_alive status: {proc.is_alive()}")
    # proc.join()
    # print("Goodbye")
    # print(f"Proc is_alive status: {proc.is_alive()}")
