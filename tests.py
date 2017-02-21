import unittest
from nose.tools import *

import logging


def setup_func():
    pass

def teardown_func():
    pass


@with_setup(setup_func, teardown_func)
def test_working():
    assert_equal("hello kitty", "hello kitty")

