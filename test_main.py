import unittest

from main import Crop, load_growlog, save_growlog


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
    
    def test_load_growlog(self):
        g = load_growlog()
        self.assertEquals(type([]), type(g))
        self.assertEquals(type(Crop), g[0])

