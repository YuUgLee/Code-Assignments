package cecs274;
import java.util.Scanner;
public class EuclidRecursion {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scnr= new Scanner(System.in);
		System.out.println("Please enter an x value: ");
		int x = scnr.nextInt();
		System.out.println("Please enter a y value: ");
		int y = scnr.nextInt();
		int result= EuclidRecursion(x,y);
		System.out.println("GCD = " + result);

	}
	
	public static int EuclidRecursion(int x, int y) {
		if (x > y && x>0 && y>0) {
			int num=x%y;
			return EuclidRecursion(num,y);
		}
		else if (y>x && x>0 && y>0) {
			int num=y%x;
			return EuclidRecursion(x,num);
		}
		else if (x==0) {
			return y;
		}
		
		else if (y==0) {
			return x;
			
		}
		return x;

	}

}
