const fetch = require('node-fetch');
const api_base = "http://0.0.0.0:5000/api/v1.0"


class ApiClient {

    static async getMills(){
        let jsonBody = await ApiClient.get(api_base + "/mills");
        return jsonBody['mills'];
    }

    static async getFoliumMap(){
        let jsonBody = await ApiClient.get(api_base + "/folium-test");
        return jsonBody['html'];
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
