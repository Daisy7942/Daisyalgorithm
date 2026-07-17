class Solution {
    public int solution(int n) {
        int answer =0;
        while (true){
            answer+=1;
            if (7*answer>=n){
                break;
            }
        }
        return answer;
    }
}