#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#include "aes256.h"

char test_key[64] = "aafeeba6959ebeeb96519d5dcf0bcc069f81e4bb56c246d04872db92666e6d4b";


// refazer ta muito ruim
unsigned char *AES_split_key(char key[64]) {
    unsigned char *AEX_key = malloc( sizeof(unsigned char) * 16);

    for (int i = 0; i < 16; i++) {
        char hex_1, hex_2;
        sscanf(&key[i * 4], "%2hhx", &hex_1);
        sscanf(&key[i * 4 + 2], "%2hhx", &hex_2);
        AEX_key[i] = (hex_1 << 4) | hex_2;

    }

    return AEX_key;  
}


int main(void) {
    
    AES_split_key(test_key);

    return 0;
}