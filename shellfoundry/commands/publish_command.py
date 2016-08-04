import os

import click
from requests import post

from shellfoundry.utilities.shell_config_reader import ShellConfigReader

URL = 'http://shellrepo.apphb.com/api/shell/upload'


class PublishCommandExecutor:
    def __init__(self, shell_config_reader = None):
        self.shell_config_reader = shell_config_reader or ShellConfigReader()

    def publish(self):
        shell_config = self.shell_config_reader.read()
        shell_filename = shell_config.name + '.zip'
        package_full_path = os.path.join(os.getcwd(), 'dist', shell_filename)

        click.echo('Publishing shell {0} to {1} '.format(package_full_path, URL))

        response = post(URL, files={shell_filename: open(package_full_path, 'rb')})

        if response.status_code == 200:
            click.echo('Shell was successfully published')
        else:
            click.echo('Shell publishing failed: ' + response.text)
