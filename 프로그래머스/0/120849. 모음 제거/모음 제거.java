class Solution {
    public String solution(String my_string) {
        String answer = "";
        String[] A = {"a", "e", "i", "o", "u"};

        for (int i = 0; i < my_string.length(); i++) {
            boolean isVowel = false;

            for (int j = 0; j < A.length; j++) {
                if (my_string.charAt(i) == A[j].charAt(0)) {
                    isVowel = true;
                    break;
                }
            }

            if (!isVowel) {
                answer += my_string.charAt(i);
            }
        }

        return answer;
    }
}