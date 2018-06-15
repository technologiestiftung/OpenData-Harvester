import requests
import json

def gather_data(package_id, url, apikey):
        urltoread = url + "/api/3/action/package_show?id=" + package_id
        headers = {'Authorization': apikey}
        r = requests.get(urltoread, headers=headers)
        pdata = {}
        try:
            urldata = r.text
            pdata = json.loads(urldata)
        except (RuntimeError, TypeError, NameError, ValueError):
            print('error for url {}'.format(urltoread))
        if 'success' in pdata and pdata['success']:
            return(pdata['result'])

def gatherCity(cityname, url, apikey):
    headers = {'Authorization': apikey}
    r = requests.get(url + "/api/3/action/package_list", headers=headers)
    r.encoding = 'utf-8'
    listpackages = json.loads(r.text)

    return listpackages['result']

