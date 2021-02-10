#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
request.get(`https://swapi-api.hbtn.io/api/films/${id}`, (err, status, body) => {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body.title));
  }
});
