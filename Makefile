PYLIB = /usr/bin
PYINC = /usr/include/python2.6
CLIB = .

_fasttoad_wrap.so: fasttoad_wrap.o $(CLIB)/fasttoad.o
	gcc -shared -fPIC fasttoad_wrap.o $(CLIB)/fasttoad.o -L$(PYLIB) -lpython2.6 -o $@
	

fasttoad_wrap.o:fasttoad_wrap.c $(CLIB)/fasttoad.h
	gcc fasttoad_wrap.c -g -fPIC -I$(CLIB) -I$(PYINC) -c -o $@
	
fasttoad_wrap.c: fasttoad.i
	swig -python -I$(CLIB) fasttoad.i
	
$(CLIB)/fasttoad.o: $(CLIB)/fasttoad.c $(CLIB)/fasttoad.h
	gcc $(CLIB)/fasttoad.c -g -fPIC -I$(CLIB) -c -o $(CLIB)/fasttoad.o
	
clean:
	rm -f *.so *.o *.pyc core
	
force:
	rm -f *.so *.o *.pyc core fasttoad_wrap.c fasttoad.py