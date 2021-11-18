#include <stdio.h>

void stringcmp(char str1[20], char str2[20]){
    for(int i = 0; i < 20; i++){
        str2[i] = str1[i];
    }
}

int main()
{
    char string1[20] = "cadena1abbb\0";
    char string2[20];
    
    stringcmp(string1, string2);

    printf("String2 be like: %s\n", string2);
    
    return 0;
}
