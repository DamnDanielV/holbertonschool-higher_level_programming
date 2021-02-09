#!/usr/bin/node
const fs = require('fs');

const args = process.argv.slice(2);
const file1 = fs.readFileSync('./' + args[0]);
const file2 = fs.readFileSync('./' + args[1]);
fs.writeFileSync(`./${args[2]}`, file1 + file2);
