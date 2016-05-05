from contextlib import contextmanager

@contextmanager
def ctxdemo():
    print('[Allocate resources]')
    print('Code before yield-statement executes in __enter__')

    yield('*** contextmanager demo***')

    print('Code after yield-statement executes in __exit__')
    print('[Free resources]')

if __name__ == '__main__':
    with ctxdemo() as value:
        print('Assigned Value: %s' % value)

