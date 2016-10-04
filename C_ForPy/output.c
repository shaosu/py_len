#include <Python.h>
#include "my_fun.h"
#include <stdio.h>

PyObject* api_fact(PyObject* self,PyObject* args)
{
	unsigned long long n=0;
	unsigned long long result=0;
	if ( !PyArg_ParseTuple(args,"K:fact",&n))
		return NULL;
	result = fact(n);
	return  Py_BuildValue("L",result);
}

static PyMethodDef my_funMethods[]=
{
	{"fact",//python fun  中使用的名字
	api_fact,// C  fun name
	METH_VARARGS,
	"caculate n!"},
	{NULL,NULL,0,NULL}
};

// The method table must be referenced in the module definition structure.
static struct PyModuleDef my_funmodule ={
	PyModuleDef_HEAD_INIT,
	"my_fun",// name of module
	NULL,
	-1,
	my_funMethods
};

PyMODINIT_FUNC  PyInit_my_fun(void)
{
	PyObject* m;
	m=PyModule_Create(&my_funmodule);
	if (m== NULL)
		return NULL;
	printf("my_fun is OK! _ setup.py \n");
	return m;
}
