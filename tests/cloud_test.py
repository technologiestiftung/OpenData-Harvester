from cloud import importer

def test_import_package(mocker):
    mock_gather_data = mocker.patch('opendata.ckan.gather_data')
    mock_importer = mocker.patch('opendata.importer.import_package')
    mock_gather_data.return_value = { id: 1 }
    importer.import_package(1, 'fake', 1)
    mock_gather_data.assert_called_once_with(1, 'fake', 1)
    mock_importer.assert_called_once_with({ id: 1 })
