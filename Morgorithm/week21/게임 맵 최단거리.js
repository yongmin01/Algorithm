// [프로그래머스] 깊이/너비 우선 탐색(DFS/BFS) > 게임 맵 최단거리

class Queue {
  constructor() {
    this.storage = {};
    this.front = 0;
    this.rear = 0;
  }

  size() {
    if (this.storage[this.rear] === undefined) {
      return 0;
    } else {
      return this.rear - this.rear + 1;
    }
  }

  add(value) {
    if (this.size() === 0) {
      this.storage["0"] = value;
    } else {
      this.rear += 1;
      this.storage[this.rear] = value;
    }
  }

  popleft() {
    let temp;
    if (this.front === this.rear) {
      temp = this.storage[this.front];
      delete this.storage[this.front];
      this.front = 0;
      this.rear = 0;
    } else {
      temp = this.storage[this.front];
      delete this.storage[this.front];
      this.front += 1;
    }
    return temp;
  }
}

function solution(maps) {
  const n = maps.length;
  const m = maps[0].length;
  let queue = new Queue();
  const visited = Array.from({ length: n }, () => Array(m).fill(false));
  queue.add([0, 0]);
  visited[0][0] = true;

  dx = [0, 1, 0, -1];
  dy = [1, 0, -1, 0];
  while (queue.size()) {
    let [x, y] = queue.popleft();
    for (let i = 0; i < 4; i++) {
      nx = x + dx[i];
      ny = y + dy[i];
      if (0 <= nx && nx < n && 0 <= ny && ny < m) {
        if (maps[nx][ny] !== 0 && visited[nx][ny] === false) {
          queue.add([nx, ny]);
          visited[nx][ny] = visited[x][y] + 1;
        }
      }
    }
  }
  return visited[n - 1][m - 1] ? visited[n - 1][m - 1] : -1;
}
