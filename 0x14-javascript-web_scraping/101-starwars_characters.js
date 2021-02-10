#!/usr/bin/node
const request = require('request');

const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;
request(url, (err, status, body) => {
  if (err) {
    console.log(err);
  } else {
    const chars = JSON.parse(body).characters;
    chars.forEach(url => {
      request(url, function (err, status, body) {
        if (err) {
          console.log(err);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
