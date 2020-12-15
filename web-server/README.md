## Flask API Server

Provides access to palm oil mill and consumer brand data.

Overview:

* **app.py**: The Flask application server. Calls methods in dal.py to retrieve appropriate data for incoming requests and then returns that data as JSON.

* **attr_collections.py**: Constants used by dal.py to filter data sent from the batch layer.

* **dal.py**:  The data access layer (DAL). Parses CSV and JSON input files produced by the batch layer and then maps and aggregates that data to create API payloads.

* **log_util.py**: Logger configuration.

* **sample_payloads**: A folder containing sample response payloads and metadata (in the form of markdown files) for each API endpoint.

* **templates/index.html**: The home page for the Flask application. Could be utilized in the future to create an interface for the API.

* **test.py**: A collection of unit tests to validate the data sent from app.py.