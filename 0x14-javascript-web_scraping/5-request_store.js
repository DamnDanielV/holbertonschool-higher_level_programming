#!/usr/bin/node
const fs = require('fs');
const request = require('request');

request.get(process.argv[2]).on('error', (err) => {
  console.log(err);
}).pipe(fs.createWriteStream(process.argv[3]));
