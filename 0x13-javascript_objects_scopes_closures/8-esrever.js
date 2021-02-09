#!/usr/bin/node
exports.esrever = function (list) {
  const nList = [];
  for (let l = list.length - 1; l >= 0; l -= 1) {
    nList.push(list[l]);
  }
  return nList;
};
