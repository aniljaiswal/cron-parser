import click

from cron_parser.cron_expression import CronExpression
# from cron_parser.parse import parse_cron_to_table


@click.command()
@click.argument('expression')
def cli(expression):
    parser = CronExpression(expression).parse()
    output = parser.format_as_table()
    click.echo(output)


if __name__ == '__main__':
    cli()
