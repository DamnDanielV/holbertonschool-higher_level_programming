#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const coin = list.filter((elemento) => elemento === searchElement);
  return coin.length;
};
