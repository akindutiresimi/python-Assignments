/*using scanner to collect input of father age
collect soon age too
multiply the sons age by two
subtract the father age from the son multiply age
print th age*/


import java.util.Scanner;

public class FathersAge{
public static void main(String[] args){

Scanner input = new Scanner(System.in);

System.out.print("Enter father age");
int father = input.nextInt();

System.out.print("Enter son age");
int son = input.nextInt();

int fatherOldAge = father - (son * 2);

if (fatherOldAge < 0){
System.out.print("Invalid");
}
else{
System.out.println("fatherOldAge:"+ fatherOldAge);
}
}


}