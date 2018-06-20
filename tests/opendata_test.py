import httpretty
import automock

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

def test_import_package_simple():
    importer.import_package(simple_package)
    mocked = automock.get_mock('opendata.importer.insert_or_update')
    assert mocked.call_count == 1
    mocked.assert_called_once_with('package', simple_package, 'id', importer.exclude_package)

def test_import_package_resource():
    package = { 'type': 'dataset', 'id': 1, 'resources': [simple_resource], 'tags': [], 'groups': [] }
    importer.import_package(package)
    mocked = automock.get_mock('opendata.importer.insert_or_update')
    assert mocked.call_count == 2

