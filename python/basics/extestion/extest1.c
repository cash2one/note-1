#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUFSIZ 512


int add(int i, int j)
{
    return i+j;
}

int fac(int n)
{
    if (n < 2)
        return 1;
    return n * fac(n - 1);
}

int sum(int arr[], int arr_len)
{
    int s = 0, i = 0;
    for (i = 0; i < arr_len; i++)
    {
        s += arr[i];
    }
    return s;
}

char *reverse(char *s)
{
    register char t,//中间变量
            *p = s,
            *q = (s + (strlen(s) - 1));
    while (p < q)
    {
        t = *p;
        *p++ = *q;
        *q-- = t;
    }
    return s;
}

int main()
{
    char s[BUFSIZ];
    printf("4! == %d\n", fac(4));
    printf("8! == %d\n", fac(8));
    printf("12! == %d\n", fac(12));
    strcpy(s, "abcdef");
    printf("reversing 'abcdef', we get '%s'\n", reverse(s));
    strcpy(s, "madam");
    printf("reversing 'madam', we get '%s'\n", reverse(s));
    int array[5] = {1,2,3,4,5};
    printf("%d\n", sum(array, 5));
    return 0;
}