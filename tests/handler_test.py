import handler

def test_import_package(mocker):
    mock_importer = mocker.patch('handler.importer.import_package')
    mock_importer.return_value = '1'
    event = { 'package_id': 1, 'url': 'fake', 'api_key': 1}
    handler.import_package(event, {})
    mock_importer.assert_called_once_with(1, 'fake', 1)

def test_load_data(mocker):
    mock_importer = mocker.patch('handler.importer.load_data')
    mock_importer.return_value = []
    event = { 'city_name': 'berlin', 'url': 'fake', 'api_key': 1}
    handler.load_data(event, {})
    mock_importer.assert_called_once_with('berlin', 'fake', 1)
