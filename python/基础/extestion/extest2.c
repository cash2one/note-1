#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "C:\Python27\include\Python.h"

#define BUFSIZE 512


double add(int i, int j)
{
    return i+j;
}

int fac(int n)
{
    if (n < 2)
        return 1;
    return n * fac(n - 1);
}

double sum(double arr[], int arr_len)
{
    double result = 0;
    int i = 0;
    for (i = 0; i < arr_len; i++)
    {
        result += arr[i];
    }
    return result;
}

char *reverse(char *s)
{
    register char t,
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

int test()
{
    char s[BUFSIZE];
    printf("4! == %d\n", fac(4));
    printf("8! == %d\n", fac(8));
    printf("12! == %d\n", fac(12));
    strcpy(s, "abcdef");
    printf("reversing 'abcdef', we get '%s'\n", reverse(s));
    strcpy(s, "madam");
    printf("reversing 'madam', we get '%s'\n", reverse(s));
    double array[5] = {1.0, 2.0, 3.0, 4.0, 5.0};
    printf("%lf\n", sum(array, 5));
    return 0;
}


static PyObject *Extest_add(PyObject *self, PyObject *args)
{
    double res;
    int i, j;
    PyObject* retval;

    res = PyArg_ParseTuple(args, "ii", &i, &j);
    if (!res)
        return NULL;
    res = add(i, j);
    retval = (PyObject *)Py_BuildValue("d", res);
    return retval;
}

static PyObject *Extest_fac(PyObject *self, PyObject *args)
{
    int res;
    int num;
    PyObject* retval;//返回值python对象--PyObject*

    //PyArg_ParseTuple将Python传过来的参数转成C类型,
    //返回1表示解析成功，为0表示失败
    res = PyArg_ParseTuple(args, "i", &num);
    if (!res)
        return NULL;
    res = fac(num);

    //"Py_BuildValue"将C类型转换成Python对象
    retval = (PyObject *)Py_BuildValue("i", res);
    return retval;
}

static PyObject *Extest_sum(PyObject *self, PyObject *args)
{
    PyObject *seq;
    double *arr, result = 0;
    int seqlen, i;

    if (!PyArg_ParseTuple(args, "Oi", &seq, &seqlen))
        return NULL;

    //解析序列类型参数, 函数第二个参数为错误信息
    seq = PySequence_Fast(seq, "argument must be iterable");
    if (!seq)
        return 0;

    //准备数组数据
    seqlen = PySequence_Fast_GET_SIZE(seq);
    arr = malloc(seqlen*sizeof(double));//申请内存
    if (!arr)
    {
        Py_DECREF(seq);//减引用计数
        return PyErr_NoMemory();
    }

    for (i = 0; i < seqlen; i++)
    {
        PyObject *fitem;
        PyObject *item = PySequence_Fast_GET_ITEM(seq, i);
        if (!item)
        {
            Py_DECREF(seq);
            free(arr);
            return 0;
        }

        fitem = PyNumber_Float(item);
        if (!fitem)
        {
            Py_DECREF(seq);
            free(arr);
            PyErr_SetString(PyExc_TypeError, "all items must be numbers");
            return 0;
        }
        arr[i] = PyFloat_AS_DOUBLE(fitem);
        Py_DECREF(fitem);
    }

    //清理,计算,返回结果
    Py_DECREF(seq);
    result = sum(arr, seqlen);
    free(arr);
    return (PyObject *)Py_BuildValue("d", result);
}

static PyObject *Extest_reverse(PyObject *self, PyObject *args)
{
    char *orignal;
    if (!(PyArg_ParseTuple(args, "s", &orignal)))
    {
        return NULL;
    }
    return (PyObject *)Py_BuildValue("s", reverse(orignal));
}

static PyObject *Extest_doppel(PyObject *self, PyObject *args)
{
    char *orig_str;
    char *dupe_str;
    PyObject *retval;
    if (!(PyArg_ParseTuple(args, "s", &orig_str)))
    {
        return NULL;
    }
    retval = (PyObject *)Py_BuildValue("ss", orig_str, \
        dupe_str = reverse(strdup(orig_str)));
    free(dupe_str);
    return retval;
}

static PyObject * Extest_test(PyObject *self, PyObject *args)
{
    test();
    return (PyObject *)Py_BuildValue("");//返回个None
}

//函数信息列表
static PyMethodDef
ExtestMethods[] = {
    {"add", Extest_add, METH_VARARGS},
    {"fac", Extest_fac, METH_VARARGS},
    {"sum", Extest_sum, METH_VARARGS},
    {"doppel", Extest_doppel, METH_VARARGS},
    {"reverse", Extest_reverse, METH_VARARGS},
    {"test", Extest_test, METH_VARARGS},
    {NULL, NULL},//表示结束
};

//模块初始化函数
void initExtest()
{
    Py_InitModule("Extest", ExtestMethods);
}