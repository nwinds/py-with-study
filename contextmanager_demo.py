""" base on http://www.ibm.com/developerworks/cn/opensource/os-cn-pythonwith/index.html demo-5
"""
class DummyResource:
    def __init__(self, tag):
        self.tag = tag
        print('Resource [%s]' % tag)

    def __enter__(self):
        print('[Enter %s]: Allocate resource.' % self.tag)
        return self    # can return different object

    def __exit__(self, exc_type, exc_value, exc_tb):
        print('[Exit %s]: Free resource.' % self.tag)
        if exc_tb is None:
            print('[Exit %s]: Exited without exception.' % self.tag)
        else:
            print('[Exit %s]: Exited with exception raised.' % self.tag)
            return False

""" self-implement: what if ctx_expr it self raised an exception """
class DummyResorceChild(DummyResource):
    def __init__(self, tag, trigger = False):
        if trigger:
            raise Exception
        DummyResource.__init__(self, tag)


if __name__ == '__main__':
    with DummyResource('Normal'):
        print('[with-body] Run without exceptions.')

    try:
        with DummyResource('With-Exception'): # NOTICE: ctx_expr it self has an exception will irectly raised!(in this case)
            print('[with-body] Run with exception.')
            raise Exception  ## forcing an exception and the ctx manager will handle it
            print('[with-body] Run with exception. Failed to finish statement-body!') # NOTICE: will not execute this line
    except Exception:
        pass


    with DummyResorceChild('Without ctx_expr exception'):
        print('[with-body] Run without exceptions.')

    with DummyResorceChild('With ctx_expr exception', True):
        print('[with-body] Run passed with exception in ctx_expr!')
