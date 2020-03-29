package cecs274;
import java.util.Arrays;
import java.util.InputMismatchException;
import java.util.Scanner;
public class DigitCounter {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int num;
		int count=0;
		int digit;
		int[] getdigits= new int[3];
		int[] numcount= new int[11];
		Scanner scnr= new Scanner(System.in);
		for (int i =0; i<3;i++) {
			num=scnr.nextInt();
			getdigits[i]=num;
			while (num > 0) {
				digit=num%10;
				num=num/10;
			for (int k=0;k<10;k++) {
				if (digit == k) {
				numcount[k]=numcount[k]+1;
				count=numcount[k];
				}
			}

		}
			for (int j=0; j<numcount.length;j++) {
				if (numcount[j]>0) {
				System.out.println(j + " " + numcount[j]);
				}
			}
		System.out.println(Arrays.toString(getdigits));
				
	

}
	}
}
