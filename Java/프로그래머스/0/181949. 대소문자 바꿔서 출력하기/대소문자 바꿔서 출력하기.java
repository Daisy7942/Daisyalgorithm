import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        String b ="";
        for(int i =0; i<a.length();i++ ){
               if((""+a.charAt(i)).equals((""+a.charAt(i)).toUpperCase())){
                   b+=("" + a.charAt(i)).toLowerCase();
               }else {b+=(""+ a.charAt(i)).toUpperCase();}
        }
         System.out.println(b);
    }
}