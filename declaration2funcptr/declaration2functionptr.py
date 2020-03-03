import os
import re


class Declaration:

    def __init__(self, definition, suffix='Ptr'):
        self._decl = definition
        self.suffix = suffix
        self.exporter_symbol = self.get_exporter_symbol()
        self.return_type = self.get_return_type()
        self.method_name = self.get_method_name()
        self.arg_types, self.arg_names = self.get_args()

    def get_exporter_symbol(self):
        match = re.findall(r'^\S*', self._decl)
        assert len(match) == 1
        return match[0]

    def get_return_type(self):
        match = re.findall(r'^\S*\s*(unsigned \S*)|^\S*\s*(const \S*)|^\S*\s*(\S*)', self._decl)
        assert len(match) == 1
        match = [i for i in match[0] if i != '']
        assert len(match) == 1
        return match[0]

    def get_method_name(self):
        match = re.findall(r'(?:^\S*\s*unsigned \S*|^\S*\s*const \S*|^\S*\s*)\S*\s*(\S*)(?=\()', self._decl)
        assert len(match) == 1
        return match[0]

    def get_args(self):
        match = re.findall(r'(?:^\S*\s*unsigned \S*|^\S*\s*const \S*|^\S*\s*)\S*\s*\S*(?=\()\((.*)\);', self._decl)
        assert len(match) == 1
        # for when we have 0 arguments
        if match[0] in ['', 'void']:
            return match,[None]
        matches = match[0].split(',')
        matches = [i.strip() for i in matches]
        types = []
        names = []
        for i in matches:
            # remove the variable name from the string
            names.append(i.split(' ')[-1])
            i = i.rsplit(' ')[:-1]
            i = ' '.join(i)
            match = re.findall(r'(const\s*\S*)|(unsigned\s*\S*)|(\S*)\s*\S*', i)
            match = [i for i in match if i != ('', '', '')]
            assert len(match) == 1
            types.append([i for i in match[0] if i != ''][0])
        return types, names

    def to_func_ptr(self):
        method_args = ','.join(self.arg_types)
        return f'typedef {self.return_type} (*{self.method_name + self.suffix})({method_args});'

    def to_getFunctionSyntax(self):
        """
        The get function c++ templated function looks like :

            .. code-block:: CPP

                template<class T>
                T getFunction(const CHAR *funcName) {
            #if defined(_WIN32)
                    T func = (T) GetProcAddress(handle, reinterpret_cast<LPCSTR>(funcName));
                    if (func == nullptr) {
                        GetLastError();
                        throw std::invalid_argument("dead");
                    }
                    return func;
                }
            #elif defined(__linux__)

            #elif defined(__APPLE__)

            #endif
            Returns:

        """
        return f'auto function = getFunction<{self.method_name + self.suffix}>("{self.method_name}");'

    def to_method_format(self):
        """
            const char* gf_getCurrentLibraryVersion() {
                auto function = getFunction<gf_getCurrentLibraryVersionPtr>("gf_getCurrentLibraryVersion");
                return function();
            }
        Returns:

        """
        args = ''
        for type, name in zip(self.arg_types, self.arg_names):
            args += f'{type} {name}, '
        args2 = ''
        for name in self.arg_names:
            args2 += f'{name}, '
        args = args.strip()
        args2 = args2.strip()
        return f'{self.return_type} {self.method_name}({"" if args[:-1] in ["None", "void"] else args[:-1]}) {{\n' \
               f'    {self.to_getFunctionSyntax()}\n' \
               f'    return function({"" if args2[:-1]  in ["None", "void"] else args2[:-1]});\n' \
               f'}}\n\n'

    def __str__(self):
        return f'Declaration({self._decl})'

    def __repr__(self):
        return self.__str__()

    def buld_arg_list(self):
        pass
