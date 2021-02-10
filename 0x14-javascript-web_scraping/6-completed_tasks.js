#!/usr/bin/node
const request = require('request');

const users = {};

request.get(process.argv[2], (err, status, body) => {
  if (err) {
    console.log(err);
  } else {
    const tasks = JSON.parse(body);
    tasks.forEach(task => {
      if (task.completed === true) {
        if (users[task.userId] === undefined) {
          users[task.userId] = 0;
        }
        users[task.userId] += 1;
      }
    });
    console.log(users);
  }
}
);
