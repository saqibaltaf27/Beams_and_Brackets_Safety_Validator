# main.py

# Entry point for the CLI tool.

import click
from validator import validate_safety_checks


@click.command()
@click.argument("json_file")
def cli(json_file):
    """CLI Tool to validate Beams & Brackets safety checklists."""
    result = validate_safety_checks(json_file)
    click.echo(result)


if __name__ == "__main__":
    cli()