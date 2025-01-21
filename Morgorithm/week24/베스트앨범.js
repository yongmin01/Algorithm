// [프로그래머스] 해시 > 베스트앨범

function solution(genres, plays) {
  // 곡 정보 묶기 {"genres": 장르 "no": 고유 번호, "play_time": 재생 횟수}
  const info = [];
  for (let i = 0; i < genres.length; i++) {
    info.push({ genre: genres[i], no: i, play_time: plays[i] });
  }

  let genres_song = new Map(); // 각 장르별로 곡 담기 {고유번호, 재생 횟수}
  let genres_playtime = new Map(); // 각 장르별 곡들의 재생 횟수 총합

  for (let song of info) {
    if (genres_song.has(song.genre)) {
      genres_song.set(song.genre, [
        ...genres_song.get(song.genre),
        [song.no, song.play_time],
      ]);
    } else {
      genres_song.set(song.genre, [[song.no, song.play_time]]);
    }

    if (genres_playtime.has(song.genre)) {
      genres_playtime.set(
        song.genre,
        genres_playtime.get(song.genre) + song.play_time
      );
    } else {
      genres_playtime.set(song.genre, song.play_time);
    }
  }

  let arr_genres_playtime = Array.from(genres_playtime);
  arr_genres_playtime = arr_genres_playtime.sort((a, b) => b[1] - a[1]); // 재생 횟수 총합 높은 순으로 장르 정렬

  // 재생 횟수 오름차순으로 곡 정렬 후 2곡의 고유번호만 추출
  var answer = [];
  for (let [genre, total_playtime] of arr_genres_playtime) {
    let temp = genres_song
      .get(genre)
      .sort((a, b) => b[1] - a[1] || a[0] - b[0])
      .slice(0, 2);
    temp.forEach((song) => answer.push(song[0]));
  }
  return answer;
}
