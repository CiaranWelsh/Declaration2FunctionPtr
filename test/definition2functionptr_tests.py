import unittest
import os
import site
site.addsitedir(os.path.dirname(os.path.dirname(__file__)))
from definition2funcptr.declaration2functionptr import Declaration

class DefinitionTests1(unittest.TestCase):

    signature = '_GraphfabExport int gf_arrowheadGetStyle(gf_specRole role);'
    expected_exporter_symbol = '_GraphfabExport'
    expected_return_type = 'int'
    expected_method_name = 'gf_arrowheadGetStyle'
    expected_arg_type_list = ['gf_specRole']

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

class DefinitionTests2(DefinitionTests1):

    signature = '_GraphfabExport void gf_freeSBMLModel(gf_SBMLModel* lo);'
    expected_exporter_symbol = '_GraphfabExport'
    expected_return_type = 'void'
    expected_method_name = 'gf_freeSBMLModel'
    expected_arg_type_list = ['gf_SBMLModel*']


class DefinitionTests3(DefinitionTests1):

    signature = '_GraphfabExport gf_SBMLModel* gf_loadSBMLbuf(const char* buf);'
    expected_exporter_symbol = '_GraphfabExport'
    expected_return_type = 'gf_SBMLModel*'
    expected_method_name = 'gf_loadSBMLbuf'
    expected_arg_type_list = ['const char*']


class DefinitionTests4(DefinitionTests1):

    signature = '_GraphfabExport unsigned int gf_canvGetWidth(gf_canvas* c);'
    expected_exporter_symbol = '_GraphfabExport'
    expected_return_type = 'unsigned int'
    expected_method_name = 'gf_canvGetWidth'
    expected_arg_type_list = ['gf_canvas*']




if __name__ == '__main__':
    pass
