from common import *

def test_copy(ds_local):
    ds = ds_local
    ds['v'] = ds.x + 1

    dsc = ds.copy()
    assert 'x' in dsc.get_column_names()
    assert 'v' in dsc.get_column_names()
    assert 'v' in dsc.virtual_columns
    dsc.x.values


def test_non_existing_column(df_local):
    df = df_local
    with pytest.raises(KeyError):
        df.copy(column_names=['x', 'not_existing'])
