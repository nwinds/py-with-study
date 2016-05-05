""" base on http://www.ibm.com/developerworks/cn/opensource/os-cn-pythonwith/index.html
contextlib:closing demo
"""
class closing(object):
    def __init__(self, thing):
        self.thing = thing

    def __enter__(self):
        return self.thing

    def __exit__(self, *exc_info):
        self.thing.close()

class ClosingDemo(object):
    """ class supporting closing
    Question: NO contextlib neither contextmanager? """
    def __init__(self):
        self.acquire()

    def acquire(self):
        print('Acquire resources.')

    def free(self):
        print('Clean up any resources acquired.')

    def close(self):
        self.free()


if __name__ == '__main__':
    with closing(ClosingDemo()):
        print('Using resources')
