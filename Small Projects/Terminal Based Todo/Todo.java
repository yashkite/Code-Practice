import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class Todo {

    private static HashMap<Integer, String> tasks = new HashMap<>();
    private static int taskId = 1;

    public static void main(String[] args) {
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
                    break;
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        } while (choice != 4);
    }

    private static void addTask(Scanner scanner) {
        System.out.println("---------------------**---------------------");
        System.out.println("Enter task description: ");
        scanner.nextLine();
        String task = scanner.nextLine();
        tasks.put(taskId, task);
        System.out.println("---------------------**---------------------");
        System.out.println("Task added with ID: " + taskId);
        System.out.println("---------------------**---------------------");
        taskId++;

    }

    private static void removeTask(Scanner scanner) {
        System.out.print("Enter task ID: ");
        int id = scanner.nextInt();
        if (tasks.containsKey(id)) {
            tasks.remove(id);
            System.out.println("Task removed.");
        } else {
            System.out.println("No task found with that ID.");
        }
    }

    private static void listTasks() {
        // if no task in list print No Task Added Yet
        if (tasks.isEmpty()) {
            System.out.println("---------------------**---------------------");
            System.out.println("No Task Added Yet");
            System.out.println("---------------------**---------------------");
        }

        else {
            System.out.println("---------------------**---------------------");

            System.out.println("Tasks:");
            for (int id : tasks.keySet()) {
                System.out.println(id + ". " + tasks.get(id));
            }
            System.out.println("---------------------**---------------------");

        }
    }

}
