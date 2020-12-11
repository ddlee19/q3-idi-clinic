
## batch-layer
The code in this directory is used to retrieve data from Google Earth Engine, store the results locally, and perform calculations on the data. The processes contained here are meant to be run once on server startup, or periodically to update with new data or risk computations.

### Running the examples locally
Due to some unresolved authentication issues with Docker, these examples require the user to use virtualenv to manage package dependencies. In addition, you must copy the private service account key (private-key.json) from the shared Google Drive folder to the `batch-layer` directory before running. **Do not share the key file or commit it to the repository.**

After copying the key, set up the virtualenv environment:
```
cd batch-layer
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```

Your environment should be ready to run the examples using the usual bash or ipython commands:
```
python3 batch.py
```
#### Input files needed
The code requires 3 input files:
1. brand_info.csv
2. complete_match_update.tsv
3. matches_from_matching.csv
