---

# Basic Calculator in C

Welcome to the Basic Calculator in C repository! This project provides a simple yet effective console-based calculator program implemented in the C programming language. Whether you're a beginner seeking to understand the foundational aspects of C or someone in need of a lightweight calculator tool, this project is designed to be a helpful resource.

## Purpose and Scope

The primary purpose of this project is to offer a hands-on experience for individuals looking to explore C programming or enhance their understanding of basic arithmetic operations. The calculator supports fundamental operations such as addition, subtraction, multiplication, and division. Its simplicity makes it an excellent starting point for learning the basics of C while also serving as a practical tool for quick calculations.

## Getting Started

Running the calculator is a straightforward process. Follow these steps to get started:

1. Ensure that you have a C compiler installed on your system.
2. Copy the provided C code into a new file, for example, `calculator.c`.
3. Open a terminal or command prompt and navigate to the directory containing the file.
4. Compile the code using the following command:

    ```bash
    gcc calculator.c -o calculator
    ```

5. Run the compiled executable:

    ```bash
    ./calculator
    ```

## Code Structure

The calculator program is organized with a modular structure, consisting of several functions for arithmetic operations and a main function to facilitate user interaction.

### Arithmetic Functions

1. **addDigits(int num1, int num2):**
   - Adds two integer numbers and returns the result.

2. **subDigits(int num1, int num2):**
   - Subtracts the second integer from the first and returns the result.

3. **mulDigits(int num1, int num2):**
   - Multiplies two integer numbers and returns the product.

4. **divDigits(int num1, int num2):**
   - Divides the first integer by the second and returns the quotient.

These functions are designed for simplicity and clarity, making them suitable for educational purposes.

### Main Function

The `main` function acts as the entry point for the program. It guides the user through the process of inputting two numbers and selecting an operator. The program then uses a switch statement to perform the corresponding arithmetic operation and displays the result.

## Educational Value

This project is an excellent educational resource for several reasons. First and foremost, it provides a hands-on experience with C programming, allowing individuals to practice writing and understanding C code. The simplicity of the calculator's design makes it accessible for beginners, while the modular structure encourages exploration and modification.

Furthermore, the use of functions for arithmetic operations introduces the concept of modular programming, emphasizing code reuse and maintainability. Students and learners can easily grasp how different components of the program work together to achieve a specific task.

## Example Usage

Let's walk through a detailed example of using the calculator to add two numbers, 5 and 3:

1. Run the compiled executable (`./calculator`).
2. Input the first number when prompted: `Num1 = 5`
3. Input the second number when prompted: `Num2 = 3`
4. Specify the operator for addition: `Operator = +`
5. The program will display the equation: `Given Equation: 5 + 3`
6. The result will be presented: `Answer of "5 + 3 = 8"`

Feel free to explore additional use cases, such as subtraction, multiplication, and division, to gain a comprehensive understanding of the calculator's capabilities.

## Conclusion

In conclusion, the Basic Calculator in C project offers a valuable learning experience for those interested in C programming and basic arithmetic operations. It combines simplicity with educational depth, making it suitable for both beginners and those looking to reinforce their programming skills. Whether you're using it for educational purposes or practical calculations, we hope this project adds value to your programming journey.

