import os
import re




class Declaration:

    def __init__(self, definition):
        self._decl = definition
        self.exporter_symbol = self.get_exporter_symbol()
        self.return_type = self.get_return_type()
        self.method_name = self.get_method_name()
        self.arg_types = self.get_arg_types()

    def get_exporter_symbol(self):
        match = re.findall('^\S*', self._decl)
        assert len(match) == 1
        return match[0]

    def get_return_type(self):
        match = re.findall('^\S*\s*(unsigned \S*)|^\S*\s*(const \S*)|^\S*\s*(\S*)', self._decl)
        assert len(match) == 1
        match = [i for i in match[0] if i != '']
        assert len(match) == 1
        return match[0]

    def get_method_name(self):
        match = re.findall('(?:^\S*\s*unsigned \S*|^\S*\s*const \S*|^\S*\s*)\S*\s*(\S*)(?=\()', self._decl)
        assert len(match) == 1
        return match[0]

    def get_arg_types(self):
        match = re.findall('(?:^\S*\s*unsigned \S*|^\S*\s*const \S*|^\S*\s*)\S*\s*\S*(?=\()\((.*)\);', self._decl)
        assert len(match) == 1
        # for when we have 0 arguments
        if match[0] == '':
            return match
        matches = match[0].split(',')
        matches = [i.strip() for i in matches]
        types = []
        for i in matches:
            # remove the variable name from the string
            i = i.rsplit(' ')[:-1]
            i = ' '.join(i)
            match = re.findall('(const\s*\S*)|(unsigned\s*\S*)|(\S*)\s*\S*', i)
            match = [i for i in match if i != ('','','')]
            assert len(match) == 1
            types.append([i for i in match[0] if i != ''][0])
        return types

    def to_func_ptr(self):
        method_args = ','.join(self.arg_types)
        return f'typedef {self.return_type} {self.method_name}({method_args});'

    def __str__(self):
        return f'Declaration({self._decl})'

    def __repr__(self):
        return self.__str__()
