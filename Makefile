# Author : Abimelec Reyes Castañeda, Erika Peña, Luis Bocanegra

# Compiler nvcc
LINK = nvcc

# Nombre del ejecutable binario
OUT_FILE = sobelFilter

# Comando 
COMANDO = -Wno-deprecated-gpu-targets -O2 -Xcompiler -fopenmp -std=c++11
OPENCV = `pkg-config opencv --cflags --libs`

all: sobelFilter

sobelFilter: sobelFilter.cu
	$(LINK) -o $(OUT_FILE) $(COMANDO) $(OPENCV) $^

clean: 
	rm -f *.o *~ core
