import yaml


class Plant:

    environment = None
    name = None
    qty = None
    start_date = None
    harvest_date = None
    notes = None

    def __init__(self, name, start_date, harvest_date=None, 
            environment='indoor', notes='',qty=1):
        self.environment = environment
        self.name = name
        self.notes = notes
        self.qty = qty
        self.start_date = start_date
        self.harvest_date = harvest_date

plant1 = Plant('Kale',
          '04-30-2018',
          environment='outdoor',
          qty=3,
          notes='Grown from seed indoors and then soil.')
plant2 = Plant('Cilantro',
          '04-30-2018',
          environment='outdoor',
          qty=2,
          notes='Grown from seed indoors and then soil.')
data = [plant1, plant2]
with open('growlog.yml', 'w') as outfile:
    yaml.dump(data, outfile, default_flow_style=False)

