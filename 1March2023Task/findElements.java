import java.util.Scanner;
public class Main
{
    public static void targetValue(int arr[],int sum)
    {
        for(int i=0;i<arr.length-1;i++){
            for(int j=i+1;j<arr.length;j++){
            if(arr[i]+arr[j]==sum){
                 System.out.println("=> "+i+" - "+j);
            }
                
            }
           
        }
    }
    
	public static void main(String[] args) {
	    int arr[]={2,4,5,6,8,12,15,1};
	    Scanner sc =new Scanner(System.in);
	    System.out.println("Enter target value sum");
	    int sum=sc.nextInt();
	    System.out.println("Two elements are:");
	    targetValue(arr,sum);
	    
	}
}
