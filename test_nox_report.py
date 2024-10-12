import nox_report
import pytest
import textwrap
from pathlib import Path


@pytest.fixture
def sample_report() -> Path:
    return Path(__file__).parent / 'sample_report.json'


def test_output(
        capsys: pytest.CaptureFixture[str], sample_report: Path) -> None:
    nox_report.parse_report(str(sample_report), 'Nox test')
    out, _ = capsys.readouterr()
    assert out == textwrap.dedent(
        '''\
        ## Nox test

        * lint: success :heavy_check_mark:
        * typecheck: success :heavy_check_mark:
        * test-3.9: skipped :large_blue_circle:
        * test-3.10: success :heavy_check_mark:
        * test-3.11: skipped :large_blue_circle:
        * coverage: success :heavy_check_mark:
        ''')
