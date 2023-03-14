public class Main
{
    public static void frequencyString(String s){
    int n=s.length();
        char ch[]=s.toCharArray();
        int count=0;
        for(int i=0;i<n;i++){
            count=1;
            for(int j=0;j<n;j++){
                if(ch[i]==ch[j]&&j!=i){
                    count++;
                    for(int k=j;k<n-1;k++){
                        ch[k]=ch[k+1];
                    }
                    n--;
                }
            }
        System.out.println(ch[i]+" "+count);
        }
    }
    
	public static void main(String[] args) {
	    String str="aabbbccdd";
	    frequencyString(str);
	    
	}
}