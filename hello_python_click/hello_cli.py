import click


from .hello import Hello

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.command(context_settings=CONTEXT_SETTINGS)
@click.option('--debug', '-D', is_flag=True, help='Show debug')
@click.option('--lower', '-L', is_flag=True, help='Show output in lower case')
@click.option('--title', '-T', help='Use a title')
@click.argument('name', required=False, default='World')
def hello(debug, lower, title, name):

    if debug:
        click.echo('Debug:')
        click.echo(' lower:{}'.format(lower))
        click.echo(' title:{}'.format(title))
        click.echo(' name:{}'.format(name))

    h = Hello(name)
    if title:
        h.title = title

    if lower:
        click.echo(h.transform())
    else:
        click.echo(h.hello())


if __name__ == '__main__':
    hello()
