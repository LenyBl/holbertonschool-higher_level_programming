#!/usr/bin/node
const i = process.argv[2];
if (isNaN(i)) {
  console.log('Missing number of occurrences');
} else {
  const num = parseInt(i);
}
const myVar = 'C is fun';
for (let j = 0; j < num; j++) {
  console.log(myVar);
}
