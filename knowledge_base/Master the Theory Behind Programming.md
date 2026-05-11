# Binary number system

https://www.mathsisfun.com/binary-number-system.html

https://www.sqa.org.uk/e-learning/NetTechDC01ACD/page_11.htm

https://www.youtube.com/watch?v=cZH0YnFpjwU

a base-2 numeral system that uses only two digits, 0 and 1, to represent all numerical values.

the binary system relies on powers of 2

> he binary system is commonly used in digital systems, including computers, where the binary digits are employed to represent data and perform operations.
>
> Computers at their most basic level use electricity to operate. Electricity only has two reliable states, on(1) and off(0).

> Deca ( Decimal System ): decimal system (base-10) uses 10 digits (0-9)

> Hexa ( Hexadecimal Number System ):  base-16 numeral system that uses sixteen symbols (the digits 0-9 and the letters A-F)  to represent values where A stands for 10, B for 11, C for 12, D for 13, E for 14, and F for 15 in decimal.  
>
> **where and why use** 
>
> - Programmers often use hexadecimal notation to represent binary data more concisely, and it's commonly employed in programming languages and debugging. When debugging programs or analyzing memory dumps, hexadecimal is frequently used to represent memory content. It allows programmers and analysts to examine memory values in a more readable and manageable format.
> - memory addresses are often expressed in hexadecimal. This is because memory addresses are usually based on powers of 2, and hexadecimal aligns well with these powers.
> - Hexadecimal is commonly used in web development and graphic design to represent colors. In this context, hexadecimal values are used to define the RGB (Red, Green, Blue) color model. Each of the three color components is represented by two hexadecimal digits, allowing for a wide range of color possibilities.
> - character encoding standards like ASCII and Unicode often represent characters using hexadecimal values.
> - In low-level programming languages like assembly, machine language instructions are often represented in hexadecimal. Each instruction corresponds to a specific operation code, and using hexadecimal makes it more manageable than binary.
> - Hexadecimal is used in various file formats to represent data structures, headers, and other information. For example, hexadecimal is often used to display and analyze the content of binary files.

> Octa: 八进制是一种基数为8的数字系统，使用数字0到7来表示数值( 0、1、2、3、4、5、6、7 ) 。 每一位的权重都是基数（8）的幂。从右到左，第一位的权重是8^0，第二位是8^1，第三位是8^2，以此类推。 
>
> 一个八进制数字的每一位对应于三个二进制位。这是因为 23=823=8。因此，八进制到二进制的转换相对容易。 
>
> 八进制数字通常以前缀“0o”或“0”开头，以表示这是一个八进制数。例如，八进制数57可以写作0o71，其中7是8^0位上的数字，1是8^1位上的数字。  
>
> 八进制仍然偶尔用于表示一些特殊的二进制模式或权限标志。在某些编程语言中，你可能会看到八进制常量 
>
> **where and why use** 
>
> - In the early days of computing, especially in the 1960s and 1970s, octal was frequently used to represent binary-coded information.
> - some digital systems and hardware still use octal representation for certain configurations, especially in the context of field-programmable gate arrays (FPGAs) or digital signal processing (DSP).
> - In Unix-based systems, octal notation is often used to represent file permissions. Each digit in the octal number corresponds to a set of permission bits (read, write, execute) for the owner, group, and others.
> - In networking, octets (8-bit groups) are commonly used, especially in the context of IPv4 addresses. Each octet is often represented in decimal or octal.
> - Octal representation might still be encountered in some low-level programming or debugging situations, particularly when examining memory dumps or specific hardware configurations.





## bit

**Each digit in a binary number** is called a **bit** (short for binary digit).

two digits, 0 and 1



## denotation

the rightmost bit represents 2^0 (1), the next bit to the left represents 2^1 (2), the next one 2^2 (4), and so on.

The position of each bit corresponds to a power of 2

> Binary: 1101
>
> Decimal: (1 * 2^3) + (1 * 2^2) + (0 * 2^1) + (1 * 2^0) = 8 + 4 + 0 + 1 = 13
>
> the binary number 1101 is equivalent to the decimal number 13.



## relationship with Transistors

### what is transistor?

Transistors are electronic devices that can act as switches.

They have two possible states: ON or OFF. This binary nature (1 or 0) of transistors corresponds directly to the binary number system.

> The binary nature of transistors allows them to efficiently represent and manipulate binary data, making them a cornerstone of modern computing systems.

### what transistor can do?

#### digital circuits

Transistors are the building blocks of **digital circuits**. They are arranged in logical configurations to perform operations based on **binary logic**.

> a group of transistors can be configured to implement AND, OR, or NOT operations, which are the basic building blocks of digital circuits.

#### memory cells

Transistors are used in memory cells to store binary data.

> In dynamic random-access memory (DRAM), for instance, each memory cell typically consists of a transistor and a capacitor, representing the binary states of 0 or 1 based on the presence or absence of charge.

#### CPU

Transistors are extensively used in the design of central processing units (CPUs). 

> Arithmetic and logical operations performed by the CPU, such as addition, subtraction, multiplication, and comparison, are based on binary representations.
>
>  A CPU processor has millions of these little switches all working in  unison 协同工作 , combining and reorganizing the 1’s and 0’s to perform  operations.    

#### Machine Language

Transistors in the CPU execute these instructions (a CPU understands) by manipulating binary data, performing computations, and controlling other parts of the system.

#### Storage Devices

Transistors are used in various storage devices such as solid-state drives (SSDs). 

> The binary nature of transistors is essential for encoding and retrieving data stored in these devices.





## Conversion

### Binary and Decimal conversion

#### Binary to Decimal

1. Write down the binary number, starting from the rightmost bit.
2. Starting from the rightmost bit, assign powers of 2 to each bit, with the rightmost bit having a power of 2^0, the next bit 2^1, and so on.
3. Multiply each bit by its corresponding power of 2 and sum the results. The sum is the decimal equivalent.

> Example: Convert 1101 (binary) to decimal:
>
> 1 * 2^3 + 1 * 2^2 + 0 * 2^1 + 1 * 2^0
> = 8 + 4 + 0 + 1
> = 13 (decimal)



#### Decimal to Binary

1. Divide the decimal number by 2 and record the remainder. The remainder is the least significant bit (LSB) 最低有效位 .
2. Continue dividing the quotient obtained in the previous step by 2 until the quotient is 0. Record each remainder.
3. Write the binary equivalent by arranging the remainders in reverse order. The result is the binary representation of the original decimal number.

> Example: Convert 13 (decimal) to binary:
>
> 13 ÷ 2 = 6, remainder 1 (LSB)
> 6 ÷ 2 = 3, remainder 0
> 3 ÷ 2 = 1, remainder 1 (MSB)
> 1 ÷ 2 = 0, remainder 1
>
> the binary representation of 13 is 1101.



###  Binary and Hexa conversion 

grouping binary digits into sets of four (since 2^4 = 16) and then converting each set to its hexadecimal equivalent.

#### Binary to Hexadecimal

1. Start from the rightmost bit of the binary number and group the bits into sets of four.[不足四位的在前面用0补全] If the leftmost group has fewer than four bits, pad it with leading zeros. 

2. Convert each group of four bits to its hexadecimal equivalent. Use the following table for reference: 

3. | binary | 0000 | 0001 | 0010 | 0011 | 0100 | 0101 | 0110 | 0111 | 1000 | 1001 | 1010 | 1011 | 1100 | 1101 | 1110 | 1111 |
   | ------ | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
   | Hexa   | 0    | 1    | 2    | 3    | 4    | 5    | 6    | 7    | 8    | 9    | A    | B    | C    | D    | E    | F    |

4. Concatenate the hexadecimal equivalents of each group from right to left. The result is the hexadecimal representation of the original binary number. 

> Example: Convert 1101 1010 1011 (binary) to hexadecimal: 
>
> | Grouped | 1101 | 1010 | 1011 |
> | ------- | ---- | ---- | ---- |
> | Hexa    | D    | A    | B    |
>
> the hexadecimal representation of 110110101011 is DAB.                  



#### Hexadecimal to Binary

1. Convert each hexadecimal digit to its binary equivalent using the reverse of the table mentioned above. 
2. Concatenate the binary equivalents of each hexadecimal digit. The result is the binary representation of the original hexadecimal number.

> Example: Convert ABC (hexadecimal) to binary:
>
> | Hexa   | A    | B    | C    |
> | ------ | ---- | ---- | ---- |
> | Binary | 1010 | 1011 | 1100 |
>
> the binary representation of ABC is 1010 1011 1100. 



### Binary and Octal conversation

grouping binary digits into sets of three (since 2^3=8) and then converting each group to its octal equivalent. 

#### Binary to Octal Conversion

1. Start from the rightmost bit of the binary number and group the bits into sets of three. If the leftmost group has fewer than three bits, pad it with leading zeros

2. Convert each group of three bits to its octal equivalent. Use the following table for reference:

3. | Binary | 000  | 001  | 010  | 011  | 100  | 101  | 110  | 111  |
   | ------ | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
   | Octal  | 0    | 1    | 2    | 3    | 4    | 5    | 6    | 7    |

4. Concatenate the octal equivalents of each group from right to left. The result is the octal representation of the original binary number.

> Example: Convert 101 101 010 111 (binary) to octal:
>
> ```
> Grouped:   101  101  010  111
> Octal:     5    5    2    7
> ```
>
>  the octal representation of 101101010111 is 5527. 



#### Octal to Binary Conversion

Convert each octal digit to its binary equivalent using the reverse of the table mentioned above.

Concatenate the binary equivalents of each octal digit. The result is the binary representation of the original octal number.

> Example: Convert 352 (octal) to binary:
>
> ```
> Octal:  3      5      2
> Binary: 011    101    010
> ```
>
> the binary representation of 352 is 01110101010.



###  Decimal and Hexa conversion 

dividing or multiplying by powers of 16.

#### Decimal to Hexadecimal

1. Divide the decimal number by 16 and record the remainder. The remainder will be a digit in the hexadecimal representation.
2. Continue dividing the quotient obtained in the previous step by 16 until the quotient is 0. Record each remainder.
3. Write the hexadecimal equivalent by arranging the remainders in reverse order. If a remainder is greater than 9, use the corresponding letter in hexadecimal (A for 10, B for 11, etc.).

> Example: Convert 255 (decimal) to hexadecimal:
>
> 255 ÷ 16 = 15, remainder F
> 15 ÷ 16 = 0, remainder F
>
> So, the hexadecimal representation of 255 is FF.



#### Hexadecimal to Decimal

1. Write down the hexadecimal number, starting from the rightmost digit.
2. Starting from the rightmost digit, assign powers of 16 to each digit, with the rightmost digit having a power of 16^0, the next digit 16^1, and so on.
3. Multiply each digit by its corresponding power of 16 and sum the results. The sum is the decimal equivalent.

> Example: Convert 1A (hexadecimal) to decimal:
>
> 1 * 16^1 + 10 * 16^0
> = 16 + 10
> = 26 (decimal)



 

# Analyzing Algorithm



## Math Refresher 

### Logarithmic Functions

$$
f(x) = log_b(x)\\
base : b\\
domain : x \in R \text{ and } x>0\\
range : f(x) \in R\\
$$

> Common bases include 10 (common logarithm, denoted as log(*x*)) and *e* (natural logarithm, denoted as ln(*x*). 

> understanding the essence of log function:
>
> Imagine you are in a building with a magical elevator, and this elevator has a unique property. This elevator is like a time machine, but instead of traveling through time, it takes you through sizes or magnitudes of things.
>
> Now, imagine each floor is a power of 10. The ground floor is 10^0, the first floor is 10^1, the second floor is 10^2, and so on.
>
> Here's where the magic comes in. The elevator has a button that says "Logarithm." When you press this button, it tells you on which floor you are based on the size of things around you.
>
> So, the logarithmic function, in a way, tells you on which "size floor" you are based on the magnitude of something. It's like a magical way of thinking about sizes and magnitudes using the power of 10. The logarithm helps you understand **how many times you need to grow or shrink by 10 to get from one size to another.**





####  relationship between expo and log

log function is the inverse of exponential functions.

Symmetry axis : y=x
$$
\text{log function: }log_xY = b\\
\text{exponential function: }x^b = Y
$$

> understanding:
>
> Imagine you have a magical machine that can transform things in a really cool way. Let's call it the "Growth Machine."
>
> Now, when you put a small seed into the Growth Machine, it multiplies and grows exponentially. Each time it goes through the machine, it multiplies by a certain factor. The more times you run it through, the bigger it gets, and it grows faster and faster. This magical growth is like an exponential function.
>
> Now, what if you want to figure out how many times you need to run the Growth Machine to get a certain size? That's where the "Shrinking Machine" comes in. Let's call it the "Logarithmic Shrinker." If you started with 1 seed and ended up with 8 after some runs through the Growth Machine, you can use the Logarithmic Shrinker to find out that the base-2 logarithm of 8 is 3 because 2^3=8. So, it took 3 runs through the Growth Machine to get to size 8.
>
> The exponential function and the logarithmic function are like two sides of the same magical machine. One makes things grow really fast (exponential), and the other tells you how many times you need to run it to reach a certain size (logarithmic).





####  logarithmic equation 

$$
log(x^{f(x)}) = b
$$

##### Power Rule of Logarithms

$$
log(a^b) = b*log(a)
$$



#### graph shape

<img src="picture\log function.png" alt="functions graph"  />

The graph of a logarithmic function is characterized by an asymptote at x=0. As x increases, the logarithm approaches infinity, but the rate of increase slows down.



#### types

##### common log function

log(x): Base 10 logarithm. 

##### natural log function

ln(x): Base *e* logarithm, where *e* is Euler's number (approximately 2.71828). 



#### why it is useful?

Its importance stems from its relationship with certain algorithms, data structures, and efficiency considerations.

- Time Complexity Analysis and Space Complexity Analysis: Logarithmic time complexity O(log n) is highly desirable in algorithms. Algorithms with logarithmic time complexity often indicate efficient and scalable solutions.
- Divide-and-conquer algorithms frequently exhibit logarithmic behavior as they divide the problem into smaller subproblems.
- Tree Structures: Logarithmic behavior is common in tree structures, such as binary search trees and heaps. The height of a balanced binary search tree with \(n\) nodes is O(log n). This property ensures efficient search, insertion, and deletion operations.
- Efficient Data Structures: Data structures like heaps and balanced search trees (e.g., AVL trees, Red-Black trees) rely on logarithmic height to maintain efficient operations.
- Graph Algorithms: Efficient algorithms for graph traversal often rely on logarithmic or linearithmic time complexities.
- Complexity of Sorting Algorithms: Merge sort and heap sort, both popular sorting algorithms, have O(n*logn) time complexity. The logarithmic term arises from the fact that these algorithms divide and merge elements in a way that exhibits logarithmic behavior.



### Factorial 阶乘  Functions

For a non-negative integer n, the factorial of n, denoted as n!, is the product of all positive integers less than or equal to n. 
$$
n! = n*(n-1)*(n-2)* \text{ ... } *3*2*1
$$

> By convention, 0! is defined to be 1. 





### Algebraic Expression

a mathematical phrase that can contain numbers, variables, and operations. It represents a combination of these elements in a structured way.

To evaluate an algebraic expression, substitute specific values for the variables and perform the indicated operations.

> describe mathematical relationships and perform calculations. 

> We will encounter a few algebraic expressions throughout the course. They may look something like nlogn or 2nlog(n^2) etc. 
>
> All this means is that we have **a variable n** that will be plugged in to the equation. Because we don’t actually know **how many pieces of data** will go in to the algorithm, we use this n **placeholder**. 
>
> Once we know the n value however, we can plug it in, and calculate the answer.





## **Algorithm**

An algorithm is a step-by-step procedure or a set of rules for solving a specific problem or accomplishing a particular task.

> They provide a clear, unambiguous set of instructions for carrying out a task or solving a problem, and they are designed to be effective, efficient, and applicable in various situations.

### Key characteristics

1. **Input:** Algorithms take some input, which may vary from problem to problem. The input is the information the algorithm processes to produce an output.

2. **Output:** Algorithms produce an output, which is the result or solution to the problem based on the provided input.

3. **Definiteness:** Each step of the algorithm must be precisely and unambiguously defined. There should be no ambiguity or confusion in the instructions.

4. **Finiteness:** An algorithm must terminate after a finite number of steps. It should not run indefinitely.

5. **Correctness:** The algorithm should produce the correct output for any valid input, adhering to the problem-solving requirements.

6. **Efficiency:** Algorithms aim to solve problems efficiently, considering factors like time complexity (how long it takes to run) and space complexity (how much memory it uses).

### example

Algorithm for Making a Peanut Butter and Jelly Sandwich:

1. Gather Ingredients:
   - Input: Bread, peanut butter, jelly
   - Output: None at this stage

2. Place Bread Slices on a Clean Surface:
   - Input: Bread
   - Output: Bread slices on the surface

3. Open Peanut Butter Jar and Jelly Jar:
   - Input: Peanut butter jar, jelly jar
   - Output: Jars are open and ready

4. Spread Peanut Butter on One Bread Slice:
   - Input: Peanut butter, bread slice
   - Output: One bread slice with peanut butter

5. Spread Jelly on Another Bread Slice:
   - Input: Jelly, another bread slice
   - Output: Another bread slice with jelly

6. Press the Two Slices Together:
   - Input: Bread slice with peanut butter, bread slice with jelly
   - Output: Peanut butter and jelly sandwich

7. Cut the Sandwich (Optional):
   - Input: Peanut butter and jelly sandwich
   - Output: Pieces of the sandwich

8. Serve:
   - Input: Pieces of the sandwich
   - Output: Ready-to-eat sandwich

> **Characteristics**
>
> - Input and Output: The input includes the ingredients, and the output is the final sandwich.
> - Definiteness: Each step is well-defined, specifying actions like spreading, cutting, and serving.
> - Finiteness: The process ends when the sandwich is ready to be served.
> - Correctness: If you follow each step correctly, you'll end up with a peanut butter and jelly sandwich.
> - Efficiency: The efficiency of this algorithm might not be a critical concern for making a sandwich, but in computer science, it would be essential to consider for more complex algorithms.

> it illustrates the key concepts of algorithms: a sequence of well-defined steps that transform input into output. 
>
> In the world of computer science, algorithms address more complex problems, and their **efficiency** is a crucial consideration for solving larger and more intricate tasks.



### Cheap or Expensive?

When we describe an algorithm as "expensive" or "cheap," we're usually talking about the **computational resources** it consumes, such as time or space.

1. **Expensive Algorithm:**
   - **Time Complexity:** An algorithm is considered "expensive" in terms of time if it takes a significant amount of time to complete, especially as the input size increases. This could mean that the algorithm has a higher time complexity, and its running time grows rapidly with larger inputs.
   - **Space Complexity:** An algorithm may be labeled as "expensive" in terms of space if it requires a large amount of memory or storage space. This suggests a higher space complexity, meaning it uses a significant amount of memory, and the memory requirements grow with the input size.

2. **Cheap Algorithm:**
   - **Time Complexity:** A "cheap" algorithm in terms of time means that it has a low time complexity. It runs quickly, even as the input size increases.
   - **Space Complexity:** A "cheap" algorithm in terms of space uses a relatively small amount of memory, and its space requirements do not grow significantly with the input size. An algorithm with low space complexity, like O(1) or O(log n), can be considered "cheap."



### Complexity of algorithm

the complexity of an algorithm involves analyzing how the algorithm's **runtime** or **space requirements** grow as the size of the **input** increases.



#### RAM Model of Computation

**RAM（Random Access Machine）模型** 是一种**抽象的计算模型**，用于分析算法的时间复杂度。

它假设计算机具有无限大小的内存，并且**基本操作（加法、乘法、赋值、数组访问等）在 O(1) 时间内完成**。

> 尽管这个模型与真实计算机的硬件架构不同，但它提供了一种**统一的方式**来分析和比较算法的性能。
>
> **不同计算机的硬件性能不同**（CPU 速度、缓存大小、内存延迟等），导致运行时间难以直接比较。**RAM 模型提供了一个通用的框架**，让我们可以忽略底层硬件细节，只关注算法的核心操作。使得时间复杂度分析（Big-O）更直观和可比。

##### 基本假设

1️⃣ **单处理器**：

- 计算机只有一个 **CPU**，不考虑并行计算或多线程。

2️⃣ **随机访问存储**：

- 访问数组或变量的时间为 **O(1)**（即，读取 `arr[i]` 只需一步）。
- 忽略 **缓存影响** 和 **内存层次结构**（如 L1/L2 缓存、硬盘 I/O）。

3️⃣ **基本操作的时间复杂度为 O(1)**：

- **算术运算（+、-、\*、/、%）**
- **赋值操作（`x = y`）**
- **比较操作（`x > y`）**
- **逻辑操作（`&&`, `||`, `!`）**
- **数组索引访问（`arr[i]`）**
- **指针操作（`p = &x`）**

4️⃣ **顺序执行**：

- 代码按行执行，每条指令 **顺序执行**，没有并行计算或指令重排。

##### 局限性

尽管 RAM 模型提供了一种统一的分析方法，但它**不完全符合现实计算机的行为**：

1. **忽略缓存** → 真实计算机的 **CPU 缓存、磁盘 I/O、虚拟内存** 会影响程序性能。
2. **忽略指令并行性** → 现代 CPU **可以同时执行多条指令**，但 RAM 模型假设是顺序执行的。
3. **不同操作的时间不一定相等** → 在实际计算机中，**乘法比加法慢**，而 RAM 模型假设它们都是 O(1)。











## Time Complexity

the **amount of time** an algorithm takes to complete as a function of the size of its **input**.

>When analyzing algorithms, it's generally desirable to design algorithms with lower time complexity to ensure efficiency, especially for large inputs. 

However, time complexity is not the only factor to consider; space complexity (memory usage) is another important consideration in algorithm analysis.



### n-Notation

In computer science we need a way to be able to compare different algorithms with each other. We typically use the n-Notation for this. We as computer scientists never know how many pieces of data our programs are going to handle. So instead, we look at how our program is going to grow with different amounts of inputs. 

N-Notation is represented as a function of n which is **an analysis of how the algorithm will scale with more and more input data.**  n is usually a count of how many operations are being run by a program. 

> how the algorithm's efficiency or resource usage grows as the input size increases. 
>
> a simple example: a linear search algorithm. In this case, if "n" represents the number of elements in an array, the time complexity of the linear search algorithm might be O(n), indicating that the worst-case time required for the algorithm to complete is proportional to the number of elements in the array.

Run times of different programs are usually written in n-Notation.  If we want to look up how  fast a certain algorithm is, we will need to know this notation to be able to understand it. This method is based off **looking at the input of the algorithm and analyzing how the algorithm works with this input.**

<img src="picture\log function.png" alt="functions graph"  />

the different values yield vastly different results. These numbers vary a lot with the given n-formulas.  

> The difference between n and n^2 is substantial. If you brought this out to infinity, the difference would almost be a 90-degree angle. (As the difference between them would grow to nearly infinity)
>
> Even though we don’t know the specific amount of data that is coming through our program, we can atleast compare it to another that accomplishes the same task. If one runs at n^2 while the other runs at n, we know the n will be faster in every case. 



#### Scaling Goals

- looking for large patterns
- see major efficiency changes between different algorithms

> minimize time and space complexity, aiming for efficient and scalable solutions.

#### Scaling Rules

- do not care about multiples (ignore constant factors or coefficients when we write the notation)
- take the largest in an equation (if we have many term in one notation, we choose the largest one and ignore these left.)

> The focus is on the dominant term that contributes most significantly to the complexity as the input size grows.

>a practical example:
>
>Suppose you have an algorithm with a time complexity expression like O(3n^2 + 2n + 8). 
>
>Following these rules, you would express the time complexity as O*(*n^2) 

#### Logn

在大O符号中，通常我们使用的是以2为底的对数，即logarithm base 2。所以当我们说时间复杂度是O(log n)时，我们默认是以2为底的对数。在数学符号中，这可以写作log₂ n。

在实际计算机科学中，对数的底数通常是隐含的，因为对数之间的差异只会导致一个常数因子，而不会影响到大O符号表示的增长趋势。所以，通常我们会省略log的底数，因为在算法分析中它往往不是决定性的因素。

如果你需要具体数值，你可以使用换底公式，将以其他底数的对数转换为以2为底的对数。
$$
log_3 n = \frac{log_2 n}{log_2 3}
$$
但请注意，通常在大O符号中，我们更关注增长的趋势而不是具体的数值。所以，O(log n)表示对数时间复杂度，而底数通常不是重点。 





###  Symbolism 

<img src="picture\big O notation.png" alt="big O notation" style="zoom: 50%;" />

 表达算法的最坏情况复杂度。 

> 如果说一个算法的时间复杂度是 *O*(*n*^2)，意味着随着输入规模 *n* 的增加，算法执行的时间最多是*n*^2 的倍数。 

除了大O，还有一些其他的渐近表示法：

- **Big Omega (Ω)**：描述算法的**下界**，即算法的最优表现情况。
- **Theta (Θ)**：描述算法的**紧确界**，即上下界同时满足的情况。
- **Little o (o)** 和 **Little ω (ω)**：表示严格的上界和下界。



####  Big-Omega (Ω) Notation: 

 表达算法的最好情况复杂度。 

> 如果说一个算法的复杂度是 Ω(*n*)，表示在最好的情况下，算法执行的时间至少与输入规模 *n* 成正比。 

####  Big-Theta (Θ) Notation: 

 表达算法的平均情况复杂度。 

> 如果说一个算法的复杂度是 Θ(*n*)，表示在平均情况下，算法执行的时间与输入规模 *n* 成正比。 

####   Small-o Notation: 

  表达算法速度比某个函数快。 

> 如果 *f*(*n*) 的增长速度比 *g*(*n*) 快，但它不能等于 *g*(*n*)，则记作 *f*(*n*)=*o*(*g*(*n*))。 
>
> 如果你说一个算法的运行时间是 *o*(*n*2)，这意味着当数据增长时，这个算法的速度比二次方增长的算法快。 

####  Small-omega (ω) Notation: 

 表达算法速度比某个函数慢。 

>如果 *f*(*n*) 的增长速度比 *g*(*n*) 慢，但它不能等于 *g*(*n*)，则记作 *f*(*n*)=*ω*(*g*(*n*))。
>
>如果你说一个算法的运行时间是 *ω*(*n*)，这意味着当数据增长时，这个算法的速度比线性增长的算法慢。 





### big O notation

The most important notation above is the Omicron, or "Big O".  It is **a relative representation** of the complexity of an algorithm. It represents a **boundry**.

渐近分析的主要工具，用来描述**算法的最坏情况时间复杂度**，即在最差情况下输入规模增大时算法的增长速率。

**定义**：对于一个函数 f(n)，如果存在正整数常数 c 和 n0，使得当 n≥n0 时，始终有 f(n)≤c⋅g(n)，那么我们可以写 f(n)=O(g(n))。

> **大O符号**专注于算法的上界，即它保证了算法在最坏情况下不会增长得比 g(n) 更快。

> [algorithm - What is a plain English explanation of "Big O" notation? - Stack Overflow](https://stackoverflow.com/questions/487258/what-is-a-plain-english-explanation-of-big-o-notation) :
>
> - **relative:** you can only compare apples to apples. You can't compare an algorithm that does arithmetic multiplication to an algorithm that sorts a list of integers. But a comparison of two algorithms to do arithmetic operations (one multiplication, one addition) will tell you something meaningful;
> - representation: Big O reduces the comparison between algorithms to a single variable. That variable is chosen based on observations or assumptions. When you say that Big O reduces the comparison between algorithms to a single variable, you're referring to the fact that it focuses on the dominant term or the most significant factor that influences the overall efficiency of an algorithm. This highlights an important aspect of algorithm analysis: the choice of what to focus on depends on the specific context and assumptions made. Different scenarios might have different dominant factors, and Big O notation is a tool that helps simplify these considerations by focusing on the most significant term as the input size grows towards infinity. In practice, it's essential to consider other factors and conduct a more detailed analysis if the specific details of the scenario suggest that the simplified assumptions made by Big O may not hold. Understanding the characteristics of the problem at hand and the nature of the operations involved is crucial for a nuanced analysis of algorithmic efficiency.
> - complexity: if it takes me one second to sort 10,000 elements, how long will it take me to sort one million? Complexity in this instance is a relative measure to something else.





#### why big O notation is so important?

The reason for this is because it gives us a worse case scenario. That means we know the absolute worse case scenario of our program, meaning **if we plan for this, we won't have any surprises or weird corner cases that come up.**

We can then compare the worst case scenarios of programs to see which are faster. **Since this is the absolute slowest the program can run, we know that one program will always run slower than another program!**

> For example let's say that we have two programs, program A which runs at Ω(n) and program B which runs at Ω(n^2). 
>
> Which of these two programs is better? 
> Well all we know is that program A is slower or equal to n and program B is slower or equal to n^2. 
>
> However that doesn't guarantee anything. Program A could end up running around n^3 or n! and meet the requirements of Ω(n). 
> B could do the exact same thing, so their speed is still arbitrary. 
>
> For example, program A could have a lower bound of Ω(n), but in reality, it might have a small constant factor, making it faster than program B for small inputs. Similarly, program B might have a higher growth rate, but if its constant factor is significantly smaller, it might outperform A for moderate input sizes.
>
> In summary, while big omega notation provides useful information about the growth rates of algorithms, it doesn't give a complete picture of their absolute performance. To assess the practical efficiency of programs, you would need to consider both the growth rate (as indicated by Ω) and the constant factors involved in the algorithms' running times. Additionally, other factors like best-case, average-case, or worst-case analysis can provide a more comprehensive understanding of algorithm behavior.



#### Better understand

Let’s say we have a time scale to determine how fast our algorithm runs. In this scale the closer to 0 we go, the faster our algorithm. We can use to show **why Big O is typically the most useful of these notations.**

- **ω(7) -**  The algorithm will run slower, or > 7. How much greater? 1,000. 1,000,000? There is no way to know. This algorithm could take years to complete the simplest of tasks.  
- **Ω(7) -** The algorithm will run “slower or equal” to 7, or >=7. Still could run in to infinity or really large run times.  
- **Θ(7) -** The algorithm is equal to 7, or = 7. This would be great. If we can guarantee an algorithm will always run equal to something we would use this. However, this is highly unlikely in the real world, so it’s not used too often.  
- **O(7) -** The algorithm will run “faster or equal” to 7, or <=7. This is good. We have a limit on the algorithm. We know in all cases, 7 is the worst this
- **o(7) -** The algorithm will run faster than 7, or < 7. It’s just less accurate than O(7). How much faster will it run? 6? 2?. We don’t know the limit. Although we can still plan a worst case scenario with this, it’s less accurate than O(7) which is why it’s rarely used.



#### Pseudo Code Example

```python
# simple example:
for each data in data_list
  {
    print data to screen
  }
  
# data_list = [3, 2, 10, buffalo]
# n = data_number = 4

# the process to get outputs: run 4 times
3
3 2
3 2 10
3 2 10 buffalo
# so the for loop have O(n)
```

```python
# more complex example
for each data "N" in data_list
  {
	//check if data "W" in data_list
	for each data "W" in data_list:
	  {
		if N==W:
		  print True
	  }
  }
  
# data_list = [3, 2, 10, buffalo]
# n = data_number = 4

# the process to get outputs: run 16=4*4 times
3=3               # True
3=2               # False
3=10              # False
3=buffalo         # False
2=3               # False
2=2               # True
2=10              # False
2=buffalo         # False
10=3              # False
10=2              # False
10=10             # True
10=buffalo        # False
buffalo=3         # False
buffalo=2         # False
buffalo=10        # False
buffalo=buffalo   # True 
# so the for loop have O(n^2)
```





###  Common Classes

<img src="picture\log function.png" alt="big O notation"  />

<img src="./picture/different time complexity.jpg" alt="different time complexity" style="zoom: 33%;" />



#### O(1) - Constant

The algorithm's runtime is constant, regardless of the input size. 

It's the most efficient time complexity.



#### O(log n) - Logarithmic 对数

The runtime grows logarithmically with the size of the input. 

Algorithms with binary search are often examples of logarithmic time complexity.



#### O(n) - Linear

The runtime grows linearly with the size of the input. 

A simple search through an array is an example of linear time complexity.



#### O(n log n) - Linearithmic 线性对数

Common for many efficient sorting algorithms, like merge sort and heap sort.



#### O(n^2) - Quadratic 平方

The runtime is proportional to the square of the input size. 

Common in nested loops or algorithms with nested iterations.



#### O(n^k) - Polynomial 多项式

The runtime grows as a polynomial function of the input size, where k is a constant.



#### O(2^n) - Exponential 指数

The runtime grows exponentially with the input size. 

Often seen in algorithms with recursive implementations that result in repeated computation.



#### O(n!) - Factorial 阶乘

The runtime grows factorially with the input size. 

Common in brute-force algorithms that generate all possible solutions.





## Space Complexity

Space complexity analyzes how the memory requirements of an algorithm grow with the input size. 

> Understanding space complexity helps in designing algorithms that use memory efficiently, especially in scenarios where memory resources are limited or costly.



### Auxiliary Space vs. Input Space

Auxiliary Space: Extra space used by the algorithm for its internal workings.

> This refers to the extra space required by the algorithm for variables, data structures, and other internal computations. 

Input Space: Space required by the input itself.

> This is the space required by the input to the algorithm. For example, in sorting algorithms, the input space might be the array to be sorted. 

> Consider both auxiliary space and input space to get a complete picture of space complexity.



### Common Classes

- **O(1) - Constant Space:** Algorithms with constant space complexity use a fixed amount of memory regardless of the input size. This is often achieved with a constant number of variables.
- **O(n) - Linear Space:** Algorithms with linear space complexity use an amount of memory that grows linearly with the size of the input.
- **O(n^2) - Quadratic Space:** Algorithms with quadratic space complexity use an amount of memory that grows quadratically with the size of the input.
- logarithmic (O(log n))
- linearithmic (O(n log n))
- cubic (O(n^3))
- exponential (O(2^n))



## **Master Method**

<img src="./picture/master method.jpg" alt="master method" style="zoom:33%;" />
$$
T(n) = aT(\frac{n}{b}) + f(n)\\
通过对比 f(n) 和 n^{logb^a} 来判断复杂度
$$
解决**分治算法递归时间复杂度**的一种常用工具。

其中：

- a >= 1：子问题的个数
- b > 1：每个子问题的规模是原来的 \frac{1}{b}
- f(n)：划分和合并的开销（不递归的部分）

### 关键问题

比较两个东西：

1. 递归子问题的总量：看起来像 logb^a（这只是个计算用的参考，不用死记）
2. 自己额外做的工作：就是那个 `+ f(n)` 里的 `n` 或 `n^2` 之类

<img src="./picture/master method2.jpg" alt="master method2" style="zoom:33%;" />

**情况 1（递归占主导）**：
$$
f(n) = O(n^{log_ba-e})\\
即比 f(n) 比n^{log_ba}小一大截\\
\text{}\\
则：T(n) = Θ(n^{log_ba})
$$
 **情况 2（两者相等）**：
$$
f(n) = O(n^{log_ba})\\
\text{}\\
则：T(n) = Θ(n^{log_ba}logn)
$$
**情况 3（f(n) 占主导）**：
$$
f(n) = O(n^{log_ba+e})\\
\text{，而且满足“regularity condition”：}\\
af(n/b)≤cf(n)，其中c<1\\
\text{}\\
则：T(n) = Θ(f(n))
$$


### Example

$$
T(n) = 2T(\frac{n}{2}) + n\\
$$

>什么意思？
>
>- 把大小为 `n` 的问题，拆成两个 `n/2` 的子问题（`2T(n/2)`）
>- 加上一点花在“拆”和“合并”的时间，比如 `n` 单位时间

我们想知道：**这个递归的总时间 T(n) 到底是多快多慢？**`T(n)` 是 `n log n`？还是 `n^2`？还是更快？
$$
a = 2, b = 2, log_22 = 1\\
f(n) = n = Θ(n^{log_ba})\\
\\
\text{符合情况 2 ⇒}\\
T(n) = Θ(nlogn)
$$




##  Trade-offs Between Time and Space Complexity 

Optimizing for one may lead to compromises in the other. For example, caching data to reduce computation time might increase space complexity.

For certain applications, space efficiency is crucial, such as in embedded systems, mobile devices, or environments with limited memory resources. 





# **Arrays**



##  What does data look like in computer? 

At its most fundamental level, data in a computer is represented using binary code. Multiple bits grouped together form larger units, such as **bytes**. A byte is typically composed of 8 bits and can represent a wider range of values.

1. **Text Data:** Characters are often represented using a character encoding system such as ASCII or Unicode. In ASCII, for example, the letter 'A' is represented as the binary value 01000001.

2. **Numeric Data:** Numbers can be represented in binary, and different conventions exist for representing integers and floating-point numbers.

3. **Images:** Images can be represented as a grid of pixels, where each pixel's color is represented by numerical values for its red, green, and blue components.

4. **Audio:** Sound can be represented digitally by recording the amplitude of the sound wave at regular intervals. Each sample is represented numerically.

5. **Files and Documents:** Files, such as documents or spreadsheets, have a structure defined by the file format. For example, a Word document might store text, formatting, and images in a specific way.

> data in a computer is essentially a series of binary digits that represent various types of information. 
>
> The specific representation and structure of data depend on the type of information being stored or processed. 
>
> Higher-level abstractions, such as programming languages and file formats, provide ways to work with and manipulate data in a more human-readable and structured manner.





## How do computer store data?

Computers store data using various types of storage devices, each with its own characteristics, advantages, and disadvantages. 

### store types

1. **Hard Disk Drives (HDD):** HDDs are magnetic storage devices that use rapidly rotating disks or platters coated with magnetic material. Data is stored in binary code as magnetic patterns on the platters. A read/write head hovers just above the surface of the spinning disk to access or modify the data.

   数据被磁化成磁性模式，读/写头通过漂浮在盘片表面上方的方式来读写这些数据。这些磁性模式的改变代表着二进制数据的 0 和 1。

2. **Solid State Drives (SSD):** SSDs use NAND-based flash memory to store data. Unlike HDDs, SSDs have no moving parts, which makes them faster, more durable, and less prone to mechanical failure. SSDs are commonly used in laptops, desktops, and increasingly in data centers.
   其中数据存储在浮动栅传输器中。浮动栅传输器中的电荷状态表示二进制数据的状态。

3. **RAM (Random Access Memory):** RAM is a volatile form of memory used by the computer to store data that is actively being used or processed. Unlike storage devices such as HDDs and SSDs, RAM loses its content when the power is turned off.
   RAM 由许多存储单元组成，每个单元都能够存储一个比特（0 或 1）。存储单元是由一个电容器和一个相关的传输器构成。电容器中的电荷表示 1，没有电荷表示 0。这些存储单元按矩阵排列，每一行和列都有一个唯一的地址，通过这些地址可以直接访问存储的数据。

4. **Flash Memory:** Flash memory is non-volatile and used in devices like USB drives, memory cards, and solid-state drives. It retains data even when the power is turned off. It is based on the same technology as SSDs but is often used for portable storage.

5. **Optical Storage:** This includes CDs, DVDs, and Blu-ray discs. Data is stored as microscopic pits on the surface of the disc. A laser is used to read the data by detecting changes in the reflection of the laser light.
   光学存储使用有微小坑的反射表面。坑和平地分别代表 0 和 1。通过激光读取这些反射模式，从而解释存储的数据

6. **Magnetic Tapes:** While less common in personal computing, magnetic tapes are used in some enterprise-level backup systems. Data is stored sequentially along a tape, and it is read or written using a tape drive.

7. **Cloud Storage:** Data can also be stored on remote servers accessed over the internet. Cloud storage services like Google Drive, Dropbox, and Amazon S3 allow users to store and retrieve data from anywhere with an internet connection.
   远程服务器可能使用多种类型的存储技术，例如硬盘驱动器（HDD 或 SSD）。存储数据的物理结构可能包括数据中心中的硬件组件，例如存储阵列和服务器。

> These storage methods serve different purposes, with factors such as speed, capacity, cost, and volatility influencing the choice of storage for a particular use case. Many systems use a combination of these storage types to balance performance and cost-effectiveness. 



### abstracted concepts

1. **内存单元（Memory Cell）:**
   - 每个内存单元是一个小的存储单元，可以存储一个比特的数据。
   - 内存单元有一个唯一的地址，通过这个地址可以访问其中的数据。
2. **字节（Byte）:**
   - 一个字节通常由 8 个内存单元组成，形成一个字节单元。
   - 字节是计算机中基本的数据单元，用于表示一个字符或其他小的数据单位。
3. **内存地址（Memory Address）:**
   - 每个内存单元都有一个唯一的地址，用于唯一标识这个存储单元。
   - 地址是一个整数，通过这个地址可以直接访问存储单元。在计算机内存中，每个内存地址通常唯一指向一个字节（8位），而不是一个比特。 
   - 在硬件层面，内存地址是一个二进制数，例如，16位系统中可能有2^16（65536）个地址。
4.  **硬件上的存储地点：**
   - 内存地址对应于计算机硬件上的实际存储位置。
   - 这个位置通常是内存芯片上的一个存储单元，可以是闪存、RAM、硬盘等不同类型的存储介质。



### abstracted process

1. **写入数据：**
   - 当计算机需要存储数据时，它会找到合适的内存地址。
   - 如果要存储的数据是一个字节，那么会找到一个连续的字节单元。
   - 将二进制数据（比特序列）写入这个字节单元，每个比特占用一个内存单元。
2. **读取数据：**
   - 当计算机需要读取存储的数据时，它会使用相应的内存地址来检索数据。
   - 如果要读取的数据是一个字节，计算机会读取相邻的字节单元，然后将它们组合成一个字节的数据。



### example

将变量 X 的值（例如 X=4）存储在内存中时 :

1. 分配内存地址：计算机会分配一个唯一的内存地址来存储变量 X 的值。这个地址是一个数字，唯一标识内存中的一个存储单元。 变量X是在编程语言中定义的符号，用于标识某个内存地址，它关联到一个特定的数据类型。 在程序中，你声明了一个变量X并赋予它值4，编译器或解释器会分配一个内存地址给这个变量，这个地址是硬件上的实际存储位置。  
2. 确定数据类型：变量 X 的值是 4， 会以二进制形式存储在内存地址对应的硬件存储位置上。 根据编程语言的规定，计算机会知道 X 是一个整数型变量。
3. 确定存储大小：根据整数的数据类型，计算机会知道需要多少个字节来存储整数 4。例如，如果是 32 位整数，需要 4 个字节。
4. 写入数据：计算机将整数 4 的二进制表示写入分配的内存地址。假设内存地址为 0x1000，那么计算机会将二进制表示的整数 4 存储在地址 0x1000 处的存储单元。



###   Address Resolution / Mapping 地址解析/ 映射 

计算机需要通过**符号表（Symbol Table）或类似的数据结构**来追踪变量（比如X）和其对应的内存地址之间的关系。 

> 符号表存储了程序中所有标识符（变量名、函数名等）与其在内存中的关联关系。 
>
> - **Address Resolution:** 这个术语通常更多地**与网络领域相关**，特别是在IP网络中。在这个背景下，地址解析通常指的是将网络层的IP地址解析为链路层的MAC地址的过程。
> - **Address Mapping:** 这个术语更广泛地用于描述**高层抽象（比如变量名）与底层实现（比如内存地址）之间的关系**的过程，无论是在编程语言中的符号解析，还是在操作系统中的内存地址分配。

1. **编译时的符号解析：**
   - 当你编写程序并使用变量时，编译器会在编译阶段建立符号表。符号表是一个数据结构，它记录了程序中每个标识符（比如变量名）和其对应的内存地址或存储位置。
2. **链接时的地址解析：**
   - 如果你的程序包含多个源文件，链接器会负责将这些文件组合成一个可执行文件。在这个阶段，符号表中的地址可能会被调整，以便正确地映射到实际的内存地址。
3. **运行时的地址访问：**
   - 当程序运行时，操作系统加载可执行文件到内存中，并为程序分配内存空间。在运行时，程序可以通过符号表查找变量名（例如X）对应的内存地址。
4. **变量的作用域和生命周期：**
   - 符号表也记录了变量的作用域和生命周期信息。这有助于确保在程序的不同部分使用相同变量名时，它们引用的是正确的内存地址。



### longer data storage

如果要存储较长的数据（例如，多字节的整数、浮点数、字符串等），这些数据将会**占据多个连续的内存地址**。计算机内存是线性的，可以将连续的地址看作是一个**单一的地址范围**，其中每个地址对应一个字节。

对于连续的内存地址范围，通常使用一个起始地址来表示这个范围。这个起始地址指向内存中数据的第一个字节。  

> 对于复杂数据结构，可能需要额外的元数据来描述结构中各个字段的类型和相对偏移。这些信息在符号表或其他元数据中被记录，以便程序在运行时能够正确地访问和操作这些结构。 

**example:**

假设变量X的地址是0x1000，而且它是一个4字节的整数。在这种情况下，X的值将存储在地址0x1000、0x1001、0x1002、0x1003这四个地址上。这四个地址对应的内存单元可以被视为一个整体，形成一个32位的整数。 

假设有一个整型数组 `arr`，它的起始地址是 `0x1000`，而且每个整数占用4个字节。在符号表中，可能包含如下信息： 

```python
Variable | Type  | Size | Address
---------|-------|------|--------
arr      | int[] | 20   | 0x1000

# arr 是一个整型数组，占用20个字节的内存，起始地址是 0x1000。
```



####  Byte-Alignment 

如果数据非常长，例如大型数组或复杂的数据结构，计算机会使用多个连续的内存地址来存储整个数据结构，但这些地址是按字节对齐的。 

按字节对齐是一种内存布局的规定，确保数据结构的起始地址和每个成员的地址都是某个特定值的倍数，通常是字节的倍数，即数据结构的每个成员都从适当的字节边界开始。 

> 这样的对齐规则有助于提高内存的访问效率，因为许多硬件平台要求数据在内存中按照一定的对齐方式存储，否则可能导致性能问题或错误。 

example：

```java
// 假设我们有以下数据结构：
struct MyStruct {
    char   a;  // 1字节
    int    b;  // 4字节
    double c;  // 8字节
};

// 在不考虑对齐的情况下，这个结构的大小总共是 1 + 4 + 8 = 13 字节。
// 根据许多计算机体系结构的对齐规则，结构体的成员通常需要按照其大小的最大值对齐。在这个例子中，double 是最大的数据类型，占用8字节，所以整个结构体的大小应该是8的倍数。

// 按字节对齐的话，MyStruct 结构体的大小会被调整为 16 字节，即：
struct MyStruct {
    char   a;      // 1字节
    char   _padding[3]; // 补充字节，使得下一个成员对齐到4字节边界
    int    b;      // 4字节
    double c;      // 8字节
};

// 使用了 _padding 数组来填充对齐字节，确保 int 类型的成员 b 从4字节对齐开始，而 double 类型的成员 c 从8字节对齐开始。
// 这种对齐的方式有助于提高内存访问的效率，因为大多数计算机体系结构更容易按照对齐的方式访问内存。
```





## **Data Structure**

a way of organizing and storing data to perform operations efficiently.

> It defines a set of operations that can be performed on the data, along with the behavior of those operations.

The choice of a data structure depends on the type of operations that need to be performed frequently and the efficiency requirements for those operations.

> Data structures like arrays, linked lists, stacks, and queues are  abstract concepts that programmers use to organize and manage data in a  way that is efficient and effective for solving specific problems. They  don't exist as physical entities in the computer's memory until a  programmer writes code to implement them. 
>
> - Data structures  define rules and behaviors for organizing and accessing data and help programmers conceptualize and design solutions to problems.
> - Programmers translate these abstract concepts into actual code using programming languages.
> - The code that implements these data structures interacts with the computer's hardware, instructing it to perform operations like reading, writing, and manipulating memory.
> - The computer's memory is then used to store the actual data based on the rules defined by the chosen data structure.

> For example, when you declare an array in code, you're instructing the  computer to allocate a block of memory to store elements in a contiguous manner. 
>
> an array allocates contiguous memory locations for its elements, while a linked list uses scattered memory locations connected by pointers.



### types

#### Arrays

- A collection of elements, each identified by an index or a key.
- Elements are stored in contiguous memory locations.
- Access time is constant, but insertion and deletion may be slow.

#### Linked Lists

 - A collection of elements, each connected to the next one by links or pointers.
 - Elements are not stored in contiguous memory locations.
 - Efficient for insertions and deletions, but access time can be slower than arrays.

#### Stacks

- A Last-In-First-Out (LIFO) data structure.
- Elements are added and removed from the same end, called the top.
- Common operations include push (addition) and pop (removal).

#### Queues

- A First-In-First-Out (FIFO) data structure.
- Elements are added at the rear and removed from the front.
- Common operations include enqueue (addition) and dequeue (removal).

#### Trees

- A hierarchical data structure with a root node and child nodes.
- Common types include binary trees, AVL trees, and B-trees.
- Used in hierarchical structures and searching algorithms.

#### Graphs

- A collection of nodes (vertices) connected by edges.
- Can be directed or undirected, weighted or unweighted.
- Used to model relationships and connections between entities.

#### Hash Tables

- An associative data structure that maps keys to values.
- Uses a hash function to compute an index into an array of buckets.
- Provides fast average-case time complexity for basic operations.

#### Heaps

- A specialized **tree-based** data structure.
- Common types include binary heaps and Fibonacci heaps.
- Used for priority queues and heap sort algorithms.



### when we need to create a data structure?

Creating a new data structure is often necessary when existing data structures do not meet the specific requirements or constraints of a problem or when a more efficient solution is needed for a particular set of operations.

> Before creating a new data structure, it's important to thoroughly analyze the problem, understand the specific requirements and constraints, and evaluate existing data structures to determine if any can be adapted or combined to meet the needs. It's often recommended to reuse existing, well-tested data structures whenever possible to benefit from established libraries and avoid reinventing the wheel.

1. **Specific Requirements:**
   - When the problem at hand has unique requirements that cannot be efficiently addressed by existing data structures. For example, if you need a data structure that maintains elements in a specific order or allows for specific types of queries, a custom data structure might be necessary.

2. **Performance Optimization:**
   - When existing data structures do not provide the desired time or space complexity for certain operations. Creating a specialized data structure can lead to more efficient algorithms for specific tasks.

3. **Domain-Specific Operations:**
   - When the problem domain requires operations that are not supported by standard data structures. For instance, if you are working with geographical data, you might design a data structure tailored for spatial queries.

4. **Concurrency or Parallelism:**
   - In concurrent or parallel computing scenarios, custom data structures may be designed to handle synchronization, locking, or other issues specific to concurrent access by multiple threads or processes.

5. **Memory Efficiency:**
   - When memory efficiency is crucial, a custom data structure can be designed to minimize space usage for a particular set of operations.

6. **Trade-offs Between Operations:**
   - Sometimes, existing data structures may have trade-offs between different types of operations (e.g., insertions, deletions, lookups). Designing a custom data structure allows you to optimize for the specific mix of operations relevant to your application.

7. **Data Organization and Retrieval:**
   - When data needs to be organized in a specific way or retrieved in a particular order, a custom data structure can be tailored to support these requirements more effectively than general-purpose structures.

8. **Specialized Algorithms:**
   - When solving specific algorithms or computational problems that require novel data structures to achieve optimal performance.

9. **Hardware Constraints:**
   - In scenarios where hardware constraints or characteristics need to be taken into account, designing custom data structures can help exploit the hardware architecture more efficiently.

10. **Application-Specific Needs:**
    - In certain applications, such as databases, compilers, or graphics, specialized data structures are often created to meet the unique demands of those domains.



### SDE's use

In a typical software development role, especially as a software development engineer (SDE) in a company, you may not frequently need to create low-level data structures from scratch. Many programming tasks involve leveraging existing libraries, frameworks, and standard data structures provided by programming languages and platforms. High-level languages such as Python, Java, C#, and others come with built-in data structures that cover a wide range of needs

> While creating basic data structures like linked lists, trees, or hash tables from scratch might be part of computer science education, in professional software development, the focus is often on using existing, well-tested implementations to build robust and maintainable software. It's crucial to understand the principles behind data structures and algorithms, even if you don't create them from scratch regularly, as this knowledge helps you make informed decisions about when to use existing solutions and when custom implementations might be beneficial.

There are scenarios where you might need to design or customize data structures:

1. **Algorithm Design:**
   - If you're working on complex algorithms that require specific data structures for optimization or to meet unique requirements, you might find yourself creating or customizing data structures.

2. **Performance Optimization:**
   - In performance-critical applications, you might need to optimize data structures for specific use cases to achieve better runtime or memory efficiency.

3. **Specialized Domains:**
   - In certain domains such as game development, graphics programming, or scientific computing, you might encounter situations where specialized data structures are beneficial.

4. **Concurrency and Parallelism:**
   - If you're dealing with concurrent or parallel programming, you might need to create or use specialized data structures that handle synchronization and avoid race conditions.

5. **System Design:**
   - When designing larger systems or components, you might need to choose or design data structures that suit the requirements of your system's architecture.

6. **Interviews and Competitive Programming:**
   - In technical interviews or competitive programming, you might be asked to create or modify data structures to solve specific problems.





## What is array?

<img src="picture\array.png" alt="array" style="zoom: 100%;" />

an array is **a fundamental data structure** that stores a collection of elements, each **identified by an index or a key**. 

The elements in an array are typically of the **same data type**, which can visited by **index** and **stored continually** in memory.

> the array provides a way to organize and efficiently access these elements.

### relationship with memory

- 当您声明一个数组时，计算机会为其分配一块连续的内存空间，以便存储数组的元素。Then whenever we call the array, it returns the location of start of the array. We can then apply the appropriate index number to get to any point in that array instantly
- 每个数组元素都有一个索引，通过该索引可以访问到数组中的特定元素。
- 数组的元素在内存中按照数组类型的大小和对齐规则进行存储。

>    - 数组的大小通常在声明时确定，且不易改变。
>    - 索引通常从0开始，所以 numbers[0] 是数组的第一个元素，numbers[4] 是数组的第五个元素。





### key  characteristics 

#### Index

a number that represents the location of an element in an array. Arrays use zero-based indexing, meaning the first element is at index 0, the second at index 1, and so on.

#### Fixed Size

the number of elements in an array is predetermined at the time of declaration. Once an array is created, its size cannot be changed. If you need a different size, you often have to create a new array.

#### Homogeneous Elements

Arrays store elements of the same data type. Every element in the array must be of the declared type. This ensures that each element takes up a consistent amount of memory, making it easier to manage and access elements.

#### Contiguous Memory Allocation

Elements of an array are stored in contiguous (adjacent) memory locations. Accessing elements is efficient because the computer can calculate the memory address of any element based on the starting address and the size of each element.





## Advantages and Disadvantages

### Pros: [access time]

- efficient for random access **directly** to elements using their index.
- Predictable Memory Access Patterns: doesn't involve complex **pointer** traversal or linked structures
- Simple and Efficient Address Calculation: the address of the i-th element in an array can be determined as **base\_address + i*element\_size**.
- Memory is allocated in a **contiguous** block, making it efficient in terms of memory utilization.
- They can also be used to build more advanced data structures like stacks and queues. 

### Cons

   - Fixed size: The size of an array is determined at compile time and cannot be easily changed during runtime. (stick to this size throughout their execution. If the size of the array needs to change frequently, other data structures like dynamic arrays or linked lists might be more suitable. )
   - Insertions and deletions can be inefficient, especially if elements need to be shifted to accommodate changes. (a time complexity of O(n))

### access time

the time it takes to retrieve or store data.  It is the total time required to complete an operation, starting from  the initiation of the request until the data is made available for  processing. 

> a critical metric for evaluating the performance of storage devices.
>
> Faster access times result in quicker retrieval and storage of data, which is especially important for applications that require rapid data access, such as databases and real-time processing systems.
>
> Solid-state drives (SSDs) generally have lower access times compared to traditional HDDs due to their lack of moving parts and faster data transfer rates.

**Access Time Formula:**

Access Time=Seek Time+Rotational Latency+Transfer Time

1. **Seek Time**: the time it takes for the read/write head to position itself over the correct track on the storage medium. 
   This component is particularly relevant for random access operations where the data is not stored sequentially.
2. **Rotational Latency** (or Rotational Delay): the time it takes for the desired disk sector to rotate under the read/write head after the head is positioned over the correct track. 
   This component depends on the rotational speed of the disk.
3. **Transfer Time**: Once the read/write head is correctly positioned, the transfer time is the time it takes to actually read or write the data. 
   This is influenced by the data transfer rate of the storage device.





## Types



### Fixed Array

elements are arranged linearly



#### Run Times

##### Insertion Behavior - O(n), Ω(1), Θ(n)

###### Insertion Random - O(n)

shift the existing elements to make room for the new element.

1. Determine the index where you want to insert the new element. 
2. Move all elements from the insertion position to the end of the array one position to the right.
3. Place the new element at the desired index.

###### Insertion Front - O(n)

shift the existing elements

1. Move all elements to the right by one position to make room for the new element.
2. Place the new element at the front (index 0) of the array.

###### Insertion Back - O(1)

simply place the new element at the end.

> Inserting at the back is generally more efficient than inserting at the  front or at random positions, especially for large arrays, because  shifting elements can be a costly operation. 
>
> In scenarios where frequent insertions are required, other data structures like linked lists might  be more suitable. 



##### Deletion Behavior - O(n), Ω(1), Θ(n)

###### Deletion Random - O(n)

need to shift the remaining elements to close the gap. 

1. Determine the index of the element you want to delete.
2. Move all elements to the left, starting from the position after the deleted element.

###### Deletion Front - O(n)

shift the remaining elements which means moving all elements to the left by one position.

##### Deletion Back - O(1)



##### Search Behavior 

###### Search Unsorted- O(n), Ω(1), Θ(n)

check each element one by one until you find the target element or determine that it is not present.

Algorithm:

1. Start from the **beginning** of the array.
2. Compare the target element with each element in the array until a match is found or the end of the array is reached.
3. If a match is found, return the index of the element; otherwise, return a value indicating that the element is not present.



###### Search Sorted: binary search- O(log(n)), Ω(1), Θ(log(n))

use a more efficient algorithm called **binary search**

> Binary search takes advantage of the sorted order to quickly **eliminate half of the remaining elements in each step.** 

Algorithm:

1. Start with the entire sorted array.
2. Compare the target element with the **middle** element of the array.
3. If the target element matches the middle element, return its index.
4. If the target element is less than the middle element, repeat the search in the left half of the array.
5. If the target element is greater than the middle element, repeat the search in the right half of the array.
6. Continue the process until the target element is found or the search space is empty.

##### Access Time - O(1)



### Circular array

a data structure that uses a single, fixed-size array but allows elements to be efficiently rotated or "cycled" within the array.

Circular arrays are used to implement queue 

> when an element is shifted off one end of the array, it reappears at the other end. 
>
> This circular structure is useful in certain scenarios where a continuous or cyclic behavior is required. 

> For example, consider a circular buffer used in computer science for tasks such as buffering data between two processes. When new elements are added to the buffer, and it reaches its capacity, the oldest elements are overwritten, creating a circular behavior.

> 在讨论循环数组时，没有一个真正的头部，但我们通常会用一个索引（或称为指针）来表示数组中的当前位置。这个索引可以被认为是“头部”或“起始位置”，并且在操作数组时会随之移动。当你使用X[0]来引用数组中的元素时，就相当于你在引用这个循环数组的起始位置，因此可以认为"头部"指针正指向这个位置。注意，在环形队列中，末尾是指针的当前位置的前一个位置。 
>
> 如果指针越界，通常采用循环的方式，即当指针到达数组末尾时，它会循环回到数组的开头。这可以通过取余操作来实现，例如 `(currentPosition + 1) % arrayLength`。 
>
> 在循环数组中，如果我们使用索引（指针）来表示当前位置，这个位置会随着数组的操作而变化。这可能导致我们之前认为的第一个数（头部）在索引变化后不再是我们期望的那个数。 
>
> 有几种方法可以解决这个问题： 
>
>  1.**使用一个额外的变量来追踪头部位置：** 你可以维护一个额外的变量，比如`head`，它表示当前循环数组的头部位置。当你进行插入、删除等操作时，可以更新这个变量，以确保你始终知道头部在哪里。 
>
>  2.**使用取余操作：** 可以通过取余操作来计算新位置。如果你知道数组的长度是`n`，那么下一个位置可以通过 `(currentPosition + 1) % n` 计算得到。这样可以确保位置在数组长度范围内循环。 



#### why we need circular array?

One of the major problems with a typical array is that we could reach O(n) whenever we tried inserting or deleting into the front. The entire array had to be shifted, causing a lot of data to be touched that didn’t really need to be touched. 

To improve this, we pretend that the array is circular. This makes it so we never need to shift data.



#### how to get it?

<img src="picture\circular array.jpg" alt="circular array" style="zoom: 65%;" />

<img src="picture\circular array.png" alt="circular array" style="zoom: 35%;" />

So how do we pretend it’s circular? We create two cursors. A “start” cursor, which points to the beginning of the array, and an “end” cursor which points to the end of the array. These cursors are then adjusted when an element is deleted or added. 

For example, let’s say we had some data in buff[0] that we wanted to delete. If we look at the typical horizontal array above, you will notice that when we delete this data, we will end up having to shift everything backwards to fill in the hole. 

However, with the circular array, what we do is to move the “front” cursor to buff[1]. This makes buff[1] our new beginning of the array. We can now add or delete anything, and instead of moving the data, we just move the cursor around. 

At some point the beginning of the array might be at buff[13] and the end might be at buff[6]. It just depends on how data is added and removed. 

Overall though, since we are only moving the location of the cursor, our run time improves to O(1) from O(n).

```python
class CircularArray:
    def __init__(self, size):
        # 初始化CircularArray对象，指定数组大小
        self.size = size
        # 创建一个大小为size的数组，初始值为None
        self.array = [None] * size
        # head表示数组中的第一个元素的索引
        self.head = 0  # Points to the first element in the circular array（索引）

    def insert(self, value):
        # 将新元素插入到循环数组中
        self.array[self.head] = value  
        # 更新head，使其指向下一个位置，考虑循环数组的特性
        self.head = (self.head + 1) % self.size

    def delete_at_index(self, index):
        # Check if the index is valid
        if index < 0 or index >= self.size:
            print("Invalid index")
            return

        # Compute the actual index in the circular array
        actual_index = (self.head + index) % self.size

        # Delete the element at the computed index
        self.array[actual_index] = None

    def display(self):
        print(self.array)

# Example usage
circular_array = CircularArray(5)
circular_array.insert(1)
circular_array.insert(2)
circular_array.insert(3)
circular_array.insert(4)
circular_array.display()  # Output: [1, 2, 3, 4, None]

circular_array.delete_at_index(1)
circular_array.display()  # Output: [1, None, 3, 4, None]
```



**create a circular array with a defined size of 5 but only store 3 numbers in it.** 

```python
# define a circular array with a size of 5:
Circular Array: [_, _, _, _, _]

# add three numbers, let's say 10, 20, and 30:
Circular Array: [10, 20, 30, _, _]
                  ^
                  Head

# add the number 40:
Circular Array: [10, 20, 30, 40, _]

# rotate the array to the right:
Circular Array: [40, 10, 20, 30, _]
# 最后插入哪个数，指针就指向哪个数
```

**have a circular array with a size of 3, but try to insert the number 40** 

```python
# origin:
Circular Array: [10, 20, 30]

# insert 40:
Circular Array: [40, 20, 30]
# 最后插入哪个数，指针就指向哪个数
```





#### Modulo %

the operation in mathematics known as the "modulus" or "mod",  finds the remainder after division of one number by another. 

It is often denoted by the percent sign (****). 
$$
a\mod  b
$$

> Here, *a* is the dividend, *b* is the divisor, and the result is the remainder when *a* is divided by *b*. 

##### applications

1. **Clock Arithmetic:** Modulo 12 is often used to represent time on a clock, where 1:00 PM is equivalent to 13:00 (1 + 12).
2. **Cryptography:** Modulo operations are used in various cryptographic 密码学的  algorithms.
3. **Data Structures:** Modulo is used in hash functions for indexing into arrays, ensuring that the result stays within the array bounds.
4. **Programming:** In programming languages, the modulo operator is commonly used for tasks like checking if a number is even or odd (*n*  mod 2), cycling through a range of values, or ensuring that an index wraps around in circular data structures.





####  Run Times

##### Insertion Behavior - O(1), Ω(1), Θ(1)

###### Insert Random - O(n)

###### Insert Front - O(1)

###### Insert Back - O(1)



##### Deletion Behavior - O(1), Ω(1), Θ(1)

###### Deletion Random - O(1) or O(n)

If you are given the index of the element to be deleted, you can directly access and remove the element in O(1) time. This is because, in a circular array, you can compute the actual index in constant time using the modulo operation.

However, if you are given the value of the element to be deleted and you need to search for its index first, then the time complexity becomes O(n), where n is the number of elements in the array. This is because you may need to traverse the entire array to find the element to be deleted.

###### Deletion Front - O(1)

###### Deletion Back - O(1)



##### Search Behavior

###### Search Unsorted- O(n)

###### Search Sorted- O(log(n))

##### Access Time - O(1)



### Dynamic Arrays

a resizable array

> its size can be dynamically changed during the execution of a program. 

> In many programming languages, dynamic arrays are implemented using structures like Python's list, Java's ArrayList, or C++'s vector. 

 automatically resize itself when elements are added or removed 

> When the capacity of the dynamic array is reached, it allocates a new, larger block of memory, copies the existing elements, and releases the old memory block. Similarly, when elements are removed, it may shrink the array to save memory. 

#### why we need circular array? - Θ(1) \ O(n)

A dynamic array gives us the ability to expand our array whenever we run out of room. This means we don’t need to know how much data is being input beforehand

#### How to get it?

<img src="picture\dynamic array.jpg" alt="dynamic array" style="zoom: 70%;" />

Expanding our array each time we run out of data however runs in O(n) time. This is because once an array is allocated, it can’t be expanded. 

So what we do is create a new array with a new size, and then transfer over all of the contents from the previous array. This though requires we touch every single piece of data in the array, making the O(n) time. 

We can however improve this if we think about the problem a little bit further. Instead of increasing the size of the array by 1 each time when we run out of data, we can instead double the size of the array. 

For this, we use the terms **logical size**, and **physical size**. The logical size is how many pieces of data are actually allocated in the array. The physical size is the size of the array itself. So what we want to do, is every time our logical size reaches our physical size, we want to double the physical size.

This doubling provides a less and less frequent use of the O(n) copying operation, which overall leads to something called an amortized O(1) relationship. **Amortize here just means averaged.** 

<img src="picture\prove dynamic array.jpg" alt="prove dynamic array" style="zoom: 70%;" />
$$
\text{最终得到这个式子：}
M = (k+1)*O(n)+(2^k-2k-1)*O(1)
$$
当 *k* 趋近于正无穷时，我们关注 *M* 中增长最快的项，因为它将主导整个表达式。 
$$
\text{当 k 趋近于正无穷时，M 的极限值将取决于 }2^k\text{ 的增长速度。}
\text{ }\\
\text{由于指数函数 }2^k\text{ 的增长是指数级的，它将迅速趋近于正无穷。}
\text{ }\\
\text{也就意味着，} 2^k
\text{的增长速度远远超过 k，因此我们可以忽略 k 的项。}\\
\text{ }\\
因此，我们可以简化 M 为：2^k*O(1)\\
$$
This means is that it is technically O(n) because of the copy operation, but when averaged out to infinity, it more closely resembles that of O(1). Because of this, we can say it's basically O(1). 

**There is also a space-time complexity that needs to be thought of with this problem.** The more you allocate after each “full” insert, the more chance there is of wasted space. It may speed up the run time, but may cost you a lot of storage space.

For example, let's say you have an array with 65,536 slots that gets filled up. If we want to add another element to this, we will then have an array which is 131,072 elements big. That is a gigantic leap. So this is usually optimized depending on the program. 

#### testing question

In a Dynamic Array, how long does it take to increase the size of the array? (So the actual operation of expanding, not the average) 

- Allocating a new array has a time complexity of O(1) for each element since it involves a single operation for each element.
- Copying the elements has a time complexity of O(n), where n is the number of elements in the array being resized.

> Since the copying operation dominates the time complexity, the overall time complexity for increasing the size of the array is O(n), where n is the current number of elements in the array. In Big O notation, we often consider the worst-case scenario, and this worst case occurs when we need to copy all existing elements to the new array.
>
> It's important to note that while resizing can be an expensive operation in terms of time complexity, the amortized time complexity (average time per operation over a sequence of operations) for dynamic array insertions is still O(1) due to the infrequency of resizing events and the geometric progression of the array size increase.



### Multidimensional Arrays

have more than one dimension.

> used to represent tables of values consisting of multiple rows and columns. 



#### why we need it?

1. **Tabular Data Representation:**
   - Multidimensional arrays are well-suited for representing tabular data, such as matrices or tables with rows and columns.
   - This makes it easier to visualize and work with structured data, like spreadsheets or images.

2. **Mathematical and Scientific Computations:**
   - In scientific computing and mathematics, multidimensional arrays are essential for representing tensors and other multi-dimensional data structures.
   - Operations involving matrices and higher-dimensional tensors are common in linear algebra, machine learning, and scientific simulations.

3. **Image and Signal Processing:**
   - In image processing, pixel values are often organized in a 2D array.
   - Signal processing applications may involve 1D or 2D arrays to represent time-series data or two-dimensional signals.

4. **Game Development:**
   - In computer graphics and game development, multidimensional arrays are used to represent and manipulate images, textures, and three-dimensional models.

5. **Grid-based Problems:**
   - Problems that can be conceptualized as grids or boards, such as chess boards, game boards, or geographical maps, are often represented using multidimensional arrays.



#### how can we get it?

The way you access and manipulate elements in multidimensional arrays depends on the programming language you're using.



#### types

##### 2D Arrays (Two-Dimensional Arrays)

each element is identified by two indices (row and column).

```python
two_d_array = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
```

##### 3D Arrays (Three-Dimensional Arrays)

Each element is identified by three indices (depth, row, and column).

```python
three_d_array = [
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ],
    [
        [13, 14, 15, 16],
        [17, 18, 19, 20],
        [21, 22, 23, 24]
    ]
]
```

##### N-Dimensional Arrays

each element is identified by N indices.

> can be useful in certain mathematical and scientific applications. 





## **Binary Search Algorithm**

an efficient algorithm for finding a specific target value within a sorted array 

> works by repeatedly dividing the search interval in half 
>
> The time complexity of the binary search algorithm is O(log n) 

### Steps

#### Initialization

- Begin with the entire sorted array.
- Set the left pointer (`low`) to the index of the first element and the right pointer (`high`) to the index of the last element.

#### Midpoint Calculation

- Calculate the middle index as `mid = (low + high) / 2`. 小数点后直接舍去

#### Comparison

- Compare the target value with the element at the middle index.
- If the target is equal to the middle element, the search is successful, and the index is returned.
- If the target is less than the middle element, update `high = mid - 1` to search in the left half.
- If the target is greater than the middle element, update `low = mid + 1` to search in the right half.

#### Repetition

- Repeat steps Midpoint Calculation and Comparison until the target is found or the search interval becomes empty (low > high).
- If the target is found, return its index; otherwise, indicate that the target is not in the array. 

### Python code

```python
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]

        if mid_value == target:
            return mid  # Target found
        elif mid_value < target:
            low = mid + 1  # Search in the right half
        else:
            high = mid - 1  # Search in the left half

    return -1  # Target not found

# Example usage:
sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_value = 7
result = binary_search(sorted_array, target_value)

if result != -1:
    print(f"Target {target_value} found at index {result}.")
else:
    print(f"Target {target_value} not found in the array.")
```







# **Linked Lists**

a data structure which consists of a sequence of elements, where each element points to the next one in the sequence. 

> linked lists do not have a fixed size in memory, and their elements can be scattered in different locations in memory. 
>
> An important difference between linked lists and arrays is that the data in the linked list aren’t directly accessible.  

<img src="picture\linked list.jpg" alt="linked list" style="zoom: 70%;" />



##  node 

basic building block of a linked list

- a data field to store the actual data
- a reference (or link) field that points to the next node in the sequence. 

> The last node in the list typically has a reference pointing to a special value like **null or NIL** to indicate the end of the list. 
>
> The very first node is designated as the “**head**” of the linked list. It is the node that is always pointed to when we call our linked list. This head is important, without it, we would lose our entire linked list. 

```
Node 1          Node 2          Node 3
+------+       +------+       +------+
| data |       | data |       | data |
+------+       +------+       +------+
| next |  -->  | next |  -->  | next |  (Reference to the next node)
+------+       +------+       +------+
```

> 在大多数编程语言中，内存管理和分配都是从开发人员那里抽象出来的。 当您创建对象（例如节点）的实例时，内存管理器为对象分配唯一的内存地址。 内存管理器处理内存分配和管理的低级细节。
>
> 开发者没有显式控制每个节点的内存地址，而是使用这些对象的引用或指针。 该引用包含下一个节点的内存地址。 
>
> 遍历链表从头（第一个节点）开始，并使用引用从一个节点移动到下一个节点，直到到达链表末尾。 



**内存管理器怎么建立节点和内存之间的联系？** 

**1-**当程序请求创建一个新的对象（如一个节点）时，内存管理器负责在堆（heap）中分配一块足够大小的内存空间。将这块内存标记为已分配。这块内存的起始地址就是对象的地址。

**2-**内存管理器将分配的内存块的起始地址返回给程序。这个地址可以被保存在对象的引用（reference）或指针中。

> 在这里，"指针"指的是一个指向分配的内存块的内存地址的数值。具体而言，这是一个指向动态分配内存的指针。 
>
> 在编程语言中，指针变量本身也需要存储在某个地方，它通常存储在栈（stack）或堆（heap）中，取决于指针的声明和生存周期。 
>
> - 如果指针是在函数内部声明的，并且没有通过动态分配内存而是指向栈上的变量，那么指针本身通常存储在栈上。栈上的内存管理是由程序的执行环境（例如操作系统和编程语言的运行时系统）自动处理的。 
> - 如果指针是通过动态内存分配函数（如 `malloc`、`calloc` 或 `new`）分配的内存块，并且它的生命周期超过了函数的范围，那么指针本身通常存储在堆上。 在这种情况下，指针变量本身是动态分配的，需要手动释放分配的内存，以免出现内存泄漏。
>
> 栈和堆是计算机内存中不同的区域，它们用于存储不同类型的变量和数据结构。指针本身的值是一个内存地址，这个地址指向分配的内存块。在栈上，指针变量的值存储在当前函数的栈帧中；在堆上，指针变量本身的内存也是通过动态分配的。 

**3-**程序通过引用或指针访问对象，并初始化对象的字段，比如给节点的 data 赋值。编译器会生成相应的机器代码，该代码将值存储到节点的内存地址中。编译器会知道节点 data 字段的偏移量，并生成适当的机器指令来执行这个操作。

**4-**如果这个对象是一个节点，程序将通过引用将这个节点与其他节点关联。在一个链表中，节点的 next 字段就是关联下一个节点的引用。





## advantages and disadvantages 

### pros

can easily grow or shrink in size

can contain multiple different types of data. 

### cons

accessing elements in a linked list can be slower compared to arrays





## Types

### Singly Linked List

Each node points to the next node in the sequence.

> an one-direction arrow reference points to the next node

#### delete one node between the lists

<img src="picture\delete one node.jpg" alt="delete one nod" style="zoom: 70%;" />

#### insert one node between the lists

<img src="picture\insert one node.jpg" alt="insert one node" style="zoom: 70%;" />



 #### Run Times

- insert randomly - O(n) \ Θ(*n*)
- insert front - O(1)
- insert back - O(n)

- delete front - O(1)
- delete back - O(n)
- delete randomly - O(n) \ Θ(*n*)

- search sorted - O(n) \ Θ(*n*)
- search unsorted - O(n) \ Θ(*n*)

- access time - O(n) \ Θ(*n*)

#### Code example and explain

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

# Example usage:
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)

linked_list.print_list()
```

```python
# This class represents a node in the linked list.
class Node:
    # The __init__ method is a constructor that initializes the node with the provided data and sets the next reference to None by default.
    def __init__(self, data):
        # two attributes
        self.data = data
        self.next = None

# This class represents the linked list itself.
class LinkedList:
    # The __init__ method initializes the linked list with an empty head.
    def __init__(self):
        # points to the first node in the list.
        self.head = None

    # adds a new node with the given data to the end of the linked list.
    def append(self, data):
        # creates a new node
        new_node = Node(data)
        # If the linked list is empty (i.e., self.head is None), it sets the head to the new node.
        if not self.head:
            # the head attribute of the linked list is set to the new node, making it the first and only node in the list.
            self.head = new_node
            return
        # If the list is not empty, it traverses the list to find the last node and sets the next reference of the last node to the new node.
        # a variable last_node is initialized with the head of the list.
        last_node = self.head
        # This loop iterates through the list until it finds the last node.The condition last_node.next checks if the current node has a next node.
        while last_node.next:
            # Inside the loop, last_node is updated to the next node in the sequence.
            last_node = last_node.next
        # Once the loop finds the last node (i.e., last_node.next is None), it sets the next reference of the last node to the new node.
        last_node.next = new_node

    # prints the elements of the linked list in order.
    def print_list(self):
        # starts from the head and iterates through the list
        current_node = self.head
        # continues until it reaches the end of the list (when current_node is None).
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

# Example usage:
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)

linked_list.print_list()
```







### Doubly Linked List

Each node has **two references**, one pointing to the next node and another pointing to the previous node. as well as creating **a tail pointer.** 

> two one-direction arrows with one node, in which one arrow points to the previous node and the other points to the next node.

#### why we need doubled linked lists?

<img src="picture\doubled linked lists.jpg" alt="doubled linked lists" style="zoom: 70%;" />

- they allow for easy traversal in both directions.
- Insertion and deletion of nodes are more efficient in doubly linked lists compared to singly linked lists.
- Reversing a doubly linked list is straightforward.
- Some algorithms and data structures, such as certain types of sorting algorithms, benefit from bidirectional traversal and easy node removal, making doubly linked lists a more suitable choice.
- While doubly linked lists require more memory per node due to the extra pointer, the additional flexibility they provide in terms of traversal and manipulation can outweigh this drawback in certain scenarios.
- can be easily adapted to create circular lists where the last node points back to the first one.

> Comparison in Real Life: O(2n) and O(n)
>
> 考虑这样一种场景，您有两种算法，一种具有 O(n) 复杂度，另一种具有 O(2n) 复杂度，解决相同的问题。 
>
> 如果输入大小加倍，算法的时间或空间要求也将大致加倍。 例如，如果处理时间为 T(n)，则对于 O(n)，新的处理时间可能与 2 * T(n) 成正比。对于 O(2n)，如果输入大小加倍，算法的时间或空间需求将大约增加四倍。 处理时间可能与 4 * T(n) 成正比。
>
> 在实际情况中，复杂度为 O(2n) 的算法可能意味着它的效率低于复杂度为 O(n) 的算法，尤其是随着输入大小的增长。O(n)代表更有利的线性增长，而O(2n)代表具有更大常数因子的线性增长。
>
> 然而，值得注意的是，常数因素和其他考虑因素也会发挥作用，有时，对于小输入大小或其他因素更为关键的情况，O(2n) 算法仍然可以接受。



#### Tail pointer

> - In a doubly linked list, you have nodes with both "**next**" and "**previous**" pointers.
> - The "**head**" of the list is the first node, and the "**tail**" is the last node. 

**By default, we have a “head” pointer.** This, as seen in the picture above, points to the beginning of a list. It is used to give us a node to start our traversals from. **Without it, we would have no way of getting to the beginning of the list, and therefore the list would be lost in memory.**

We however can also create another pointer, a “tail” pointer. This will point directly to the very last node added to the list. A tail pointer is a small addition that can improve the deletion and insertion to the back of the list. 

##### How does this help us? 

Well think of the two cases in which we want to delete or add information to the back of the list. Without a tail pointer we have to traverse the entire list until we get to the end, which by default is an O(n) operation. 

> So in the example H<->E<->A<->P (<-> signifies doubly-linked). **Even with it being doubly-linked, it would still take O(n) operation to get to the back, and then O(n) operation to print from back to front.**This would create O(2n) as the final run time. (This is simplified down to O(n) sure, but efficiency does matter at some point). 
>
> With a tail pointer however, we can just start directly on the end, and then add or delete from there. This takes the O(n) operation and brings it back to O(1). So now our print back to front will require a O(1) + O(n) operation, which is just a natural O(n) timing. 



#### Run Times

- insert randomly - O(n) \ Θ(n)
- insert front - O(1)
- insert back - O(n) \ O(1) with a tail pointer

- delete front - O(1)
- delete back - O(n) \ O(1) with a tail pointer
- delete randomly - O(n) \ Θ(n)

- search sorted - O(n) \ Θ(n)
- search unsorted - O(n) \ Θ(n)

- access time - O(n) \ Θ(n)





### Circular Linked List

the last node points back to the first node, forming a loop.

> Terminating a circular linked list involves breaking the cycle by setting the "next" pointer of the last node to `None` (or another suitable termination condition). 

> a circular linked list does have a concept similar to a head, which is  often referred to as the "start" or "head" node. In a circular linked  list, there isn't a distinct separation between the head and the tail,  as the last node in the list points back to the first node, forming a  loop. However, for ease of implementation and understanding, the term  "head" is commonly used to represent the starting point of the circular  linked list. 

> It's important to note that in a circular  linked list, you can start traversal from any node, and by following the "next" pointers, you will eventually return to the node from which you  started. 

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            # If the list is empty, set the new node as the head
            self.head = new_node
            new_node.next = self.head
        else:
            # Traverse to the last node and make it point to the new node
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

# Example usage:
cll = CircularLinkedList()
cll.append(1)
cll.append(2)
cll.append(3)
```



#### why we need doubled linked lists?

Circular Buffers/Ring Buffers:

   - Circular linked lists are useful for implementing circular buffers or ring buffers. In such scenarios, data is written to the buffer until it is full, at which point the write operation continues from the beginning of the buffer.

> it's important to note that they also come with challenges, such as the need for careful handling to avoid infinite loops and ensuring proper termination conditions when traversing the list.



# **Stack and Queue**

 fundamental data structures 

> While you can implement stacks and queues using arrays or linked lists,  each structure has its unique properties that make it suitable for  specific scenarios. 
>
> Linked lists are usually best for these structures, as they can expand indefinitely. 

> In the context of software implementation, the computer keeps track of  the "top" of a stack or the "front" and "rear" of a queue using  variables or pointers. These variables or pointers point to the memory  location of the current position of interest within the data structure. 



## Why use a stack or queue, what makes them special?

In computer science, modeling is very important. Through modeling and abstraction we can take a machine that only does 1’s and 0’s and turn it in to anything we want. 

Stacks and queues are just another example of this abstraction. It’s just another layer of rules to add onto a pre-existing structure, so that we can control the data in a slightly different manner. 

- Stacks are widely used in almost every aspect of computer design. Just through reading your email, hundreds of stacks are probably being implemented. 
- Processors love queues as they give it a linear set of instructions to execute.



## Pointer

A pointer is a variable that stores the memory address of another variable or data structure. It "points" to the location in memory where the actual data is stored.

Pointers are commonly used in low-level programming and data structure implementations.

In the context of stacks and queues, pointers are frequently used to keep track of the current position within the data structure.

> These pointers are managed by the programming language and are translated into specific memory addresses by the compiler and runtime environment. 
>
> The hardware then interacts with these memory addresses to read and write data.





## Stack

<img src="picture\stack.jpg" alt="stack" style="zoom: 40%;" />

a Last-In, First-Out (LIFO) or “Last Come, First Served(LCFS)” relationship

data structure, meaning that the last element added is the first one to be removed.

>Stacks are a data structure that are built off the backs of other data structures. They work off a set of important rules. These rules are usually applied to either a linked list or array. It’s like a specialization. Through the rules we are able to create a specialized structure with new pros and cons. 

> pushing elements onto the **top** of the stack and popping elements off the top. This means you will have a relationship where the most recentelement that has come, will be the first serviced. 
>
> The "top" of the stack is typically represented by a variable or pointer.
>
> - When an element is pushed onto the stack, the "top" is incremented or adjusted to point to the new top element.
> - When an element is popped from the stack, the "top" is decremented to move to the next element.

1. **Push:** Adds an element to the top of the stack.
2. **Pop:** Removes the element from the top of the stack.
3. **peek \ top:** Retrieves the element from the top of the stack without removing it, to see what the next pop operation would reveal. 
4. **isEmpty:** Checks if the stack is empty. Returns true if the stack has no elements, false otherwise.

Visualized as **a vertical structure** with elements stacked on top of each other. 

> Think of a stack of plates where you add and remove plates from the top. 



### code

```python
# implement a stack using arrays
class StackUsingArray:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)
    
# implement a stack using linked lists.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackUsingLinkedList:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.is_empty():
            popped_item = self.top.data
            self.top = self.top.next
            return popped_item

    def peek(self):
        if not self.is_empty():
            return self.top.data

    def size(self):
        current = self.top
        count = 0
        while current:
            count += 1
            current = current.next
        return count
```

```python
# implement a stack using
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        # The "not" keyword is a logical negation operator. It negates the result of the expression that follows it. "not self.is_empty()" 当栈不是空的时候为 True，当栈是空的时候为 False。
        if not self.is_empty():
            # in Python, the list.pop() method removes and returns the last item from the list.
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]   # refers to the last element.

    def size(self):
        return len(self.items)
    
# Create a stack
my_stack = Stack()

# Push elements onto the stack
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

# Pop elements from the stack
print(my_stack.pop())  # Output: 3
print(my_stack.pop())  # Output: 2

# Peek at the top element without removing it
print(my_stack.peek())  # Output: 1

# Check if the stack is empty
print(my_stack.is_empty())  # Output: False

# Get the size of the stack
print(my_stack.size())  # Output: 1
```



### use

- navigate through a maze
- helping traverse a graph.  遍历图表 

- This mimics real-world scenarios where items are stacked on top of each other, and the top item is accessed or removed first. 
- When a function is called, the return address and local variables are  pushed onto the call stack. When the function completes, the stack is  popped, and control returns to the calling function. 
- Many applications use a stack to implement an undo and redo mechanism. Each  action (e.g., typing, formatting) is pushed onto a stack, and the undo  operation pops the last action from the stack to revert changes. 
- Stacks play a crucial role in managing memory in computer systems. The call stack is used for storing local variables and managing function calls, while the system stack is used for handling interrupts and exceptions.
- In algorithms and artificial intelligence, stacks are used for backtracking. For example, depth-first search in a graph is often implemented using a stack to keep track of the explored nodes.

> Notice how it looks like we are "stacking" books or trays up. We keep stacking. Then when we want to remove one, we take it off the top. We never remove from anywhere else in a stack!
>
> Now, if we kept popping and pushing in a loop, we would get a situation where the first data could potentially never be touched again. 
>
> For this reason, these aren't typically used for scheduling purposes. Imagine if you used a stack to run your computer. Old windows would be frozen indefinitely as new requests keep getting serviced first. 



### Run Time

- insert randomly - O(n)
- insert front - O(1) 
- insert back- Not applicable

- delete randomly - O(n) 
- delete front - O(1) 
- delete back - Not applicable 

- search sorted - O(n) 
- search unsorted - O(n)





## Queue

<img src="picture\queue.jpg" alt="queue" style="zoom: 100%;" />

a First-In, First-Out (FIFO) data structure, meaning that the first element added is the first one to be removed.

> enqueuing elements at the **rear** (or **back**) and dequeuing elements from the **front**. 
>
> The "front" and "rear" of a queue are also represented by variables or pointers.
>
> - When an element is enqueued, the "rear" is adjusted to point to the new rear element.
> - When an element is dequeued, the "front" is adjusted to move to the next element.

1. **Enqueue:** Adds an element to the rear of the queue.
2. **Dequeue:** Removes the element from the front of the queue.
3. **peek:**  Retrieves the element at the front of the queue without removing it, to check who is at the front of the line without serving them.
4. **isEmpty:** Checks if the queue is empty. Returns true if the stack has no elements, false otherwise.

Visualized as **a horizontal structure** with elements forming a line. 

> Think of people waiting in line, where the first person in line is served first. 



### code

```python
# Using an Array to Implement a Queue
# note that using pop(0) for dequeuing has a time complexity of O(n), making it less efficient compared to using a doubly linked list.
class QueueUsingArray:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
    
# using a circular array to implement the queue
class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, item):
        if not self.is_full():
            if self.is_empty():
                # If the queue is empty, set both front and rear to 0
                self.front = self.rear = 0
            else:
                # If the queue is not empty, move the rear to the next position (circular)
                self.rear = (self.rear + 1) % self.capacity
            # Add the item to the rear of the queue
            self.queue[self.rear] = item
        else:
            print("Queue is full. Cannot enqueue item:", item)

    def dequeue(self):
        if not self.is_empty():
            # Get the item at the front of the queue
            removed_item = self.queue[self.front]
            if self.front == self.rear:
                # If there is only one element in the queue, set both front and rear to -1
                self.front = self.rear = -1
            else:
                # If there is more than one element, move the front to the next position (circular)
                self.front = (self.front + 1) % self.capacity
            return removed_item
        else:
            print("Queue is empty. Cannot dequeue.")

    def size(self):
        if self.is_empty():
            return 0
        elif self.front <= self.rear:
            return self.rear - self.front + 1
        else:
            return self.capacity - self.front + self.rear + 1
```

```python
# Using a Linked List to Implement a Queue:
# A doubly linked list is a commonly used data structure for implementing a queue efficiently. You can enqueue elements by adding to the rear (tail) and dequeue elements by removing from the front (head).
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class QueueUsingLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if not self.is_empty():
            dequeued_item = self.front.data
            if self.front == self.rear:
                self.front = self.rear = None
            else:
                self.front = self.front.next
                self.front.prev = None
            return dequeued_item

    def is_empty(self):
        return self.front is None
    	# If self.front is None, it means the queue is empty, and the method returns True. 
        # If self.front is not None, it means there is at least one element in the queue, and the method returns False.

    def size(self):
        count = 0
        current = self.front
        while current:
            count += 1
            current = current.next
        return count

# Choose the implementation that best suits your requirements based on the expected operations and their associated time complexities.
```



```python
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Queue is empty.")

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print("Queue is empty.")

    def is_empty(self):
        return len(self.items) == 0
```



### use

- They are great for processing data where order is important, like CPU operations, or tree traversals.  

- Scheduling











### Run Time

- insert randomly - O(n)
- insert front - O(n) 
- insert back - O(1)

- delete randomly - O(n) 
- delete front - O(1)
- delete back - O(n)

- search sorted - O(logn) 
- search unsorted - O(n)

> 如果使用双向链表实现队列，确实可以在中间执行插入操作，时间复杂度为 O(1)。 在这种情况下，队列允许在前面和后面进行高效的插入，使其成为一种更通用的数据结构。 
>
> 但是，需要注意的是，时间复杂度的分析取决于您正在考虑的具体操作以及实现细节。 对于用单链表实现的标准队列来说，中间的插入确实需要遍历链表来找到插入点，导致时间复杂度为O(n)。 
>
>  因此，在选择数据结构时，考虑应用程序的具体要求以及您将经常执行的操作至关重要。 不同的实现可能会在时间和空间复杂度方面提供不同的权衡。 



## exercise

We have a stack and queue, [-,-,4,3] and [-,-,2,1] respectively. When you  pop off of the stack, it enqueues on to the queue, implemented as a  circular array. (So pop(x) => both pop off the stack, and enqueue(x))

(Front of the queue is currently on 2, and back on 1. We queue on to the front, and remove from the back. **Note: This pattern is different from question 2!**!).    

What will the stack and queue look like after:

1. pop()
2. push(4)
3. pop()
4. dequeue()
5. push(5)
6. push(6)
7. pop()
8. dequeue()
9. push(4)
10. pop()
11. dequeue()

(This question is meant to be a challenge. Get some paper out and try to work it out. If you can't check the next lecture for an  explanation) 

```
stack:[-,-,4,3]
queue:[-,-,2f,1b]
Front of the queue is currently on 2, and back on 1.
When you  pop off of the stack, it enqueues on to the queue
We queue on to the front, and remove from the back.

1. pop()
[-,-,-,3]
[-,4f,2,1b]

2. push(4)
[-,-,4,3]
[-,4f,2,1b]

3. pop()
[-,-,-,3]
[4f,4,2,1b]

4. dequeue()
[-,-,-,3]
[4f,4,2b,-]

5. push(5)
[-,-,5,3]
[4f,4,2b,-]

6. push(6)
[-,6,5,3]
[4f,4,2b,-]

7. pop()
[-,-,5,3]
[4,4,2b,6f]

8. dequeue()
[-,-,5,3]
[4,4b,-,6f]

9. push(4)
[-,4,5,3]
[4,4b,-,6f]

10. pop()
[-,-,5,3]
[4,4b,4f,6]

11. dequeue()
[-,-,5,3]
[4b,-,6f,4]
```





# **Sorting Algorithms**

how to sort the data structures

 [Sorting (Bubble, Selection, Insertion, Merge, Quick, Counting, Radix) - VisuAlgo](https://visualgo.net/en/sorting) 



## Runtime Comparison

| Sorting Algorithms | Best Run Time | Average Run Time | Worst Run Time | Stability |
| ------------------ | ------------- | ---------------- | -------------- | --------- |
| Bubble Sort        | Ω(n)          | Θ(n^2)           | O(n^2)         | stable    |
| Selection Sort     | Ω(n^2)        | Θ(n^2)           | O(n^2)         | unstable  |
| Insertion Sort     | Ω(n)          | Θ(n^2)           | O(n^2)         | stable    |
| Quick Sort         | Ω(nlogn)      | Θ(nlogn)         | O(n^2)         | unstable  |
| Merge Sort         | Ω(nlog⁡n)      | Θ(nlog⁡n)         | O(nlog⁡n)       | stable    |

> **Quadratic Sorting（二次排序）** 指的是 **时间复杂度为 O(n^2) 的排序算法**，因为其执行时间随着输入规模 n 的增长呈 **二次方关系**。这种排序通常适用于小规模数据集，因为它们在大规模数据集上表现较差。



## why is it so important to sort an array?

The search runtime for our arrays is O(n). However, if it's sorted, then it's O(logn), And then we even further said that O(logn) is basically constant time. That means that roughly we can get O(1) from searching an array that is that is sorted, which means **sorting will improve our runtime overall a whole lot**.

- Many search algorithms, like binary search, work efficiently on sorted arrays. 
- In databases, sorted data can be retrieved more efficiently.
- Some algorithms and techniques become more efficient when applied to sorted data. For example, dynamic programming algorithms and greedy algorithms often benefit from having input data in sorted order.





## Recursion

In computer science, recursion is a technique where a function calls itself. Recursive algorithms often have a base case, which is a condition that, when met, stops the recursion and provides a solution directly.

```python
def factorial(n):
    # Base case: factorial of 0 is 1
    if n == 0:
        return 1
    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n - 1)

# Example usage:
result = factorial(5)
print("Factorial of 5:", result)
```

1. **Base Case:** A base case is the condition under which the recursion stops. Without a base case, the function would keep calling itself indefinitely, leading to a stack overflow. 

2. **Divide and Conquer:** a problem is divided into smaller subproblems that are solved independently. The solutions to the subproblems are then combined to solve the original problem.

3. **Function Calls Itself:** In a recursive function, there is a call to the same function within its definition. This is what allows the problem to be solved by breaking it down into smaller instances.

4. **Memory Usage:** Recursion uses the call stack to keep track of function calls. Each recursive call adds a new frame to the call stack. Excessive recursion can lead to a stack overflow, so it's important to design recursive functions with care.



### divide and conquer

"Divide and conquer" is a problem-solving paradigm or algorithmic technique that involves breaking down a problem into smaller subproblems, solving each subproblem independently, and then combining the solutions of the subproblems to solve the original problem. The key steps in the divide-and-conquer approach are as follows:

1. Divide:
   - Break the original problem into smaller, more manageable subproblems. This step is often recursive, meaning that each subproblem may be further divided into even smaller subproblems.

2. Conquer:
   - Solve each subproblem independently. This is typically the base case of the recursion, where the problem is small enough to be solved directly without further division.

3. Combine:
   - Combine the solutions of the subproblems to obtain the solution for the original problem.

The divide-and-conquer strategy is particularly effective for solving complex problems and often leads to more efficient algorithms. This approach is used in various areas of computer science and mathematics, including sorting algorithms, searching algorithms, and algorithmic problem-solving.



### Recursive Base Case for Advanced Algorithms

For sorting algorithms, particularly those with a divide-and-conquer approach like Merge Sort or Quick Sort, recursion is often used to break down the sorting problem into smaller subproblems. 

The base case is the condition under which the algorithm stops the recursive division and directly solves the smaller subproblem.

Here's how Insertion Sort can be used as a base case in a recursive sorting algorithm:

1. Divide-and-Conquer Sorting Algorithm:
   - Imagine you have a sorting algorithm that uses a divide-and-conquer strategy, such as Quick Sort or Merge Sort.
   - The algorithm recursively divides the input into smaller subarrays until it reaches a base case.

2. Base Case:
   - The base case is a condition under which the algorithm stops dividing the array and directly applies a simple sorting algorithm to the remaining small subarrays.
3. Insertion Sort as the Base Case:
   - For small subarrays where the number of elements is below a certain threshold, the algorithm might switch to using Insertion Sort instead of further dividing the array.
   - Insertion Sort is efficient for small datasets and has a low overhead, making it a good choice for the base case.
4. Hybrid Approach:
   - This combination of using a more advanced algorithm for larger subarrays and switching to Insertion Sort for smaller subarrays is a hybrid approach.
   - The goal is to take advantage of the efficiency of more advanced algorithms for larger datasets while benefiting from the simplicity and efficiency of Insertion Sort for smaller datasets.

In summary, the term "recursive base case" refers to the condition in a recursive sorting algorithm under which the recursion stops, and a simpler sorting algorithm, like Insertion Sort, is applied directly to small subarrays. This hybrid strategy aims to balance efficiency and simplicity for various input sizes.





## Adversarial inputs

Adversarial inputs, in the context of algorithms, refer to intentionally crafted input data that is designed to exploit weaknesses or vulnerabilities in the algorithm's behavior. Adversarial inputs are created with the goal of causing the algorithm to exhibit poor performance, high time complexity, or unintended behaviors.

For sorting algorithms like Quick Sort, adversarial inputs are those that, when specifically tailored, can lead to worst-case scenarios. In the case of Quick Sort, the worst-case scenario occurs when the algorithm consistently chooses a poorly selected pivot, resulting in inefficient partitioning and an overall time complexity of O(n^2)

Here's an example to illustrate adversarial inputs for Quick Sort:

**Example:**
Consider a scenario where Quick Sort consistently selects the first element of the array as the pivot. If the input array is already sorted or nearly sorted, this deterministic pivot selection can lead to a worst-case scenario.

1. **Deterministic Pivot Selection:**
   - If the first element is always chosen as the pivot, and the array is sorted in ascending order, each partitioning step may only move one element to its final sorted position.
   - This results in n recursive calls (one for each element in the array), leading to a worst-case time complexity of O(n^2).

2. **Adversarial Input:**
   - An adversarial input, in this case, would be an intentionally crafted sorted array that exploits the deterministic pivot selection, causing the algorithm to perform poorly.

3. **Mitigation with Random Pivot Selection:**
   - Randomized pivot selection helps mitigate the impact of adversarial inputs by introducing an element of randomness. Even if a few poorly chosen pivots occur, the randomness tends to balance out over multiple recursive calls, reducing the chances of consistently poor choices.

In general, algorithms are designed to perform well on average and in typical scenarios. Adversarial inputs challenge these algorithms by intentionally creating scenarios that exploit specific weaknesses. Understanding how algorithms behave in the face of adversarial inputs is crucial for assessing their robustness and making informed decisions about their use in practical applications.

The creation of adversarial inputs is mainly a theoretical concept used  in algorithm analysis and complexity theory to understand the worst-case behavior of algorithms. 

The creation of adversarial inputs is a tool used in theoretical analysis to explore the limits of algorithm performance. While it's important to understand worst-case scenarios, practical considerations and real-world performance often drive the selection and use of algorithms. In practice, algorithms are chosen based on their overall efficiency, ease of implementation, and suitability for the expected range of inputs.





## stability

The concept of stability in sorting algorithms refers to the preservation of the relative order of equal elements during the sorting process.

When a sorting algorithm is stable, if two elements have equal keys in the original input, their order will remain unchanged in the sorted output.

> The stability of an algorithm is an important consideration in certain applications where maintaining the initial order of equal elements is necessary. For tasks like sorting objects with multiple keys or performing secondary sorts, a stable sorting algorithm is preferred. 
>
> Many common sorting algorithms, such as Merge Sort and Insertion Sort, are stable, while others, like Quick Sort, are generally unstable. 

>**Why Stability Matters:**
>
>**Preservation of Input Order**: Stability is often important when the initial order of equal elements carries meaningful information that needs to be preserved.
>
>**Applications with Multiple Sort Keys**: In situations where sorting is performed based on multiple keys (e.g., sorting students by grade and then by name), stability ensures that the sorting algorithm respects the order of the first key when sorting based on the second key.
>
>**Deterministic Behavior**: Stability contributes to the deterministic behavior of the algorithm. With a stable sorting algorithm, the output is more predictable, making it easier to reason about and debug.
>
>**Compatibility with Previous Implementations**: In some cases, the stability of an algorithm is required for compatibility with existing systems or databases that depend on the relative order of equal elements.
>
>**Ease of Implementation**: Stable algorithms simplify the implementation of certain algorithms or data structures that rely on stable sorting. For example, merging two sorted lists can be done more efficiently if the input lists are stable-sorted.

> While stability is a desirable property in many situations, there are cases where it may not be a critical factor. Unstable algorithms might be faster or use less memory, and for tasks where the original order of equal elements is not important, an unstable algorithm could be a valid choice.

### Example

Say we have a data set that contains groups of information. It looks like this:  

```
{  
(Bob, A)  
(Chris, B)  
(Kathy, A)  
(Phillis, B)  
}  
```

> This algorithm is already sorted in to alphabetic order. Now, let’s say we want to sort this algorithm based on the letters on the back end, so A’s come before B’s.  

If we use a non-stable sorting algorithm, we could very well get a result that looks like this: 

```
{  
(Chris, A)  
(Phillis, A)  
(Kathy, B)  
(Bob, B)
}  
```

> If you notice, the A’s and B’s have been sorted, however the order of the names wasn’t respected (Kathy now comes before Bob). Because of the non-stable nature of the sorting algorithm, we lost the alphabetical grouping of the names.  

This is situation where a stable sorting algorithm would be important. If we applied a stable  sorting algorithm to this group, we would instead get:  

```
{  
(Chris, A)  
(Phillis, A)  
(Bob, B)  
(Kathy, B)  
}  
```

> Now, not only are the names sorted by A’s and B’s, but they are also sorted with respect to the order they came in, which was alphabetical.  



### Test question

What does stability in a sorting algorithm mean?  

A. It will not crash your computer.

B. It will sort correctly.

C. The position in the list will be preserved.

>C is Correct! The position within the array will be preserved. This is  important when doing something like a double sort on an array. The first for alphabetical, and then the second by date. With an unstable sort,  the first sort will be broken.  





## Bubble Sort

a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. Continue this process until the list is sorted. 

> it is generally not recommended for large datasets due to its quadratic time complexity. 

> The name "Bubble Sort" comes from the way smaller elements gradually "bubble" to the top of the array (or larger elements to the bottom) during each pass of the algorithm.



### Why it is bad?

The worst-case scenario for the Bubble Sort algorithm occurs when the input array is in reverse order, meaning that the largest element is at the beginning of the array, and the smallest element is at the end. 

In this case, Bubble Sort will require the maximum number of comparisons and swaps in each pass, leading to its worst-case time complexity.

- Compare and swap elements throughout the entire array, moving the largest element to the last position. (n times)

- Again, compare and swap elements throughout the array, moving the second-largest element to the second-to-last position.

- Repeat this process for each pass until the entire array is sorted. (repeat n times)

This leads to a worst-case time complexity of O(n^2), making Bubble Sort highly inefficient for large datasets in comparison to more advanced sorting algorithms like Merge Sort or Quick Sort, which have better average and worst-case time complexities.



### Algorithm Steps

1. Start from the beginning of the array.
2. Compare the first two elements. If the first element is greater than the second, swap them.
3. Move to the next pair of elements and repeat the comparison and swapping process.
4. Continue this process until the end of the array is reached. At this point, the largest element is guaranteed to be at the end of the array.
5. Repeat the process for the remaining elements in the array, excluding the last one that is already in its correct position.
6. Continue this process until the entire array is sorted.



###  Code Example

```python
def bubble_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already sorted, so we don't need to check them
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Example usage:
my_list = [64, 34, 25, 12, 22, 11, 90]
print("Original List:", my_list)
bubble_sort(my_list)
print("Sorted List:", my_list)
```



### Time Complexity

- a worst-case time complexity of O(n^2), where 'n' is the number of elements in the array.
- In the best case, if the array is already sorted, it has a time complexity of Ω(n).
- The average-case time complexity is also Θ(n^2).

### Space Complexity 

an in-place sorting algorithm, meaning it doesn't require additional memory to sort the array.





## Selection Sort

a simple sorting algorithm that divides the input list into two parts: a sorted and an unsorted region. The algorithm repeatedly selects the smallest (or largest) element from the unsorted region and swaps it with the first unsorted element.

> It is not commonly used in practical scenarios for large datasets due to its quadratic time complexity. 

> The term "Selection" in "Selection Sort" comes from the fact that, at each step of the algorithm, it selects or chooses the smallest (or largest) element from the unsorted portion of the array and places it in its correct position in the sorted portion.



### Algorithm Steps

1. The algorithm starts with the entire array considered as unsorted.
2. The algorithm iterates through the unsorted part of the array to find the minimum element.
3. Once the minimum element is found, it is swapped with the first element of the unsorted region.
4. The sorted region is expanded to include the newly swapped element, and the unsorted region is reduced.
5. Steps 2-4 are repeated until the entire array is sorted.



### Code Example

```python
def selection_sort(arr):
    n = len(arr)

    # Traverse through all array elements starting from 0
    for i in range(n):
        # Assume the current index is the minimum
        min_index = i

        # Iterate through the unsorted part of the array to find the minimum element
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Example usage:
my_list = [64, 25, 12, 22, 11]
print("Original List:", my_list)
selection_sort(my_list)
print("Sorted List:", my_list)
```



### Time Complexity

time complexity of O(n^2) in all cases, where 'n' is the number of elements in the array.

### Space Complexity

an in-place sorting algorithm, meaning it doesn't require additional memory proportional to the size of the input.

### Stability

not a stable sorting algorithm, meaning that the relative order of equal elements might change during sorting.





## Insertion Sort

a simple sorting algorithm that builds the final sorted array one element at a time.

it performs well for small datasets or partially sorted datasets and is often used in practice for small inputs or as the recursive base case for more advanced algorithms.

> It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.  



### Algorithm Steps

1. The algorithm starts with the assumption that the first element in the array is already sorted.
2. Iterate through the unsorted part of the array. For each element, compare it with the elements in the sorted region and insert it at the correct position in the sorted region by shifting the larger elements to the right.
3. The sorted region is expanded to include the newly inserted element, and the unsorted region is reduced.
4. Steps 2-3 are repeated until the entire array is sorted.



### Code Example

```python
def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]

        # Move elements of arr[0..i-1] that are greater than key
        # to one position ahead of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

# Example usage:
my_list = [12, 11, 13, 5, 6]
insertion_sort(my_list)
print("Sorted array:", my_list)
```



### Time Complexity

- The worst-case time complexity of Insertion Sort is O(n^2).
- The best-case time complexity occurs when the array is already sorted, making it O(n).
- The average-case time complexity is also O(n^2).

### Space Complexity

Insertion Sort is an in-place sorting algorithm, meaning it does not require additional memory proportional to the size of the input.

### Stability

Insertion Sort is stable, meaning that the relative order of equal elements remains unchanged during sorting.





## Quick Sort

“fast” sorting algorithm

a widely used and efficient sorting algorithm that follows the divide-and-conquer paradigm.

The key idea behind Quick Sort is to partition the array into smaller segments, recursively sort each segment, and then combine the sorted segments to get the final sorted array.

<img src="picture\quick sort.jpg" alt="quick sort" style="zoom: 50%;" />

>在选择了主元后，通过比较，将数组中小于主元的元素放在它的左边，大于主元的元素放在右边。这个时候，主元被放在了它最终的位置上。
>
>之后，对划分得到的左右两个子数组进行递归排序。递归的过程中，主元已经在其最终的位置上，不再需要额外处理。

> This sorting algorithm uses a smart way to  divide the data so that it can reduce the run time. This comes at the cost of added complexity.  
>
> Because the algorithm involves careful handling of pivot selection and  partitioning, making its implementation more intricate than simpler  sorting algorithms like bubble sort or insertion sort. 





### Algorithm Steps

1. Choose a pivot element from the array. The pivot's choice can vary (e.g., first, last, middle, or randomly selected element). 
2. Rearrange the array elements such that all elements smaller than the pivot are on the left, and all elements greater than the pivot are on the right. 
3. The pivot is now in its final sorted position.
4. Recursively apply Quick Sort to the subarrays on the left and right of the pivot.

> No explicit combining step is needed as the array is sorted in place during the partitioning process.



### Code Example

```python
def quick_sort(arr, start=0, end=None):
    if end is None:
        end = len(arr) - 1

    if start < end:
        # Partition the array, get the index of the pivot
        pivot_index = partition(arr, start, end)

        # Recursively sort the subarrays
        quick_sort(arr, start, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, end)

def partition(arr, start, end):
    pivot = arr[end]
    i = start - 1

    for j in range(start, end):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1

# Example usage:
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
quick_sort(arr)
print(arr)
```



### Time Complexity

- The average-case time complexity of Quick Sort is O(n log n), making it one of the fastest sorting algorithms in practice.
- The worst-case time complexity is O(n^2), but this occurs rarely in practice and can be mitigated with optimizations (e.g., choosing a good pivot strategy).

>每个递归层次中，数组被划分为两个部分。树的高度是递归调用的次数。如果每层都将数组对半分，而递归调用次数为log n，则总计O(log n)个层次。 
>
>每个层次上，你在整个数组上进行操作，该操作的工作量与该层级上的数组大小成比例。 在每个层次上，你都会做O(n)的工作（处理每个元素一次：对比 n-1 次，选pivot 1 次，加起来 n 次）。
>
>将每个层次的工作（O(n)）乘以层次的数量（O(log n)），得到的结果是O(n log n)的总时间复杂度。

> The worst-case time complexity of quicksort is O(n^2), and this occurs when the pivot selection and partitioning lead to highly  unbalanced subproblems, means at each recursive step, the pivot  chosen is either the smallest or largest element in the current  subarray. 
>
> In the worst-case scenario, the pivot selection consistently leads to one subarray of size 0 and another subarray of size (n-1). 

> 快速排序的平均情况时间复杂度为 O(n log n)，因为平均而言，该算法倾向于表现出平衡的划分行为，即使存在复杂度较高的情况（最坏情况场景） 。 加权平均值说明了这种最坏情况在实践中不太可能发生的事实。 
>
> 快速排序的平均情况时间复杂度并不是最好情况和最坏情况复杂度的简单平均。 它受到算法执行过程中遇到不同情况的概率的影响。
>
> 平均情况时间复杂度考虑了所有可能输入的预期性能，并考虑了主元选择和分区的各种场景。 在实践中，快速排序的平均性能往往非常好，分区会导致更平衡的子问题。 平均情况分析涉及考虑不同情况发生的概率，然后取加权平均值。 当使用随机或仔细选择的主元时，遇到高度不平衡分区（导致最坏情况）的概率相对较低。 



###  Space Complexity 

Quick Sort is an in-place sorting algorithm, meaning it doesn't require additional memory proportional to the size of the input.



### Stability

Quick Sort is not stable by default. However, stability can be achieved with additional effort and is generally not a primary concern for Quick Sort.



### Optimizations

#### Randomized Pivot: 

Choosing the pivot randomly can help avoid worst-case scenarios.

```python
import random

def quick_sort(arr, start=0, end=None):
    # Check if the end parameter is None (initial call)
    # 如果没有提供结束索引，就将结束索引设置为列表长度减1
    if end is None:
        end = len(arr) - 1
	
    # Check if there is more than one element in the subarray
    # 检查起始索引是否小于结束索引，如果是，进行排序；否则，不需要排序
    if start < end:
        # Partition the array, get the index of the pivot
        # 随机选择一个索引作为基准元素的位置
        pivot_index = random_partition(arr, start, end)

        # Recursively sort the subarrays
        # 对基准元素左右的子数组进行递归排序
        quick_sort(arr, start, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, end)

def random_partition(arr, start, end):
    # Randomly choose the pivot index
    # 随机选择一个索引作为基准元素的位置
    pivot_index = random.randint(start, end)
    
    # Swap the chosen pivot with the rightmost element
    # 将选定的基准元素与数组中最右边的元素进行交换
    arr[pivot_index], arr[end] = arr[end], arr[pivot_index]
    
    # Perform regular partition using the new pivot
    # 调用常规的partition函数，返回新的基准元素位置
    return partition(arr, start, end)
        
def partition(arr, start, end):
    # Choose the rightmost element as pivot
    # 将最右边的元素作为基准元素
    pivot = arr[end]
    # Initialize the index of the smaller element
    # 初始化较小元素的索引：用来表示当前已经处理的小于等于基准元素（pivot）的元素的最右边位置。这个索引 i 的初始值是 start - 1，其中 start 表示当前子数组的起始位置。
    # i 的作用是在遍历过程中找到小于等于基准元素的元素，然后将它们交换到数组的左边。最后，基准元素会被放置在 i + 1 的位置上，这就完成了一次划分。
    i = start - 1
	
    # 遍历整个子数组
    for j in range(start, end):
        # If the current element is smaller than or equal to the pivot
        if arr[j] <= pivot:
            # 交换元素位置，将较小的元素放到前面
            # Swap arr[i] and arr[j]
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Swap arr[i+1] and arr[end] (put the pivot in its correct position)
    arr[i + 1], arr[end] = arr[end], arr[i + 1]

    # Print the current state of the array
    print(f"Step: {arr}")

    # Return the index of the pivot
    # 返回新的基准元素位置
    return i + 1

# Example usage
my_list = [7, 2, 1, 8, 6, 3, 5, 4]
print("Original list:", my_list)
# Call the quick_sort function
quick_sort(my_list)
print("Sorted list:", my_list)
```

#### Three-Way Partitioning

For arrays with many duplicate elements, a three-way partitioning strategy can be more efficient.

```python
import random

def quick_sort(arr, start=0, end=None):
    if end is None:
        end = len(arr) - 1

    if start < end:
        # 三取中法：选择子数组的第一个、中间和最后一个元素，取它们的中值作为基准元素
        mid_index = (start + end) // 2
        median_of_three(arr, start, mid_index, end)

        # Partition the array, get the index of the pivot
        pivot_index = partition(arr, start, end)

        # Recursively sort the subarrays
        quick_sort(arr, start, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, end)

def median_of_three(arr, start, mid, end):
    # Compare elements at start, mid, and end; rearrange them to be in non-decreasing order
    if arr[start] > arr[mid]:
        arr[start], arr[mid] = arr[mid], arr[start]
    if arr[mid] > arr[end]:
        arr[mid], arr[end] = arr[end], arr[mid]
    if arr[start] > arr[mid]:
        arr[start], arr[mid] = arr[mid], arr[start]

def partition(arr, start, end):
    pivot = arr[end]
    i = start - 1

    for j in range(start, end):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1

# Example usage:
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
quick_sort(arr)
print(arr)
```

> Three-way partitioning is an enhancement to the traditional Quick Sort  algorithm that is particularly useful when dealing with arrays that  contain many duplicate elements. The goal of three-way partitioning is  to efficiently handle elements that are equal to the chosen pivot. This  strategy helps avoid unnecessary comparisons and swaps for duplicate  elements, making the sorting process more efficient. 
>
> 1-Like in the traditional Quick Sort, a pivot element is chosen from the array. 
>
> 2-Elements are partitioned into three groups based on their relationship to the pivot:
>
> - Elements less than the pivot: These elements go to the left partition.
> - Elements equal to the pivot: These elements go to the middle partition.
> - Elements greater than the pivot: These elements go to the right partition.
>
> 3-Recursively apply the three-way partitioning strategy to the left and right partitions, excluding the middle partition (which already contains elements equal to the pivot).
>
> 4-The final sorted array is obtained by concatenating the sorted left, middle, and right partitions.





## Merge Sort

one of the fastest comparison sorts.

a divide-and-conquer sorting algorithm

The key idea behind Merge Sort is to divide the unsorted list into n sublists, each containing one element, and then repeatedly merge sublists to produce new sorted sublists until there is only one sublist remaining, which is the sorted list.

> **Advantages:** 
>
>- Efficient for large datasets due to its O(nlogn) time complexity.
>- Stable sorting preserves the order of equal elements.
>- Can be easily adapted for external sorting (sorting large datasets that do not fit into main memory).

>**Visualization:**
>
>Merge Sort is often visualized as a tree structure, with each level representing a recursive call and each node representing a merge operation. This tree structure helps in understanding the divide-and-conquer nature of the algorithm.





###  Algorithm Steps 

1. The unsorted list is divided into n sublists, each containing one element. This is the base case of the recursion. 
2. The algorithm recursively sorts each sublist.
3. The sorted sublists are repeatedly merged to produce new sorted sublists until there is only one sublist remaining, which is the sorted list.

> The key operation is the merging step, where two sorted halves are combined into a single sorted array. 

### Example

Let's take an example array: `[38, 27, 43, 3, 9, 82, 10]` 

**Step 1: Divide**: Initial Array: `[38, 27, 43, 3, 9, 82, 10]`

Divide into two halves:

- Left half: `[38, 27, 43]`
- Right half: `[3, 9, 82, 10]`

**Step 2: Recursively Sort**: Recursively apply Merge Sort:

1-Sort the left half [38, 27, 43]

- Divide into `[38]`, `[27]`, `[43]`
- Merge `[38]` and `[27]` to get `[27, 38]`
- Merge `[27, 38]` with `[43]` to get `[27, 38, 43]`

2-Sort the right half [3, 9, 82, 10]

- Divide into [3, 9], [82, 10]
  - For `[3, 9]`, no further division needed as they are sorted.
  - For `[82, 10]`, divide into `[82]` and `[10]`, then merge to get `[10, 82]`
- Merge `[3, 9]` and `[10, 82]` to get `[3, 9, 10, 82]`

**Step 3: Merge:** Merge the sorted halves: Merge [27, 38, 43] and [3, 9, 10, 82]

- Start with two pointers at the beginning of each sorted array.
- Compare the elements at the pointers and pick the smaller one.
- Move the pointer of the chosen element to the next position.
- Repeat until you reach the end of one of the arrays.
- Concatenate the remaining elements from the other array.

Final sorted array: `[3, 9, 10, 27, 38, 43, 82]`



### Code Example

```python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Find the middle index

        # Divide the array into two halves
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively sort the two halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the sorted halves
        merge(arr, left_half, right_half)

def merge(arr, left, right):
    i = j = k = 0

    # Compare elements and merge into the original array
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Check for any remaining elements in left and right halves
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

# Example usage:
arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort(arr)
print("Sorted Array:", arr)
```



### Time Complexity

The time complexity of Merge Sort is O(nlog⁡n) in all cases (worst-case, average-case, and best-case). This makes Merge Sort highly efficient for large datasets.

> The list is divided into two halves, which takes constant time: \(O(1)\).
>
> Recursively sorting the two halves involves log(n) levels of recursion.
>
> At each level, the total work done is proportional to \(n\), where \(n\) is the size of the input. In this example, \(n = 10\).
>
> So, the time complexity for the conquer step is O(nlog⁡n)

### Space Complexity

Merge Sort has a space complexity of O(n) due to the need for additional space to store temporary sublists during the merging process.

### Stability

Merge Sort is a stable sorting algorithm, meaning that the relative order of equal elements is preserved during the sorting process.



### Test question

Why does Merge Sort have the fastest Average run time?  

A. Because it is fastest speed is nlogn. 

B. Because it is average speed is nlogn. 

C. Because it is worst speed is nlogn.

> A is Correct! All of the other programs we have seen have a worst case slower than this. This one guarantees that no matter what happens, it will always run at nlogn, giving us the best average run time. 
>
> B is Not Quite! This is a decent sign of the run time of the program, however many other programs share an average run time with this algorithm.



## BST Sort












## Heap Sort???

a comparison-based sorting algorithm that uses a binary heap data structure to build a max-heap or min-heap.

In the context of Heap Sort, we typically use a max-heap to sort elements in ascending order.



### Algorithm Steps

1-Build Max-Heap:

- The first step is to build a max-heap from the given array. This involves rearranging the elements in the array to satisfy the max-heap property: the value of each node is greater than or equal to the values of its children.
- The build process starts from the last non-leaf node and goes backward to the root.

2-Heapify:

- After building the max-heap, the largest element (at the root) is moved to the end of the array (position n-1).The heap property is then restored by heapifying the reduced heap (excluding the last element). 
- This involves moving the next largest element to the root and repeating the process.

3-Repeat:

- Steps 2 are repeated until the heap size is reduced to 1. At this point, the entire array is sorted.



### Time Complexity

Heap Sort has a time complexity of O(n log n) for the worst, average, and best cases. The build max-heap step takes O(n) time, and the heapify step (repeated n times) takes O(log n) time.

### Space Complexity

Heap Sort is an in-place sorting algorithm, meaning it doesn't require additional memory proportional to the input size.





## Radix Sort???







## std::Sort





## std::Stable Sort





## Shell Sort







## Cocktail Shaker Sort







## Gnome Sort











## Bitonic Sort







## Bogo Sort















# **Trees**

a "tree" refers to a hierarchical data structure that consists of nodes connected by edges.

> It is called a tree because it resembles an inverted tree, with the root at the top and branches emanating downward.
>
> Trees are also typically one directional, so you go from parent, to child, to child, to child, etc. You don't typically go back up the tree for any purpose, except maybe a printing of the tree

> Trees are widely used in computer science for representing hierarchical relationships, such as directory structures in file systems, hierarchical data in databases, and the structure of expressions in compilers. 
>
> They also serve as the basis for various tree-based algorithms and data structures, like binary search trees, AVL trees, and heap structures.

<img src="picture\tree.jpg" alt="tree" style="zoom: 100%;" />



## Time complexity

| Types               | best run time | average run time | worst run time |
| ------------------- | ------------- | ---------------- | -------------- |
| Binary Search Trees |               | O(log n)         | O(n)           |
| B-Trees             |               |                  |                |
| AVL Trees           |               | O(log n)         |                |
| Trie (Prefix Tree)  |               |                  |                |
| Heap (Binary Heap)  |               |                  |                |
| Quad Trees          |               |                  |                |
| Oct Trees           |               |                  |                |
| Ternary Trees       |               | O(log n)         |                |
| Splay Trees         |               | O(log n)         |                |





## Key

"key" refers to a unique identifier associated with each node in the tree.

It's a value or attribute that is used to determine the position of a node within the tree's structure.

> The key serves as the basis for organizing and searching for nodes in the tree.



### meaning

1-Ordering and Searching

The key provides a basis for ordering the nodes within the tree. In binary search trees (BSTs), for example, the left subtree of a node contains keys less than the node's key, and the right subtree contains keys greater than the node's key. This ordering facilitates quick searches, as the structure of the tree guides the search based on the comparison of keys.

2- Efficient Retrieval

With keys, it becomes possible to quickly locate and retrieve specific elements from the tree. During searches, insertions, and deletions, the comparison of keys helps determine the path to follow within the tree, leading to the desired node efficiently

3-Uniqueness and Identification

The uniqueness of keys ensures that each node in the tree represents a distinct element or entity. This uniqueness is essential for identifying and distinguishing between different nodes. In practical applications, keys are often used to represent identifiers, such as unique IDs in databases.

4-Dynamic Sorting

The ordering imposed by keys allows for dynamic sorting of data as elements are added or removed from the tree. This ordering property is particularly advantageous in scenarios where maintaining a sorted order is important for efficient data retrieval.

5-Algorithmic Operations

Various algorithms that operate on tree structures, such as search, insertion, deletion, and traversal algorithms, leverage the key comparisons to determine the flow of the algorithm. Keys guide the algorithmic decisions and actions, leading to effective and optimized operations.

6-Application-Specific Data Representation

The choice of keys depends on the nature of the data being stored and the requirements of the application. Keys can represent various types of information, such as numerical values, strings, or other data structures, depending on what makes sense for the context.



### comparison

| types                    | has key? |
| ------------------------ | -------- |
| Binary Search Tree (BST) | Yes      |
| B-tree                   | Yes      |
| AVL Tree                 | Yes      |
| Trie (Prefix Tree)       | Yes      |
| Heap (Binary Heap)       | Yes      |
| Quad Tree and Oct Tree   | No       |
| Ternary Tree             | Yes      |
| Splay Tree               | Yes      |

> 1-Binary Search Tree (BST)
>
> BSTs use keys to organize data in a way that facilitates efficient search, insertion, and deletion operations.

> 2-B-tree
>
> B-trees are used in file systems and databases and organize data with keys to provide balanced and efficient search, insertion, and deletion operations.

> 3-AVL Trees
>
> AVL Trees are a type of self-balancing binary search tree where the heights of the two child subtrees of any node differ by at most one. They use keys to maintain a balanced structure, ensuring efficient search, insertion, and deletion operations. AVL Trees are commonly used in scenarios where it is important to avoid degeneration into a skewed tree, providing guaranteed logarithmic height.

> 4-Trie (Prefix Tree)
>
> Tries organize data based on sequences of characters (keys), making them efficient for tasks such as autocomplete and storing dictionary-like information.

> 5-Heap (Binary Heap)
>
> Heaps use keys to maintain a partially ordered structure, where the parent's key is either greater (max-heap) or smaller (min-heap) than the keys of its children. Heaps are often used in priority queues.

> 6-Quad Tree and Oct Tree
>
> These trees are used for spatial indexing, where keys aren't explicitly assigned. Instead, the structure is based on the spatial coordinates of points.

> 7-Ternary Trees
>
> Ternary Trees are trees where each node can have up to three children. They use keys to organize data, similar to binary search trees but with a higher branching factor. Ternary Trees are used in applications where nodes often have more than two possible outcomes or in scenarios where a branching factor of three is beneficial. One specific use case is in ternary search trees, which are used in spell-checking algorithms.

> 8-Splay trees
>
> Splay trees use keys to organize data dynamically, adjusting the tree structure based on access patterns to optimize search times.





## important terms

### Node

Each element in a tree is called a "node." Nodes represent entities and may contain data.

### Root

The topmost node in a tree is called the "root." It is the starting point for traversing the tree.

### Parent and Child

A node in a tree is connected to other nodes. The node from which a branch originates is called the "parent," and the nodes connected to it are called its "children."

### Leaf

A node that has no children is called a "leaf" or a "terminal node."

### Subtree

A subtree is a tree formed by a node and all its descendants.

### Level

The level of a node is its distance from the root. The root is at level 0, its children are at level 1, and so on.

### Depth

The depth of a tree is the length of the longest path from the root to a leaf.

### Height

The height of a tree is the length of the longest path from the root to a leaf. Alternatively, the height of a leaf node is 0.

### Binary Tree

A binary tree is a tree in which each node has at most two children, referred to as the left child and the right child.

### Binary Search Tree (BST)

A binary search tree is a binary tree with the property that the left child of a node contains values less than the node, and the right child contains values greater than the node.





## Types

### Binary Search Trees

- Each node has at most two children, a left child and a right child. 
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.  (You can put the equal to on the right or left)

> **Characteristics:** 
>
> - **Recursive :** The left and right subtrees of a node are also binary search trees. 
> - **No Duplicates:** Each node in a BST has a unique key. There are no duplicate keys in the tree.

>**In-order Traversal:** In-order traversal of a BST yields a sorted sequence of keys.

> **operations:**
>
> Search Operation
>
> - To search for a key in a BST, start at the root.
> - If the key to be searched is equal to the current node's key, the search is successful.
> - If the key is less than the current node's key, continue the search in the left subtree.
> - If the key is greater than the current node's key, continue the search in the right subtree.
> - Repeat the process until the key is found or a null (empty) subtree is encountered.
>
> Insertion Operation
>
> - To insert a new key into a BST, perform a search for the key as if you were searching for it.
> - When the search reaches a null subtree, insert the new key as the left child (if the key is less than the current node's key) or the right child (if the key is greater than the current node's key).
>
> Deletion Operation
>
> - To delete a key from a BST, perform a search for the key.
>   - If the key is found:
>     - If the node has no children, simply remove the node.
>     - If the node has one child, replace the node with its child.
>     - If the node has two children, find the node's in-order successor (the smallest key in its right subtree), replace the node's key with the in-order successor's key, and recursively delete the in-order successor.

> **Runtime complexity:**
>
> The time complexity of basic operations (search, insertion, deletion) in a balanced BST is O(log n) on average, where n is the number of nodes in the tree. 
>
> However, in the worst case (for a skewed tree), the time complexity can be O(n), making it important to maintain balance in the tree. 
>
> This has led to the development of **self-balancing binary search trees**, such as **AVL trees** and **Red-Black trees**, to ensure more predictable performance.
>
> | operations | average | worst case |
> | ---------- | ------- | ---------- |
> | search     | Θ(logn) | O(n)       |
> | insert     | Θ(logn) | O(n)       |
> | delete     | Θ(logn) | O(n)       |

> **code example**
>
> ```python
> # 在此示例中，“BinarySearchTree”类具有插入、搜索和中序遍历的方法。 树中的每个节点都由“Node”类表示。 “insert”方法将键插入 BST，“search”方法搜索键，“inorder_traversal”方法执行树的中序遍历。
> # 在完整的实现中，您可能需要添加更多功能，例如删除、前序和后序遍历以及平衡操作，以确保树保持平衡以实现高效的搜索操作。
> class Node:
>     def __init__(self, key):
>         self.key = key        # the value it holds
>         self.left = None
>         self.right = None
>         
> # In the provided example code, the `Node` class does not include a reference to its parent. While it's common for some tree data structures, like AVL trees or Red-Black trees, to include a parent reference, the absence of a parent reference in this specific implementation simplifies the code and is not strictly necessary for a basic binary search tree.
> # Including a parent reference in each node adds a little more complexity to the implementation and increases memory usage. The absence of a parent reference in this code means that traversing from a node to its parent would require additional logic or methods that keep track of the parent during tree operations.
> # If you choose to use a parent reference, you would need to update the tree operations accordingly, ensuring that the parent reference is maintained correctly during insertions, deletions, and rotations.
>         
> class BinarySearchTree:
>     def __init__(self):
>         self.root = None
> 
>     def insert(self, key):
>         self.root = self._insert(self.root, key)
> 
>     def _insert(self, root, key):
>         if root is None:
>             return Node(key)
> 
>         if key < root.key:
>             root.left = self._insert(root.left, key)
>         elif key > root.key:
>             root.right = self._insert(root.right, key)
> 
>         return root
> 
>     def search(self, key):
>         return self._search(self.root, key)
> 
>     def _search(self, root, key):
>         if root is None or root.key == key:
>             return root
> 
>         if key < root.key:
>             return self._search(root.left, key)
>         else:
>             return self._search(root.right, key)
> 
>     def inorder_traversal(self):
>         result = []
>         self._inorder_traversal(self.root, result)
>         return result
> 
>     def _inorder_traversal(self, root, result):
>         if root:
>             self._inorder_traversal(root.left, result)
>             result.append(root.key)
>             self._inorder_traversal(root.right, result)
> 
> # Example usage:
> bst = BinarySearchTree()
> keys = [50, 30, 70, 20, 40, 60, 80]
> 
> for key in keys:
>     bst.insert(key)
> 
> print("Inorder Traversal:", bst.inorder_traversal())
> 
> search_key = 40
> result = bst.search(search_key)
> 
> if result:
>     print(f"Key {search_key} found in the tree.")
> else:
>     print(f"Key {search_key} not found in the tree.")
> ```





### B-trees 

a self-balancing tree data structure that maintains sorted data and allows searches, insertions, and deletions in logarithmic time.

> **Characteristics:**
>
> Balanced Structure ---- B-trees are self-balancing, meaning that after every insertion or deletion operation, the tree is automatically adjusted to maintain balance. This ensures that the depth of the tree remains logarithmic in the number of elements, leading to efficient search operations.
>
> Variable Branching Factor --- Unlike binary trees, B-trees have a variable, often large, branching factor. Each internal node can have a variable number of child nodes, and this number is typically within a specified range.
>
> Multiple Keys in a Node --- Nodes in a B-tree can have more than two keys. Think of these keys as markers that separate different ranges of data. Having more keys in a node means the tree can organize and sort a larger amount of data more efficiently.
>
> 在 B 树中，一个节点包含多个键并不是为了标志一个唯一的节点。相反，这些键用于划分节点中的数据范围，并指导搜索过程。每个键都对应一个子树，而子树又对应节点中的一组数据。因此，每个键并不是唯一地标识一个节点，而是用来决定在哪个子树中进行下一步搜索。多个键的设计允许节点在同一层次上划分和存储更多的数据，这有助于减少树的高度，提高整体性能。
>
> 具体来说，在内存中，一个节点通常由一个包含多个键的数组组成。这个数组的大小由 B 树的阶（order）决定，阶表示一个节点中最多可以有的键的数量。每个键关联着相应的子树或数据。这样的结构使得一个节点能够容纳多个键，而不仅仅是一个。每个键都对应着一个子树或数据范围。在搜索时，可以根据键的值决定接下来进入哪个子树，以此类推。
>
> ```
> # 假设有一个3阶的 B 树，每个节点可以有最多两个键。
> [Key1, Key2, Pointer1, Pointer2, Pointer3]
> # Key1 和 Key2 是节点中的两个键，它们用于划分节点中的数据范围。
> # Pointer1, Pointer2, 和 Pointer3 是对应于这两个键的子树的指针或数据的引用。
> ```
>
> 简单来说，B 树就像一个大图书馆中的目录。 每个目录（节点）都有标签（键），告诉您在哪里可以找到某些书籍（数据）。 目录中的标签越多，组织和查找书籍的效率就越高，并且需要步行到图书馆不同部分的次数就越少（高效的磁盘 I/O）。 

> **How to be self-balanced?**
>
> through a series of balancing operations performed during insertions and deletions. The key to maintaining balance in a B-tree is to ensure that the tree remains approximately balanced after each modification operation.
>
> - Balancing Operations:
>   Whenever an insertion or deletion occurs, the B-tree undergoes balancing operations to ensure that the tree remains balanced. These operations involve redistributing keys between nodes, splitting nodes, or merging nodes to maintain a balanced structure.
> - Node Splitting
>   In the case of an insertion that causes a node to overflow (exceed the maximum allowed number of keys), the node is split into two nodes. The median key is moved up to the parent node, effectively redistributing the keys. This ensures that each child of the parent has a roughly equal number of keys.
> - Node Merging
>   In the case of a deletion that causes a node to underflow (have fewer than the minimum required keys), adjacent nodes are considered for merging. Merging involves combining two nodes and moving a key down from the parent to maintain order and balance.
> - Adjusting Parent Nodes
>   After a split or merge operation, the parent node may need to be adjusted to accommodate the changes. If the parent node overflows due to a key moving up from a child, a similar split operation is performed on the parent. Conversely, if the parent underflows after a child merges, the parent may borrow a key from a sibling.
> - Recursive Approach
>   Balancing operations are performed recursively up the tree from the point of insertion or deletion. This ensures that changes made at one level do not cause imbalances at higher levels of the tree.
> - Maintaining Invariant Conditions
>   Throughout the balancing process, B-tree invariant conditions are maintained. These conditions include the minimum and maximum number of keys allowed in each node and the ordering of keys within nodes
> - Height Balancing
>   The balancing operations ensure that the height of the B-tree remains logarithmic in the number of elements. This logarithmic height is crucial for achieving efficient search, insertion, and deletion operations.

> **File Systems and Databases:** B-trees are commonly used in file systems and databases to store and manage large amounts of data efficiently. They provide a balanced structure that allows for efficient searching, insertion, and deletion operations. 
>
> B-trees provide balanced search times, making them suitable for systems that require frequent data modifications. 
>
> B-trees are particularly well-suited for organizing and managing large amounts of data on storage devices such as hard drives. They are commonly used in file systems and databases. 
>
> **Efficient Disk I/O:** 
>
> B-trees are good at working with data stored on disks or hard drives. Because each node in a B-tree can store a bunch of keys and data, when you're searching for something, you often only need to go to a few specific nodes. This reduces the number of times you have to read from or write to the disk, making operations faster.





### AVL Trees

Self-balancing binary search tree,  which is named after their inventors Adelson-Velsky and Landis.

The key feature of an AVL tree is that, after each insertion or deletion operation, the tree performs rotations to ensure that the balance factor of every node (the height difference between its left and right subtrees) is within a specified range, typically -1, 0, or 1.

> **characteristics:**
>
> - Binary Search Tree Property
>   Like any other binary search tree, an AVL tree ensures that the left subtree of a node contains elements with keys less than the node's key, and the right subtree contains elements with keys greater than the node's key.
> - Balance Factor
>   The balance factor of a node is the height of its left subtree minus the height of its right subtree. Mathematically, for a node 'N', the balance factor (BF) is given by: 
>   BF(N) = height(left subtree) − height(right subtree) 
> - Balancing Operations
>   When a new node is inserted or a node is deleted, the balance factor of the affected nodes may violate the AVL property. 
>   If the balance factor of a node becomes less than -1 or greater than 1, the tree needs to be rebalanced. 需要对以插入路径上**离插入节点最近的**平衡**因子绝对值大于1的**节点**为根**的树进行调整
>   There are four possible cases (left-left, left-right, right-right, and right-left) that may require rotation operations to restore balance.
> - Rotations
>   Rotations are the fundamental operations used to maintain balance in AVL trees. There are four types of rotations: Left Rotation (LL Rotation) \ Right Rotation (RR Rotation) \ Left-Right Rotation (LR Rotation) \ Right-Left Rotation (RL Rotation)
> - Left Rotation (LL)
>   Occurs when the balance factor of a node becomes -2 and its right subtree is unbalanced.  It involves a single rotation to the left to restore balance.
> - Right Rotation (RR)
>   Occurs when the balance factor of a node becomes 2 and its left subtree is unbalanced. It involves a single rotation to the right to restore balance.
> - Left-Right Rotation (LR)
>   Occurs when the balance factor of a node becomes -2 and its left subtree is unbalanced. It involves a left rotation on the left child followed by a right rotation on the original node.
> - Right-Left Rotation (RL)
>   Occurs when the balance factor of a node becomes 2 and its right subtree is unbalanced. It involves a right rotation on the right child followed by a left rotation on the original node.

> **what is the rotation progress specifically?**??
>
> https://blog.csdn.net/weixin_49561506/article/details/130951354
>
> Left Rotation (LL Rotation)
> Occurs when the balance factor of a node becomes -2 and its right subtree is unbalanced. 
>
> ```
> 1.Let A be the unbalanced node, B be its right child, and C be the left child of B.
> 2.Perform a left rotation by making B the new root, A its left child, and C the right child of A.
> 3.Adjust the heights of A and B.
> 4.The tree is now balanced.
>     A            B
>      \          / \
>       B   =>   A   C
>        \
>         C
> ```
>
> Right Rotation (RR Rotation)
> Occurs when the balance factor of a node becomes 2 and its left subtree is unbalanced. 
>
> ```
> 1.Let A be the unbalanced node, B be its left child, and C be the right child of B.
> 2.Perform a right rotation by making B the new root, A its right child, and C the left child of A.
> 3.Adjust the heights of A and B.
> 4.The tree is now balanced.
>         A        B
>        /        / \
>       B   =>   C   A
>      /
>     C
> ```
>
> Left-Right Rotation (LR Rotation)
> Occurs when the balance factor of a node becomes -2 and its left subtree is unbalanced. 
>
> ```
> 1.Apply a left rotation on the left child.
> 2.Apply a right rotation on the original node.
> 3.Adjust the heights.
> 4.The tree is now balanced.
>     A          A         C
>      \          \       / \
>       B   =>     C  => A   B
>      /            \
>     C              B
> ```
>
> Right-Left Rotation (RL Rotation)
> Occurs when the balance factor of a node becomes 2 and its right subtree is unbalanced.
>
> ```
> 1.Apply a right rotation on the right child.
> 2.Apply a left rotation on the original node.
> 3.Adjust the heights.
> 4.The tree is now balanced.
>       A          A          B
>        \          \        / \
>         C   =>     B  =>  C   A
>        /            \
>       B              C
> ```

> **Runtime complexity**
>
> The AVL tree guarantees a logarithmic height, ensuring efficient search, insert, and delete operations with a time complexity of O(log n) for each operation, where n is the number of nodes in the tree.

> **Databases and Indexing:** AVL trees are a type of self-balancing binary search tree. They are used in scenarios where it is crucial to maintain a balanced tree to ensure efficient search times. This is often used in database indexing. 





### Trie (Prefix Tree)

Tree-like structure used for storing a dynamic set of strings, with each node representing a character.  where the keys are usually sequences, such as words or phone numbers. 

The term "Trie" comes from the word "retrieval" and is sometimes pronounced as "try."

> **characteristics:**
>
> ```
>       (root)
>         |
>         b
>         |
>         a
>       / | \
>      t  n  o
>     / \    \
>    m   o    b
>    |   |    |
>    a   b    i
>    |   |    |
>    n   i    l
>    |   |
>    o   l
>    |
>    b
>    |
>    i
>    |
>    l
>    |
>    e
> ```
>
> - Nodes: Each node in a Trie represents a single character of a string.
> - Edges: The path from the root to a particular node spells out a specific string.
> - Root: The topmost node represents an empty string or the null string.
> - Leaf Nodes: Nodes that mark the end of a word in the Trie.
> - Path to a Node: The path from the root to any node in the Trie represents a string.
> - Prefix Property: All prefixes of strings in the Trie can be read by traversing down from the root to some node.
> - Common Prefixes: Nodes with a common prefix share the same initial sequence of characters.

> **Operations:**
>
> Insertion: To insert a string into a Trie, traverse the Trie from the root, creating nodes as needed.
>
> Deletion: To delete a string, remove the nodes corresponding to that string. If removing a node results in a node with no children, it can be removed as well.
>
> Search: To check if a string is present in the Trie, traverse the Trie from the root along the path corresponding to the string. If the path exists and ends in a leaf node, the string is present.

> **Text and IP Address Storage:** Tries are tree-like structures used for storing a dynamic set of strings, where the keys are usually sequences (e.g., characters or bits). Tries are efficient for tasks such as autocomplete in text editors or storing IP addresses. 
>
> Autocomplete:
> Tries are commonly used in autocomplete systems. The Trie structure makes it easy to find all words with a given prefix.
>
> Spell Checking:
> Tries can be used for spell checking by quickly identifying whether a given sequence of characters forms a valid word.
>
> Dictionary Implementations:
> Tries are used in dictionary implementations to efficiently store and look up words.
>
> IP Routing:
> Tries are used in IP routers for routing lookups, where each level represents part of the IP address.



### Heap (Binary Heap)???

Complete binary tree with a heap property (either min-heap or max-heap).









> **Priority Queues:** Binary heaps are often used to implement priority queues, where the element with the highest (or lowest) priority can be efficiently extracted. 





### Quad Trees 四叉树 and Oct Trees

A Quad Tree is a tree data structure primarily used for spatial partitioning in two-dimensional space. "Quad" refers to the four children each node can have, corresponding to the four quadrants of a 2D coordinate system.

An Octree is an extension of the Quad Tree concept to three-dimensional space. It is a tree data structure used for spatial partitioning in 3D space. The name "Oct" refers to the eight children each node can have, corresponding to the eight octants of a 3D coordinate system.

> **Structure:**
>
> Quad Trees' Each node contains:
>
>   - Information about a rectangular region in the 2D space (bounding box).
>   - Pointers or references to data associated with that region.
>   - Four children nodes, corresponding to the four quadrants (top-left, top-right, bottom-left, bottom-right).
>
>  Oct Trees' Each node contains: 
>
>  - Information about a cubical region in 3D space (bounding box).
>   - Pointers or references to data associated with that region.
>   - Eight children nodes, corresponding to the eight octants (top-front-left, top-front-right, top-back-left, top-back-right, bottom-front-left, bottom-front-right, bottom-back-left, bottom-back-right).

> **Operations**
>
> Quad Trees' operations
>
> 1. Subdivision:
>    - When a node needs further detail or a region becomes too small, it is subdivided into four quadrants, and each quadrant becomes a child node.
>
> 2. Merging:
>    - Nodes with similar characteristics or small enough regions can be merged to reduce the tree's size.
>
> Oct Trees' operation
>
> 1. Subdivision:
>    - When a node needs further detail or a region becomes too small, it is subdivided into eight octants, and each octant becomes a child node.
>
> 2. Merging:
>    - Similar to Quad Trees, nodes with similar characteristics or small enough regions can be merged to reduce the size of the Octree.

> **Spatial Indexing:** These trees are used in computer graphics and geographic information systems to represent and efficiently query spatial data. Quad trees are used in two-dimensional space, while oct trees extend the concept to three dimensions. 
>
> **Quad Trees' use cases**
>
> 1. Spatial Indexing:
>    - Quad Trees are used in spatial indexing applications, such as organizing and searching spatial data efficiently.
>
> 2. Collision Detection:
>    - In computer graphics and simulations, Quad Trees help with collision detection by organizing objects based on their spatial positions.
>
> 3. Image Compression:
>    - Quad Trees can be used for image compression by recursively subdividing regions with similar color characteristics.
>
> **Oct Trees' use cases**
>
> 1. 3D Spatial Indexing:
>    - Octrees are used in 3D spatial indexing applications, such as organizing and searching spatial data in three dimensions.
>
> 2. Volume Rendering:
>    - In computer graphics and medical imaging, Octrees assist in volume rendering by organizing volumetric data efficiently.
>
> 3. Collision Detection in 3D:
>    - In 3D simulations and video games, Octrees help with collision detection by organizing objects based on their spatial positions in three dimensions.
>
> 4. Scientific Applications:
>    - Octrees find applications in scientific simulations and modeling where three-dimensional spatial data needs efficient organization and access.





### Ternary Trees 三叉树 

a tree data structure in which each node has at most three children.

The structure of a ternary tree is such that each node has a left child, a middle child, and a right child.

> **Node structure**
>
>   - A key or value.
>   - A left child, representing values smaller than the node's key.
>   - A middle child, representing values equal to the node's key.
>   - A right child, representing values greater than the node's key.

> **Characteristics:**
>
> 1. Number of Children:
>    - Each node in a ternary tree has three children.
>
> 2. Ordering:
>    - The ordering among the children is typically left < middle < right.

> **operations:**
>
> 1. Insertion:
>    - To insert a new value into a ternary tree, compare it with the current node's key.
>    - If smaller, move to the left child; if equal, move to the middle child; if greater, move to the right child.
>    - Repeat this process until an appropriate location is found.
>
> 2. Deletion:
>    - Deleting a node involves finding the node with the value to be deleted and then adjusting the tree accordingly.
>    - If a node has only one or two children, it may need to be replaced with its child or children.
>
> 3. Search:
>    - Search for a value by comparing it with the node's key and navigating to the appropriate child until the value is found or a leaf node is reached.

> **Runtime Complexity**
>
> The time complexity of operations in a ternary tree is generally logarithmic O(log n) for balanced trees, similar to binary search trees.

> **Spell Checking:** Ternary search trees are used in spell-checking algorithms. They allow for efficient searching and insertion of words with similar prefixes. 
>
> **Use cases:**
>
> 1. Ternary Search:
>    - Ternary trees can be used for ternary search, a technique used in computer science to find the minimum or maximum of a unimodal function.
>
> 2. Database Indexing:
>    - Ternary trees can be used for indexing in databases, providing an ordered structure for quick search and retrieval.
>
> 3. Spell Checking:
>    - Ternary trees are suitable for spell checking algorithms, where they can efficiently store and search for words in a dictionary.





### Splay Trees  伸展树

a self-adjusting binary search tree with the property that recently accessed elements are quick to access again. 

It achieves this property by restructuring itself during each operation to bring the most recently accessed node to the root. This restructuring is known as "splaying."

Splay Trees are considered a good choice when the access patterns of the elements are not entirely random and have temporal locality, i.e., recently accessed elements are likely to be accessed again soon.

> **splaying steps**
>
> The splaying operation involves a series of rotations and restructuring to bring the target node to the root. There are three main types of splaying steps:
>
> 1. Zig Step:
>    - This step is performed when the target node is the left or right child of the root.
>    - A single rotation brings the target node to the root.
> 2. Zig-Zig Step:
>    - This step is performed when the target node is the left child of the left child or the right child of the right child.
>    - Two rotations are performed to bring the target node to the root.
> 3. Zig-Zag Step:
>    - This step is performed when the target node is the left child of the right child or the right child of the left child.
>    - Two rotations are performed to bring the target node to the root.

> **characteristics**
>
> 1. Splaying Operation:
>    - The primary operation in a Splay Tree is the splaying operation, which moves a node to the root of the tree.
> 2. Access Time:
>    - The amortized time complexity for a single operation (search, insert, or delete) in a Splay Tree is typically O(logn), where n is the number of nodes.

> **operations**
>
> 1. Search:
>    - The node being searched is splayed to the root.
>    - If the target node is found during the search, it becomes the new root.
>    - If the target node is not present, the last accessed node becomes the new root.
> 2. Insertion:
>    - Insert the new node as in a regular binary search tree.
>    - Splay the newly inserted node to the root.
> 3. Deletion:
>    - Delete the target node as in a regular binary search tree.
>    - Splay the parent of the deleted node to the root.

> **advantages and disadvantage**
>
> - Advantages:
>   - Simplicity: Splay Trees are relatively simple compared to other self-adjusting binary search trees.
>   - Amortized Efficiency: While individual operations may have worst-case O(n)O(n) time complexity, the amortized time complexity is O(log⁡n)O(logn).
> - Disadvantages:
>   - Lack of Balance Guarantee: Unlike AVL trees or Red-Black trees, Splay Trees do not maintain a strict balance property.

> **Caching and Memory Management:** Splay trees are self-adjusting binary search trees that reorder themselves based on the access patterns. They are used in caching and memory management to optimize for frequently accessed items.
>
> 1. Caching:
>    - Splay Trees are used in caching algorithms where frequently accessed items are brought to the top of the tree for faster access.
> 2. Dynamic Optimality:
>    - Splay Trees are part of dynamic optimality in online algorithms, where the optimal binary search tree is adapted dynamically based on access patterns







## Tree Traversals???

methods used to visit and process each node in a tree data structure systematically. 

Trees can be traversed in different orders, each resulting in a distinct sequence of visiting nodes.



###  three primary types 

1- Inorder Traversal: 中序遍历 [The term "inorder" suggests that the root node is visited in between the exploration of the left and right subtrees.]

- Visit the left subtree.
- Visit the root.
- Visit the right subtree.

```
     1
    / \
   2   3
  / \
 4   5

Inorder Traversal: 4, 2, 5, 1, 3
```

2- Preorder Traversal: 前序遍历 [The term "preorder" suggests that the root node is visited before exploring both the left and right subtrees.]

- Visit the root.
- Visit the left subtree.
- Visit the right subtree.

```
     1
    / \
   2   3
  / \
 4   5

Preorder Traversal: 1, 2, 4, 5, 3
```

3 - Postorder Traversal: 后序遍历 [The term "postorder" suggests that the root node is visited after exploring both the left and right subtrees.]

- Visit the left subtree.
- Visit the right subtree.
- Visit the root.

```
     1
    / \
   2   3
  / \
 4   5

Postorder Traversal: 4, 5, 2, 3, 1
```

#### example

```
# example:
      1
     / \
    2   3
   / \
  4   5
 / \
7   8
Inorder Traversal: 7, 4, 8, 2, 5, 1, 3
Preorder Traversal: 1, 2, 4, 7, 8, 5, 3
Postorder Traversal: 7, 8, 4, 5, 2, 3, 1
```

```
# example: inorder-
      1
     / \
    2   3
   / \  /
  4   5 23
   \     \
    8    24
   / \
  9  11
Inorder Traversal: 4, 9, 8, 11, 2, 5, 1, 23, 24, 3 
# 从root走，遇到最底下的左边先算，然后再算中间，再算右边
Preorder Traversal: 1, 2, 4, 8, 9, 11, 5, 23, 24
# 从root走，遇到中间的就先算上，算到最后一个中间再算左边，然后算右边
Postorder Traversal: 9, 11, 8, 4, 5, 2, 24, 23, 3, 1
# 从root走，遇到最底下的左边先算，然后再算右边，再算中间
```



### Algorithms

Traversals can be implemented using recursive or iterative algorithms. 

> Recursive algorithms are often more concise and elegant, while iterative algorithms may use a stack or queue to achieve the traversal without recursion.

```python
# a simple recursive Python implementation for the three traversals:
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.value, end=' ')
        inorder_traversal(node.right)

def preorder_traversal(node):
    if node:
        print(node.value, end=' ')
        preorder_traversal(node.left)
        preorder_traversal(node.right)

def postorder_traversal(node):
    if node:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.value, end=' ')

# Example Usage:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Inorder Traversal:", end=' ')
inorder_traversal(root)
print("\nPreorder Traversal:", end=' ')
preorder_traversal(root)
print("\nPostorder Traversal:", end=' ')
postorder_traversal(root)
```



#### what is the difference between recursive and iterative?

**Recursion:** a programming technique where a function calls itself directly or indirectly to solve a smaller instance of a problem. It involves breaking down a problem into smaller subproblems and solving each subproblem.

递归解决方案涉及将问题分解为同一问题的较小实例，并通过应用相同的算法来解决每个实例。 每个递归调用都解决原始问题的更小或更简单的版本。 

> Control Flow: managed by the function calls and the call stack. Each recursive call adds a new frame to the call stack, and the solution is built when the base case is reached.
>
> Code Simplicity: often more concise and elegant, especially for problems that naturally decompose into smaller instances.
>
> Memory Usage: use more memory due to the call stack, potentially leading to a stack overflow for deeply nested recursion.
>
> Readability: Recursive solutions can be more readable when the problem is naturally expressed in terms of smaller instances of itself.

```python
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)
```

**Iteration:** a programming technique where a set of instructions is repeatedly executed until a certain condition is met. It involves using loops, such as `for` or `while` loops, to repeat a block of code.

> Control Flow: managed explicitly by loop constructs. It involves specifying the initialization, condition, and update steps.
>
> Code Simplicity: require more explicit handling of loop control variables and may be more verbose than equivalent recursive code.
>
> Memory Usage: usually use less memory compared to recursion, as there is no call stack overhead.
>
> Readability: can be more readable for some problems, especially when the flow of  control is straightforward and doesn't naturally break down into smaller instances. 

```python
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
```





#### how to choose?

In many cases, both recursion and iteration can be used to solve the same problem, and the choice depends on the specific requirements and characteristics of the problem at hand.

- Nature of the Problem:
  - Some problems are naturally expressed in recursive terms, while others may be more straightforward to solve iteratively.
- Performance:
  - Recursive solutions may have a higher overhead due to the call stack. In cases where performance is critical, iteration might be preferred.
- Readability and Maintainability:
  - Choose the approach that results in more readable and maintainable code for a given problem.
- Language and Platform Considerations:
  - Some programming languages or platforms may have limitations on the depth of recursion, influencing the choice between recursion and iteration.





### Applications

1. Expression Trees:
   - Traversals are used to convert infix expressions to postfix or prefix notation.
2. File System Representation:
   - Traversals are used to represent hierarchical file systems.
3. Tree-based Queries:
   - Traversals are employed in queries on hierarchical structures, such as XML or JSON documents.
4. Binary Search Trees (BST):
   - Traversals help in searching, inserting, or deleting elements in BSTs.
5. Syntax Tree in Compilers:
   - Traversals are used in compilers to build and analyze syntax trees for source code.
6. Expression Evaluation:
   - Traversals are used to evaluate expressions represented as trees.



# **Heaps**

a specialized tree-based data structure that satisfies the heap property.

The term "heap" is borrowed from the notion of a heap in the sense of a heap of objects, where the topmost (root) object is either the minimum or maximum, making it **easy to access extremal values.**

> The term "heap" in the context of the data structure is a bit of a historical artifact, and its origin can be traced back to the concept of a "heap" as a broad and disorganized collection of things. The use of "heap" to describe this data structure might be somewhat metaphorical, emphasizing the structure's ability to quickly provide the minimum or maximum element, depending on whether it's a min heap or a max heap.

> the term "heap" is used to emphasize a particular property and structure that makes it efficient for certain operations. 
>
> The emphasis on heaps arises from their efficiency in handling priority-based data and their relevance in various algorithms and applications.
>
> provide a data structure that makes finding the extreme value O(1) time.  

> Heaps in essence are just stricter trees. They have all the same properties of trees, with the additional “Heap Property” rule added.
>
> a heap does not necessarily have to have at most 2 children in one node. 
>
> These are known as d-ary heaps, where d represents the maximum number of children each node can have.  In a d-ary heap, each node has at most d children. The structure and properties of a d-ary heap are similar to those of a binary heap, but with adjustments to accommodate the increased number of children. 
>
> In a d-ary heap:
>
> - If d=2, it is a binary heap.
> - If d=3, it is a ternary heap.
> - If d>2, it is a d-ary heap.
>
> The choice of the degree (d) depends on the specific requirements of the application or algorithm  using the heap. In practice, binary heaps are commonly used because of  their simplicity and ease of implementation. However, for certain  scenarios where there is a need to balance between space efficiency and  quick access to elements, d-ary heaps with larger values of d might be chosen. 





## types

### Max Heap

In a max heap, for every node i other than the root:

- The value of i is greater than or equal to the values of its children.

> In simpler terms, the largest element is at the root, and each parent node has a value greater than or equal to its children.

### Min Heap

In a min heap, for every node i other than the root:

- The value of i is less than or equal to the values of its children.

> Here, the smallest element is at the root, and each parent node has a value less than or equal to its children.



## properties

1. Complete Binary Tree:
   - Heaps are typically implemented as complete binary trees. This means that all levels of the tree are filled, except possibly the last level, which is filled from left to right.
2. Array Representation:
   - Heaps can be efficiently represented using arrays. The children of a node at index i are at indices 2i+1 (left child) and 2i+2 (right child).



## operations

1. Insertion:
   - Add a new element to the heap while maintaining the heap property. This typically involves inserting the element at the next available position and then **"bubbling up 向上冒泡 "** or **"sifting up 向上筛选 "** the element until the heap property is restored.
2. Deletion:
   - Remove the root element (max or min, depending on the heap type) and replace it with the last element. Then, "heapify" the tree by moving the new root down (also known as **"bubbling down 向下冒泡 "** or **"sifting down 向下筛选 "**) until the heap property is restored.



## Time Complexity

- Insertion and Deletion:
  - Both insertion and deletion operations on a heap have a time complexity of O(logn), where n is the number of elements in the heap.
- Building a Heap:
  - Building a heap from an array has a time complexity of O(n).



## use cases

### Priority Queues

- Heaps are commonly used to implement priority queues. In a max heap, the maximum priority element (such as the highest priority task) is always at the front.
- A priority queue is a data structure where each element has an associated priority, and elements with higher priority are served before elements with lower priority. The heap property (max heap or min heap) ensures quick access to the element with the highest (or lowest) priority.

>**Examples**
>
>**计算机任务优先级队列**
>
>假设你的计算机正在运行多个任务，并且有一个任务队列来管理它们的执行。在这些任务中，有一些任务对计算机的正常运行更为关键，而另一些任务则是后台任务，对计算机性能要求较低。
>
>1.任务到达（添加到队列）：
>有两个任务：一个是后台任务（更新Facebook状态），另一个是关键任务（CPU关键任务）。这两个任务按照它们的重要性（优先级）被加入任务队列。
>
>2.任务优先级分配：
>每个任务都有一个优先级，CPU关键任务的优先级较高，后台任务的优先级较低。
>
>3.队列组织（优先级队列结构）：
>任务队列以优先级为基础组织，CPU关键任务排在队列的前面，后台任务排在队列的后面。
>
>4.执行过程（处理任务）：
>计算机开始执行任务队列中的任务。由于CPU关键任务具有较高的优先级，它首先被执行。
>
>5.任务完成（更新GPU和界面）：
>CPU关键任务执行完成后，计算机继续执行后台任务。后台任务可能涉及更新Facebook状态，但这个任务的优先级较低。
>
>6.用户体验：
>用户在执行CPU关键任务时可能会感觉到计算机的响应性，因为它是一个关键任务。后台任务的执行不会中断用户界面的正常更新，因为它具有较低的优先级。
>
>**机场登机优先队列**
>
>您在机场，有一个优先队列供乘客登机。 航空公司根据机票舱位、飞行常客身份或需要特殊帮助等因素为乘客分配不同的优先级。
>
>1.任务到达（加入队列）：
>
>- 乘客到达登机口并根据分配的优先级加入优先队列。
>- 商务舱乘客拥有最高优先权，其次是豪华经济舱，最后是经济舱。
>
>2.优先级分配（优先级队列创建）：
>
>- 登机口工作人员在乘客到达时为其分配优先级。 持有商务舱机票的乘客被分配最高优先级，豪华经济舱乘客次之，经济舱乘客最低。
>
>3.队列组织（优先级队列结构）：
>
>- 队列的组织方式是，优先级最高（商务舱）的乘客排在最前面，其次是豪华经济舱乘客，最后是经济舱乘客。
>
>4.登机流程（处理任务）：
>
>- 登机口工作人员从队列前面的乘客开始（最高优先级），呼叫乘客登机。
>- 商务舱乘客首先登机，然后是豪华经济舱，然后是经济舱。
>
>5.任务完成（旅客登机）：
>
>- 每位乘客完成登机流程并在飞机上就座。
>- 一旦乘客登机，他们就不再处于优先队列中。



### Efficient Insertion and Deletion

The heap structure allows for efficient insertion and deletion of elements while maintaining the heap property. Specifically:
- Insertion: Adding a new element and restoring the heap property by "bubbling up" the new element takes O(log n) time.
- Deletion: Removing the root (max or min) and restoring the heap property by "bubbling down" the new root also takes O(log n) time.



### Heap Sort

- Heapsort is a comparison-based sorting algorithm that uses a binary heap data structure to build a max heap and repeatedly extract the maximum element.
- Heap Sort uses a max heap to repeatedly extract the maximum element, leading to a sorted sequence. Heap Sort has a time complexity of \(O(n \log n)\), making it suitable for certain scenarios.



### Graph Algorithms:

- Heaps are used in various graph algorithms like Dijkstra's algorithm for finding the shortest path. [find the smallest path from one point to another point]



### Space Efficiency

Heaps can be efficiently represented using arrays, making them space-efficient compared to other tree structures. The array representation enables direct access to elements, making heap operations faster.



### Memory Locality

Heap operations, especially those involving the root, are often more cache-friendly than linked structures. This can lead to better performance in practice.





## complete tree???

a special type of binary tree in which every level, except possibly the last, is completely filled, and all nodes are as left as possible. 

In simpler terms, a complete binary tree is a binary tree in which nodes are added from left to right across each level, and there are no missing nodes in the tree until the last level, where missing nodes, if any, are concentrated towards the right.

This means that the tree is structured in such a way that nodes are added from left to right across each level, and the last level is filled from the left with any missing nodes concentrated towards the right.

> **Characteristics**
>
> 1. Filled Levels:
>    - All levels, except possibly the last, are completely filled with nodes.
>
> 2. Left-Filled:
>    - Nodes are added from left to right across each level, maintaining a left-to-right order.
>
> 3. Last Level Filling:
>    - In the last level, if there are any missing nodes, they are concentrated towards the right.

```
# Complete Binary Tree:
      1
     / \
    2   3
   / \ /
  4  5 6

# Non-Complete Binary Tree:
      1
     / \
    2   3
   / \
  4   5
```

> Complete binary trees are commonly used in implementations of binary  heaps, where the elements are stored in an array, and the array indices  correspond to the positions of nodes in a complete binary tree. The  completeness property ensures a compact representation and efficient  access to elements in the array. 
>
> 完全二叉树和二叉堆之间的关系是，二叉堆是一种特定类型的完全二叉树，它遵循堆顺序属性，并在数组中有效地表示。 完整性属性确保结构保持平衡，使其适合优先级队列和堆排序等应用程序。 
>
> **the relationship between binary heap and the complete tree:**
>
> 1. Array Representation:
>    - One of the key relationships is that a binary heap can be efficiently represented using an array, leveraging the complete binary tree property.
>    - In this array representation, the root of the heap is stored at index 0, and for any node at index ii, its left child is at index 2i+12i+1 and its right child is at index 2i+22i+2.
> 2. Efficient Insertion and Deletion:
>    - The complete binary tree property ensures that the structure remains balanced during insertions and deletions, allowing for efficient operations.
>    - When elements are inserted, they are added as the leftmost node in the last level, ensuring that the tree remains complete.
>    - When the maximum element is removed (in the case of a max heap), it is usually the root, maintaining the heap order property, and then the last element replaces the root and is moved down the tree to restore the heap order property.
> 3. Efficient Representation in Memory:
>    - Because of the array representation and the complete binary tree structure, a binary heap uses memory efficiently.



























# **Graphs**



## graph & chart & diagram

1. **Graph:**
   - In mathematics and computer science, a graph is **a collection of nodes (vertices) and edges that connect pairs of nodes.** Graphs are used to **model relationships between entities.**
   - In a more general sense, "graph" can refer to any visual representation that shows the relationship between different elements. For example, a flowchart or network diagram may be considered a type of graph.
   - The meaning of "graph" can vary depending on the context in which it is used.

2. **Chart:**
   - A chart is a visual representation of data that is often used to **illustrate trends, relationships, or comparisons.** It typically involves the use of graphical elements such as bars, lines, pie slices, or other symbols to convey information.
   - Common types of charts include bar charts, line charts, pie charts, and scatter plots.
   - Charts are widely used in various fields, including business, science, and education, to present data in a visually accessible format.

3. **Diagram:**
   - A diagram is a visual representation that uses symbols, lines, and shapes to **illustrate the structure or workings of a system or process.** Diagrams are often used to simplify complex concepts and make them easier to understand.
   - Diagrams can encompass various types, such as flowcharts, Venn diagrams, organizational charts, and circuit diagrams.
   - Unlike charts and graphs, which primarily represent data, diagrams convey structural or procedural information.

> Here are some common types of diagrams used in computer science:
>
> 1. **Flowchart:**
>    - A flowchart is a diagram that represents a process, algorithm, or workflow. It uses different shapes to represent different types of steps or actions and arrows to indicate the flow of control.
>
> 2. **UML Diagrams (Unified Modeling Language):**
>    - UML diagrams are a set of standardized diagrams used in software engineering to visualize and document different aspects of software systems. Common types of UML diagrams include class diagrams, sequence diagrams, activity diagrams, and more.
>
> 3. **Entity-Relationship Diagram (ERD):**
>    - ER diagrams are used to model the structure of a database. They illustrate the relationships between different entities in a database and help in designing and understanding database schemas.
>
> 4. **Network Diagram:**
>    - Network diagrams depict the connections between devices and components in a computer network. They are used for network design, troubleshooting, and documentation.
>
> 5. **Data Flow Diagram (DFD):**
>    - DFDs represent the flow of data within a system. They illustrate how data moves through different processes, data stores, and external entities.
>
> 6. **State Diagram:**
>    - State diagrams, also known as state machines, depict the different states that an object or system can be in and the transitions between these states.
>
> 7. **Class Diagram:**
>    - A class diagram in UML represents the structure and relationships between classes in object-oriented programming. It includes information about classes, attributes, methods, and associations.
>
> 8. **Sequence Diagram:**
>    - Sequence diagrams in UML show the interactions and messages exchanged between objects or components over time, illustrating the dynamic behavior of a system.





## Types

### Directed

A directed graph, also known as a digraph, is a graph that is made up of a set of vertices (nodes) and a set of directed edges (arcs) connecting pairs of vertices. 

In a directed graph, each edge has a direction, indicating that it goes from one vertex to another. This directionality implies a one-way relationship between the connected vertices.

> Directed graphs have applications in various areas, including  representing dependencies, modeling networks, describing processes, and  more. 

#### key characteristics

1. Vertices (Nodes):
   - Represent entities or points in the graph.
2. Directed Edges (Arcs):
   - Connect pairs of vertices with a specific direction from one vertex to another.
   - An edge (u,v)(u,v) goes from vertex uu (the starting or tail vertex) to vertex vv (the ending or head vertex).
3. Adjacency:
   - Two vertices uu and vv are considered adjacent if there exists a directed edge from uu to vv.
4. Outdegree and Indegree:
   - The outdegree of a vertex is the number of outgoing edges from that vertex.
   - The indegree of a vertex is the number of incoming edges to that vertex.
5. Cycles and Acyclic Graphs:
   - A directed graph may contain cycles, forming a cycle if there is a sequence of directed edges that loops back to a vertex.
   - A directed acyclic graph (DAG) is a special case of a directed graph with no cycles.



### Undirected

An undirected graph is a graph in which edges have no direction. 

If there is an edge between vertices u and v, it implies that there is a connection between uu and v, and vice versa.

>Undirected graphs are commonly used to model relationships where the connection between entities is mutual or bidirectional. They have applications in various fields, including social network analysis, transportation networks, computer networks, and more.

#### key characteristics

1. Vertices (Nodes):
   - Represent entities or points in the graph.
2. Undirected Edges:
   - Connect pairs of vertices without a specific direction.
   - An edge between vertices uu and vv is often denoted as {u,v}{u,v} or simply uvuv.
3. Adjacency:
   - Two vertices uu and vv are considered adjacent if there exists an undirected edge between them.
4. Edge Symmetry:
   - The edges are symmetric; if there is an edge uvuv, then there is also an edge vuvu.
5. Cycles:
   - An undirected graph may contain cycles, forming a cycle if there is a sequence of edges that loops back to a vertex.



### Weighted

A weighted graph is a type of graph where each edge is assigned a numerical value, called a "weight." 

These weights represent some measure of distance, cost, or any other relevant quantity associated with the connection between the vertices connected by that edge.

Weighted graphs allow for a more nuanced representation of relationships between entities by considering the associated costs or distances. Algorithms and techniques for weighted graphs often involve finding paths, such as the shortest path or minimum spanning tree, that optimize the total weight based on specific criteria.

> Weighted graphs are commonly used in various applications, including:
>
> 1. Networks and Transportation:
>    - Modeling transportation networks where edges represent roads or routes, and weights represent distances or travel times.
> 2. Telecommunications:
>    - Representing communication networks where edges correspond to communication links, and weights represent the cost or quality of the connection.
> 3. Optimization Problems:
>    - Solving optimization problems where the goal is to find the path with the minimum or maximum total weight.
> 4. Resource Allocation:
>    - Allocating resources in scenarios such as project planning, where edges represent tasks and weights represent time or resource requirements.

#### key characteristics

1. Vertices (Nodes):
   - Represent entities or points in the graph.
2. Weighted Edges:
   - Connect pairs of vertices and are assigned numerical values **(weights)**.
   - The weight of an edge between vertices u and v is denoted as **w(u,v)**.
3. Adjacency:
   - Two vertices u and v are considered adjacent if there exists a weighted edge between them.
4. Edge Symmetry:
   - The weights on edges are not necessarily symmetric; w(u,v) may be different from w(v,u).





## Terminology

### Vertex (vertices)

A point on the graph. We have called these “nodes” in the past. Usually represented as letters or numbers in theory. 

### Edge

A connection between to vertices. Represented by naming the two vertices. So (A,B) would be the edge between Vertex A and Vertex B.

### Set

A group of items that have no importance or order to them. So {A,B,C} is equivalent to {B,C,A} and {C,B,A} etc. The order doesn't' matter. They are just a group of items that share something in common. 【Edge set: {(A,B),(B,C),(A,C)}】

### Cyclic

A **directed graph** which has **at least one cycle**. A cycle is where you can start at onevertex, and arrive back at that vertex through the graph. So A->B->C->A. This path starts at A, and ends at A.

### Ayclic

A **directed graph** which **doesn’t have any cycles**. Once you touch a vertex, there is no way to get back to that vertex

### Connected

A graph in which each vertex is connected to together by some path. So from any node, one could follow the edges and make it to every other node.

### Disconnected

A graph in which every single vertex is not connected. This could be a single vertex by itself or a bunch of smaller connected graphs. The point is at least one of these vertices are not connected with the rest.  

> A disconnected graph is a graph in which there is no path between at least two vertices. In simpler terms, a graph is considered disconnected if it consists of two or more separate components (subgraphs), and there is no direct connection between these components.

### Adjacency

When two vertices are connected to one another. So if we have the edge (A,B), A and B are adjacent to one another.



##  Graph Traversal 

### Depth First Search (DFS) 

a graph traversal 遍历  algorithm to explore and visit all the vertices of a graph in a systematic manner 系统的方式 . 

<img src="picture\depth first search.jpg" alt="depth first search" style="zoom: 100%;" />

DFS can be implemented using either recursion or an explicit stack data structure. 

The recursive version is more elegant, while the iterative version using a stack is often preferred in practice to avoid stack overflow errors for large graphs. 

> It starts at a selected source vertex and explores as far as possible  along each branch before backtracking. 
>
> The basic idea is to go as deep as possible along one branch before exploring other branches. 

> The name "Depth-First Search" comes from the strategy employed by the algorithm as it traverses a graph. The term "depth" refers to the depth or distance from the starting vertex that the algorithm explores before backtracking. The algorithm goes as deep as possible along one branch  before exploring other branches. 
>
> The "depth-first" aspect of the algorithm's name reflects its tendency to explore as deeply as possible along one path before considering other paths, making it well-suited for tasks like exploring and searching in graphs. 

#### how DFS works?

1. Start at a Source Node: Choose a starting vertex (or node) as the source of the traversal.
2. Explore as Deep as Possible: Move to an adjacent, unvisited vertex and continue the process, going as deep as possible along each branch before backtracking.
3. Backtrack When Necessary: If you reach a vertex with no unvisited neighbors, backtrack to the previous vertex that has unexplored branches and continue the process.
4. Mark Visited Nodes: Keep track of visited vertices to avoid infinite loops in case of cycles. This is commonly done by marking each visited node.

#### applications

- Graph Traversal: Visiting and processing all vertices of a graph.
- Pathfinding: Finding a path between two vertices in a graph.
- Topological Sorting: Ordering the vertices of a directed acyclic graph (DAG) based on precedence.
- Connected Components: Identifying connected components in an undirected graph.
- Maze Solving: Determining a path through a maze.



### Breadth First Search (BFS) 

a graph traversal algorithm used to explore and visit all the vertices of a graph in a breadthward motion 广度运动 , i.e., it explores all the neighbors of a vertex before moving on to the next level of neighbors.

<img src="picture\breadth first search.jpg" alt="breadth first search" style="zoom: 100%;" />

BFS is often employed when the goal is to find the shortest path between two vertices or to visit all vertices in a connected component. 

#### how BFS works?

1. Start with a source vertex. This is the vertex from which the BFS begins. Create a queue data structure to keep track of the vertices to be visited.
2. Enqueue the source vertex into the queue. Dequeue a vertex from the queue and visit it. Enqueue all unvisited neighbors of the visited vertex into the queue.
3. Repeat the process until the queue is empty. Dequeue a vertex, visit it, and enqueue its unvisited neighbors. Continue this process until all vertices have been visited or until the desired condition is met.
4. Keep track of visited vertices to avoid processing the same vertex multiple times. This is commonly done by marking each visited node.

####  Applications 

- Shortest path finding in an unweighted graph.
- Network analysis.
- Web crawling and indexing.
- Finding connected components in an undirected graph.



### Runtime

often expressed in terms of the number of vertices (n) and edges (m) in the graph being traversed.

| types                | time complexity expression | relationship |
| -------------------- | -------------------------- | ------------ |
| depth first search   | O(V+E)                     | linear       |
| breadth first search | O(V+E)                     | linear       |

> The recursive implementation of DFS usually involves a depth-first traversal of the entire graph, which contributes to the linear time complexity.
>
> BFS systematically explores vertices level by level, and in the worst case, it may visit all levels.
>
> making them efficient algorithms for graph traversal, especially in scenarios where the number of vertices and edges is not prohibitively large.

It's important to note that these time complexities assume that the graph is represented in an adjacency list or adjacency matrix data structure, where the time to access vertices and edges is O(1). If a different representation is used, the time complexity might vary.

Additionally, in a graph with a constant number of edges per vertex (**sparse graph**), the terms involving edges may be dominated by the term involving vertices, and the time complexity is often expressed as O(V).



#### sparse and dense gragh

In the context of a graph, density refers to the ratio of the number of edges (E) to the number of vertices (V). A **sparse graph** is one where the number of edges is much less than the maximum possible number of edges.

> If a graph is sparse, meaning that E is much less than V^2, the terms involving edges may become less significant compared to the terms involving vertices. In such cases, the time complexity is often expressed as O(V), as the contribution from edges is relatively small in comparison.
>
> This observation is relevant when analyzing the efficiency of graph algorithms, particularly in scenarios where the graph is expected to be sparse.

A graph can have a large number of edges relative to the number of vertices which is referred to as "dense graphs." Density in this context refers to the proportion of actual edges to the total number of possible edges in a graph.

>A classic example of a dense graph is the complete graph, denoted as \( K_n \), where every pair of distinct vertices is connected by an edge. In a complete graph with \( n \) vertices, there are \( n(n-1)/2 \) edges, which grows quadratically with the number of vertices. As a result, the edge density is high in complete graphs.
>
>Another example might be a graph representing a fully connected network where each vertex is connected to every other vertex. In certain communication or social network scenarios, this kind of dense connectivity can occur.
>
>In these cases, even if the number of vertices is not extremely large, the number of edges can become prohibitively large, especially as a function of the number of vertices. Algorithms that depend on edge-wise processing, traversal, or storage may face challenges with the increased number of edges.

It's important to consider the characteristics of the graph, such as density, when choosing algorithms and data structures to process or represent the graph efficiently.

Calculating the time complexity of algorithms on dense graphs, where the number of edges is relatively high compared to the number of vertices, involves considering the impact of both vertices and edges on the algorithm's performance.

1. Vertex and Edge Counts:
   - Let V be the number of vertices in the graph.
   - Let E be the number of edges in the graph.
2. Algorithm Complexity:
   - For algorithms that depend on vertices (e.g., DFS, BFS), the time complexity will typically have a term involving V.
   - For algorithms that depend on edges (e.g., algorithms for finding minimum spanning trees, edge-based traversals), the time complexity will have a term involving E.
3. Vertex and Edge Density:
   - Calculate the density of the graph by considering the ratio E/V (edges per vertex).
   - For dense graphs, this ratio tends to be higher, potentially close to V or even V2 in extreme cases.
4. Dominant Term:
   - Identify the dominant term in the time complexity expression. In a dense graph, the term involving either V or E may dominate the other.
5. Expressing Complexity:
   - Express the time complexity with the dominant term. For example, if the term involving vertices dominates, the time complexity might be expressed as O(V2) or O(V3), depending on the specific algorithm.
6. Consider Other Factors:
   - Consider other factors that may contribute to the overall complexity, such as constant factors, lower-order terms, and additional operations within the algorithm.





##  Graph Algorithms ???

###  Shortest Path Algorithms 

Dijkstra's algorithm, Bellman-Ford algorithm for finding the shortest paths in weighted graphs.

#### Dijkstra's algorithm

一个用于计算单源最短路径的经典算法，适用于图中所有边的权重非负的情况。

##### 核心思想

通过贪心策略，每次选择当前已知的最短路径进行扩展，逐步扩展已知的最短路径，最终求得从源节点到所有其他节点的最短路径。这种局部最优的选择最终会导致全局最优解。

##### 时间复杂度

- 使用邻接矩阵时，时间复杂度为 $O(V^2)$，其中 V 是图的顶点数。
- 使用优先队列（最小堆）时，时间复杂度可以优化到 O((V + E) log V)，其中 E 是边的数量。

##### 步骤

1. 初始化：
   >设置一个距离数组 `dist[]`，用于存储从源节点到每个节点的最短路径初始值。将源节点到自身的距离设为0，其他节点到源节点的距离设为无穷大（表示尚未访问）。
   >
   >使用一个优先队列（最小堆）来选择当前距离源节点最近的节点。队列中存储的元素是节点及其对应的最短距离。
   >
   >设置一个访问标记数组，用于标记哪些节点已被处理。

2. 选择当前距离最小的节点：从优先队列中选择一个最短路径未确定的节点，记为 `u`，并将其标记为已访问。

3. 更新邻接节点的距离：对于节点 `u` 的所有邻居节点 `v`，检查从 `u` 到 `v` 的距离（即边的权重）是否能提供更短的路径。如果是，更新 `v` 的最短路径（即 `dist[v] = dist[u] + weight(u, v)`），并将 `v` 放入优先队列。

4. 重复过程：重复步骤2和步骤3，直到优先队列为空或所有节点的最短路径都已确定。

5. 结束：最终，`dist[]` 数组中存储了从源节点到所有节点的最短路径。





###  Minimum Spanning Tree (MST)  最小生成树 





###  Topological  拓扑 Sorting 

> 图可以用于表示部分排序或先后关系（precedence），这种结构广泛应用于很多领域，比如课程要求的序列、软件构建的依赖关系等。
>
> - **大学课程要求序列**：假设你必须先修完某些课程才能修其它课程，这就可以通过有向无环图（DAG）来表示。每个课程是一个节点，课程之间的依赖关系通过有向边表示。例如，修完数学 101 才能修数学 102，修完数学 102 才能修数学 201，等等。
> - **软件构建依赖关系**：在软件开发中，编译和构建步骤可能有先后顺序。例如，库 A 必须在库 B 之前构建，库 C 依赖于 A 和 B。这样的依赖关系也可以用图来表示，确保所有必要的组件按照正确的顺序构建。
>
> 在这些图中，并不是所有的节点都有前驱或后继关系。例如，有些课程可能不依赖于其他课程，也没有其他课程依赖它们；这些课程将是“独立”的节点，不需要被排序或依赖。

一种对有向无环图（DAG，Directed Acyclic Graph）进行排序的方法，它将图中的所有节点排列成一个线性顺序，满足以下条件：

1. **所有边的方向都得到遵循**：如果有一条边从节点 A 指向节点 B，则在排序中，节点 A 必须出现在节点 B 之前。
2. 拓扑排序的结果通常不是唯一的：在大学课程的安排中，通常有多种方式可以完成这些课程。例如，你可以选择先修 `CS 101` 再修 `CS 102`，或者先修 `CS 103` 再修 `CS 105`，但最终你仍然需要按照某种顺序完成所有课程。这个顺序的确定通常有多种可能的排列方法。
3. **适用于有向无环图**：拓扑排序只对没有环路的有向图有效。如果图中存在环路，无法进行拓扑排序。

>### 为什么不允许图中存在环路（Cycles）？
>
>图中如果存在环路，意味着有一个任务或依赖关系形成了循环，例如：
>
>- 任务 A 依赖任务 B，
>- 任务 B 依赖任务 C，
>- 任务 C 又依赖任务 A。
>
>这会导致无法找到一个明确的执行顺序，因为任务 A、B、C 之间的依赖关系互相回环，无法确定哪个任务应该先执行。
>
>环路的存在会使得拓扑排序无法进行，因为拓扑排序要求没有依赖关系的任务可以按顺序执行。因此，只有没有环路的有向图（即有向无环图，DAG）才适合进行拓扑排序。

拓扑排序常用于表示依赖关系的场景，例如任务调度、编译器中的依赖管理等。



可以使用两种常见的方法：

1. **深度优先搜索（DFS）**：递归地访问每个节点，并在访问完成时将节点加入结果列表。
2. **入度为 0 的节点**：使用队列管理当前入度为 0 的节点，每当一个节点被处理完后，将其邻接节点的入度减少，如果入度为 0，则加入队列。



#### Kahn’s algorithm

实现拓扑排序的一种算法，适用于有向无环图（DAG）。

##### 核心思想

通过处理图中的入度为零的节点（没有前置任务的节点），逐步更新图的入度，直到所有节点都被处理完。

##### 时间复杂度

 O(V + E)，其中 V 是节点数，E 是边数。这个复杂度来自于两部分：计算每个节点的入度 O(V)，以及处理每条边 O(E)。



##### 步骤

1. **确定所有节点的入度**：首先计算每个节点的入度（即有多少条边指向该节点）。

2. **初始化一个队列**：创建一个队列，用来存放入度为零的节点（这些节点可以先执行，因为它们没有依赖关系）。

3. **将所有入度为零的节点放入队列**：将图中所有入度为零的节点加入队列。

4. **处理队列**：

   >- 从队列中取出一个节点，并将它添加到排序后的列表中。
   >- 找出该节点的所有出边（即该节点指向的节点），并将这些出边指向节点的入度减 1。
   >- 如果减去入度后，某个节点的入度变为零，则将该节点加入队列。

5. **当队列为空时停止**：队列为空时，说明所有节点都已处理完，排序完成。













# Hashing

a technique used to map data of arbitrary 任意 size to fixed-size values, usually for the purpose of efficiently organizing, indexing, and retrieving 检索 data.

a powerful tool that can help improve the lookup times in a dataset. 

It works to help store random input into a reliable quick O(1) access time  (if optimized). The algorithms used for this also help with password storage, databases, and cryptography.  



## hash origin

The term "hash" has roots in mathematics, particularly in the field of cryptography, where it refers to a process of converting input data into a fixed-size string of characters.

> The concept of hashing, involving hash functions and hash codes, was adopted into computer science and various applications due to its utility in achieving certain desirable properties:
>
> - Uniform Distribution: the hash codes should be evenly spread across the possible range of values, reducing the likelihood of collisions.
> - Deterministic Output: the same input will always produce the same hash code.
> - Fixed-Size Representation: Hashing produces a fixed-size representation (hash code) regardless of the size of the input.
> - Efficiency in Retrieval: By using the hash code as an index or address in a data structure like a hash table, applications can achieve **constant-time average-case complexity** for operations like insertion, retrieval, and deletion.
> - Security in Cryptography: hash functions are used for purposes like data integrity verification, digital signatures, and password storage. The one-way nature of cryptographic hash functions makes it computationally difficult to reverse the process and retrieve the original input.
>
> Due to these properties, the term "hash" has become **synonymous with the process of using hash functions to convert data into a fixed-size representation.** The word has been widely adopted and used in various fields, including computer science, cryptography, and information retrieval.



## Hash Function

A hash function is a mathematical function that takes input data (or a "key") and produces a **fixed-size string of characters**, which is typically a hash code.

> Ideally, a good hash function minimizes the likelihood of producing the same hash code for different inputs (**collision-resistant**).

```python
# a simple example to illustrate basic hashing using the built-in hash() function:
data = "example"
hash_value = hash(data)
print(f"The hash value of '{data}' is: {hash_value}")
```



### Common Functions

MD5 (Message Digest Algorithm 5): Although widely used in the past, MD5 is now considered insecure for cryptographic purposes due to vulnerabilities.

SHA-256 (Secure Hash Algorithm 256-bit): A widely used cryptographic hash function for secure applications.



### Applications

   - Data Retrieval: Hashing is used in hash tables for efficient data retrieval based on keys.
   - Cryptographic Hash Functions: Hash functions are used in cryptography for integrity checking, digital signatures, and password storage.
   - Caching: Hashing is used in caching mechanisms to quickly check whether a particular piece of data is in the cache.



###  applications about zipping and condense files 

While hashing itself is not the primary method for compressing or condensing files, it plays a role in ensuring data integrity, identifying duplicate chunks, and facilitating efficient operations within compression algorithms. The combination of various techniques, including hashing, contributes to the effectiveness of compression and deduplication processes.

1. **Hashing in Data Integrity Checking:**
   - Hash functions are commonly used in data integrity checking. Before compression, a hash value (checksum) of the original file may be calculated using a hash function (e.g., SHA-256). This hash value is then stored or transmitted along with the compressed file.
   - After decompression, the hash function is applied to the decompressed data, and the result is compared with the original hash value. If they match, it indicates that the decompressed data is likely intact.

2. **Data Deduplication:**
   - Hashing is used in data deduplication, a process where duplicate copies of data are identified and removed. Each unique chunk of data is assigned a unique hash value.
   - When compressing files, duplicate chunks are replaced with references to a single copy, significantly reducing the amount of storage needed.

3. **Content-Defined Chunking:**
   - Some compression algorithms use content-defined chunking, where the data is divided into fixed-size or variable-size chunks based on the content. Hash functions are used to identify the boundaries of these chunks.
   - This approach can be more effective in handling data with repetitive patterns, as it adapts to the actual content rather than fixed block sizes.

4. **Lossless Compression Algorithms:**
   - Hashing is not the primary technique in lossless compression algorithms like ZIP, but these algorithms often involve a combination of techniques, including dictionary-based compression and entropy coding.
   - In some cases, a hash table might be used for efficient dictionary lookups, helping in the compression process.

5. **Condensing Files Through Compression:**
   - Compression algorithms, such as ZIP or gzip, aim to condense files by representing data in a more efficient manner. Common techniques include replacing repeated sequences with shorter representations (dictionary compression) and encoding symbols with variable-length codes (Huffman coding).
   - Hash functions might be involved in building data structures like hash tables or hash trees to efficiently manage and access compressed data.





## Hash Code / Value

The **output** of a **hash function** is commonly referred to as a **hash code** or **hash value**.

The output of a hash function should be **deterministic**, meaning the same input will always produce the same hash code.



## Hash Table

a data structure which uses a hash function to compute an index into an array of buckets or slots, from which the desired value can be found, that allows you to store and retrieve data quickly.

The most important thing about a hashing algorithm is that it repeatable. [means must be consistent] 

If you input x and it outputs "ikdiejd", it should output that value every single time. If it doesn't have a 100% chance of creating the output every single time, then it's not a hashing algorithm. This assumption allows us to store data and retrieve data reliably, which gives us the constant access time.

> The primary idea is to use the hash code of the data (or key) as an index to quickly locate the data in the table without having to search through each element.

> a hash table is like a bookshelf with labeled sections (buckets), where each section has multiple shelves (elements). 
>
> The hash function acts as a guide to quickly find the right section, and each section may contain a list of items (due to collisions) that you need to look through. 
>
> The goal is to make data retrieval efficient by narrowing down the search space using the hash code.



### Array or Bucket

A hash table consists of an array (or bucket) where data is stored. Each element in the array is called a "bucket" or a "slot."



### Basic Operations

1. Insertion:
   - To insert data into a hash table, the hash function is applied to the key to determine the index where the data should be stored. The data is then placed in the corresponding bucket.
   
2. Retrieval:
   - When you want to retrieve data from the hash table, the hash function is applied to the key to find the index. The data is then looked up in the bucket at that index.
   
3. Deletion:
   - To delete data, you apply the hash function to find the index and then remove the data from the corresponding bucket.



### Examples

Suppose you have a hash table with an array of size 10. You want to store the phone numbers of your friends based on their names.

1. You use a hash function to convert each name into a hash code.
2. The hash code determines the index in the array where the phone number should be stored.
3. When you want to find a friend's phone number, you use the hash function on their name to quickly locate the corresponding bucket and retrieve the phone number.



### Collision

A collision occurs when two different inputs produce the same hash code.

> Since a hash table is essentially an array with a finite number of slots, multiple keys may hash to the same slot.
>
> Collisions are common, and handling them is a critical aspect of designing a hash function and hash table.



### Collision Resolution

Separate Chaining: Each index in the hash table stores a linked list of elements that hash to the same index.

>  In chaining, each slot in the hash table contains a linked list or another data structure (like a tree) to store multiple elements that hash to the same index.
>
>  When a collision occurs, the new element is simply added to the existing list at that index.
>
>  ```
>  Slot 0: [data1] -> [data2] -> [data3]
>  Slot 1: [data4] -> [data5]
>  Slot 2: [data6]
>  # To retrieve an element, you use the hash function to find the index and then search through the linked list or data structure at that index.
>  ```

Open Addressing: When a collision occurs, the algorithm searches for the next available slot in the table.

>In open addressing, when a collision occurs, the algorithm searches for the next available (unoccupied) slot in the hash table until an empty slot is found.
>
>There are different strategies for finding the next slot, such as linear probing (check the next slot), quadratic probing (check slots with increasing gaps), and double hashing (use a second hash function to determine the step size).



### Collision Handling

Collisions occur when two different keys produce the same hash code, i.e., they map to the same index. 

Common methods to handle collisions include **chaining** (where each index stores a linked list of elements) or **open addressing** (where the algorithm searches for the next available slot).

#### Pros and Cons

- Chaining:
  - Pros: Simple to implement. Allows for a variable number of elements in each slot.
  - Cons: Requires additional memory for pointers or data structures.

- Open Addressing:
  - Pros: No need for additional data structures. Can be more memory-efficient for small data sets.
  - Cons: More complex to implement. May lead to clustering (consecutive occupied slots).

> The choice between chaining and open addressing depends on factors like the size of the data set, expected number of collisions, and memory considerations.



### Runtime Complexity

| resolution types  | activity         | best case O | average case O | worst case O |
| ----------------- | ---------------- | ----------- | -------------- | ------------ |
| open addressing   | searching        | O(1)        | O(1)           | O(n)         |
|                   | insertion        | O(1)        | O(1)           | O(n)         |
|                   | deletion         | O(1)        | O(1)           | O(n)         |
|                   | space complexity | O(n)        | O(n)           | O(n)         |
| closed addressing | searching        | O(1)        | O(1)           | O(n)         |
|                   | insertion        | O(1)        | O(1)           | O(n)         |
|                   | deletion         | O(1)        | O(1)           | O(n)         |
|                   | space complexity | O(m+n)      | O(m+n)         | O(m+n)       |





## Load factor and Load balance

**load factor** is the ratio of the number of elements stored in the hash table to the total number of slots in the hash table. 

**load balance** refers to the even distribution 均匀分布 of keys across the available slots in the hash table. 

> A common guideline is to try to keep the load factor below a certain threshold to balance the trade-offs between memory usage and performance. 
>
> The exact threshold may vary based on the specific application and the collision resolution strategy used in the hash table.

>A well-balanced hash table ensures that the keys are distributed  uniformly, minimizing the likelihood of collisions and optimizing the  performance of the hash table. 
>
>Ensuring load balance is crucial for the efficiency of hash tables. An imbalanced hash table, where keys are concentrated in a few slots, can result in poor performance and defeat the purpose of using a hash table for fast data access.

It is a measure of how "full" the hash table is.  The load factor is commonly denoted by the symbol λ and is calculated using the formula: 
$$
\lambda = \frac{N}{M}\\\text{ }\\lambda \text{ is the load factor}\\N \text{ is the number of elements (keys) stored in the hash table}\\m \text{ is the total number of slots (size) of the hash table}\\
$$

> - A high load factor means that a large portion of the hash table is occupied by elements, and as a result, collisions are more likely to occur. 
> - A low load factor implies that the hash table has plenty of empty slots, reducing the chances of collisions.
>
> 1. **Low Load Factor:**
>    - Pros: Lower likelihood of collisions, potentially better performance.
>    - Cons: Wasted memory due to empty slots, and the hash table may be larger than necessary.
>
> 2. **High Load Factor:**
>    - Pros: More memory-efficient, as there are fewer empty slots.
>    - Cons: Increased likelihood of collisions, potentially degrading performance.



### goals

1. Even Distribution:
   - The primary goal of load balancing is to distribute keys evenly across the slots of the hash table. An even distribution minimizes the number of collisions and ensures that each slot is utilized effectively.
2. Optimal Performance:
   - Load balancing contributes to the optimal performance of hash table operations (insertion, retrieval, deletion). When keys are evenly distributed, the time complexity of these operations remains low, leading to efficient data access.
3. Preventing Clustering:
   - Uneven distribution, known as clustering, can occur when multiple keys hash to the same slot or a small set of slots. This can lead to a degradation in performance as the number of collisions increases. Load balancing helps prevent clustering.



### Load Balancing Strategies

1. Rehashing:
   - When the load factor becomes too high, rehashing may be performed. Rehashing involves creating a new, larger hash table and redistributing the keys to achieve a lower load factor. This helps maintain a well-balanced hash table.
2. Dynamic Resizing:
   - Some hash table implementations dynamically resize the table based on the load factor. When the load factor exceeds a certain threshold, the table size is increased, and when it falls below another threshold, the table size is decreased.
3. Probing Methods:
   - The choice of probing methods in collision resolution techniques (e.g., linear probing, quadratic probing) can impact load balancing. Some probing methods may lead to better load balancing under certain conditions.



### relationship with collision resolution

The way collisions are handled directly affects load balance.





## Rehashing

a process used in hash tables to resize the table when the load factor becomes too high or too low.

The goal is to **maintain a balance** between the number of elements in the table and the number of slots available, optimizing the performance of the hash table.

The term "rehashing" encapsulates the entire process, including the multiple hashings of existing keys as they are moved to new locations in the resized or restructured hash table. This process is crucial for achieving better load balance and maintaining the efficiency of hash table operations.

To sum up, rehashing involves hashing existing keys multiple times as part of the process of redistributing them to a new or resized hash table.

>The new hash table might have a different size, which influences the load factor and, consequently, the efficiency of the hash table.
>
>It's important to note that the choice of a new table size during rehashing is often based on considerations such as load factor targets, anticipated future growth, and the desire to avoid clustering. 
>
>Additionally, some implementations may use more sophisticated techniques, such as doubling or halving the size, to achieve efficient rehashing.



### situations where rehashing is applied

1. Load Factor Too High:
   - When the number of elements (keys) in the hash table becomes significant compared to the total number of slots, resulting in a high load factor, collisions are more likely to occur. Rehashing is performed to increase the size of the table, reducing the load factor and alleviating the potential for collisions.

2. Load Factor Too Low:
   - Conversely, when the load factor becomes too low (meaning the hash table has many empty slots), rehashing may be performed to decrease the size of the table. This helps conserve memory and ensures that the table is appropriately sized for the number of elements.



### basic steps

1. Initial Hashing:

   - When you initially insert keys into the hash table, you hash each key once to determine its initial position in the table.

2. Load Factor Check:
   
- Over time, as more keys are added or removed, the load factor of the hash table may change. A high load factor indicates that the table is becoming crowded.
  
3. Rehashing Decision:
   
- If the load factor exceeds a certain threshold, you decide to rehash the table. Rehashing involves creating a new, typically larger, hash table.
  
4. Hashing Again**:**
   
- Now comes the part where multiple hashings occur. You take each existing key from the old hash table, hash it again (using a new hash function or the same one adjusted for the new table size), and place it in the corresponding slot in the new hash table.
  
   > To achieve the desired outcome during rehashing, **you generally need to either repeat the original hash function with adjustments for the new size** or use a completely new hash function. The key is to ensure that the keys are distributed in a way that minimizes collisions and maintains good load balance in the resized hash table.
   
   
   
5. Replacing the Old Table:

   - Once all keys have been rehashed and placed in the new table, you replace the old table with the new one.





#### 2 ways of hashing again

1. Reuse the Original Hashing Function repeatedly: **(need to avoid loops)**
   - In this approach, you continue using the original hash function that was employed when the hash table was initially created. The keys from the old hash table are rehashed using the same function but considering the new size or structure of the hash table.

2. Use a New Hashing Function:
   - Alternatively, you may choose to use a completely new hashing function during the rehashing process. This new function could be selected based on the new size or structure of the hash table. The goal is to distribute the keys differently in the resized table compared to the original one.

> Reusing the Original Hashing Function:
> - Simplicity: This approach is straightforward and requires minimal changes to the existing code.
> - Uniformity Concerns: However, if the original hash function is not well-suited for the new hash table size, it might result in clustering or other load balance issues.
>
> Using a New Hashing Function:
> - Flexibility: This approach allows you to choose a hash function specifically tailored for the new hash table size, potentially improving load balance.
> - Implementation Overhead: Implementing a new hashing function adds some complexity to the rehashing process.



### example to understand

Now, let's say you've been adding books to your shelf, and it's becoming quite full. You've noticed that you're running out of space, and the shelf is getting cluttered. This is similar to the situation where the load factor in a hash table becomes too high.

To address this issue, you decide to rehash:

1. Choose a New Bookshelf:
   - You decide to get a larger bookshelf with 10 slots (let's say slots numbered 0 to 9).

2. Create a New Hash Table:
   - You create a new hash table with 10 slots.

3. Rehash Existing Books:
   - Now, you need to take each book from the old bookshelf and find its place on the new bookshelf. You **use the same hash function but consider the new number of slots.**

4. Moving Books to New Slots:
   - **For each book, you hash its title using the new hash function, and you place it in the corresponding slot on the new bookshelf.**

5. Replace Old Bookshelf:
   - Once you've rehashed all the books, you replace the old bookshelf with the new one.

### Outcome

- The new bookshelf (hash table) has more space, and the books are more evenly distributed across the slots.
- The load factor has been reduced, and you've avoided clutter and potential collisions.







## Open Addressing

Open addressing is a collision resolution technique used in hash tables. 

In open addressing, when a collision occurs (i.e., two keys hash to the same index), the algorithm searches for the next available slot within the hash table and places the colliding key there. 

The search for an open slot is performed based on a probing sequence, which determines the order in which the algorithm examines slots.



### Linear Probing 线性探测 

a technique used in **open addressing**, a method for **resolving collisions** in hash tables.

When a collision occurs (i.e., two keys hash to the same index), linear probing involves searching for the next available slot in a sequential manner until an empty slot is found.



#### how linear probing works?

1. Collision Occurs:
   - When hashing a new key, if its hash code corresponds to an index that is already occupied by another key, a collision occurs.

2. Linear Probing:
   - To resolve the collision, the algorithm starts probing or searching for the next available slot by examining consecutive positions in the array. The probing is done in a linear fashion, moving one slot at a time from the original hashed index.
   
3. Next Available Slot:
   - The algorithm continues probing until it finds the next available (unoccupied) slot. Once an empty slot is found, the new key is placed in that slot.
   
4. Retrieval:
   - When retrieving data, the same linear probing process is followed. The algorithm searches for the key by hashing it and then probing linearly until it either finds the key or encounters an empty slot.

5. Deletion:
   - For deletion, **the key is marked as deleted without actually removing it from the table.** This is because subsequent probing might still depend on the original location of the deleted key. During retrieval, deleted slots are treated as available.



#### example

Consider a hash table with 10 slots and the following keys:

1. Hash("apple") = 3
2. Hash("banana") = 5
3. Hash("cherry") = 3 (collision with "apple")

In linear probing, the algorithm would look for the next available slot when a collision occurs. If slot 3 is occupied, it would linearly probe to the next slots until an empty slot is found. For instance:

- Hash("cherry") → Slot 3 (occupied)
- Probing: Slot 4 (empty)
- Place "cherry" in Slot 4

 The resulting hash table might look like this: 

```
Index:  0  1  2  3  4  5  6  7  8  9
Keys:  -- -- -- apple cherry banana -- -- -- --
```



#### Pros and Cons

Pros:
- Simple and easy to implement.
- Memory-efficient since it doesn't require additional data structures.

Cons:
- Tends to lead to clustering, where consecutive slots are filled, potentially causing more collisions. [O(1) ---> O(n)]
- Performance may degrade when the table becomes more than half full (load factor is high).

>With linear probing, we move along and input it at the end of the  cluster, making it larger. This cycle continues until the cluster grows  to such a level that almost every entry starts to run into a collision.  Soon additions and accesses start to take longer and longer as they have to go through more and more collisions. 



### Quadratic Probing

Similar to linear probing, quadratic probing searches for the next available slot when a collision occurs, but it does so using a quadratic function. 

The probing sequence is determined by incrementing the probe 探测  index by successive 连续  squares 平方  of an increment value 增量值 .



#### how linear probing works?

1. Collision Occurs:

- When hashing a new key, if its hash code corresponds to an index that is already occupied by another key, a collision occurs.

2. Quadratic Probing:
   - To resolve the collision, the algorithm starts probing or searching for the next available slot using a quadratic function. The probing sequence is determined by incrementing the probe index by successive squares of an increment value.
   - The general probing formula is **i = (i + c^2) mod M**, where ***i is the current index***, ***c is the increment value***, and ***M is the size of the hash table***.

3. Next Available Slot:
   - The algorithm continues probing until it finds the next available (unoccupied) slot.
   - Once an empty slot is found, the new key is placed in that slot.

4. Retrieval:
   - When retrieving data, the same quadratic probing process is followed. The algorithm searches for the key by hashing it and then probing quadratically until it either finds the key or encounters an empty slot.

5. Deletion:
   - For deletion, the key is marked as deleted without actually removing it from the table. During retrieval, deleted slots are treated as available.



#### increment value

The increment value \(c\) is a **constant** that influences the shape of the quadratic probing sequence. 

The choice of \(c\) is essential, as it can affect the efficiency of the probing process and the avoidance of clustering.

##### Common choices

1. **\(c = 1\):** Traditional quadratic probing often uses \(c = 1\), resulting in a probing sequence of **i, (i + 1^2) \mod M, (i + 2^2) \mod M, (i + 3^2) \mod M, ...**
2. **\(c = 2\):** Another common choice is \(c = 2\), leading to a sequence of **i, (i + 2^2) \mod M, (i + 4^2) \mod M, (i + 6^2) \mod M, ...**

>So if you start at index 1, instead of going to 2 then 3, you would  go 1, 2, 4, 8, 16, etc. Some way to create distance. This makes it so  the collision has a smaller chance of generating a cluster. 
>
>Even  though the chance of a collision is smaller, it doesn't mean that it is  0. This only reduces the chance, and non-randomized data can still  easily create clusters. 



#### Pros and Cons

Pros:
- Avoids clustering that linear probing can lead to.
- Generally performs better than linear probing in scenarios with a moderate number of collisions.

Cons:
- May still lead to clustering, especially when the table is nearly full. (a suitable increment value is crucial for mitigating this issue.)
- Performance may degrade when the table becomes more than half full (load factor is high).







## Closed Addressing 封闭寻址 

Closed addressing, also known as open hashing or separate chaining, is a collision resolution technique used in hash tables.

In closed addressing, each slot of the hash table maintains a linked list or another data structure (such as a tree) that stores all the elements that hash to the same index. When a collision occurs, the new element is added to the existing list at that index.

<img src="picture\closed addressing.png" alt="closed addressing" style="zoom: 80%;" />





### basic steps

1. Hash Function:
   - The hash function is applied to each key to determine its hash code and the corresponding index in the hash table.

2. Collision Occurs:
   - If two keys hash to the same index, a collision occurs.

3. Linked List or Data Structure:
   - Instead of overwriting the existing element, closed addressing stores both the new and existing elements in a linked list or another data structure at that index.
   - Each index in the hash table becomes the head of a linked list or the root of a data structure.

4. Insertion:
   - The new element is inserted at the beginning or end of the linked list, or according to the specific rules of the chosen data structure.

5. Retrieval:
   - When retrieving an element, the hash function is used to find the index, and then a linear search through the linked list or data structure at that index is performed to find the desired element.

6. Deletion:
   - For deletion, the element is located in the linked list, and it is either removed or marked as deleted, depending on the implementation.



### Pros and Cons

Pros:

- Simple implementation.
- Memory-efficient, especially when the load factor is high or when dealing with many collisions.
- Can handle a large number of elements without increasing the size of the hash table.

Cons:
- Retrieval performance may degrade if the linked lists become long (clustering).
- Inefficient when there are many collisions, and the linked lists become too lengthy.
- Overhead of managing the linked lists or data structures.





## Encryption vs Hashing

Encryption and hashing are cryptographic techniques used to secure and protect information, but they serve different purposes and have distinct characteristics.



### Encryption

With encryption, there is a small addition to the hashing algorithm, the ability to decrypt the data afterwards. We don't want to just transfer the data into some other form, we want to be able to transfer it back.

This creates additional work during the hash, as we need to use a method that is easy to decrypt with a key. We don't want it to be so easy to guess that it's easy to decrypt. We do however want to make it so the key is the only way to decrypt the data. 



#### Purpose

Encryption is primarily used for confidentiality. 

It transforms data into a format that is unreadable without the appropriate key or algorithm, ensuring that only authorized parties can access and understand the original information.

#### Two-Way Process

Encryption is a reversible process. 

Encrypted data can be decrypted back to its original form using the appropriate decryption key or algorithm.

#### Key Dependency

Encryption relies on keys. 

The same key is used for both encryption and decryption in symmetric encryption, while different keys are used in **asymmetric encryptio**n (public-key cryptography).

#### Common Algorithms

Common encryption algorithms include AES (Advanced Encryption Standard), DES (Data Encryption Standard), and RSA (Rivest-Shamir-Adleman).

#### Use Cases

Encrypting sensitive information such as personal data, financial transactions, and communication to protect it from unauthorized access.

AES encryption and AES online decryption



### Hashing

#### Purpose

Hashing is primarily used for data integrity verification and fast data retrieval. 

It transforms data into a fixed-size string of characters (hash code), which is typically unique to the input data.

#### One-Way Process

Hashing is a one-way process. 

It is designed to be irreversible, meaning that it should be computationally infeasible to reverse the process and retrieve the original data from its hash code.

#### Keyless

There is no secret key involved, and the same hashing algorithm will produce the same hash code for the same input.

#### Common Algorithms

Common hashing algorithms include SHA-256 (Secure Hash Algorithm 256-bit), MD5 (Message Digest Algorithm 5), and SHA-1 (Secure Hash Algorithm 1).

#### Use Cases

   - Verifying data integrity by comparing hash codes before and after data transfer.
   - Storing passwords securely by hashing and comparing hash codes during authentication.



### Differences

1. Reversibility:
   - Encryption is reversible, allowing the original data to be recovered with the right key. Hashing is designed to be irreversible, providing a fixed-size representation of the data.

2. Purpose:
   - Encryption is used for confidentiality, while hashing is used for data integrity verification and fast data retrieval.

3. Key Dependency:
   - Encryption relies on keys for both encryption and decryption. Hashing is keyless.



## "Salt"

Including a "salt" in a hash refers to adding an additional random or unique value to the data before hashing it. This practice enhances the security of hashed passwords and other sensitive information.

> Adding a salt is a fundamental practice in password security. It helps protect against various attacks, including rainbow table attacks and dictionary attacks, by ensuring that even identical passwords result in different hash values due to the unique salts used.

1. **Hashing Without Salt:**
   - In a basic hashing process, the same input will always produce the same hash output. For example, if you hash the password "password123" without any additional considerations, the hash will be the same every time.

2. **Adding Salt:**
   - To make the hashing more secure, a random or unique value called a "salt" is introduced. This salt is combined with the original data before hashing. The salt is typically a random string of characters.

3. **Increased Security:**
   - Adding a salt ensures that even if two users have the same password, their hashed values will be different because of the unique salt. This prevents attackers from using precomputed tables (rainbow tables) or other common attack techniques.

4. **Per-User Salting:**
   - For each user, a unique salt should be generated and stored along with their hashed password. This means that even if an attacker gains access to the hashed passwords, they cannot easily use precomputed tables to look up common passwords.

5. **Example:**
   - Without salt: `hash("password123")` produces the same result every time.
   - With salt: `hash("password123" + "random_salt")` produces a different result for each user.

6. **Database Security:**
   - In systems where passwords are stored in databases, the salt is often stored alongside the hashed password. This ensures that during the authentication process, the system can apply the correct salt to the entered password and check it against the stored hash.



# Algorithm Toolbox



## Brute Force

## Greedy Approach

一种求解优化问题的算法策略

基本思想是：在每一步的选择中，都采取在当前状态下最优的选择，以期通过局部最优的选择达到全局最优。

### 核心特点

1. **局部最优选择**：每一步的选择都是当前情况下的最佳选择。
2. **无回溯**：一旦做出了选择，就不再回头调整。
3. **全局最优性**：虽然算法通过局部最优选择来推进，但我们假设最终能够得到全局最优解（并非所有问题都满足这一点）。

### 步骤

1. **问题分析**：确定问题是否适合使用贪心策略，是否满足贪心选择性质和最优子结构。
2. **构建选择规则**：定义每一步的局部最优选择。
3. **实现贪心选择**：从问题的初始状态开始，按贪心规则进行选择。
4. **评估结果**：最终检查得到的解是否为全局最优解。

### 适用场景

贪心算法并不是适用于所有问题。对于某些问题，贪心算法可能无法保证找到全局最优解。适用于贪心算法的问题通常具有“贪心选择性质”和“最优子结构”：

- **贪心选择性质**：问题的最优解可以通过局部最优解逐步构建出来。
- **最优子结构**：问题的整体最优解可以通过子问题的最优解组合成。

### 常见问题及解法

1. **背包问题（0/1背包问题）**： 贪心算法不一定能找到最优解。一般来说，背包问题使用动态规划（Dynamic Programming）方法解决效果更好，但贪心算法在某些特定条件下仍有应用，例如“分数背包问题”。
2. **最小生成树（如 Prim 或 Kruskal 算法）**： 在这些图算法中，贪心选择每次选择当前最小的边来扩展生成树。贪心算法可以保证最小生成树的最优解。
3. **活动选择问题**： 选择不重叠的活动，使得总的活动数量最大。贪心算法的做法是每次选择结束时间最早的活动。
4. **霍夫曼编码**： 用于数据压缩，选择出现频率最小的字符来构造编码。



## Divide & Conquer

一种将大问题分解成小问题的策略，最终解决每个小问题，再将它们的解组合起来形成最终解的算法思想。

核心思想是“分而治之”

### 步骤

1. **分解**：将问题分解成若干个规模较小的子问题。
2. **解决**：递归地解决每个子问题，直到子问题的规模足够小，可以直接解决。
3. **合并**：将子问题的解合并，得到原问题的解。

### 特性

- 每个子问题都是相同类型的子问题。
- 每个子问题的规模较小。
- 通过递归求解子问题，可以减少复杂度。











## Tabulation 表格法

动态规划的实现方式之一，通常用于自底向上的求解。

在表格法中，通常会创建一个表格（或数组）来存储子问题的解，逐步填充表格，最后得到整个问题的解。

### 步骤

1. **定义状态**：确定表格中每个元素的含义，通常表示问题的一个子问题。
2. **初始化表格**：根据问题的基础条件，初始化表格的部分值。
3. **填充表格**：通过已有的状态计算其他状态。
4. **返回解**：最终从表格中取出问题的解。











## Memoization 备忘录法

动态规划的另一种实现方式，通常用于自顶向下的递归求解。

通过使用一个数据结构（通常是字典或数组）来记录已经计算过的子问题的解，避免了重复计算。

递归计算时，先检查该子问题的解是否已经计算过，如果已计算过，则直接返回缓存中的结果；如果没有计算过，则递归地计算并缓存结果。

### 步骤

1. **递归求解**：通过递归方式逐步求解问题，直到子问题的规模足够小。
2. **记忆化**：在计算每个子问题时，将结果存储在一个字典或数组中。
3. **查找缓存**：如果某个子问题的解已经计算过，就直接从缓存中读取结果，而不是重新计算。





# Greedy Algorithm



## What is Greedy?

贪心的本质是**选择每一阶段的局部最优**，从而达到全局最优。

> 这时候就需要动态规划。

### 什么时候用贪心

唯一的难点就是如何通过局部最优，推出整体最优。

如何能看出局部最优是否能推出整体最优呢？有没有什么固定策略或者套路呢？**没有！**

**刷题或者面试的时候，手动模拟一下感觉可以局部最优推出整体最优，而且想不到反例，那么就试一试贪心**。

一般数学证明有如下两种方法：

- 数学归纳法
- 反证法

**贪心没有套路，说白了就是常识性推导加上举反例**。



### 解题步骤

贪心算法一般分为如下四步：

- 将问题分解为若干个子问题
- 找出适合的贪心策略
- 求解每一个子问题的最优解
- 将局部最优解堆叠成全局最优解

做题的时候，只要想清楚 局部最优 是什么，如果推导出全局最优，其实就够了。











## Shortest Path Problem

最短路径问题定义在带权有向图或无向图上，目标是找到从一个或多个起点到一个或多个终点的最短路径。

### 单源单汇（One-to-One, SSSP - Single Source Single Destination）



#### 单源多汇（One-to-Many, SSSP - Single Source Shortest Path）

- Dijkstra's Algorithm

最短路径问题通常采用**贪心算法**（Greedy Algorithm）来求解，特别是在 **Dijkstra 算法** 中。**贪心算法的核心思想是**：每一步都做出局部最优的选择，最终能够得到全局最优解。

在 **Dijkstra 算法** 中，我们每次从当前未访问的节点中选择**距离源点最短**的节点（局部最优），然后更新与其相邻的节点的最短路径。这个选择保证了已访问的节点的最短路径不会再改变，从而构造出全局最优解。

1. 选取当前**距离源点最近**的节点 u 作为当前最优解。
2. 以 u 为中心，更新所有相邻节点 v 的最短路径。
3. 重复步骤 1 和 2，直到所有节点的最短路径都确定。

因为如果 u 不是最优的，那就意味着有更短的路径能到达 u，但我们已经按照最短距离顺序选择了 u，所以不会存在更短的路径。





#### 多源单汇（Many-to-One）



#### 多源多汇（Many-to-Many, APSP - All-Pairs Shortest Path）











## Minimum Spanning Tree 

最小生成树

一个**包含所有顶点的无环子图**，并且所有边的权值之和最小。

> 适用于连通无向图

### 经典贪心算法

最小生成树主要有两种经典的贪心算法：

| **算法**    | **适用情况** | **数据结构**                 | **时间复杂度** | **贪心策略**       |
| ----------- | ------------ | ---------------------------- | -------------- | ------------------ |
| **Prim**    | 稠密图       | 邻接矩阵 / 邻接表 + 优先队列 | $O(E \log V)$  | 选最近的顶点       |
| **Kruskal** | 稀疏图       | 边列表 + 并查集              | $O(E \log E)$  | 选最小的边，不成环 |



### （1）Prim 算法

**核心思想：** 每次选择**距离当前生成树最近的顶点**，并加入 MST。

1. 任选一个顶点作为起点。
2. 在所有已选顶点的相邻边中，选择权值最小的边，并把新顶点加入 MST。
3. 重复步骤 2，直到所有顶点都被加入。

### （2）Kruskal 算法

**核心思想：** 每次选择最短的边，**如果不会形成环**，就把它加入 MST。

1. **排序**所有边，按权值从小到大排列。
2. **依次选取**最小的边：如果不会形成环，则加入 MST。否则跳过。
3. **重复步骤 2**，直到选取的边数为 $V - 1$（树的性质）。

bruvka's algorithm



## Traveling Salesman Problem



















# Find Maxing Timing Problem

which code snippet is faster, and why?

```javascript
// 1.
var max = array.sort.pop
    
// 2. 
var max = 0
for (i=0; i<array.length; i++){
    if (array[i]>max){
        max = array[i]
    }
}

/*
Code Snippet 1 has a higher time complexity O(n log n) due to the sorting operation. This is because the sorting algorithm used by JavaScript's `sort` method (commonly a variant of merge sort or quicksort) has a logarithmic factor.
Code Snippet 2 has a lower time complexity O(n) and is more efficient for finding the maximum value in an array.
In practice, if you only need the maximum value from an array, Code Snippet 2 is generally preferred for its simplicity and better time complexity.
*/

/*
n=100,000 and the execution time for one iteration of each code is 0.1 milliseconds:
For Code Snippet 1 Total time = 0.1ms/iteration×1,661,000 ≈ 166,100 ms ≈ 166,100ms ≈ 166.1s
For Code Snippet 2 Total time = 0.1 ms/iteration×100,000 = 10,000 ms = 10s
*/
```

- time complexity
- space complexity



# knowledge supplement

##  e+ 

在科学计数法中，数字中的 "e+" 表示指数形式，用来表示一个数字的数量级。这个表示法通常用于极大或者极小的数字，以方便表示和理解。

例如，如果你看到一个数字像是 `3.5e+6`，这意味着这个数字是 3.5 乘以 10 的 6 次方，也就是 3.5 乘以 1,000,000。这样的表示法让大的数字更加紧凑，方便书写和阅读。

同样地，如果是负指数，比如 `2.5e-3`，那么这个数字就是 2.5 乘以 10 的负 3 次方，也就是 2.5 除以 1,000。这种表示法通常用于表示小数或者接近零的数字。

总的来说，"e+" 表示 "乘以 10 的"，而 "e-" 表示 "除以 10 的"。这样的表示法让科学家和工程师更容易处理和交流极大或者极小的数值。



## % 

在计算机代码中，百分号（%）通常用于表示取余运算（modulus operation）。取余运算返回除法的余数，即两个数相除后的剩余部分。 

例如： result = 17 % 5, 结果将是 2，因为 17 除以 5 等于 3 余 2。 

取余运算在许多情况下都很有用，例如：

1. **循环：** 取余运算经常用于循环中，以便在达到一定条件时重新开始循环。
2. **判断奇偶性：** 通过 `x % 2` 可以判断一个数 `x` 是奇数还是偶数。
3. **时间计算：** 在一些时间相关的问题中，取余运算可以帮助处理周期性的情况，比如小时、分钟、秒的循环。

需要注意的是，在一些编程语言中，取余运算的行为可能与除法的方向有关，具体规则需要根据语言的规范来确定。例如，有的语言对负数取余的规则略有不同。



## //

在计算机代码中，表示取商的符号通常是斜杠（//）。斜杠用于表示除法操作，而取商即表示除法的结果中的整数部分。 

