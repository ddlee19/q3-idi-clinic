# IDI Clinic

A web framework for the IDI project at the University of Chicago's Civic Data and Technology Clinic.


## Running the application locally
To run the complete application locally, you need to open two terminal windows: one for the frontend and the second for the backend. Alternatively, both applications can be run independently without depending on the other. 

To start the backend:
```
git clone https://github.com/danielgrzenda/q3-idi-clinic.git

cd web-server
sh run.sh
```

To start the frontend, you must install/update the node.js depedencies with `npm install` before starting the Docker container:
```
cd ui/app
npm install
docker-compose up
```
The web interface is available at http://localhost:3000 in your browser.




