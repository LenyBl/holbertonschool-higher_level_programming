#!/usr/bin/node
const argv = process.argv;
if (argv == 0) {
  console.log('No argument');
} else {
  console.log(argv[2]);
}
