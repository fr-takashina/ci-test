from pathlib import Path
from pytest import fixture


@fixture(scope="session")
def test_root():
    return Path(__file__).parent


@fixture(scope="session")
def data_root():
    return Path(__file__).parent.parent / "data_test"
