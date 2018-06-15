import httpretty

from opendata import importer, ckan

def test_exclude_from_dict():
    start_dict = {
            'isopen': True,
            'state': 'active'
            }
    exclude= ('state')
    expected = { 'isopen': True }
    assert importer.exclude_from_dict(start_dict, exclude) == expected


simple_package = { 'type': 'dataset', 'id': 1, 'resources': [], 'tags': [], 'groups': [] }
simple_resource = { 'id': 1 }

def test_import_package_simple(mocker):
    mocked_insert_o_update = mocker.patch('opendata.importer.insert_or_update')
    importer.import_package(simple_package)
    assert mocked_insert_o_update.call_count == 1
    mocked_insert_o_update.assert_called_once_with('package', simple_package, 'id', importer.exclude_package)

def test_import_package_resource(mocker):
    mocked_insert_o_update = mocker.patch('opendata.importer.insert_or_update')
    package = { 'type': 'dataset', 'id': 1, 'resources': [simple_resource], 'tags': [], 'groups': [] }
    importer.import_package(package)
    assert mocked_insert_o_update.call_count == 2

