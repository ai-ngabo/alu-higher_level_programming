#!/usr/bin/node
const fs = require('fs'); //This line imports file system module to handle file operations
fs.readFile(process.argv[2], function(err, data){
  err && console.log(err); // this logs any error to the console
  const content = data;
  console.log(content.toString());
});
