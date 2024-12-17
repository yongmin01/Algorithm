// 2019 카카오 개발자 겨울 인턴십 > 크레인 인형뽑기 게임

function solution(board, moves) {
  const stack = [];
  var answer = 0;
  for (move of moves) {
    for (row of board) {
      if (row[move - 1] !== 0) {
        stack.push(row[move - 1]);
        row[move - 1] = 0;
        if (stack.at(-1) === stack.at(-2)) {
          stack.pop();
          stack.pop();
          answer += 2;
        }
        break;
      }
    }
  }
  return answer;
}
