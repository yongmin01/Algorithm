// [프로그래머스] 2020 카카오 인턴십 > 보석 쇼핑

function solution(gems) {
  var answer = [0, gems.length - 1]; // gems 전체를 구매하는 경우로 초기 세팅

  const gemType = new Set(gems).size; // 보석의 종류
  const gemMap = new Map(); // 구매할 구간에 포함된 보석의  { 종류 -> 개수 }
  let left = 0,
    right = 0;

  while (right < gems.length) {
    // 구간을 끝까지 탐색
    if (gemMap.size === gemType) {
      // 모든 종류의 보석이 포함되면
      if (answer[1] - answer[0] > right - 1 - left) {
        // 기존 정답 구간보다 짧은지 체크 (여기서 right는 이전 반복문에서 이미 1이 증가되어서 넘겨진 것이기 때문에 -1하여 검사한다)
        answer = [left, right - 1]; // 짧을 경우 구간 업데이트
      }
      gemMap.set(gems[left], gemMap.get(gems[left]) - 1); // 왼쪽 포인터를 오른쪽으로 이동시키고 그에 맞게 보석의 수를 조절
      if (gemMap.get(gems[left]) === 0) {
        // 왼쪽 포인터 이동에 따라 보석의 종류가 구간에 포함되지 않게 되면 map에서 아예 제거
        gemMap.delete(gems[left]);
      }
      left++;
    } else {
      gemMap.set(gems[right], (gemMap.get(gems[right]) || 0) + 1); // 새로운 구간을 탐색하면서 보석 담기
      right++;
    }
  }

  return [answer[0] + 1, answer[1] + 1];
}
