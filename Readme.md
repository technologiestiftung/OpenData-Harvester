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
<table>
  <tr>
    <td align="center"><a href="http://milafrerichs.com/"><img src="https://avatars.githubusercontent.com/u/688980?v=4?s=64" width="64px;" alt=""/><br /><sub><b>Mila Frerichs</b></sub></a><br /><a href="https://github.com/technologiestiftung/OpenData-Harvester/commits?author=milafrerichs" title="Code">💻</a> <a href="https://github.com/technologiestiftung/OpenData-Harvester/commits?author=milafrerichs" title="Documentation">📖</a></td>
    <td align="center"><a href="http://www.sebastianmeier.eu/"><img src="https://avatars.githubusercontent.com/u/302789?v=4?s=64" width="64px;" alt=""/><br /><sub><b>Sebastian Meier</b></sub></a><br /><a href="https://github.com/technologiestiftung/OpenData-Harvester/commits?author=sebastian-meier" title="Code">💻</a> <a href="https://github.com/technologiestiftung/OpenData-Harvester/commits?author=sebastian-meier" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/vogelino"><img src="https://avatars.githubusercontent.com/u/2759340?v=4?s=64" width="64px;" alt=""/><br /><sub><b>Lucas Vogel</b></sub></a><br /><a href="https://github.com/technologiestiftung/OpenData-Harvester/commits?author=vogelino" title="Documentation">📖</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!

## Credits

<table>
  <tr>
    <td>
      <a src="https://odis-berlin.de">
        <br />
        <br />
        <img width="200" src="https://logos.citylab-berlin.org/logo-odis-berlin.svg" />
      </a>
    </td>
    <td>
      Together with: <a src="https://citylab-berlin.org/en/start/">
        <br />
        <br />
        <img width="200" src="https://logos.citylab-berlin.org/logo-citylab-berlin.svg" />
      </a>
    </td>
    <td>
      A project by: <a src="https://www.technologiestiftung-berlin.de/en/">
        <br />
        <br />
        <img width="150" src="https://logos.citylab-berlin.org/logo-technologiestiftung-berlin-en.svg" />
      </a>
    </td>
    <td>
      Supported by: <a src="https://www.berlin.de/rbmskzl/en/">
        <br />
        <br />
        <img width="80" src="https://logos.citylab-berlin.org/logo-berlin-senweb-en.svg" />
      </a>
    </td>
  </tr>
</table>

