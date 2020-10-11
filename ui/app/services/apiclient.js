const fetch = require('node-fetch');
const MILLS_URL = "https://opendata.arcgis.com/datasets/5c026d553ff049a585b90c3b1d53d4f5_34.geojson?where=country%20%3D%20'Indonesia'";

class ApiClient {

    static async getMills(){
        let jsonBody = await ApiClient.get(MILLS_URL);
        let millDict = {};
        jsonBody["features"].forEach(function(mill){
            millDict[mill["properties"]["objectid"]] = mill["properties"];
        });
        return millDict;
    }

    static async get(url, retries=2, retryIntervalInSeconds=1){
        try {
            let response = await fetch(url);
            if (response.ok){
                return response.json();
            }
            else if (retries > 0) {
                setTimeout(() => { return ApiClient.get(url, retries - 1, retryIntervalInSeconds * 2)}, retryIntervalInSeconds);             
            } 
            else {
                throw Error(response);
            }
        }
        catch (error){
            console.error(error);
        }
    }
}

module.exports = ApiClient;