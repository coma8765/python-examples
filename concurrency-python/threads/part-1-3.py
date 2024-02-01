class CustomThread(Thread):
    def __init__(self, limit):
        Thread.__init__(self)
        self._limit = limit
    def run(self):
        for i in range(self._limit):
            print(f"from CustomThread: {i}")
            sleep(0.5)
cth = CustomThread(3)
cth.start()
