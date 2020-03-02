import unittest
import os
import site

site.addsitedir(os.path.dirname(os.path.dirname(__file__)))
from declaration2funcptr.declaration2functionptr import Declaration


class DefinitionTests1(unittest.TestCase):
    signature = '_GraphfabExport int gf_arrowheadGetStyle(gf_specRole role);'
    expected_exporter_symbol = '_GraphfabExport'
    expected_return_type = 'int'
    expected_method_name = 'gf_arrowheadGetStyle'
    expected_arg_type_list = ['gf_specRole']
    expected_func_ptr = 'typedef int gf_arrowheadGetStyle(gf_specRole);'

    def setUp(self) -> None:
        pass

    def test_get_exporter_symbol(self):
        d = Declaration(self.signature)
        symb = d.get_exporter_symbol()
        self.assertEqual(self.expected_exporter_symbol, symb)

    def test_get_return_type(self):
        d = Declaration(self.signature)
        symb = d.get_return_type()
        self.assertEqual(self.expected_return_type, symb)

    def test_get_method_name(self):
        d = Declaration(self.signature)
        symb = d.get_method_name()
        self.assertEqual(self.expected_method_name, symb)

    def test_get_arg_types(self):
        d = Declaration(self.signature)
        symb = d.get_arg_types()
        self.assertEqual(self.expected_arg_type_list, symb)

    def test_get_arg_types(self):
        d = Declaration(self.signature)
        actual = d.to_func_ptr()
        self.assertEqual(self.expected_func_ptr, actual)


class DefinitionTests2(DefinitionTests1):
    signature = '_GraphfabExport void gf_freeSBMLModel(gf_SBMLModel* lo);'
    expected_exporter_symbol = '_GraphfabExport'
    expected_return_type = 'void'
    expected_method_name = 'gf_freeSBMLModel'
    expected_arg_type_list = ['gf_SBMLModel*']
    expected_func_ptr = 'typedef void gf_freeSBMLModel(gf_SBMLModel*);'


class DefinitionTests3(DefinitionTests1):
    signature = '_GraphfabExport gf_SBMLModel* gf_loadSBMLbuf(const char* buf);'
    expected_exporter_symbol = '_GraphfabExport'
    expected_return_type = 'gf_SBMLModel*'
    expected_method_name = 'gf_loadSBMLbuf'
    expected_arg_type_list = ['const char*']
    expected_func_ptr = 'typedef gf_SBMLModel* gf_loadSBMLbuf(const char*);'


class DefinitionTests4(DefinitionTests1):
    signature = '_GraphfabExport unsigned int gf_canvGetWidth(gf_canvas* c);'
    expected_exporter_symbol = '_GraphfabExport'
    expected_return_type = 'unsigned int'
    expected_method_name = 'gf_canvGetWidth'
    expected_arg_type_list = ['gf_canvas*']
    expected_func_ptr = 'typedef unsigned int gf_canvGetWidth(gf_canvas*);'


class DefinitionTests5(DefinitionTests1):
    signature = '_GraphfabExport const char* gf_getSBMLwithLayoutStr(gf_SBMLModel* m, gf_layoutInfo* l);'
    expected_exporter_symbol = '_GraphfabExport'
    expected_return_type = 'const char*'
    expected_method_name = 'gf_getSBMLwithLayoutStr'
    expected_arg_type_list = ['gf_SBMLModel*', 'gf_layoutInfo*']
    expected_func_ptr = 'typedef const char* gf_getSBMLwithLayoutStr(gf_SBMLModel*,gf_layoutInfo*);'


class DefinitionTests6(DefinitionTests1):
    signature = '_GraphfabExport void gf_moveNetworkToFirstQuad(gf_layoutInfo* l, double x_disp, double y_disp);'
    expected_exporter_symbol = '_GraphfabExport'
    expected_return_type = 'void'
    expected_method_name = 'gf_moveNetworkToFirstQuad'
    expected_arg_type_list = ['gf_layoutInfo*', 'double', 'double']
    expected_func_ptr = 'typedef void gf_moveNetworkToFirstQuad(gf_layoutInfo*,double,double);'


class DefinitionTests7(DefinitionTests1):
    signature = '_GraphfabExport gf_SBMLModel gf_SBMLModel_new();'
    expected_exporter_symbol = '_GraphfabExport'
    expected_return_type = 'gf_SBMLModel'
    expected_method_name = 'gf_SBMLModel_new'
    expected_arg_type_list = ['']
    expected_func_ptr = 'typedef gf_SBMLModel gf_SBMLModel_new();'

class DefinitionTests8(DefinitionTests1):
    signature = '_GraphfabExport const char* gf_getCurrentLibraryVersion(void);'
    expected_exporter_symbol = '_GraphfabExport'
    expected_return_type = 'const char*'
    expected_method_name = 'gf_getCurrentLibraryVersion'
    expected_arg_type_list = ['void']
    expected_func_ptr = 'typedef const char* gf_getCurrentLibraryVersion(void);'


if __name__ == '__main__':
    unittest.main()
