package org.pyamf;

import org.python.core.PyException;
import org.python.core.PyInteger;
import org.python.core.PyObject;
import org.python.util.PythonInterpreter;

public class HelloWorld
{
    /**
     * @param args the command line arguments
     */
     public static void main(String[] args) throws PyException
     {
        PythonInterpreter interp = new PythonInterpreter();
        interp.exec("import sys");
        interp.exec("print sys.path");
        interp.execfile("test.py");
    }
}
