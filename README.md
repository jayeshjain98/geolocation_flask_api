# geolocation_flask_api
A rest api in flask framework which returns the address and coordinated in json as well as xml as required.

First clone the repo on your system using:
```
git clone https://github.com/jayeshjain98/geolocation_flask_api.git
```

# set up the environment
run the requirements.txt file in your python environment

```
pip install -r requirements.txt
```

# run the server 
before running the server enter your google api service key in the geoapp/\_\_init\_\_.py file and then 
```
python run.py
```

# sample input for api

```json
{
    "address": "# 3582,13 G Main Road, 4th Cross Rd, Indiranagar,Bengaluru, Karnataka 560008",
    "output_format": "XML"
}
```
