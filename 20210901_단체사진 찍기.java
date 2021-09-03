// https://programmers.co.kr/learn/courses/30/lessons/1835
// 참고: https://youngest-programming.tistory.com/586
// 순열 참고: https://bcp0109.tistory.com/14


class GroupPhotoSolution {
    private int answer = 0;
    private String[] friends = {"A", "C", "F", "J", "M", "N", "R", "T"};

    public int solution(int n, String[] rules) {
        boolean[] visited = new boolean[8];
        dfs("", visited, rules);
        return answer;
    }

    private void dfs(String names, boolean[] visited, String[] rules) {
        if (names.length() == 8) {
            if (checkCondition(names, rules)) { // 조건을 만족하는지 체크
                answer++;
            }
            return;
        }
        for (int i = 0; i < 8; i++) { // 순열 만들기
            if (!visited[i]) {
                visited[i] = true;
                String name = names + friends[i];
                dfs(name, visited, rules);
                visited[i] = false;
            }
        }
    }

    private boolean checkCondition(String names, String[] rules) {
        for (String rule : rules) {
            int position1 = names.indexOf(rule.charAt(0)); // 프렌즈 포지션1
            int position2 = names.indexOf(rule.charAt(2)); // 프렌즈 포지션2

            char op = rule.charAt(3); // 연산자
            int index = rule.charAt(4) - '0'; // 간격
            // char - '0'하면 바로 int로 변환 가능 (아스키코드 기반 연산)

            switch (op) {
                case '=':
                    if (!(Math.abs(position1 - position2) == index + 1)) { // 포지션 차이를 구하기 위해선 +1을 해야함
                        return false;
                    }
                    break;
                case '>':
                    if (!(Math.abs(position1 - position2) > index + 1)) {
                        return false;
                    }
                    break;
                case '<':
                    if (!(Math.abs(position1 - position2) < index + 1)) {
                        return false;
                    }
                    break;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        GroupPhotoSolution groupPhotoSolution = new GroupPhotoSolution();
        int n = 2;
        String[] data = {"N~F=0", "R~T>2"};
        System.out.println(groupPhotoSolution.solution(n, data));
    }
}
