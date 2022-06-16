from pathlib import Path

import pandas as pd
from pytest import fixture

from opt_app_boilerplate.usecase.sample import print_project_root


@fixture(scope="module")
def path_data(test_root, data_root) -> Path:
    path_relative = Path(__file__).parent.relative_to(test_root)
    return data_root / path_relative


class SuperTestCase:
    @fixture(scope="class")
    def path_case(self, path_data: Path):
        return path_data / f"{self.__class__.__name__}.csv"

    @fixture(scope="class")
    def data(self, path_case):
        return pd.read_csv(path_case, header=0)


class IfCsvHasNoBody(SuperTestCase):
    def test_df_size_is_0(self, data):
        assert len(data) == 0


class IfCsvHas3Rows(SuperTestCase):
    def test_df_size_is_3(self, data):
        assert len(data) == 3


class TestImport:
    def test_import(self):
        print_project_root()
