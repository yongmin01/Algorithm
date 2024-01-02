const INPUT = require("fs").readFileSync("input.txt").toString().split("\n");
const list = INPUT[1].trim().split(" ");
const v = INPUT[2];

let count = 0;
function solution(list, v) {
  for (i = 0; i < list.length; i++) {
    if (list[i] == v) count++;
  }

  return count;
}
console.log(solution(list, v));
