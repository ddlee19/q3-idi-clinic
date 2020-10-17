const express = require('express')
const app = express()
const port = 3000
const path = require('path');
const ApiClient = require('./services/apiclient')

// Configuration
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');
app.use(express.static(path.join(__dirname, 'public')));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));

// Routing
app.get('/', (req, res) => {
  ApiClient.getMills().then(millsDict => {
    res.render('index', { 
      title: 'IDI Palm Oil Tracker', 
      millsDictStr: JSON.stringify(millsDict)
    });
  });
})
app.get('/folium-test', (req, res) => {
  ApiClient.getFoliumMap().then(html => {
    res.send(html);
  });
})

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})

// Error handling
app.use(function(req, res, next) {
  next(createError(404));
});

app.use(function(err, req, res, next) {
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  res.status(err.status || 500);
  res.render('error');
});
