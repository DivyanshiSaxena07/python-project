public class Main
{
    public static void converBinary(int decimalNumber){
        int binaryArr[]=new int[20];
        int index=0;
        while(decimalNumber>0)
        {
            binaryArr[index]=decimalNumber%2;
            index++;
            decimalNumber=decimalNumber/2;
        }
        for(int i=index-1;i>=0;i--)
        System.out.print(binaryArr[i]);
    }
	public static void main(String[] args) {
	converBinary(21);
	}
}