from cloud import importer
import automock

automock.register('db.connect.get_connection')

def test_import_package(mocker):
    mock_gather_data = mocker.patch('cloud.importer.ckan.gather_data')
    mock_importer = mocker.patch('cloud.importer.importer.import_package')
    mock_gather_data.return_value = { id: 1 }
    importer.import_package(1, 'fake', 1)
    mock_gather_data.assert_called_once_with(1, 'fake', 1)
    mock_importer.assert_called_once_with({ id: 1 })
