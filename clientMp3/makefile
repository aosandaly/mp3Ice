ifeq ($(OS),Windows_NT)
# CMD / Environnement Windows
PATH_DELIMITER=;
else
# Environnement Linux
PATH_DELIMITER=:
endif

# Ice
ICE_LIBS=../lib/ice-3.7.0.jar

# Ensemble de libs
LIBS=$(ICE_LIBS)


all: build run

build:
	slice2java ../interface/server.ice
	javac -d classes -classpath "$(LIBS)" Client.java enumFilter.java enumMenu.java app/*.java
run:
	java -classpath "$(LIBS)$(PATH_DELIMITER)classes" Client
clean:
ifeq ($(OS),Windows_NT)
#	 remove file generate per javac - compilation
	cd classes && del *.class && del app\*.class && cd ..
	cd app && del *.java && cd ..
else
#	 remove file generate per javac - compilation
	cd classes; rm -r *.class;rm -r app/*.class; cd ..
#	 remove file generate per silce2java
	cd app; rm -r *.java; cd ..
endif



