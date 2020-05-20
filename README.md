# Declaration2FunctionPtr

This is a small python package for automating the creation of interfaces into shared libraries (.dll/.so/dylib). When creating a shared library, you often have declarations in a header file like so:
```
Export void pkg_function_name(int list, const char* of, double parameters);
```
Where `Export` is a marco for cross platform support and the rest is a normal C/C++ declaration. After compiling a shared library, clients (users of) must 'unpack' the functions manually by creating a function pointer, like so: 

```
typedef new_pkg_function_name (*pkg_function_name)(int, const char*, double);
```
This package automates this process. 

## Notes

- This package is in fairly early stages of development. It was created specifically for a single package and tested on that package. Therefore it may need modifications when testing with different input. However, more generally, this code has the potential to be able to work with any package. 

## To Do
- Parsing C++ header files is already done and uses regular expressions to detect different types of signature. It would be fairly straight forward to write support for Python `ctypes` clients.  
