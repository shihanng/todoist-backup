import json

import click
from todoist_api_python.api import TodoistAPI


@click.command()
@click.option("--token")
def main(token):
    api = TodoistAPI(token)
    try:
        tasks = api.get_tasks()
        click.echo(json.dumps([task.to_dict() for task in tasks]))
    except Exception as error:
        raise click.ClickException(error)


if __name__ == "__main__":
    main()
