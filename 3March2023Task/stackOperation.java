import java.io.*;
import java.util.*;
 
class Main {
   
    public static void main(String[] args)
    {
 
 
        Stack<Integer> stack1 = new Stack<Integer>();
 
        stack1.push(5);
        stack1.push(6);
        stack1.push(7);
        
        
        stack1.pop();
        
        stack1.peek();
 
        System.out.println(stack1);
        System.out.println(stack1.peek());
       
    }
}