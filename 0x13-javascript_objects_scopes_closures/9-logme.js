#!/usr/bin/node
let c = 0;
exports.logMe = function (item) {
  const nList = [];
  nList.push(item);
  for (let i = 0; i < nList.length; i++) {
    console.log(`${c}: ${nList[i]}`);
  }
  c += 1;
};
