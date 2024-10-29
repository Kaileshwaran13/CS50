---

# String Calculator

This project introduces a versatile string calculator, offering a user-friendly interface for basic arithmetic operations using string inputs. Emphasizing simplicity and adaptability, this calculator enables users to perform calculations seamlessly through expressive string-based expressions. The supported arithmetic operations include:

- Addition (Add)
- Subtraction (Sub)
- Multiplication (Mul)
- Division (Div)

To enhance precision and accommodate decimal values in calculations, input strings are intelligently converted into float-based variables.

## Usage

Navigating the calculator is intuitive. Input strings using the following format:

```python
calculator.calculate("num1 operation num2")
```

Replace "num1" and "num2" with the numerical values for the desired operation, and "operation" with one of the supported operations.

Example:

```python
result = calculator.calculate("5.2 + 3.8")
print(result)  # Output: 9.0
```

Experiment with various numerical inputs and operations to unlock the calculator's potential for a wide range of calculations.

## Testing

Ensuring the calculator's accuracy and reliability is a top priority. The test suite covers a spectrum of scenarios:

- **Addition Test (AddTest):** Rigorously verifies the correct functionality of addition operations.
- **Subtraction Test (SubTest):** Assures accurate results for subtraction operations.
- **Multiplication Test (MulTest):** Validates the correctness of multiplication operations.
- **Division Test (DivTest):** Confirms the reliability of division operations.

This comprehensive testing approach instills confidence in users regarding the calculator's consistent and accurate performance. Users can rely on these tests for validation, ensuring that the string calculator consistently meets their expectations.

## Customization

For users seeking additional functionality or customization, the calculator's modular design allows for easy expansion. Users can explore extending the calculator's capabilities to suit specific needs or integrate it into more extensive projects. The codebase is open for modifications, encouraging users to tailor the string calculator to their unique requirements.
