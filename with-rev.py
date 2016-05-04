"""
this Python program is for python-with review based on pep-0343 and... (to-be-add)

"""
import sys
def try_except_final(input_arg):
    try:
        # add input to an int
        x = 1
        x += input_arg
        print('normal result %d' % x)
    except Exception, eAny:
        print(str(eAny))
    finally:
        #  return result
        print('%s done!' % sys._getframe().f_code.co_name)


def with_expr(input_arg):
    with open(input_arg, 'r') as f:
        print('normal result:')
        for line in f.readlines():
            print(line)
        f.close()
    #  except Exception, eAny:
        #  print(str(eAny))
    print('%s done!' % sys._getframe().f_code.co_name)


if __name__ == '__main__':
    print(__doc__)
    try_except_final(2)
    with_expr('FileDoExists')
    with_expr('FileNotExists')




