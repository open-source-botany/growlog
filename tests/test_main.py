import sys
import unittest

from growlog.main import Crop
from growlog.main import add_to_growlog
from growlog.main import create_growlog
from growlog.main import delete_crop_from_growlog
from growlog.main import load_growlog
from growlog.main import save_growlog
from growlog.main import update_crop_in_growlog

try:
    from unittest.mock import patch, mock_open
except ImportError:
    from mock import patch, mock_open  # py27


class TestCrop(unittest.TestCase):

    def test_init(self):
        name = 'Kale'
        date = '04-30-2018'
        c = Crop(name, date)
        self.assertEquals(c.name, name)
        self.assertEquals(c.start_date, date)
        self.assertEquals(c.environment, 'outdoor')

    def test_to_dict(self):
        name = 'Cilantro'
        date = '04-30-2018'
        c = Crop(name, date)
        _dict = c.to_dict()
        self.assertEquals(type({}), type(_dict))
        self.assertEquals(_dict['start_date'], date)
        self.assertEquals(_dict['harvest_date'], None)


class TestLoader(unittest.TestCase):
    def setUp(self):
        if sys.version_info.major <= 2:
            self.builtin_name = "__builtin__.open"
        else:
            self.builtin_name = "builtins.open"

    def test_load_growlog(self):
        mocked_content = """
        - environment: indoor
          harvest_date: null
          name: 'Cannabis'
          notes: Good for migraine
          qty: 420
          start_date: 2018
        """
        with patch(self.builtin_name, mock_open(read_data=mocked_content)) as mock_file:
            g = load_growlog()
            self.assertEqual(g[0].environment, 'indoor')
            mock_file.assert_called_with('./growlog.yml', 'r')

    def test_save_growlog(self):
        mock_file = mock_open()
        crop_list = [Crop(name="Cannabis", qty=420, notes="Good for depression")]

        with patch(self.builtin_name, mock_file, create=True):
            save_growlog(crop_list)
        mock_file.assert_called_with('./growlog.yml', 'w')
        # handle = mock_file()
        # handle.write.assert_called_once_with(mocked_data)

    @patch('growlog.main.load_growlog', lambda *x: [])
    @patch('growlog.main.save_growlog')
    def test_add_to_growlog(self, save_mock=None):
        crop_data = dict(name="Cannabis", qty=420, notes="Great for eating disorders")
        add_to_growlog(crop_data)
        save_mock.assert_called_once_with([{
            'environment': 'outdoor',
            'name': 'Cannabis',
            'qty': 420,
            'start_date': '2018',
            'harvest_date': None,
            'notes': 'Great for eating disorders'
        }])

    def test_create_growlog(self):
        self.assertEqual(create_growlog(), [])

    @patch('growlog.main.save_growlog')
    @patch('growlog.main.load_growlog')
    def test_update_crop_in_growlog(self, load_mock=None, save_mock=None):
        load_mock.return_value = [
            Crop(name="Cannabis", qty=420, notes="Good to grow")
        ]
        update_crop_in_growlog(name="Cannabis", key="notes", val="Good to dry")

        save_mock.assert_called_once_with([{
            'environment': 'outdoor',
            'name': 'Cannabis',
            'qty': 420,
            'start_date': '2018',
            'harvest_date': None,
            'notes': 'Good to dry'
        }])
        load_mock.assert_called_once_with = ()

    @patch('growlog.main.save_growlog')
    @patch('growlog.main.load_growlog')
    def test_delete_crop_from_growlog(self, load_mock=None, save_mock=None):
        load_mock.return_value = [
            Crop(name="Cannabis", qty=420, notes="Good to sell and delete")
        ]
        delete_crop_from_growlog(name="Cannabis")

        save_mock.assert_called_once_with([])
        load_mock.assert_called_once_with = ()
