import java.util.ArrayList;
import java.util.Arrays;

class DevelopFunction {
    public static int[] solution(int[] progresses, int[] speeds) {
        // 1 - 혼자 풀이
        // 정확성 테스트 3/11
        int num = progresses.length;
        ArrayList<Integer> answer = new ArrayList<>();
        int[] left = new int[num];

        for (int i = 0; i < num; i++) {
            left[i] = ((100 - progresses[i]) % speeds[i] == 0) ? (100 - progresses[i]) / speeds[i] : ((100 - progresses[i]) / speeds[i]) + 1;
        }

        int j = 0;
        int count = -1;
        while (j < num) {
            if (j == 0 || left[j-1] < left[j]) {
                answer.add(1);
                count++;
            }
            else if (j != 0 && left[j-1] >= left[j]) {
//                System.out.println(answer);
                answer.set(count, answer.get(count)+1);
            }
            j++;
        }

        return answer.stream().mapToInt(i -> i).toArray();
    }

    public static void main(String[] args) {
        int[] progresses = {95, 90, 99, 99, 80, 99};
        int[] speeds = {1, 1, 1, 1, 1, 1};
        System.out.println(Arrays.toString(solution(progresses, speeds)));
    }
}