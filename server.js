// File to start the Server

// ------- Importing Required Libraries -------
// To use the express module
const express = require('express');

// To inform the express server to use var of config.env file (which has value of PORT var)
const dotenv = require('dotenv');

// Adding morgan module to log user requests
const morgan = require('morgan');

// To parse incoming request bodies in the URL-encoded format
const bodyparser = require('body-parser');

// To create the app, initialising app variable as express application
const app = express();

// To specify path
const path = require('path');
const { render } = require('ejs');

// Connecting Mongodb file
const connectDB = require('/Users/vinayabomnale/Desktop/React/Recovery_Tracker/assets/server/database/connection.js');

// -----------------------------------------------

// Specifying the path of the config.env file to get PORT var value
dotenv.config({path: 'config.env'});

// Log Requests on console whenever we make a request
app.use(morgan('tiny'));

// MongoDb connection
connectDB();

// parse request to body-parser
app.use(bodyparser.urlencoded({ extended : true}))

// set view engine, Using default ejs files
app.set('view engine', 'ejs'); //(View engine parameter, type of view engine)
app.set("views", path.resolve(__dirname, "/Users/vinayabomnale/Desktop/React/Recovery_Tracker/assets/views"));

// Load assets onto the server
app.use('/css', express.static(path.resolve(__dirname, "assets/css"))) //So now if we have a style.css file in css folder, we can use thevirtual path created and use the sytle file eg. css/style.css
app.use('/img', express.static(path.resolve(__dirname, "assets/img")))
app.use('/js', express.static(path.resolve(__dirname, "assets/js")))

// Storing all dot env variable info in Port. If file not available, we pass the code 8080
const PORT = process.env.PORT || 8080 // Passing the port number 

// Load Routers
app.use('/', require('/Users/vinayabomnale/Desktop/React/Recovery_Tracker/assets/server/routes/router'));

app.listen(PORT, ()=> { console.log(`Server is running on http://localhost:${PORT}`)});