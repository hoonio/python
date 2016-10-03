#
#  Simple Makefile
#  For compiling C extension modules for 
#  python.
#

###################################################
#
# Basic Swig Procedure :~)
# 
# // First make the wrapper from the interface file
# swig -python utility.i
# // Then compile both the utility_wrap.c and the utility.c code.
# gcc -c utility.c utility_wrap.c -I/usr/include/python2.2
# // Then link :~)
# ld -shared utility.o utility_wrap.o -o _utility.so
#
##################################################

includes = -I/usr/include/python2.4 -I/usr/lib/python2.4
interface = *.i
source = *.c
objects = *.o
library = _example.so
junk = *.so *.o *_wrap.c *_wrap.doc
linkopts = -shared -o
ccopts = -c


${library} : ${objects} #pointer
	ld ${linkopts} ${library} ${objects}

${objects} : interface ${source} 
	gcc ${ccopts} ${source} ${includes}

interface : ${interface}
	swig -python ${interface}

clean :
	-rm ${junk}

