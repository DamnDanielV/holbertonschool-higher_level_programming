#!/usr/bin/node
const request = require('request');

if (process.argv.length >= 3) {
  const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

  request(url, (err, status, body) => {
    if (err) {
      console.log(err);
    } else {
      console.log(JSON.parse(body).title);
    }
  });
}
