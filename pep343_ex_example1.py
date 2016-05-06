"""
based on pep343's example 1 and ibm tutorial

[1]https://www.python.org/dev/peps/pep-0343/
[2]http://www.ibm.com/developerworks/cn/opensource/os-cn-pythonwith/index.html

"""


from contextlib import contextmanager
import threading

@contextmanager
def locked(lock):
    lock.acquire()
    try:
        print('[Allocate resources]')
        print('Code before yield-statement executes in __enter__')
        yield '*** message:ahahaha*** By contextmanager demo:)'

        print('Code after yield-statement executes in __exit__')
        print('[Free resources]')

    finally:
        lock.release()


if __name__ == '__main__':
    mutex = threading.Lock()
    ## Oops, this line cannot print, what ever, this is not the point right now
    with locked(mutex):
        print('hahahaha, I\'ve entered the locked door! show me the message inside!')

    print('\ntry again!\n')
    ## (with locked(xxx):with-body, no as)
    ## in 'as' statement in with, yield the string to with-body and execute it
    with locked(mutex) as room:
        print('hahahaha, I\'ve entered the locked door! show me the message inside!')
        print('message: %s' % room)

