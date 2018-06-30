import yaml
from click.testing import CliRunner

from growlog.cli import main
from growlog.main import Crop
from growlog.main import save_growlog


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


def test_main():
    runner = CliRunner()
    save_growlog(seed_data())
    result = runner.invoke(main)

    assert yaml.dump(seed_data()) in result.output
    assert result.exit_code == 0
