package com.example.calculator;

import static org.junit.Assert.assertEquals;

import com.example.calculator.testmethodset.CalculationFunction;
import org.junit.Test;

/**
 * Unit test for simple App.
 */
public class AppTest 
{
    /**
     * Rigorous Test :-)
     */
    @Test
    public void addTwoPositiveNumber()
    {
        float addResult = CalculationFunction.add(1, 2);
        assertEquals(addResult, 3,0.1);
    }

    @Test
    public void addPositiveAndNegativeNumber()
    {
        float addResult = CalculationFunction.add(1, -2);
        assertEquals(addResult, -1,0.1);
    }

    @Test
    public void addTwoNegativeNumber()
    {
        float addResult = CalculationFunction.add(-1, -2);
        assertEquals(addResult, -3,0.1);
    }

    @Test
    public void subtractTwoPositiveNumber()
    {
        float subtractResult = CalculationFunction.subtract(1, 2);
        assertEquals(subtractResult, -1,0.1);
    }

    @Test
    public void subtractPositiveAndNegativeNumber()
    {
        float subtractResult = CalculationFunction.subtract(1, -2);
        assertEquals(subtractResult, 3,0.1);
    }

    @Test
    public void subtractTwoNegativeNumber()
    {
        float subtractResult = CalculationFunction.subtract(-1, -2);
        assertEquals(subtractResult, 1,0.1);
    }

    @Test
    public void multiplyTwoPositiveNumber()
    {
        float multiplyResult = CalculationFunction.multiply(1, 2);
        assertEquals(multiplyResult, 2,0.1);
    }

    @Test
    public void multiplyPositiveAndNegativeNumber()
    {
        float multiplyResult = CalculationFunction.multiply(1, -2);
        assertEquals(multiplyResult, -2,0.1);
    }

    @Test
    public void multiplyTwoNegativeNumber()
    {
        float multiplyResult = CalculationFunction.multiply(-1, -2);
        assertEquals(multiplyResult, 2,0.1);
    }

    @Test
    public void divideTwoPositiveNumber()
    {
        float divideResult = CalculationFunction.divide(1, 2);
        assertEquals(divideResult, 0.5F,0.1);
    }

    @Test
    public void dividePositiveAndNegativeNumber()
    {
        float divideResult = CalculationFunction.divide(1, -2);
        assertEquals(divideResult, -0.5F,0.1);
    }

    @Test
    public void divideTwoNegativeNumber()
    {
        float divideResult = CalculationFunction.divide(-1, -2);
        assertEquals(divideResult, 0.5F,0.1);
    }
}
