package cecs274;
import java.util.Scanner;
/* Newton Bao and Krimika Keemtee
March 10, 2020
Purpose: This program is used calculate Pascal's Triangle based on user's input
Inputs: The user’s choice for nth row.
Output: Pascal's triangle based on nth row.
*/

public class PascalTriangle {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scnr = new Scanner(System.in);
		// user input
		System.out.println("Please enter a number: ");
		int a = scnr.nextInt();
		// for loop that for new row and new column that calls on Pascal method
		for (int i=0; i<=a; i++) {
			for (int j=0; j<=i; j++) {
				System.out.print( Pascal(i,j)+ " ");
				
			}
			System.out.println();
		}
		
	}
	// method to calculate value of Pascal's Triangle
	public static int Pascal(int i, int j) {
		if (j==0 || j==i) {
			return 1;
		}
		else {
			return Pascal(i-1,j-1)+Pascal(i-1,j);
		}
	}

}
