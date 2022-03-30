![](https://img.shields.io/badge/Build%20with%20%E2%9D%A4%EF%B8%8F-at%20Technologiesitftung%20Berlin-blue)

# Open Data Berlin

This project collects the metadata of CKAN based Open Data Portals. In this specific case the metadata for the Berlin Open Data Portal. And saves them into a database as is for further analysis.

# Testing

Run test via

`pytest`

# Local Development

Install packages with `pip install -r requirements.txt`

Create a `.env` file.

Run `local.py` to test it out locally.


# Structure

This project is meant to be run in a serverless infrastructure. The preferred way is AWS Lambda.

## Lambda Functions

For AWS Lambda the file `handler.py` is the entry point. The event object does contain the information needed to proceed.
Especially the API Key for the Berlin Open Data Portal and the URL and City Name.
URL should be `https://datenregister.berlin.de` and `city_name` would be `berlin`

### `load_data`

The `load_data` method/entry will use the CKAN API to retreive all packages in the Open Data Portal and will start new lambda functions to import them into the DB.
This method does not need DB env parameters

### `import_package`

`import_package` can be called individually for a `package_id` but will be called from `load_data` for every package in the Open Data Portal.  
Parameters are `package_id`, `url`, `api_key`.
It will use the CKAN API to retreive the package information and save them including resources, tags, groups to the DB.

This method does need DB env parameters!!

- `DB_USER`
- `DB_PASSWORD`
- `DB_HOST`
- `DB_PORT`
- `DB_NAME`

### `create_db`

Will create the needed DB tables for the importer method.
This method does need DB env parameters!!

# Deployment

Deployment can be done with the `serverless` npm package. The profile needs to be update and the necessary AWS rights are needed.

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!