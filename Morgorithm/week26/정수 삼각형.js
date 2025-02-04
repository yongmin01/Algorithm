// [프로그래머스] 동적계획법 > 정수 삼각형

function solution(triangle) {
  const dp = Array.from(new Array(triangle.length), () =>
    new Array(triangle.at(-1).length).fill(0)
  );
  dp[0][0] = triangle[0][0];
  for (let i = 1; i < triangle.length; i++) {
    for (let l = 0; l < triangle[i].length; l++) {
      if (l === 0) {
        dp[i][l] = dp[i - 1][l] + triangle[i][l];
      } else if (l === triangle[i].length - 1) {
        dp[i][l] = dp[i - 1][l - 1] + triangle[i][l];
      } else {
        dp[i][l] = Math.max(dp[i - 1][l - 1], dp[i - 1][l]) + triangle[i][l];
      }
    }
  }
  return Math.max(...dp.at(-1));
}
