package com.example.todo;

import static org.junit.Assert.assertTrue;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import org.junit.Test;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

/**
 * Unit test for simple App.
 */
public class AppTest {
    /**
     * Rigorous Test :-)
     */
    @Test
    public void shouldAnswerWithTrue() {
        assertTrue(true);
    }

    private final ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
    private final ByteArrayInputStream inputStream = new ByteArrayInputStream("5\n".getBytes()); // Simulate user input
                                                                                                 // for exiting the
                                                                                                 // program

    @BeforeEach
    public void setUp() {
        System.setOut(new PrintStream(outputStream));
        System.setIn(inputStream);
    }

    @Test
    public void testAddTask() {
        Todo.main(new String[] {});
        String input = "1\nTest Task\n5\n";
        System.setIn(new ByteArrayInputStream(input.getBytes()));

        Todo.main(new String[] {});
        String consoleOutput = outputStream.toString();

        assertTrue(consoleOutput.contains("Task added with ID: 1"));
    }

    @Test
    public void testEditTask() {
        Todo.main(new String[] {});
        String input = "1\nTest Task\n2\n1\nNew Task\n5\n";
        System.setIn(new ByteArrayInputStream(input.getBytes()));

        Todo.main(new String[] {});
        String consoleOutput = outputStream.toString();

        assertTrue(consoleOutput.contains("Data Updated."));
    }

    @Test
    public void testRemoveTask() {
        Todo.main(new String[] {});
        String input = "1\nTest Task\n3\n1\n5\n";
        System.setIn(new ByteArrayInputStream(input.getBytes()));

        Todo.main(new String[] {});
        String consoleOutput = outputStream.toString();

        assertTrue(consoleOutput.contains("Task removed."));
    }

    @Test
    public void testListTasks() {
        Todo.main(new String[] {});
        String input = "4\n5\n";
        System.setIn(new ByteArrayInputStream(input.getBytes()));

        Todo.main(new String[] {});
        String consoleOutput = outputStream.toString();

        assertTrue(consoleOutput.contains("No Task Added Yet"));
    }

    @Test
    public void testExitProgram() {
        Todo.main(new String[] {});
        String input = "5\n";
        System.setIn(new ByteArrayInputStream(input.getBytes()));

        Todo.main(new String[] {});
        String consoleOutput = outputStream.toString();

        assertTrue(consoleOutput.contains("Exiting..."));
    }

    @Test
    public void testInvalidChoice() {
        Todo.main(new String[] {});
        String input = "6\n5\n";
        System.setIn(new ByteArrayInputStream(input.getBytes()));

        Todo.main(new String[] {});
        String consoleOutput = outputStream.toString();

        assertTrue(consoleOutput.contains("Invalid choice. Please try again."));
    }

    @Test
    public void testEditTaskInvalidId() {
        Todo.main(new String[] {});
        String input = "2\n0\n5\n";
        System.setIn(new ByteArrayInputStream(input.getBytes()));

        Todo.main(new String[] {});
        String consoleOutput = outputStream.toString();

        assertTrue(consoleOutput.contains("No task found with that ID."));
    }

    @Test
    public void testEditTaskInvalidChoice() {
        Todo.main(new String[] {});
        String input = "2\n1\n3\n5\n";
        System.setIn(new ByteArrayInputStream(input.getBytes()));

        Todo.main(new String[] {});
        String consoleOutput = outputStream.toString();

        assertTrue(consoleOutput.contains("Invalid choice. Please try again."));
    }

    @Test
    public void testEditTaskStatusInvalidChoice() {
        Todo.main(new String[] {});
        String input = "2\n1\n2\n3\n5\n";
        System.setIn(new ByteArrayInputStream(input.getBytes()));

        Todo.main(new String[] {});
        String consoleOutput = outputStream.toString();

        assertTrue(consoleOutput.contains("Invalid choice. Please try again."));
    }

    @Test
    public void testRemoveTaskInvalidId() {
        Todo.main(new String[] {});
        String input = "3\n0\n5\n";
        System.setIn(new ByteArrayInputStream(input.getBytes()));

        Todo.main(new String[] {});
        String consoleOutput = outputStream.toString();

        assertTrue(consoleOutput.contains("No task found with that ID."));
    }

    @Test
    public void testAddDataToCSV() {
        // This test does not simulate user input but checks if the data is saved to CSV
        // successfully.
        Todo.addDataToCSV();
        // You may need to implement a method to read data from the CSV file and check
        // if it matches the expected data.
        // assertEquals(expectedData, actualData);
    }
}
