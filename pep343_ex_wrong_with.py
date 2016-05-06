""" based on **Context Managers in the Standard Library** chapter
'  I think we should be careful with this; it could lead to mistakes
like:

    f = open(filename)
    with f:
        BLOCK1
    with f:
        BLOCK2
which does not do what one might think (f is closed before BLOCK2
is entered).
'
"""


import sys
def correct_fopen():
    print(sys._getframe().f_code.co_name)
    with open('test', 'r') as f:
        for line in f.readlines():
            print(line)
    assert f.closed == True

def wrong_fopen():
    print(sys._getframe().f_code.co_name)
    f = open('test', 'r')
    with f:
        f.seek(0)
        for line in f.readlines():
            print(line)
    # file is supposed to be closed after the 1st with exit.
    # so the following should  throw exception
    try: ## hehe
        with f:
            f.seek(0)
            for line in f.readlines():
                print(line)
    except Exception, e:
        # should be portable
        print('%r' % e)




if __name__ == '__main__':
    correct_fopen()
    wrong_fopen()
    """
    result: in wrong_fopen(), line 40 print('%r' % e):
        ValueError('I/O operation on closed file',)
     """

