class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        String sum = "";
        int A = Integer.parseInt(Integer.toString(a)+Integer.toString(b));
        int B = Integer.parseInt(Integer.toString(b)+Integer.toString(a));
        if(A>=B){sum = Integer.toString(a)+Integer.toString(b);
        }else{
            sum=Integer.toString(b)+Integer.toString(a);
        }
        answer = Integer.parseInt(sum);
        
        return answer;
    }
}