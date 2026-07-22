class Solution {
    public int[] solution(int[] num_list) {
        int[] answer = new int[2];
        int count = 0;
        int count2 =0;
        for (int i =0; i < num_list.length; i++){
            if (num_list[i]%2==0){
                count+=1;
            }else{ 
                count2+=1;
            }
            
        answer[0]=count;
        answer[1]=count2;
        }
        return answer;
    }
}