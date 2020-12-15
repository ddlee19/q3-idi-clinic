## web-server
This directory contains a Flask API for the IDI application backend. The API makes endpoints available for brand, mill, and treeloss aggregations computed in the batch layer.


### Running locally

#### Required inputs
The backend requires four csv files to run. These files are located in the parent directory named `data`.

#### Docker
The code can be run in a Docker container with the included bash script. The script will copy the required input files into the container, build, and run the app.
```
sh run.sh
```

Alternatively, you can run outside of the container by installing dependencies with pip and running the following:
```
python3 -m pip install -r requirements.txt
python3 app.py local
```

The backend runs on http://localhost:5000/.

### File Structure
Overview:

* **app.py**: The Flask application server. Calls methods in dal.py to retrieve appropriate data for incoming requests and then returns that data as JSON.

* **attr_collections.py**: Constants used by dal.py to filter data sent from the batch layer.

* **dal.py**:  The data access layer (DAL). Parses CSV and JSON input files produced by the batch layer and then maps and aggregates that data to create API payloads.

* **log_util.py**: Logger configuration.

* **sample_payloads**: A folder containing sample response payloads and metadata (in the form of markdown files) for each API endpoint.

* **templates/index.html**: The home page for the Flask application. Could be utilized in the future to create an interface for the API.

* **test.py**: A collection of unit tests to validate the data sent from app.py.