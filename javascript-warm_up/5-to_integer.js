#!/usr/bin/node
const arg1 = Number(process.argv[2]);
console.log(isNaN(arg1) ? 'Not a number' : `My number: ${arg1}`);
