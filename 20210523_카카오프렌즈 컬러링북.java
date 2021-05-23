// https://programmers.co.kr/learn/courses/30/lessons/1829
// 참고: https://swycha.tistory.com/141

import java.util.Arrays;
import java.util.Iterator;
import java.util.LinkedList;

/*
 * BFS 변형하여 사용
 */

class ColoringBookSolution {
    int areaSize;
    int[][] directions = {{1, 0}, {-1, 0}, {0, -1}, {0, 1}};

    LinkedList<Node> queue;
    LinkedList<Node> adjacent;
    boolean[][] visited;

    static class Node {
        int x;
        int y;

        public Node(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    void bfs(int x, int y, int[][] picture) {
        visited[x][y] = true;
        queue.add(new Node(x, y));

        while (queue.size() != 0) {
            Node curr = queue.poll();

            // 인접한 영역 adjacent에 담기
            adjacent = new LinkedList<Node>();
            for (int[] d : directions) {
                try {
                    if (picture[curr.x+d[0]][curr.y+d[1]] != 0) {
                        adjacent.add(new Node(curr.x+d[0], curr.y+d[1]));
                    } else { // 0일 경우
                        visited[curr.x+d[0]][curr.y+d[1]] = true;
                    }
                } catch (ArrayIndexOutOfBoundsException e) {
                    continue;
                }
            }

            Iterator<Node> i = adjacent.listIterator();
            while (i.hasNext()) {
                Node next = i.next();
                if (!visited[next.x][next.y] && picture[curr.x][curr.y] == picture[next.x][next.y]) { // 방문 여부 확인과 같은 영역 여부 동시 확인
                    visited[next.x][next.y] = true;
                    queue.add(next);
                    areaSize++;
                }
            }
        }
    }

    public int[] solution(int m, int n, int[][] picture) {
        int numberOfArea = 0;
        int maxSizeOfOneArea = 0;

        queue = new LinkedList<>();
        visited = new boolean[m][n];

        for(int i = 0; i < m; i++){ // 영역이 항상 상하좌우로 연결되어 있는 것은 아님
            for(int j = 0; j < n; j++){ // 모든 좌표에서 BFS, 대신 BFS할 때 같은 영역일 경우만 확인한다 --> 영역 사이즈 체크를 위해
                if(picture[i][j] > 0 && !visited[i][j]){
                    areaSize = 1;
                    numberOfArea++;
                    bfs(i, j, picture);

                    if(maxSizeOfOneArea < areaSize)
                        maxSizeOfOneArea = areaSize;
                }

            }
        }

        int[] answer = new int[2];
        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;
        return answer;
    }

    public static void main(String[] args) {
        ColoringBookSolution coloringBookSolution = new ColoringBookSolution();
        int m = 6;
        int n = 4;
        int[][] picture = {{1, 1, 1, 0}, {1, 2, 2, 0}, {1, 0, 0, 1}, {0, 0, 0, 1}, {0, 0, 0, 3}, {0, 0, 0, 3}};
        System.out.println(Arrays.toString(coloringBookSolution.solution(m, n, picture)));
    }
}