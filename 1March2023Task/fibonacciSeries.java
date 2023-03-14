import java.util.Scanner;
public class Main
{
    public static void findFibonacci(int n){
        int a=0,b=1,c=0;
        System.out.print(a+" "+b+" ");
        for(int i=1;i<=n;i++){
        c=a+b;
            System.out.print(c+" ");
            a=b;
            b=c;
        }
        
    }
	public static void main(String[] args) {
	    Scanner sc=new Scanner(System.in);
	    System.out.print("Enter number:");
	    int n=sc.nextInt();
		System.out.println("First"+n+" Fibonacci number:");
	    findFibonacci(n);
	}
}