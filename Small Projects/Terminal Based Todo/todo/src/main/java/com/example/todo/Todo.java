package com.example.todo;

import java.io.File;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;

import com.opencsv.CSVReader;
import com.opencsv.CSVWriter;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.List;

public class Todo {

    static File databasePath = new File("todo\\src\\database\\database.csv");
    static List<String[]> data = new ArrayList<String[]>();

    private static int taskId = 1;

    public static void main(String[] args) {
        // check the file is exist at the file location
        if (databasePath.exists()) {
            readData();
        } else {
            data.add(new String[] { "ID", "Task", "Status" });
        }

        Scanner scanner = new Scanner(System.in);
        int choice;

        do {

            System.out.println("1. Add task");
            System.out.println("2. Remove task");
            System.out.println("3. List tasks");
            System.out.println("4. Exit");
            System.out.print("Enter your choice: ");
            choice = scanner.nextInt();
            switch (choice) {
                case 1:
                    addTask(scanner);

                    break;
                case 2:
                    removeTask(scanner);
                    break;
                case 3:
                    listTasks();
                    break;
                case 4:
                    System.out.println("Exiting...");
                    addDataToCSV();
                    break;
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        } while (choice != 4);
    }

    private static void readData() {
        try {

            // Create an object of filereader
            // class with CSV file as a parameter.
            FileReader filereader = new FileReader(databasePath);

            // create csvReader object passing
            // file reader as a parameter
            CSVReader csvReader = new CSVReader(filereader);
            String[] nextRecord;

            // we are going to read data line by line
            while ((nextRecord = csvReader.readNext()) != null) {
                data.add(nextRecord);

            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void addTask(Scanner scanner) {
        System.out.println("---------------------**---------------------");
        System.out.println("Enter task description: ");
        scanner.nextLine();
        String task = scanner.nextLine();
        System.out.println("---------------------**---------------------");
        System.out.println("Task added with ID: " + taskId);
        System.out.println("---------------------**---------------------");

        data.add(new String[] { String.valueOf(taskId), task, "Open" });

        taskId++;

    }

    private static void addDataToCSV() {

        try {

            FileWriter outputfile = new FileWriter(databasePath);

            CSVWriter writer = new CSVWriter(outputfile);

            writer.writeAll(data);

            // closing writer connection
            writer.close();

        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }

    }

    private static void removeTask(Scanner scanner) {
        System.out.print("Enter task ID: ");
        int id = scanner.nextInt();
        if (id >= 1) {
            for (int i = 1; i < data.size(); i++) {

                String[] temp = data.get(i);

                if (Integer.parseInt(temp[0]) == id) {
                    data.remove(i);
                    System.out.println("---------------------**---------------------");
                    System.out.println("Task removed.");
                    System.out.println("---------------------**---------------------");

                } else {

                    System.out.println("---------------------**---------------------");
                    System.out.println("No task found with that ID.");
                    System.out.println("---------------------**---------------------");
                }

            }
        } else {

            System.out.println("---------------------**---------------------");
            System.out.println("No task found with that ID.");
            System.out.println("---------------------**---------------------");
        }

    }

    private static void listTasks() {
        // if no task in list print No Task Added Yet
        if (data.size() < 2) {
            System.out.println("---------------------**---------------------");
            System.out.println("No Task Added Yet");
            System.out.println("---------------------**---------------------");
        }

        else {
            System.out.println("---------------------**---------------------");

            System.out.println("Tasks:");
            for (int i = 0; i < data.size(); i++) {

                String[] temp = data.get(i);
                System.out.printf("%s. %s - %s\n", temp[0], temp[1], temp[2]);

            }

            System.out.println("---------------------**---------------------");

        }
    }

}
