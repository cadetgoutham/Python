"""
Indian Denomination Monetary Calculator (Method Chaining)

Description:
    A self-contained utility class that implements a fluent interface 
    (method chaining) to accumulate monetary values across standard 
    Indian numbering system denominations.

Output Preview:
    Total amount: 3000350.0

How It Works:
    Each denomination method performs an in-place addition to an internal 
    accumulator and returns 'self' (the class instance). This allows subsequent 
    methods to be called sequentially in a single line. The chain is resolved 
    by calling '.get_value()'.

How to Run:
    $ python monetary_calculator.py
"""

class MonetaryCalculator:
    def __init__(self):
        """Initializes the running currency accumulator to zero."""
        self._total_balance = 0.0

    def hundreds(self, scale_value):
        """Adds values in hundreds ($10^2$)."""
        self._total_balance += (scale_value * (10**2))
        return self

    def thousands(self, scale_value):
        """Adds values in thousands ($10^3$)."""
        self._total_balance += (scale_value * (10**3))
        return self

    def lakhs(self, scale_value):
        """Adds values in lakhs ($10^5$)."""
        self._total_balance += (scale_value * (10**5))
        return self

    def crores(self, scale_value):
        """Adds values in crores ($10^7$)."""
        self._total_balance += (scale_value * (10**7))
        return self

    def get_value(self):
        """Returns the final accumulated total value."""
        return self._total_balance


def main():
    # Instantiate the chaining calculator
    account = MonetaryCalculator()

    # Process: 10 lakhs + 0.2 crores + 3.5 hundreds
    # Calculation: (10 * 100,000) + (0.2 * 10,000,000) + (3.5 * 100)
    final_amount = account.lakhs(10).crores(0.2).hundreds(3.5).get_value()
    
    print("Total amount:", final_amount)


if __name__ == "__main__":
    main()