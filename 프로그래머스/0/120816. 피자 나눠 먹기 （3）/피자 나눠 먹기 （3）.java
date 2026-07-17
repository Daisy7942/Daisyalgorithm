class Solution {
    public int solution(int slice, int n) {
        int answer = 0;
        while (true){
            answer+=1;
            if(slice*answer>=n){
                break;
            }
        }
        return answer;
    }
}