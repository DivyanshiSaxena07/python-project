import java.util.*;
public class Main
{
    public static int[] commonValue(int arr1[],int arr2[]){
	    int len1=arr1.length;
	    int len2=arr2.length;
	    int arr3[]=new int[len1];
	    int index=0;
	    for(int i=0;i<len1;i++){
	        for(int j=0;j<len2;j++){
	            if(arr1[i]==arr2[j]){
	                arr3[index]=arr1[i];
	            index++;
	            }
	        }
	      
	    }
	    return arr3;
    }
    
	public static void main(String[] args) {
	    int arr1[]={10,20,30,40,50};
	    int arr2[]={11,22,30,20,34};
	     System.out.print("CommonValue:");
	    int arr[]=commonValue(arr1,arr2);
	    for(int k=0;k<arr.length;k++)
	    System.out.print(arr[k]+" ");
	}
}
