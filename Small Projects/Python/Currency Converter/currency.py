# Currency Converter
import forex_python.converter as CurrencyRates

"""
    This program is designed to be used as a module, meaning that you can import this program in any other program then use it. However, it doesn't means that you cannot modify this code, you can modify this code however you want.

    How does it work?
    We are using the forex-python modules to get the exchange rates.

    Then we created a class method named convert which takes in 3 parameters - inCurr, outCurr, values. The values parameter defaults to None, to prevent any errror if user forgets to enter a value to convert

    After that, it's pretty much smooth sailing!
"""

class Main:
    
    @classmethod
    def convert(cls, inCurr, outCurr, values:float = None): # type: ignore
        """
    Convert currency from one unit to another.

    Parameters:
        in_curr (str): The currency code of the input currency.
        out_curr (str): The currency code of the desired output currency.
        values (float, optional): The amount to be converted. If not provided, the user will be prompted to enter it.

    Returns:
        str: A formatted string representing the converted currency value.

    Raises:
        ValueError: If either input or output currency codes are empty.
        ValueError: If the exchange rates are not available for the specified currencies.

    Example:
        To convert 100 USD to EUR:
        >>> CurrencyConverter.convert('USD', 'EUR', 100)
        '100.0 USD is 87.0 EUR'
        """

        if inCurr == "" or outCurr == "":
            return "Please provide some values."
        else: pass

        try:
            rates = CurrencyRates.get_rate(inCurr, outCurr)
        except CurrencyRates.RatesNotAvailableError as e:
            print(f"Error: {e}")
            return "Please make sure that the currencies are right."
        
        if values is None:
            values = float(input(f"Enter amount in {inCurr}: "))
        else:
            pass

        return (f"{values} {inCurr} is {round(rates * values, 2)} {outCurr}") # type: ignore