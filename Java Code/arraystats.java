package cecs277;
import java.util.*;


public class arraystats {
	public static int max(int [] n)

	{

		int i;
		int length=n.length;
		int total = n[0];
		for (i=0;i<length;i++) {
			if (n[i]>total) {
				total=n[i];
			}
			
		}
		return total;
	}

	public static int min(int [] n)

	{

		int i;
		int length=n.length;
		int total = n[0];
		for (i=0;i<length;i++) {
			if (n[i]<total) {
				total=n[i];
			}
			
		}
		return total;

	}

	public static double ave(int [] n)

	{

		int i;
		int length=n.length;
		int total = 0;
		for (i=0;i<length;i++) {
			total+= n[i];
			
		}
		total /= length;
		return total;

	}

	public static int sum(int [] n)

	{
		int i;
		int length=n.length;
		int total = 0;
		for (i=0;i<length;i++) {
			total+= n[i];
			
		}
	return total;

	}

	public static void main(String[] args) {
		Scanner scnr =new Scanner(System.in);
		Random rand= new Random();
		int i;
		int [] numbers = new int[20];
		for (i=0; i<20;i++) 
		{
			numbers[i]=rand.nextInt(401) + 100;
		}
		System.out.println(Arrays.toString(numbers));
		
		double ave = ave(numbers);

		int max = max(numbers);

		int min = min(numbers);

		int sum = sum(numbers);

		System.out.println("Print the list of numbers here");

		System.out.println("Ave:"+ ave);

		System.out.println("Max:"+ max);

		System.out.println("Min:"+ min);

		System.out.println("Sum:"+ sum);

	}

	}