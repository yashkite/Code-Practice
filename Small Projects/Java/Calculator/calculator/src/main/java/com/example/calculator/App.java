package com.example.calculator;

import java.util.Scanner;

public class App {
    public static void main(String[] args) {
        int choice;
        float num1;
        float num2;
        do {
            Scanner scanner = new Scanner(System.in);

            System.out.println("-------**-------");
            System.out.println("1. Addition");
            System.out.println("2. Subtraction"); // Changed to "Subtraction"
            System.out.println("3. Multiplication");
            System.out.println("4. Division");
            System.out.println("5. Exit");
            System.out.println("-------**-------");

            System.out.println("Enter a Choice: ");
            choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    num1 = getNumber1(scanner);
                    num2 = getNumber2(scanner);
                    add(num1, num2);
                    break;
                case 2:
                    num1 = getNumber1(scanner);
                    num2 = getNumber2(scanner);
                    substract(num1, num2);
                    break;
                case 3:
                    num1 = getNumber1(scanner);
                    num2 = getNumber2(scanner);
                    multiply(num1, num2);
                    break;
                case 4:
                    num1 = getNumber1(scanner);
                    num2 = getNumber2(scanner);
                    divide(num1, num2);
                    break;
                case 5:
                    break;
                default:
                    System.out.println("-------**-------");

                    System.out.println("Enter a Valid Number");

                    break;

            }
        } while (choice != 5);
    }

    private static float getNumber1(Scanner scanner) {
        System.out.println("-------**-------");
        System.out.print("Enter a First Number: ");
        return scanner.nextFloat();

    }

    private static float getNumber2(Scanner scanner) {
        System.out.println("-------**-------");
        System.out.print("Enter a Second Number: ");
        return scanner.nextFloat();

    }

    private static void divide(float num1, float num2) {
        System.out.println("-------**-------");
        System.out.println(num1 + " / " + num2 + " = " + (num1 / num2));
        System.out.println("-------**-------");
    }

    private static void multiply(float num1, float num2) {
        System.out.println("-------**-------");
        System.out.println(num1 + " * " + num2 + " = " + (num1 * num2));
        System.out.println("-------**-------");
    }

    private static void substract(float num1, float num2) {
        System.out.println("-------**-------");
        System.out.println(num1 + " - " + num2 + " = " + (num1 - num2));
        System.out.println("-------**-------");
    }

    private static void add(float num1, float num2) {
        System.out.println("-------**-------");
        System.out.println(num1 + " + " + num2 + " = " + (num1 + num2));
        System.out.println("-------**-------");
    }
}
