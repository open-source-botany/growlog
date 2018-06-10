import os
import sys

import yaml


class Crop:

    environment = None
    name = None
    qty = None
    start_date = None
    harvest_date = None
    notes = None

    def __init__(self, name='', start_date='2018', harvest_date=None,
                 environment='outdoor', notes='', qty=1):
        self.environment = environment
        self.name = name
        self.notes = notes
        self.qty = qty
        self.start_date = start_date
        self.harvest_date = harvest_date

    def to_dict(self):
        # get any "default" attrs defined at the class level
        class_vars = vars(Crop)
        inst_vars = vars(self)  # get any attrs defined on the instance (self)
        all_vars = dict(class_vars)
        all_vars.update(inst_vars)
        # filter out private attributes
        public_vars = {k: v for k, v in all_vars.items()
                       if not k.startswith('_')}
        del public_vars['to_dict']
        return public_vars


def seed_data():
    plant1 = Crop('Kale',
                  '04-30-2018',
                  qty=3,
                  notes='Grown from seed indoors and then soil.')
    plant2 = Crop('Cilantro',
                  '04-30-2018',
                  environment='indoor',
                  qty=2,
                  notes='Grown from seed indoors and then soil.')
    data = [plant1.to_dict(), plant2.to_dict()]
    return data


def save_growlog(data):
    with open('growlog.yml', 'w') as outfile:
        yaml.dump(data, outfile, default_flow_style=False)


def load_growlog(seed=False):
    file_path = './growlog.yml'
    if not os.path.exists(file_path):
        # data = seed_data()
        data = create_growlog()
        save_growlog(data)
    with open(file_path, 'r') as f:
        grow_dict = yaml.load(f)
    return [Crop(**crop) for crop in grow_dict]


def convert_list_objs(log):
    """ Deserializes Crop objects to dict format """
    return [obj.to_dict() for obj in log]


def print_growlog(log):
    new_log = convert_list_objs(log)
    yaml.dump(new_log, sys.stdout)


def add_to_growlog(crop_data):
    new_crop = Crop(**crop_data)
    log = load_growlog()
    log.append(new_crop)
    log_data = convert_list_objs(log)
    save_growlog(log_data)


def create_growlog():
    return []
