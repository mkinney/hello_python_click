import subprocess
import re

import pytest


def test_help():
    rc, out = subprocess.getstatusoutput('hello --help')
    assert re.match('Usage', out)
    assert rc == 0
