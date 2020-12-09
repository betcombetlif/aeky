import java.util.Arrays;

class StockPrice {
    public static int[] solution(int[] prices) {
        /* 1 - 혼자 풀이
         * 정확성 테스트 10/10, 효율성 테스트 5/5
         */
        int[] answer = new int[prices.length];

        for (int i=0; i< prices.length; i++) {
            for (int j=i+1; j< prices.length; j++) {
                answer[i] += 1;
                if (prices[i] > prices[j]) {
                    break;
                }
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        int[] prices = {1, 2, 3, 2, 3};
        System.out.println(Arrays.toString(solution(prices)));
    }
}