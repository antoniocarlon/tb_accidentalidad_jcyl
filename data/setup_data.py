import requests

CSV_FILE = 'https://datosabiertos.jcyl.es/web/jcyl/risp/es/transporte/accidentalidad-carreteras/1284967604431.csv'

with open('data.csv', 'w') as outfile:
    with requests.get(CSV_FILE, stream=True) as r:
        for line in r.iter_lines():
            line_ = line.decode('utf-8')
            if line_.split(';')[1] not in ['NOMBRE', 'TOTAL']:
                outfile.write(f"{line_}\n")
