CC = gcc 
CFLAGS = -Wall -std=c99 -g -O2

TARGET = aes256

OBJECT = aes256.o

$(TARGET) : $(OBJECT) main.c 
	$(CC) $(CFLAGS) -o $(TARGET) $(OBJECT) main.c

%.o : %.c %.h
	$(CC) $(CFLAGS) -c $<