class Solution {
    public int[] solution(int n, int m) {
        int[] answer = new int[2];
        int num = n;
        int num2 = m;
        while (m !=0){
            int a = n%m;
            n = m;
            m = a;
            answer[0]=n;
        }
        answer[1] = num*num2/answer[0];
        return answer;
    }
}

