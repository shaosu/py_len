
C_Flag= -fpic -c 
Py_Flag=-I /usr/include/python3.5m \
		-I /usr/lib/python3.5/config-3.5m-x86_64-linux-gnu


my_fun.o:my_fun.c  my_fun.h
	gcc  $(C_Flag)  $(Py_Flag)   my_fun.c 

output.o:output.c my_fun.h
	gcc $(C_Flag) $(Py_Flag) output.c 

all:my_fun.o  output.o
	gcc -shared -o my_fun.so output.o my_fun.o

clear:
	rm  my_fun.o  output.o    my_fun.so  


