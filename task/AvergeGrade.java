/*import Scanner 
collect three input from user
using if else statement 
input the numerical score range 
print the grade after each if statement 
add the three number together then divid by three
print the average of the score.*/


import java.util.Scanner;

	public class AvergeGrade{
	public static void main(String[] args){

Scanner input = new Scanner(System.in);

System.out.print("Enter Score1");
int Score1 = input.nextInt(); 

System.out.print("Enter Score2");
int Score2 = input.nextInt();

System.out.print("Enter Score3");
int Score3 = input.nextInt();

int Score= (Score1 + Score2 + Score3) / 3;

System.out.print(+ Score);

if(Score >= 90 && Score <= 100){
System.out.print("A");
}
	else if (Score > 80 && Score < 90){
	System.out.print("B");
}
	else if (Score > 70 && Score < 80){
	System.out.print("C");
}
	else if (Score > 60 && Score < 70){
	System.out.print("D");
}
	else{
	System.out.print("F");
}

	}

}
