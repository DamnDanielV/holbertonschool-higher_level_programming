#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
request(url, (err, res, body) => {
  if (err) { 
      console.log(err);
    } else {
    let count = 0;
    const movies = JSON.parse(body).results;
    movies.forEach(movie => {
        let chars = movie['characters'];
        chars.forEach(id => {
          if (id.includes('18')) {
            count += 1;
          }
        });
      });
    console.log(count);
  }
});