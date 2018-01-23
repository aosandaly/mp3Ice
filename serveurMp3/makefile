all: build run

build:
#pip install Ice
#pip install zeroc-ice
	slice2py ../interface/server.ice
run:
	python ./Server.py
clean:
ifeq ($(OS),Windows_NT)
#remove file generate per silce2py
	del app\*.py ; del server_ice.py
else
#remove file generate per silce2py
	rm "./app/*.py" ; rm "server_ice.py"
endif

