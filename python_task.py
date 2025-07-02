
"""
## 📝Python Developer - Task 1

Submitted by:  REKHA SHEORAN  
Platform: Google Colab  
Institute: Main Flow Services and Technologies Pvt. Ltd.

---

### 📌 Project Overview

This notebook contains Python solutions for the following problems:

1. Sum of Two Numbers  
2. Odd or Even Checker  
3. Factorial Calculation  
4. Fibonacci Sequence Generator  
5. Reverse a String  
6. Palindrome Check  
7. Leap Year Checker  
8. Armstrong Number Checker  
9. Custom Encryption-Decryption System

Each task includes its Objective, Approach, Challenges, and Output in the respective section.

---

##  🔷 Task 1: Sum of Two Number

Objective: Calculate and return the sum of two integers.

Approach:  
- Get input from the user using input()
- Convert inputs to integers
- Add them using the + operator

Challenges:  
Handled input conversion properly to avoid string concatenation.

Example Output:
"""

# Task 1: Sum of Two Numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Sum:", num1 + num2)

"""
## 🔷 Task 2: Odd or Even

Objective:  
Determine if an integer is odd or even.

Approach:  
- Use the modulus operator %
- If number % 2 == 0, it is even; otherwise, it's odd

Key Challenges:  
- None significant. Straightforward condition.

Example Output:  

"""

# Task 2: Odd or Even
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

"""## 🔷 Task 3: Factorial Calculation

Objective:  
Calculate the factorial of a number.

Approach:  
- Use math.factorial() for simplicity  
- Or implement a loop

Key Challenges:  
- May forget to import the math module
- Input must be a non-negative integer

Example Output:  

"""

# Task 3: Factorial Calculation
import math

n = int(input("Enter a number: "))
if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"Factorial of {n} is {math.factorial(n)}")

"""
## 🔷 Task 4: Fibonacci Sequence

Objective:  
Generate the first n Fibonacci numbers.

Approach:  
- Start with a list [0, 1]
- Use a loop to add the sum of the last two numbers to the list
- Repeat until you reach n terms

Key Challenges:  
- Ensuring the list doesn’t go beyond n numbers


Example Output:  


"""

# Task 4: Fibonacci Sequence
n = int(input("Enter the number of terms: "))
fib = [0, 1]

for i in range(2, n):
    fib.append(fib[i-1] + fib[i-2])

print("Fibonacci Sequence:", fib[:n])

"""## 🔷 Task 5: Reverse a String
Objective:  
Reverse a given string.

Approach:  
- Use Python’s slicing feature [::-1] to reverse the string

Key Challenges:  
- None significant. Python slicing is simple and direct


Example Output:  
"""

# Task 5: Reverse a String
text = input("Enter a string: ")
print("Reversed string:", text[::-1])

"""
## 🔷 Task 6: Palindrome Check

Objective:  
Check whether a string reads the same forwards and backwards.

Approach:  
- Compare the string to its reverse using ==

Key Challenges:  
- Ignoring case sensitivity or spaces can affect the result

Example Output:  """

# Task 6: Palindrome Check
word = input("Enter a word: ")
cleaned = word.replace(" ", "").lower()

if cleaned == cleaned[::-1]:
    print("True – It's a palindrome")
else:
    print("False – Not a palindrome")

"""



## 🔷 Task 7: Leap Year Check

Objective:  
Determine whether a year is a leap year.

Approach:  
- Divisible by 4 and (not 100 unless also 400)

Key Challenges:  
 Logic can be confusing with AND/OR conditions

Example Output:  """

#Task 7: Leap Year Check
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("True – It's a leap year")
else:
    print("False – Not a leap year")

"""

## 🔷 Task 8: Armstrong Number

Objective:  
Check if number equals sum of its digits raised to the power of total digits.

Approach:  
- Convert number to string to count digits  
- Raise each digit to the power and sum them

Key Challenges:  
Must convert between str and int types frequently

Example Output:  


"""

# Task 8: Armstrong Number
num = int(input("Enter a number: "))
power = len(str(num))
total = sum(int(digit) ** power for digit in str(num))

if total == num:
    print("True – It's an Armstrong number")
else:
    print("False – Not an Armstrong number")

"""## 🔷 Task 9: Custom Encryption-Decryption (Caesar Cipher)

Objective:  
Encrypt and decrypt a message using Caesar Cipher.

Approach:  
- Shift characters by a fixed value (e.g., 3)  
- Use ord() and chr() to shift ASCII values  
- Only shift alphabetic characters

Key Challenges:  
- Wrapping around Z→A  
- Keeping upper/lowercase intact  
- Ignoring non-alphabetic characters

"""

# Caesar Cipher Encryption Function
def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if 'a' <= char <= 'z':
            encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        elif 'A' <= char <= 'Z':
            encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            encrypted_text += char  # Keep spaces, digits, symbols unchanged
    return encrypted_text

# Caesar Cipher Decryption Function
def caesar_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if 'a' <= char <= 'z':
            decrypted_text += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        elif 'A' <= char <= 'Z':
            decrypted_text += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        else:
            decrypted_text += char
    return decrypted_text

# Main Program
def main():
    print("=== Custom Caesar Cipher Encryption ===")
    message = input("Enter your message: ")
    shift = int(input("Enter shift value (e.g., 3): "))

    encrypted = caesar_encrypt(message, shift)
    print("Encrypted Message:", encrypted)

    decrypted = caesar_decrypt(encrypted, shift)
    print("Decrypted Message:", decrypted)

# Run the program
if __name__ == "__main__":
    main()