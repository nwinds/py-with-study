python with
============================




attemp 1: pep 343
----------------------------
- with attemp based on pep itself
```
In [2]: run with-rev.py

this Python program is for python-with review based on pep-0343 and... (to-be-add)


normal result 3
try_except_final done!
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
/home/vagrant/documents/pyrev/with-rev.py in <module>()
     26     print(__doc__)
     27     try_except_final(2)
---> 28     with_expr(3)
     29 
     30 

/home/vagrant/documents/pyrev/with-rev.py in with_expr(input_arg)
     18 
     19 def with_expr(input_arg):
---> 20     with input_arg+1 as x:
     21         print('normal result %d' % x)
     22     print('%s done!' % sys._getframe().f_code.co_name)

AttributeError: __exit__

```

- Question: why? not totally understand with statement
    - sol: read pep 343 one more time

```
In [5]: int.__exit__
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-5-585be2589bea> in <module>()
----> 1 int.__exit__

AttributeError: type object 'int' has no attribute '__exit__'
</module>

```


### what about exception IN with?
```
 In [13]: run with-rev.py

 this Python program is for python-with review based on pep-0343 and... (to-be-add)


 normal result 3
 try_except_final done!
 normal result:
 hello world

 with_expr done!
 ---------------------------------------------------------------------------
IOError                                   Traceback (most recent call last)
/home/vagrant/documents/pyrev/with-rev.py in <module>()
32     try_except_final(2)
33     with_expr('FileDoExists')
---> 34     with_expr('FileNotExists')
35 
36 

/home/vagrant/documents/pyrev/with-rev.py in with_expr(input_arg)
18 
19 def with_expr(input_arg):
---> 20     with open(input_arg, 'r') as f:
21         print('normal result:')
22         for line in f.readlines():

IOError: [Errno 2] No such file or directory: 'FileNotExists'
```
### result: what the fuck are you talking about

attemp 2: figure out what is entry/exit
-------------------------------------
- plan: based on C entry function, and C's goto
- maybe, related to system like xv6, exit/enter, long jump on asm level

### c_entry_func.c demo
> [1](http://mosir.org/html/y2012/the-custom-start-address-of-c-program.html)
```
 Start from myentry

 Segmentation fault

```
```
 return 0
```
- that's it

    -(you are missing gdb cmd on your vm)

- add exit
    ```
$ gcc -nostartfiles -e myentry c_entry_func.c -o myentry -g
c_entry_func.c: In function ‘myentry’:
c_entry_func.c:9:5: warning: incompatible implicit declaration of built-in function ‘exit’ [enabled by default]
  exit(0);
       ^


    ```
    - solution: ```#include <stdlib.h>```

    ```
vagrant@ub14:pyrev $ gcc -nostartfiles -e myentry c_entry_func.c -o myentry -g
vagrant@ub14:pyrev $ ls
1  c_entry_func.c  FileDoExists  Makefile  myentry  README.md  with-rev.py
vagrant@ub14:pyrev $ ./myentry
Start from myentry




    ```
- gcc编译指定入口点，配合exit函数使用
- further：system call：entry/exit

- 缺省库：这个先不管了（绕远了）

TODO
further
## system level
- exit
- entry(sth like that?)


attemp 2.5: goto，准确的说，是跳转问题
--------------------------------
### 回去再说
### 函数内跳转：goto
- 一般的使用
- goto label
    > http://blog.csdn.net/fjb2080/article/details/5248359
    - 标签也是有地址的！
### 函数间跳转：setjmp, longjmp


attemp 3: 回到起点
----------------------------------
> http://www.ibm.com/developerworks/cn/opensource/os-cn-pythonwith/index.html
- 似乎绕的远了（或许底层实现确实是C，但是似乎不需要知道这些）

