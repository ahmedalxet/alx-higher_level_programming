#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p)
{
	if (!PyList_Check(p))
	{
		printf("Error: p is not a list\n");
		return;
	}

	int size = PyList_Size(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (int i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, item->ob_type->tp_name);
	}
}

void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p))
	{
		printf("Error: p is not a bytes object\n");
		return;
	}

	char *data = PyBytes_AsString(p);
	int size = PyBytes_Size(p);
	printf("[.] bytes object info\n");
	printf("  size: %d\n", size);
	printf("  trying string: %s\n", data);
	size = (size > 10) ? 10 : size;
	printf("  first %d bytes: ", size);
	for (int i = 0; i < size; i++)
		printf("%02x ", data[i] & 0xff);
	puts("");
}

void print_python_float(PyObject *p)
{
	if (!PyFloat_Check(p))
	{
		printf("Error: p is not a float object\n");
		return;
	}

	double value = PyFloat_AsDouble(p);
	printf("[.] float object info\n");
	printf("  value: %.16g\n", value);
	unsigned char *data = (unsigned char *)&value;
	printf("  bytes: ");
	for (int i = 0; i < 8; i++)
		printf("%02x ", data[i]);
	puts("");
}
