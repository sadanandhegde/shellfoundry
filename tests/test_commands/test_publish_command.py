import os

from mock import patch
from pyfakefs import fake_filesystem_unittest
from requests import post

from shellfoundry.commands.publish_command import PublishCommandExecutor

LOGIN_ERROR_MESSAGE = 'Login failed for user: YOUR_USERNAME. Please make sure the username and password are correct.'


class TestPublishCommandExecutor(fake_filesystem_unittest.TestCase):
    def setUp(self):
        self.setUpPyfakefs()

    def test_when_config_files_exist_publish_succeeds(self):
        # Arrange
        self.fs.CreateFile('nut_shell/shell.yml', contents="""
shell:
    name: nut_shell
    driver: NutShellDriver
    """)
        self.fs.CreateFile('nut_shell/cloudshell_config.yml', contents="""
install:
    host: localhost
    port: 9000
    username: YOUR_USERNAME
    password: YOUR_PASSWORD
    domain: Global
    """)

        self.fs.CreateFile('nut_shell/dist/nut_shell.zip', contents='ZIP')

        os.chdir('nut_shell')

        with patch('shellfoundry.commands.publish_command.requests.post') as post_mock:

            command_executor = PublishCommandExecutor()

            # Act
            command_executor.publish()

            # Assert
            self.assertTrue(post_mock.called)
            args, kargs = post_mock.call_args
            self.assertEqual(args[0], 'http://shellrepo.apphb.com/api/shell/upload')

