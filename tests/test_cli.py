import unittest

from click.testing import CliRunner

from growlog.cli import main
from growlog.main import Crop

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch  # py27


class TestCli(unittest.TestCase):
    @patch('growlog.cli.load_growlog', lambda: [
        Crop(name="Catatonic Tegridy Bud", qty=420, start_date="9-11-2001")
    ])
    @patch('growlog.cli.add_to_growlog')
    def test_new_crop(self, add_mock):
        expected = {
            'name': 'Purple Skunky Kush',
            'environment': 'indoor',
            'start_date': '9-11-2001',
            'qty': 420,
            'notes': 'Good shit'
        }
        runner = CliRunner()

        result = runner.invoke(main, ['--add'], input='\n'.join(
            ['Purple Skunky Kush', 'indoor', '9-11-2001', '420', 'Good shit']))
        self.assertEqual(result.exit_code, 0)
        assert not result.exception
        add_mock.assert_called_with(expected)

    @patch('growlog.cli.load_growlog', lambda: [
        Crop(name="Green Willy Stranger", qty=420, start_date="9-11-2001")
    ])
    @patch('growlog.cli.update_crop_in_growlog')
    def test_update_crop(self, update_mock):
        runner = CliRunner()
        result = runner.invoke(main, ['--update'],
                               input='\n'.join(['Green Willy Stranger', 'notes', 'Really good shit']))
        self.assertEqual(result.exit_code, 0)
        assert not result.exception
        update_mock.assert_called_with('Green Willy Stranger', 'notes', 'Really good shit')

    @patch('growlog.cli.load_growlog', lambda: [
        Crop(name="Tegridy Jungle Bud", qty=420, start_date="9-11-2001",
             notes="I don't know what tegridy is, but that is some good shit!")
    ])
    @patch('growlog.cli.delete_crop_from_growlog')
    def test_delete_crop(self, delete_mock):
        runner = CliRunner()
        result = runner.invoke(main, ['--remove'], input='\n'.join(['Tegridy Jungle Bud']))
        self.assertEqual(result.exit_code, 0)
        assert not result.exception
        delete_mock.assert_called_with('Tegridy Jungle Bud')
