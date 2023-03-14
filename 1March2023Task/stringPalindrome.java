import java.util.Scanner;
    public class Main
    {
        public static boolean stringPalindrome(String str){
            String rev="";
            int length=str.length();
            for(int i=length-1;i>=0;i--){
                rev=rev+str.charAt(i);
            }
            if(str.equals(rev))
            return true;
            else
            return false;
        }
    	public static void main(String[] args) {
    	    Scanner sc =new Scanner(System.in);
    		System.out.println("Enter String:");
    	    String str=sc.nextLine();
    		System.out.println(stringPalindrome(str));
    	}
    }
