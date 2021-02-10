#!/usr/bin/node
const request = require('request');

let count = 0;

request(process.argv[2], (err, status, body) => {
  if (err) {
    console.log(err);
  } else {
    const movies = JSON.parse(body.results);
    movies.forEach(movie => {
      const chars = movie.characters;
      chars.forEach(id => {
        if (id.includes('18')) {
          count += 1;
        }
      });
    });
  }
  console.log(count);
});
