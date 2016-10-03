#include "lsystem.h"
#include <Python.h>

LSystem::LSystem(const string& start_string)
  : start(start_string), cur_string(start_string)
{
}

void LSystem::reset() {
  cur_string = start;
}

string LSystem::iterate(int iterations) {
  string next_string;
  
  PyObject *pModule, *pFunc, *pValue;							// python extension parts
  Py_Initialize();  
  pModule = PyImport_ImportModule("LSYSTEM_FILE");
  pFunc = PyObject_GetAttrString(pModule, "generate");
  pValue = PyObject_CallObject(pFunc, NULL);
  cur_string = PyString_AsString(pValue);
  return cur_string;
  Py_Finalize();

}
