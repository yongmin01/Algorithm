// [프로그래머스] 해시 > 의상

function solution(clothes) {
  var answer = 1;

  const clothes_dic = {};
  for (c of clothes) {
    if (!Object.keys(clothes_dic).includes(c[1])) {
      clothes_dic[c[1]] = 1;
    } else {
      clothes_dic[c[1]] += 1;
    }
  }
  for (t of Object.keys(clothes_dic)) {
    answer *= clothes_dic[t] + 1;
  }
  return answer - 1;
}
