from proj_python_core import py_unit_test


def test_add():
    assert py_unit_test.add(5, 4) == 9
    assert py_unit_test.add(15) == 22
