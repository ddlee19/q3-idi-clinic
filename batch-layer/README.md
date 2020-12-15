
## batch-layer
The code in this directory is used to retrieve data from Google Earth Engine, store the results locally, and perform calculations on the data. The processes contained here are meant to be run once on server startup, or periodically to update with new data or risk computations.

### Running locally

#### Set up Google Earth Engine
A Google Earth Engine service account and json key file are required to run the code. The key must be copied to this directory and named `privatekey.json`. The service account name needs to be copied into the `SERVICE_ACCOUNT` variable in `batch.py`. [Read about service accounts here.](https://developers.google.com/earth-engine/guides/service_account)

#### Required inputs
The code requires 3 input files, which are available in the `./input` directory contained here:
1. brand_info.csv
2. complete_match_update.tsv
3. matches_from_matching.csv

#### Docker
The code can be run in a Docker container with the following commands:
```
docker build -t batch-layer .
docker run batch-layer
```

Alternatively, you can run outside of the container by installing dependencies with pip and running the following:
```
python3 -m pip install -r requirements.txt
python3 batch.py
```


### Output files
Transformed and generated data is written to a `data/` directory at the parent level. This allows the web server to read from the same directory.
