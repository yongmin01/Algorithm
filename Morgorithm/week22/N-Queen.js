// [프로그래머스] 연습문제 > N-Queen

function solution(n) {
  var answer = 0;
  let queens = [];

  function promissing(r, c) {
    for ([x, y] of queens) {
      if (r === x || c === y) return false;
      if (Math.abs((r - x) / (c - y)) === 1) return false;
    }
    return true;
  }

  function backtracking(r) {
    if (r === n) {
      answer += 1;
      queens.pop();
      return;
    }
    for (let c = 0; c < n; c++) {
      if (promissing(r, c)) {
        queens.push([r, c]);
        backtracking(r + 1);
      }
    }
    queens.pop();
    return;
  }

  backtracking(0);
  return answer;
}
