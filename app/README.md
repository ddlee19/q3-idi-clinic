## app
This directory contains an Express.js wrapper for the Angular application. The Angular app is read and served as a static file.


### Running locally

#### Docker
The code can be run in a Docker container with the included bash script. The script will copy the required input files into the container, build, and run the app.
```
sh run.sh
```

Alternatively, you can run outside of the container by installing dependencies with npm and running the following:
```
npm install
npm start
```

The frontend runs on http://localhost:3000/.
