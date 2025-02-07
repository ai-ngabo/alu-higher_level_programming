#!/usr/bin/node
const fs = require('fs');

fs.writeFile(process.argv[2], 'process.argv[3]', 'utf-8', function(err, data) {
  err && console.log(err);
  const content = data;
  console.log(content);
}) 
