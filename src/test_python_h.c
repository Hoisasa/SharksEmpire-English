#include <Python.h>
int main() {
    Py_Initialize();
    Py_Finalize();
    return 0;
}