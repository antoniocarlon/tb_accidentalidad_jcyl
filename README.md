# Studying the accidents in the roads of Castilla y León, Spain using Tinybird

## Setup
Create a [Tinybird](https://www.tinybird.co/) account if you don't have one.

Create and activate a virtual environment:
```
virtualenv -p python3.8 venv
source venv/bin/activate
```

Install the requirements:
```
pip install -r requirements.txt
```

Download the original data (and digest it a bit):
```
python3 data/setup_data.py
```

Authenticate in Tinybird using the CLI:
```
tb auth --token <MYTOKEN>
```

Push the datasource to Tinybird:
```
tb push tb/accidentalidad.datasource
```

Append the data to the datasource:
```
tb datasource append accidentalidad data.csv accidentalidad
```

Get the most dangerous road sections in 2021:
```
tb push tb/accidentalidad_2021_mostdangerous.pipe
```

Get the most dangerous road sections in 2021 compared to 2020:
```
tb push tb/accidentalidad_2020_vs_2021_mostdangerous.pipe
```
