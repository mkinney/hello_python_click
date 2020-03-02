from .utils import lower


class Hello():

    def __init__(self, name=''):
        if name is None:
            name = ''
        self.name = name
        self.title = ''

    def hello(self):
        title = ''
        if self.title:
            title = '{} '.format(self.title)
        return 'Hello {}{}'.format(title, self.name)

    def transform(self):
        """Silly example on how to call function from another file."""
        return lower(self.hello())
