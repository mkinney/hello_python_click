import subprocess
import re


from click.testing import CliRunner


from .hello_cli import hello


def test_help():
    rc, out = subprocess.getstatusoutput('hello --help')
    assert re.match('Usage', out)
    assert rc == 0


def test_with_name():
    rc, out = subprocess.getstatusoutput('hello Mike')
    assert re.match('Hello Mike', out)
    assert rc == 0


def test_lower():
    rc, out = subprocess.getstatusoutput('hello --lower Bob')
    assert rc == 0
    assert out == 'hello bob'


def test_lower_and_title():
    rc, out = subprocess.getstatusoutput('hello --lower --title Dr. Bob')
    assert rc == 0
    assert out == 'hello dr. bob'


def test_debug_short():
    rc, out = subprocess.getstatusoutput('hello -D')
    assert rc == 0
    assert re.search('Hello World', out, re.MULTILINE)
    assert re.search('Debug', out, re.MULTILINE)


def test_debug_long():
    rc, out = subprocess.getstatusoutput('hello --debug')
    assert rc == 0
    assert re.search('Hello World', out, re.MULTILINE)
    assert re.search('Debug', out, re.MULTILINE)


def test_with_name_using_runner():
    runner = CliRunner()
    result = runner.invoke(hello, ['Mike'])
    assert result.exit_code == 0
    assert result.output == 'Hello Mike\n'
