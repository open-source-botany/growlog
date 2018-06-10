import yaml
from click.testing import CliRunner

from growlog.cli import main
from growlog.main import seed_data


def test_main():
    runner = CliRunner()
    result = runner.invoke(main)

    assert yaml.dump(seed_data()) in result.output
    assert result.exit_code == 0
