import os
import urllib.request


def download_data(start_year, end_year, folder='downloads'):
    if not os.path.exists(folder):
        os.makedirs(folder)
    years = list(range(start_year, (end_year + 1)))
    for year in years:
        download_url = f'https://contrataciondelsectorpublico.gob.es/sindicacion/sindicacion_643/licitacionesPerfilesContratanteCompleto3_{year}.zip'
        fpath = os.path.join(folder, f'licitacionesPerfilesContratanteCompleto3_{year}.zip')
        urllib.request.urlretrieve(download_url, fpath)
