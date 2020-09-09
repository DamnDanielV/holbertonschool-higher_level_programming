#include <stdio.h>
#include <Python.h>
/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: list
 *
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	PyObject *element = NULL;
	PyListObject *list = (PyListObject *) p;
	long int i = 0;

	printf("[*] Size of the Python List = %ld\n", Py_SIZE(p));
	printf("[*] Allocated = %ld\n", list->allocated);
	while (i < Py_SIZE(p))
	{
		element = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);
		i++;
	}
}
