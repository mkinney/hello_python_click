from setuptools import setup

setup(
    name='hello_python_click',
    version='0.1',
    py_modules=['hello_python_click'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        hello=hello_python_click.hello:hello
    ''',
)
