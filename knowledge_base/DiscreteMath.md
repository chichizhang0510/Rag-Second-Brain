https://www.khoury.northeastern.edu/cs5002-discrete-data-structures-course-charter/

# Representation, Counting, and Relations 

## Learning Objectives

At the end of 5002, a student should be able to do the following:

1. **Convert** between decimal, binary, and hex.
2. **Understand** two’s complement representations of negative numbers.
3. Read and write mathematical logical formulas.
4. Use logical operators effectively.
5. Understand the set operators of union, intersection, and complement.
6. Understand relations and functions.
7. Perform basic counting tasks – e.g. counting possible passwords – using permutations and combinations as appropriate.
8. Calculate basic probabilities by counting success outcomes and total outcomes.
9. Apply proof techniques, particularly mathematical induction.
10. Model problems using trees and graphs.
11. Describe the number of operations in an algorithm as a function of  the input size, and identify superpolynomial running times as  intractable.
12. Understand the meaning of big-O notation.



## Evaluation 

1. Weekly problem sets.
2. Exams. There are typically 2 exams: midterm and final.



## Mastery 

- ***Familiarity\***: The student understands what a concept is or what it means. This level of mastery concerns a basic  awareness of a concept as opposed to expecting real facility with its  application. It provides an answer to the question “What do you know  about this?”
- ***Usage\***: The student is able to use or apply a concept in a concrete way. Using a concept may include, for example,  appropriately using a specific concept in a program, using a particular  proof technique, or performing a particular analysis. It provides an  answer to the question “What do you know how to do?”
- ***Assessment\***: The student is able to  consider a concept from multiple viewpoints and/or justify the selection of a particular approach to solve a problem. This level of mastery  implies more than using a concept; it involves the ability to select an  appropriate approach from understood alternatives. It provides an answer to the question “Why would you do that?”



## Course Topics & Learning Outcomes 

### Structural induction  结构归纳法 

>**Structural Induction**  结构归纳法   一种数学证明技术，通常用于证明递归定义的结构（如树、列表、表达式）上的性质或命题。 
>
>### 步骤：
>
>1. **基础情况**（Base Case）：
>     证明命题对最简单的结构是成立的。这个最简单的结构通常是递归定义的基础部分，例如空列表、叶子节点或其他简单的基本结构。
>2. **归纳假设**（Inductive Hypothesis）：
>     假设命题对于较小的或较简单的结构成立，例如假设命题对递归定义的某个部分已经成立。
>3. **归纳步骤**（Inductive Step）：
>     证明如果命题对较小的结构成立，那么它对由该较小结构递归构造的更复杂的结构也成立。

*State the relationship between ideas of  mathematical and/or structural induction to recursion and recursively  defined structures. [Familiarity]*  

### Binary/Hexadecimal representation of numbers 

- Numeric data representation and number bases
- Fixed- and floating-point systems 定点和浮点系统 
- Signed and twos-complement representations

> **Numeric Data Representation**  数字数据表示 ：在计算机中使用二进制、十进制、八进制、十六进制等不同的数制来表示数值数据。
>
> **Number Bases (数制)**: 指数字系统使用的基数。 例如，二进制的基数是2，十进制的基数是10，十六进制的基数是16。不同的数制在不同的应用场景中有不同的用处。 

> **Fixed-Point System (定点表示)**: 系统中，数字的小数点位置是固定的。定点数可以精确表示小数点前后一定数量的位数，通常用于**对速度要求高且精度要求不高**的场景，如嵌入式系统。  示例：固定小数点表示的 `23.45` 可能表示为 `2345`，将其隐含的小数点位置固定。 
>
> **Floating-Point System (浮点表示)**: 系统中，小数点的位置是可变的。用于表示非常大或非常小的数字。类似于科学记数法，例如 `1.23×1051.23 * 10^51.23×105`，在计算机中类似表示为 `1.23E+5`。 示例：IEEE 754标准是常用的浮点数表示标准。 

> **Signed Representation (带符号表示)**: 也叫做 Sign-Magnitude Representation ，用来表示正数和负数。最常见的方法是使用符号位，通常在最高位（最左边的比特），0代表正数，1代表负数。  示例：`+5` 可能在二进制中表示为 `00000101`，而 `-5` 则表示为 `10000101`。 
>
> **Twos-Complement Representation (二进制补码表示)**: 计算机中表示有符号整数的标准方法之一。将负数表示为正数的补码，简化加减法运算。计算方法是将数字的所有位取反（按位取反），然后加1。 示例：十进制 `-5` 在8位的二进制补码表示中是 `11111011`。 

*Explain the reasons for using alternative formats to represent numerical data. [Familiarity]* 

*Explain how fixed-length number representations affect accuracy and precision. [Familiarity]* 

*Describe how negative integers are stored in sign-magnitude  and twos-complement representations. [Familiarity]*  

*Convert numerical data from one format to another. [Usage]*  

*Representation of non-numeric data (character codes, graphical data)*

*Describe the internal representation of non-numeric data, such as characters and strings. [Familiarity]*  





### Basic Logic  

- Propositional logic 命题逻辑 
- Logical connectives 逻辑联结词 
- Truth tables 真值表 
- Predicate logic (primarily so students are familiar with concepts and notation of “for all” and “there exists”) 谓词逻辑 

>**Propositional logic**   一种最基本的逻辑系统 
>
>一个命题是一个可以明确为真或假的陈述。命题逻辑的目标是分析和操作这些命题，通过使用逻辑联结词来构造更复杂的表达式，并推导出它们的真值。 

>**Logical Connectives**    将命题组合成复合命题的符号或关键词。 
>
>常见的逻辑联结词包括：
>
>- **AND (∧)**：表示“且”，两个命题都为真时，复合命题为真。
>- **OR (∨)**：表示“或”，只要至少一个命题为真，复合命题为真。
>- **NOT (¬)**：表示“非”，将命题的真值取反。
>- **IMPLICATION (→)**：表示“如果……则……”，即如果前一个命题为真，则后一个命题也必须为真。
>- **BICONDITIONAL (↔)**：表示“双向的如果……则……”，即两个命题的真值必须相同。

> **Truth Tables**    展示复合命题在不同输入条件下的真值情况的表格。 列出所有可能的输入组合以及对应的输出真值。 

> **Predicate Logic**    比命题逻辑更强大的逻辑系统，处理包含变量的逻辑表达式，使用**量词**（quantifiers）表达复杂逻辑关系。
>
> **谓词**：描述某种性质或关系的表达式。它接受一个或多个参数。 例如，`P(x)` 可以表示 "x 是偶数"，其中 `x` 是变量。 
>
> **全称量词 ( ∀ )**："对所有……都成立"。  例如，`∀x P(x)` 表示 "对于所有x，x是偶数"。 `∀x (x > 0)` 表示 "对所有x，x大于0"。  
>
> **存在量词 ( ∃ )**："存在……使得"。  例如，`∃x P(x)` 表示 "存在一个x，使得x是偶数"。  `∃x (x > 0)` 表示 "存在一个x，使得x大于0"。 

*Convert logical statements from informal language to propositional expressions. [Usage]*

*Describe how symbolic logic can be used to model real-life situations or applications, including those arising in computing contexts such as circuit design. [Familiarity]*

*Apply **formal logic proofs 形式逻辑证明 ** and/or **informal, but rigorous, logical reasoning 非正式但严谨的逻辑推理 ** to real problems, such as predicting the behavior of software or solving problems such as puzzles. [Usage]* 



### Sets   集合论 

- Venn diagrams
- Union, intersection, complement 补集, Difference 差集  
- Cartesian product 笛卡尔积 
- Power sets 幂集 
- Cardinality of finite sets 有限集的基数 

>**Cartesian product** 笛卡尔积   两个集合的所有有序对的集合。 
>
>A×B 表示集合 A 和集合 B 的笛卡尔积。  如果 A={1,2}，B={x,y}，则 A×B={(1,x),(1,y),(2,x),(2,y)}。 
>
>用于定义关系和函数。  例如，二维平面中的点集可以看作是实数集合的笛卡尔积 R×R。 

>**Power Sets** (幂集)    某个集合的所有子集的集合。  如果集合 A 是某个集合，幂集 P(A)包含所有 A 的子集。  如果 A={1,2}，则 P(A)={∅,{1},{2},{1,2}}。 
>
>性质：如果一个集合有 nnn 个元素，则它的幂集包含 2n2^n2n 个子集。 

> **Cardinality of Finite Sets** (有限集的基数)
>
> 基数表示一个集合中元素的数量。有限集的基数是一个有限的自然数。 
>
> 基数用 ∣A∣表示，表示集合 A 中的元素个数。 如果 A={1,2,3}，则 ∣A∣=3。 
>
> 基数在集合运算中有很多应用。例如，集合的基数在定义并集、交集的元素个数时非常重要。 

*Explain with examples the basic terminology of **functions**, **relations**, and sets. [Familiarity]*

*Perform the operations associated with sets, functions, and relations. [Usage]* 

*Relate practical examples to the appropriate set, function, or  relation model, and interpret the associated operations and terminology  in context. [Assessment]* 

> **Relations** (关系)    两个集合之间元素的有序对的集合。给定两个集合 𝐴 和 𝐵，它们之间的关系 𝑅 是 𝐴×𝐵 的子集。
>
> R⊆A×B 表示关系 R 是集合 A 和 B 的笛卡尔积的子集。 
>
> 如果 A={1,2}，B={x,y}，关系 R={(1,x),(2,y)} 表示 A 中的元素 1 关联到 B 中的元素 x，而 2 关联到 y。
>
> **Relation Operations (关系运算)** 
>
> **反转 (Inverse Relation)**：反转关系 R 是将原关系中的每个有序对的顺序对调。 如果关系 R={(1,x),(2,y)}，则 R^{-1} = \{(x, 1), (y, 2)}。  
>
> **合成 (Relation Composition)**：如果关系 R⊆A×B 和 S⊆B×C，则关系的合成 S∘R 是从 A 到 C 的关系。 如果 R={(1,x)} 和 S={(x,z)}，那么 S∘R={(1,z)}。 

> **Functions** (函数)     集合之间的一种特殊关系，它将每个输入（自变量）唯一地映射到一个输出（因变量）。 
>
> 给定集合 A 和 B，函数 f 是一个从 A 到 B 的映射，记作 f:A→B。 
>
> 如果 f 是从 A 到 B 的函数，并且 f(a)=b，表示 a∈A 被映射到 b∈B。  例子：函数 f(x)=x^2 将每个数字 x 映射到其平方。比如 f(2)=4。 
>
> **Function Operations (函数运算)** 
>
> **函数求值**：给定函数 f，对某个输入求函数值。 
>
> **函数组合 (Function Composition)**：两个函数 f 和 g 的组合是将函数 g 的输出作为函数 f 的输入。 

### Relations 

- Reflexivity 自反性 , symmetry 对称性 , transitivity 传递性 
- Equivalence relations 等价关系 , partial orders 偏序关系 

>**Reflexivity**   一个关系 R 在集合 A 上是自反的，如果对于 A 中的每个元素 a，都有 (a,a)∈R。 
>
>如果关系 R 是自反的，记作 ∀a∈A, (a,a)∈R 
>
>集合 A={1,2} 和关系 R={(1,1),(2,2),(1,2),(2,1)}。关系 R 是自反的，因为 (1,1)∈R 和 (2,2)∈R。 

>**symmetry**   一个关系 R 在集合 A 上是对称的，如果对于 A 中的任意两个元素 a 和 b，当 (a,b)∈R 时，(b,a) 也在 R 中。 
>
>如果关系 R 是对称的，记作 ∀a,b∈A,(a,b)∈R  ⟹  (b,a)∈R。 

> **Transitivity** (传递性)     一个关系 R 在集合 A 上是传递的，如果对于 A 中的任意三个元素 a、b 和 c，当 (a,b)∈R 和 (b,c)∈R 时，(a,c) 也在 R 中。 
>
> 如果关系 R 是传递的，记作 ∀a,b,c∈A,(a,b)∈R and (b,c)∈R  ⟹  (a,c)∈R。 

>**Equivalence Relations** (等价关系)   一个关系 R 如果是自反的、对称的和传递的, 那么 R 在集合 A 上是等价的。等价关系 R 将集合 A 划分为若干个互不相交的子集，每个子集称为一个**等价类**。 
>
>一种特殊的关系，它满足自反性、对称性和传递性，将集合划分为等价类。 
>
>如果关系 R 是等价的，记作 R 是自反的∧R 是对称的∧R 是传递的。 
>
>考虑集合 A={1,2,3} 和关系 R={(1,1),(2,2),(3,3),(1,2),(2,1)}。这个关系是等价的，因为它自反、对称且传递。等价类是 {1,2} 和 {3}。 

> **Partial Orders (偏序关系)**    一个关系 R 在集合 A 上是偏序的，如果它是自反的、反对称的（对于任意 a 和 b，如果 (a,b)∈R 且 (b,a)∈R，则 a=b），且传递的。偏序关系用于表示集合中的元素之间的部分顺序。 
>
> 一种描述部分顺序的关系，满足自反性、反对称性和传递性，用于表示集合中的部分顺序。 
>
> 如果关系 R 是偏序的，记作 R 是自反的∧R 是反对称的∧R 是传递的。 
>
> 考虑集合 A={1,2,3} 和关系 R={(1,1),(2,2),(3,3),(1,2),(1,3),(2,3)}。这个关系是偏序的，因为它自反、反对称且传递。这个关系表示数字的“大小”关系，其中 1 小于 2，1 小于 3，2 小于 3。 

### Functions

- Surjections 满射 , injections 单射 , bijections 双射 
- Inverses 反函数 
- Composition 复合函数 

>**Surjections 满射**
>
>一个函数 f:A→B 是满射（或称为“onto”），则每个 B 中的元素都是 A 中至少一个元素的像。
>
>对于集合 B 中的每个元素 b，都存在一个 A 中的元素 a，使得 f(a)=b。 
>
>**函数的每个输出都有至少一个输入对应。** 
>
>如果函数 f 是满射，记作 f:A→B is surjective。 

>**injections 单射**  
>
>一个函数 f:A→B 是单射（或称为“one-to-one”），如果不同的 A 中的元素被映射到不同的 B 中的元素。 
>
>**每个输入有唯一的输出，不会出现不同输入映射到同一输出的情况。** 
>
>对于 A 中的任意两个不同的元素 a1 和 a2，如果 a1≠a2，则 f(a1)≠f(a2)。 
>
>如果函数 f 是单射，记作 f:A→B is injective。 

>**bijections 双射**
>
>一个函数 f:A→B 是双射（或称为“one-to-one correspondence”），如果它既是单射又是满射。 
>
>每个 A 中的元素与每个 B 中的元素一一对应。 
>
>**函数既是单射又是满射，确保每个输入和输出之间都有唯一的一一对应关系。** 
>
>如果函数 f 是双射，记作 f:A→B is bijective。 

>**Inverses 反函数**
>
>如果函数 f:A→B 是双射，则它有一个反函数 f−1:B→A。
>
>反函数 f−1 满足 f−1(f(a))=a 对于 A 中的所有 a 和 f(f−1(b))=b 对于 B 中的所有 b。 
>
>**双射函数具有反函数，使得可以在输入和输出之间互相转换。** 
>
>如果函数 f 是双射，记作 f−1 是 f 的反函数。 

> **Composition (函数的复合)** 
>
> 将一个函数的输出作为另一个函数的输入。
>
> 给定函数 f:A→B 和 g:B→C，它们的复合函数 g∘f:A→C 定义为 (g∘f)(a)=g(f(a))
>
> **函数复合是将一个函数的输出作为另一个函数的输入，生成一个新的函数。** 
>
> 复合函数用 g∘f 表示，即 g∘f 表示 g(f(a))



### Counting arguments 计数论证 

- Set cardinality and counting
- Sum and product rule
- Arithmetic and geometric progressions 数列 

>**Sum Rule (求和规则)** 
>
>如果一个问题可以被分解为几个不重叠的子问题，则解决这些子问题的总数等于各个子问题解决方案数量的总和。 

>**Product Rule (乘法规则)** 
>
>如果一个问题可以被分解为几个相互独立的步骤，则总的解决方案数等于每一步解决方案数量的乘积。 

>**Arithmetic Progression (算术数列)**
>
>算术数列是一个数列，其中每一项与前一项的差是一个常数，称为公差（d）。 
>
>**通项公式**：第 n 项的公式为 an=a1+(n−1)d，其中 a1 是首项，d 是公差。 
>
>**求和公式**：前 n 项和 
>$$
>S_n = \frac{n}{2}[2a_1 + (n-1)d]
>$$

> **Geometric Progression (几何数列)** 
>
> 几何数列是一个数列，其中每一项与前一项的比是一个常数，称为公比（r）。 
>
> **通项公式**：第 n 项的公式为 
> $$
> a_n = a_1 * r^{(n-1)}
> $$
> ，其中 a1 是首项，r 是公比。
>
> **求和公式**：
>
> 对于有限数列
> $$
> S_n = a_1\frac{1-r^n}{1-r} (当r\neq1)
> $$
> 对于无限数列:  当公比的绝对值小于 1 时，数列的和趋向于一个有限的值。 
> $$
> S_n = \frac{a_1}{1-r}(当|r| < 1)
> $$

*Apply counting arguments, including sum and product rules,  inclusion-exclusion principle 包含-排除原理  and arithmetic/geometric progressions 级数 .  [Usage]* 

*Solve a variety of basic recurrence relations. [Usage]*

*Analyze a problem to determine underlying recurrence relations. [Usage]*

>**inclusion-exclusion principle  (包含-排除原理)** 
>
> ∣A∪B∣=∣A∣+∣B∣−∣A∩B∣ 
>
> ∣A∪B∪C∣=∣A∣+∣B∣+∣C∣−∣A∩B∣−∣A∩C∣−∣B∩C∣+∣A∩B∩C∣ 
>
>用于计算集合的并集的大小时，排除那些被重复计算的元素。它适用于计算复杂的集合交集和并集问题。 

>**recurrence relations 递推关系** 
>
>基于其前面几项， 定义一个序列的项 
>
>常见的递推关系包括线性递推关系和非线性递推关系。 
>
>**线性递推关系**  
>
>斐波那契数列定义为 F(n)=F(n−1)+F(n−2)。
>
>**非线性递推关系**  给定递推关系 
>$$
>a_{n+1} = a^2_n - a_{n-1}
>$$

>**determine underlying recurrence relations**
>
>首先需要识别出序列或算法中各项之间的关系，并将这些关系转化为递推关系。 
>
>**示例问题**：计算一组任务的完成时间，已知每个任务的完成时间依赖于前两个任务的完成时间。通过观察任务的完成时间如何由前面的任务决定，我们可以得到类似于 Tn=T{n−1}+T{n−2} 的递推关系。  



###  Solving recurrence relations  解决递归关系 

-  Permutations and combinations  排列 和 组合

>

*Compute permutations and combinations of a set, and interpret the meaning in the context of the particular application. [Usage]* 

 *Map real-world applications to appropriate counting  formalisms, such as determining the number of ways to arrange people  around a table, subject to constraints on the seating arrangement, or  the number of ways to determine certain hands in cards (e.g., a full  house). [Usage]* 



###  The pigeonhole principle 

> **鸽巢原理 (The Pigeonhole Principle)** 
>
> 如果有 n 只鸽子要放入 m 个鸽巢，而 n>m，那么至少有一个鸽巢里至少有两只或更多的鸽子。 
>
> **拉姆齐理论（Ramsey Theory）问题证明** 
>
> 在一个有6个顶点的完全图中，每条边被染成两种颜色，问题是是否可能避免任意颜色形成三角形。答案是**不可能**。
>
> 设有一个包含 6 个顶点的完全图 K6，其每条边要么被染成红色，要么被染成蓝色。任意从图中选择一个顶点 A，该顶点与其他 5 个顶点之间的边可能是红色或者蓝色。**根据鸽巢原理，至少有 3 条边是同色的**（例如，假设是红色）。
>
> 现在，我们只考虑顶点 B、C、D 之间的边。 B、C、D 之间共有 3 条边（BC、CD、BD）。这些边也要被染色成红色或蓝色。
>
> **情况 1**：如果这 3 条边中至少有一条是红色，那么我们就可以找到一个全红色的三角形。例如，假设 BC 是红色的，那么三角形 △ABC 就是一个全红色的三角形（因为边 AB、AC、BC 都是红色）。
>
> **情况 2**：如果 B、C、D 之间的三条边都是蓝色，那么三角形 △BCD 就是一个全蓝色的三角形（因为边 BC、CD、BD 都是蓝色）。
>
> 因此，无论如何染色，都不可避免地会形成一个单色的三角形。  

*Apply the pigeonhole principle in the context of a formal proof. [Usage]*  





###  Discrete Probability  离散概率论 

- Finite probability space, events  有限概率空间，事件 
- Axioms of probability and probability measures 概率的公理与概率度量 
- Conditional probability, Bayes’ theorem
- Independence
- Integer random variables (Bernoulli 伯努利 , binomial 二项分布 )
- Expectation 期望 , including Linearity of Expectation

> **Finite Probability Space** 有限概率空间
>
> 在离散概率空间中，样本空间 S 是有限的，包含所有可能的结果。每个结果（样本点）被赋予一个非负数（即概率），这些概率之和为 1。 
>
> **events  事件** 
>
> 样本空间的子集称为事件。  
>
> 例如，抛硬币两次，样本空间 S={HH,HT,TH,TT}，事件“至少有一个正面”可以写成 {HH,HT,TH}

>**Axioms of Probability   柯尔莫哥洛夫的三大公理** 
>
>1. **非负性（Non-negativity）**： 对于任何事件 AAA，事件发生的概率是一个非负数
>2. **标准化（Normalization）**： 整个样本空间 SSS 的概率是 1 
>3. **可加性（Additivity）**： 如果两个事件 AAA 和 BBB 互不相容（即它们不同时发生，A∩B=∅），那么这两个事件的联合发生的概率等于它们各自发生的概率之和 

>**Probability Measures**    将样本空间的子集（即事件）映射到实数（即概率）上 
>
>概率度量 P 是一个从样本空间的事件集到实数集的函数，它满足以下条件： 
>
>1. P(A)≥0，对于任意事件 A；
>2. P(S)=1；
>3. 对于互不相容的事件集 A1,A2,…，有 P(A1∪A2∪… )=P(A1)+P(A2)+…。
>
>### **推论**
>
>- **子集的概率**：对于任意事件 A，其补集 A^c 的概率为
>
>$$
>P(A^c) = 1 - P(A)
>$$
>
>- **有限可加性（Finite Additivity）**：如果 A1,A2,…,An 是一组互不相容的事件，那么这些事件的联合发生的概率等于它们各自发生的概率之和。 
>
>$$
>P\left( \bigcup_{i=1}^n A_i \right) = \sum_{i=1}^n P(A_i)
>$$

> **Conditional Probability** 
>
> 在事件 B 已经发生的情况下，事件 A 发生的概率。 
> $$
> P(A|B) = \frac{P(A∩B)}{P(B)}\\
> 其中 P(B)>0。
> $$
>
> - P(A∣B) 是在事件 B 已经发生的条件下，事件 AAA 发生的概率。
> - P(A∩B) 是事件 A 和事件 B 同时发生的概率。
> - P(B) 是事件 B 的概率，并且 P(B)>0。

> **Bayes’ Theorem**  由条件概率导出，用来反转条件概率 
> $$
> P(A|B) = \frac{P(B|A)*P(A)}{P(B)}
> $$
> 利用新信息（证据）来更新我们对某一事件的概率估计。
>
> - A：某个假设或事件，我们希望根据新信息来更新对其发生概率的估计。 
> - B：新发生的事件，作为证据或信息，用来更新对 A 的概率估计。 
>
> - P(A∣B) 是在事件 B 已经发生的条件下，事件 A 发生的概率。
> - P(B∣A) 是在事件 A 已经发生的条件下，事件 B 发生的概率。
> - P(A) 是事件 A 的先验概率。主观估计。
> - P(B) 是事件 B 的总概率。复杂计算。
>
> 事件 B 的总概率，可以通过全概率公式计算： 
> $$
> P(B) = \sum_i P(B|A_i) * P(A_i)
> $$
>
> ## **后验概率（posterior probability）**与**先验概率（prior probability）**和**条件概率（likelihood）**之间的关系 
>
> 1. P(A∣B) 是在事件 B 发生的前提下，事件 A 发生的**后验概率**。即，**根据新证据 B 更新后事件 A 的概率**。 
> 2. P(B∣A) 是在事件 A 发生的前提下，事件 B 发生的**条件概率**，也叫**似然**（likelihood）。即**事件 A 发生后，我们得到证据 B 的可能性**。 
> 3. P(A) 是事件 A 的**先验概率**，即**在没有考虑证据 B 的情况（B没发生）下，事件 A 发生的原始概率**。
> 4. P(B) 是证据 B 的**全概率**，表示所有情况下证据 B 发生的总概率。 
>
> 虽然 P(A∣B)和P(B∣A)的结构类似，但它们代表的意义和用途在贝叶斯定理中是不同的。关键区别在于**后验概率**和**条件概率（似然）**在贝叶斯框架中的角色和含义。  
>
> 条件概率 P(B∣A)和后验概率 P(A∣B)都涉及到在已知某个事件发生的情况下，计算另一个事件的概率。但它们的具体定义和用途在贝叶斯定理中是不同的。 
>
> - **条件概率**（如 P(B∣A)）是**固定条件下**的概率。你已知某个条件 A，然后计算在这个条件下，另一个事件 B 发生的概率。这是**从已知条件到结果的推理。** 
> - **后验概率**（如 P(A∣B)）是**在新证据（B）出现后**，更新对某事件 A 的概率估计。它依赖于贝叶斯定理的计算，从结果（证据）到假设的更新。这是**从结果（证据）到假设的更新。** 
>
> ## **先验概率（prior probability）**和 **全概率（Law of  Total Probability）**
>
> - **先验概率**指在没有新数据或证据的情况下，对某一事件发生的概率的主观估计，基于先前的知识或假设，而不是依赖于新数据或证据。它反映了你对事件的初步信念或假设。  
> - **全概率**指 一种计算复杂事件总体概率的方法，通过将所有互斥事件的条件概率加权平均来获得。 
>
> ## 如何计算  P(B∣A)  似然概率？
>
> 在统计和机器学习中，**似然（Likelihood）** 是指在已知数据和模型参数的情况下，观察到**实际数据的概率**。 
>
> 1. **从数据中估计**：  如果你有相关的数据，P(B∣A)P(B \mid A)P(B∣A) 可以通过直接观察事件 BBB 在事件 AAA 发生时的频率来估计。 
> 2. **基于理论模型**：  如果有一个理论模型描述了事件 AAA 和事件 BBB 之间的关系，你可以使用模型的公式来计算 
> 3. **利用领域知识**：如果事件 AAA 和事件 BBB 的关系在你的领域中有广泛的研究和了解，你可以使用领域专家的知识或已有的文献来提供估计值。 
>
> ## 怎么计算  P(B) 全概率？
>
> 将事件 B 的条件概率加权平均，考虑所有可能的互斥情况，来计算 BBB 的边际概率。
>
> 1. **识别互斥事件**： 确定事件 B 可以由哪些互斥事件 Ai 影响。这些事件应该是互斥的（不重叠）且能够涵盖所有可能的情况。
> 2. **计算条件概率**： 对每个互斥事件 Ai，计算在该事件发生的条件下，事件 B 发生的条件概率 P(B∣Ai)。
> 3. **计算互斥事件的概率**： 计算每个互斥事件 Ai 的概率 P(Ai)。
> 4. **应用全概率定理**： 将步骤2和步骤3中的结果代入全概率定理的公式中，求和得到 P(B)。 

> **Independence (独立性)** 
>
> 当且仅当 P(A∩B)=P(A)⋅P(B) 时，事件 A 和 B 是独立的

> **伯努利随机变量（Bernoulli Random Variable）** 
>
> 一个伯努利随机变量 X 取值为 1（成功）或 0（失败），成功的概率为 p，即 P(X=1)=p，P(X=0)=1−p。 

> **二项分布（Binomial Distribution）** 
>
> 如果一个实验独立重复 n 次，每次实验的成功概率为 p，那么成功的次数 X 服从二项分布 X∼Binomial(n,p)，其概率质量函数为：
> $$
> P(X=k) = (_k^n)p^k(1-p)^{n-k}
> $$
> 其中 k=0,1,…,n。 

> **Expectation (期望)** 
>
> **期望值（Expectation）**: 随机变量 X 的期望是其可能取值的加权平均，权重是这些取值发生的概率 
> $$
> E(X) = \sum_{x} x ·  P(X=x)
> $$
> **线性期望（Linearity of Expectation）**: 即使随机变量不独立，期望的线性性仍然成立。如果 X 和 Y 是随机变量，则 E(X+Y)=E(X)+E(Y) 

*Calculate probabilities of events and expectations of random variables for elementary problems such as games of chance. [Usage]* 

*Differentiate between dependent and independent events. [Usage]* 

*Comp**ute a probability using that distribution. [Usage]* 

*Apply Bayes theorem to determine conditional probabilities in a problem. [Usage]* 





###  Basic modular arithmetic 基本模运算 

> Basic modular arithmetic 基本模运算
>
> 在有限范围内进行数学运算的方法，主要是对整数取余数。
>
> **模运算** 
>
> 核心是“取模”**，也称为**“取余数” 。被表示为：**a mod  n** ，其中 n 被称为**模数**，而计算的结果是**余数**。
>
> 在数学中，模运算通常表示为**“同余”（congruence）**，即 **a≡b mod n** ， 意思是 a 和 b 在模 n 意义下是同余的，a 和 b 除以 n 后有相同的余数。  
>
> **基本性质** 
>
> - **加法**：(a+b) mod  n=((a mod  n)+(b mod  n)) mod  n
> - **减法**：(a−b) mod  n=((a mod  n)−(b mod  n)) mod  n
> - **乘法**：(a×b) mod  n=((a mod  n)×(b mod  n)) mod  n

 *Perform computations involving modular arithmetic. [Usage]*  





###  Notion of contrapositive  逆否命题 

- Proof by contradiction 反证法 
- Disproving by counterexample 反例法反证 
- Induction over natural numbers 自然数归纳法 

>**Notion of contrapositive  逆否命题** 
>
>对给定命题进行逻辑转换，得到一个等价的命题。 
>
>**命题 P **
>
>一个陈述句，它有明确的真值，即要么是真的，要么是假的。
>
>**条件命题 P→Q** 
>
>条件命题（即“如果...那么...”）表示“如果 
>P 为真，那么 Q 也为真”。
>
>- P 是**前件**（antecedent），也叫**条件**。
>- Q 是**后件**（consequent），也叫**结论**。
>
>**逆命题 （Converse） **
>
>将条件和结论对调，将命题 P→Q 改写为 Q→P，表示“如果 Q 为真，那么 P 也为真”。 
>
>**否命题 （Inverse） **
>
>将前件和后件同时取反，即 ¬P→¬Q，意思是“如果 P 不成立，那么 Q 也不成立”。 
>
>**逆否命题 （Contrapositive） ** 
>
>同时对前件和后件取反，并对调它们的位置。 P→Q 的逆否命题是 ¬Q→¬P，表示“如果 Q 不成立，那么 P 也不成立”。 
>
>**特点** 
>
>**逆否命题与原命题是等价的**，即如果原命题 P→Q 为真，那么它的逆否命题 ¬Q→¬P 也一定为真；反之亦然。如果原命题为假，逆否命题也为假。**逆命题和否命题则不一定与原命题等价。** 
>
> **真值表验证** 
>
>| P    | Q    | P→Q  | ¬Q   | ¬P   | ¬Q→¬P |
>| ---- | ---- | ---- | ---- | ---- | ----- |
>| T    | T    | T    | F    | F    | T     |
>| T    | F    | F    | T    | F    | F     |
>| F    | T    | F    | F    | T    | F     |
>| F    | F    | T    | T    | T    | T     |

>**Proof by contradiction 反证法** 
>
>一种间接证明方法，其思路是通过**假设结论不成立**，然后**推导出矛盾**，从而**证明原命题成立**。
>
>**步骤：**
>
>1. **假设命题不成立**：首先假设你要证明的命题是假的。
>2. **推导矛盾**：从这个假设出发，使用逻辑推理，推导出一个矛盾。这个矛盾可以是与已知事实相冲突，或与命题自身的假设相矛盾。
>3. **结论**：由于假设导致了矛盾，因此假设是错误的，所以原命题必须为真。

>**Disproving by counterexample 反例法** 
>
>**找到一个反例**，即与命题相反的具体例子，来**证明命题为假**。
>
>步骤：
>
>1. **命题假设**：设一个命题 P 为真。
>2. **寻找反例**：找到一个例子 x，使得对于这个例子，P(x) 不成立。
>3. **结论**：由于存在反例，命题 P 为假。

>**Induction over natural numbers 自然数归纳法** 
>
>一种**直接证明**方法，通常用于**证明递归定义**或**在自然数范围内有效的命题**。
>
>证明命题对于初始值成立，假设其在任意自然数 n 上成立，推导出其在 n+1 上也成立。
>
>步骤：
>
>1. **基例 (Base Case)**：证明命题对于 n=0 或 n=1 成立。
>2. **归纳假设 (Induction Hypothesis)**：假设命题对于某个自然数 n=k 成立，即假设 P(k) 为真。
>3. **归纳步骤 (Inductive Step)**：基于归纳假设，证明命题对于 n=k+1 也成立，即证明 P(k+1) 为真。
>4. **结论**：根据归纳法原理，命题对于所有 n≥0 的自然数成立。
>
>**结构归纳法**（**Structural Induction**）和**自然数归纳法**（**Mathematical Induction**）非常相似，都依赖于归纳推理的思想，但应用在不同领域。联系在于，它们都是通过建立一个递归关系来证明命题在一系列对象（自然数或递归结构）上成立。
>
>- **自然数归纳法**主要用于证明与**自然数**相关的命题。
>- **结构归纳法**则用于证明关于**递归定义结构**的命题。常见的递归结构包括树、列表、表达式等。它不仅仅应用于自然数，而且应用于通过递归定义的任意结构，通常依赖于结构构造规则来进行递归推理。  

*Identify the proof technique used in a given proof. [Familiarity]*

*Outline the basic structure of each proof technique. [Usage]* 

*Apply each of the proof techniques correctly in the construction of a sound 合理的  argument 论证 . [Usage]* 



### Trees and Graphs (tie with Structural Induction) 

>**Trees（树）** 
>
>一种**递归定义**的数据结构，它由**节点**组成，节点之间通过**边**连接。特点是**没有环**，并且**每个节点只有一个父节点（根节点除外）**。 
>
>树通常由一个根节点开始，其他节点通过边与根节点相连。每个节点可以有多个子节点。 
>
>每个节点的子树本身也是一棵树。正因为这种递归结构，很多关于树的性质和算法都可以用**结构归纳法**证明。 
>
>**常见类型：**
>
>- 二叉树：每个节点最多有两个子节点，称为左子节点和右子节点。
>- 完全二叉树：每层除了最后一层的节点都填满，并且最后一层的节点尽可能地靠左排列。
>- 平衡二叉树：每个节点的左右子树的高度差最多为1。
>- 二叉搜索树 (BST)：每个节点的左子树节点值小于节点本身，右子树节点值大于节点本身。
>
>**常见操作：**
>
>- 插入：在树中添加一个新的节点。
>- 删除：从树中移除一个节点，并保持树的结构。
>- 遍历：访问树中的节点，有几种常见遍历方法，如前序遍历、中序遍历和后序遍历。

>**Graphs（图）**
>
>由一组**顶点（vertices）**和一组**边（edges）**组成的数据结构。与树不同，图**可以有环**，并且顶点之间**可以存在多条边**。
>
>图不具有递归结构，但特殊类型的图（如树形图、分层图等）可以通过递归方式进行处理。也可以使用**结构归纳法**来证明一些性质。 
>
>**常见类型：**
>
>- 无向图：边没有方向，表示两个顶点之间的双向连接。
>- 有向图：边有方向，表示从一个顶点到另一个顶点的单向连接。
>- 加权图：边具有权重，表示两个顶点之间的连接代价。
>- 连通图：图中任意两个顶点之间都至少有一条路径相连。
>- 树（图的一种特殊情况）：树可以看作是一种**连通且无环的无向图**。
>
>**常见算法：**
>
>- 广度优先搜索 (BFS) 和 深度优先搜索 (DFS)：用于遍历图中的节点。
>- 最短路径算法：如Dijkstra算法，用于找到图中两个顶点之间的最短路径。
>- **最小生成树 (MST)**：如Prim和Kruskal算法，用于**构建一个权重最小的连通图**。

*Illustrate by example the basic terminology of graph theory, as well as some of the properties and special cases of each type of  graph/tree (unrooted, rooted, binary, not binary). [Familiarity]*

*Demonstrate different traversal methods for trees and graphs, including pre-, post-, and in-order traversal of trees. [Usage]* 

*Model* *a variety of* *real-world problems in  computer science using appropriate forms of graphs and trees, such as  representing a network topology or the organization of a hierarchical  file system. [Usage]* 





### Basic Analysis 

- Differences among best and worst-case behaviors of an algorithm
- Asymptotic analysis of upper complexity bounds



*Explain what is meant by “best” and “worst” case behavior of an algorithm. [Familiarity]*

*Determine informally the time and space complexity of simple  algorithms. Good examples for this are searching and sorting algorithms. Note that these are also covered in 5001. Faculty may wish to  coordinate. Some repetition/reinforcement can work very well, if  planned.  [Usage]*  





### Big O notation 

- Complexity classes, such as constant, logarithmic, linear, quadratic, and exponential
- Time and space trade-offs in algorithms





*State the formal definition of big O. [Familiarity]* 

*List and contrast standard complexity classes. [Familiarity]* 

*Give examples that illustrate time-space trade-offs of algorithms. [Familiarity]* 







# Module 1: **Number** **Representation**

## Learning Objectives

-  **Convert** between number bases, positive and negative 
-  Recognize the benefit of **two’s complement** 



## Content

### Decimal, Binary, and Hexadecimal

- **Decimal system**/**base 10 system**: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
- **Binary system**/**base 2 system**: 0, 1
- **Hexadecimal system**/**base 16 system**: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F

> **n 位二进制数**可以表示 2^n 个不同的数。这是因为每一位二进制数（bit）有两种可能的状态：**0** 或 **1**。因此，当你有 n 位时，每一位可以独立选择 0 或 1，所有可能的组合数就是 2^n。 



#### Terminology







##### nibble

 表示 **4 位（bit）**，即半个字节（byte）。在二进制中，4 位可以表示 16 个不同的值（从 0000 到 1111），也就是十进制的 0 到 15。 

> 因为 1 个 nibble 可以表示 16 种可能值，刚好对应 1 个十六进制数（0 到 F），因此 nibble 通常用于简化十六进制数的表示。 

##### Byte







#### Decimal Expansion  十进制扩展 

将一个数以十进制小数的形式表示。它表示了数值在不同小数位上的权重，依次递减。

> 每个小数位表示相应的十进制位数，基于权重依次递减。

$$
例如：\\
0.375 = 3*10^{-1}+7*10^{-2}+5*10^{-3}
$$



> 通常适用于实数，尤其是分数、小数或无理数。 

>**有限小数**：如果一个数的十进制扩展有有限位数，例如：
>
>- 1/2= 0.521=0.5
>- 1/4= 0.2541=0.25
>
>**无限循环小数**：如果一个数的十进制扩展是无限的，但有某个循环节重复出现，例如：
>
>- 13=0.3333(可以写作 0.3‾，表示3无限循环)
>- 17=0.142857142857…(可以写作 0.142857‾，表示142857循环)
>
>**无限不循环小数**：某些数的十进制扩展是无限且不重复的，例如无理数：
>
>- π=3.1415926535……
>- sqrt{2} = 1.4142135623…



##### Floating-point representation（浮点数表示）

计算机使用浮点数来表示非整数，但因为内存有限，无法精确存储所有小数，只能存储**有限位数的近似值**。

> 例如，1/3 在十进制中是 0.3‾，但计算机会将其存储为某个近似值，如 0.333333，这与十进制扩展的原理相吻合。 



##### 舍入误差

某些数在二进制和十进制之间的转换可能导致舍入误差。

>通常出现在以下场景：
>
>- **有限位数表示**：计算机中的浮点数只能使用有限的位数表示，而某些数值（如无理数或非有限小数）不能精确表示，必须被近似为有限位数的小数。
>- **算法舍入**：在进行数值计算时，比如加法、乘法等，计算结果可能需要舍入到某个小数位，从而产生误差。
>- **进制转换**：将一个进制系统中的数转换为另一种进制时，可能会导致精度损失。例如，将某些十进制小数转换为二进制时，二进制表示可能是无限的，因此需要截断或舍入。

>舍入误差在实际应用中可能引发各种问题：
>
>累积误差：在长时间的数值运算中，多个舍入误差的累积可能导致计算结果远离实际值。例如，进行大量浮点数加法时，每一步的舍入误差会叠加，导致最终结果与精确值相差较大。
>
>不精确比较：由于舍入误差，两个本应相等的浮点数在比较时可能被认为不相等。例如，在 Python 中 0.1+0.2 的结果可能不是精确的 0.3，而是一个非常接近 0.3 的值。



#### **Convertion** between bases

##### Remember

$$
2 ^ 0 = 1\\
2 ^ 1 = 2\\
2 ^ 2 = 4\\
2 ^ 3 = 8\\
2 ^ 4 = 16\\
2 ^ 5 = 32\\
2 ^ 6 = 64\\
2 ^ 7 = 128\\
2 ^ 8 = 256\\
2 ^ 9 = 512\\
2 ^ 10 = 1024\\
$$

| Binary (nibble) | Hexadecimal |
| --------------- | ----------- |
| 0000            | 0           |
| 0001            | 1           |
| 0010            | 2           |
| 0011            | 3           |
| 0100            | 4           |
| 0101            | 5           |
| 0110            | 6           |
| 0111            | 7           |
| 1000            | 8           |
| 1001            | 9           |
| 1010            | A           |
| 1011            | B           |
| 1100            | C           |
| 1101            | D           |
| 1110            | E           |
| 1111            | F           |



##### 2 based <---> 10 based



##### 16 based <---> 10 based 



##### 16 based <---> 2 based

- 10110101 ---> (1011-> B & 0101 -> 5) ---> B5
- 8E ---> (8 -> 1000 & E -> 1110) ---> 10001110



##### x based ---> y based

use decimal as the intermediary 



#### Fixed-sized 固定大小 binary numbers

具有固定位数的二进制数

> 在计算机科学中，二进制数以 0 和 1 表示，并且存储在内存中的位数是固定的。 
>
> 使用固定大小的二进制数有助于计算机高效存储和操作数据。通常，数据类型如 `int`、`char`、`long` 等在编程语言中都是固定大小的二进制数。这些数值可以用于表示整数、浮点数，甚至字符编码等。

常见的固定大小的二进制数有：

- **8位（1字节）**：如 `00001010`，最大值是 255，最小值是 0（无符号）。
- **16位**：如 `0000000000010101`，最大值是 65535（无符号）。
- **32位**：如 `00000000000000000000000000001010`，最大值是 2^32 - 1。
- **64位**：如 `0000000000000000000000000000000000000000000000000000000000001010`，最大值是 2^64 - 1。















### Do **operations** on numbers in binary

#### Adding, Subtracting, Multiplying  and  Dividing



#### Computer adds two numbers

当计算机执行两个数的相加操作时，通常是以**二进制**的方式进行的。计算机内部的所有数字都以二进制（0 和 1）表示，通过**处理单个比特位**来实现加法运算。

##### 加法器（Adder）

计算机中用硬件电路实现加法，这个电路称为 **加法器（Adder）**。 

- **半加器（Half Adder）**：处理两个输入位的加法，并返回一个结果和一个进位。
- **全加器（Full Adder）**：处理两个输入位和一个来自低位的进位。 多个全加器可以串联起来，形成处理多位数的加法器。 

##### 不同类型的数字

- **无符号整数（Unsigned integers）**：计算机可以直接相加，无需考虑正负号。
- **有符号整数（Signed integers）**：使用 **二进制补码（Two's complement）** 表示负数，这样正负数的加法也可以按相同的方式进行，只需处理溢出问题。
- **浮点数（Floating-point numbers）**：浮点数加法更复杂，需要对齐小数点，调整指数，再进行二进制加法。



### Store **negative numbers**: **Two’s Complement** 二进制补码 

#### 两种表示负数的方法

- 符号位表示法（Sign-Magnitude Representation）最前面的位（最高位，第 8 位）是符号位，而剩下的 7 位表示数值大小
- 二进制补码表示法（Two’s Complement Representation）最高位仍然表示符号， 但数值部分是通过二进制补码表示的，即通过模 2^8 来表示。 

> 计算机或编程语言的文档通常会说明其使用的数值表示方法。大多数现代计算机系统和编程语言（如 C、C++、Java、Python）使用的是**二进制补码表示法**，因为它在硬件实现上更高效。 



#### Sign-Magnitude Representation‘ inadequacies 

在符号位表示法（Sign-Magnitude）中，一个数有两种表示：正零和负零（比如 +0 和 -0） 可能会导致歧义和额外的逻辑处理，因为在数值比较或判断时，它们的数学意义相同，但在计算机中是两个不同的表示。 

如果使用符号位表示法，当不同符号的数相加或相减时，必须仔细处理符号位，并且需要专门的逻辑去处理溢出和进位的情况。

直接使用符号位的话，需要分别处理符号位和数值部分，增加了硬件复杂性和成本 。



#### **Two’s Complement**

在计算机中，**负数的表示和处理**通常通过一种称为 二进制补码（Two's Complement） 的方法来实现。

> 通过检查**最高位（ MSB，Most Significant Bit 符号位）**是否为 1 可以直接判断一个数是负数。 

> 使正数和负数的加减运算使用同一套电路来处理。 使用二进制补码后，计算机只需要实现加法电路，不需要额外的减法电路，不需要专门的符号处理单元。 。  
>
> 假设我们在 8 位的系统中，计算 5+(−5)：
>
> - 5 的二进制表示是：`00000101`。
> - -5 的二进制补码 通过对 5 的补码取反后再加 1 来得到 ：`11111011`。
>
> ```
>   00000101  (5)
> + 11111011  (-5)
> -----------
>   00000000  (0)
> ```

二进制补码是一种**将负数表示为二进制**的方法。  负数的表示是**通过对正数的补码**来实现的。  

> 在固定位数的二进制系统中，通常使**用最左边的一位（称为符号位）来表示正负号**
>
> - 如果符号位是 **0**，表示正数。
> - 如果符号位是 **1**，表示负数。

##### 生成方法

- 将正数的二进制表示取反（即将 0 变为 1，将 1 变为 0）。
- 加 1。

>正数 5 的二进制表示是：`00000101`（8 位，最高位是符号位）。符号位是 0，表示这是一个正数。
>
>1. 首先将 5 的二进制表示取反：`00000101` → `11111010`。
>2. 然后加 1：`11111010 + 1 = 11111011`。
>
>因此，-5 的二进制补码表示为：`11111011`。



##### 本质

> 为什么负数这样表示会使负数正数相加刚好是0？

正负数相加实际上是在两者之间寻找一个中间数，它们的符号位能够正确地更新。
$$
二进制补码实际上是一种模运算，具体来说是模2^n的运算。\\
对于n位系统，所有的操作都是在2^n的模空间内进行的。\\
正数自然位于 0 到 2^{n-1}−1 范围内。\\
负数被映射到到2^n 到 2^n−1 的高位区域。
$$

> 通过这种模运算的设计，负数的表示与正数相加时能够正确“绕回”到结果范围内。 
>
> 模运算（modulus operation）是一种环状运算，它确保任何操作结果都在一个固定范围内循环。 
>
> 补码中，负数通过模 2^n 的方式变成大数。如果我们把负数想象成模空间内的正数（因为补码的负数实际上就是高位正数），那么当它与另一个数相加时，结果有可能会超出最大表示范围。但**计算机会自动忽略超出的位数**，只保留低 n 位数值。因为数值是按模 2^n 处理的，当发生进位时，系统丢弃超出 n 位的部分，自动把数值“绕回”到合法范围。

>例子：计算 5+(−3) （4 位系统） 
>
>5 的二进制表示是 `0101`。
>
>−3 的补码表示：我们用 **2^4−3**=16−3=13，即 `1101`。这是负数在补码中的表示。
>
>```
># 5+(−3)
>0101  (5)
>+ 1101  (-3)
>------------
>  10010   ---> 结果是 10010，这是 5 加上 -3 的二进制结果。
>```
>
> 因为我们使用的是 4 位系统，结果 `10010` 是 5 位的，需要丢弃最高位的 `1`。剩下的 4 位是 `0010`，即十进制的 2。 



##### 表示的整数范围

在 n 位的系统中，二进制补码能表示的整数范围为：

- **正数范围**：0 到 2^{n-1} - 1。
- **负数范围**：-2^{n-1} 到 −1。

> 最高位会不会有时表示符号，有时表示数字?
>
> 在 8 位二进制补码系统中，能够表示的数值范围是从 `-128` 到 `127`。
>
> - **正数范围**：`0` 到 `127`。
> - **负数范围**：`-128` 到 `-1`。
>
> **`11111110`** 的二进制表示是 8 位的。**最高位是 `1`**，这表明这是一个负数。
>
> **计算负数 `11111110` 的实际值**：1.**取反**（每个位取反） `00000001`。2.**加 1**对取反后的结果 `00000001` 加 `1`，得到 `00000010`。
>
> 因此，`11111110` 在 8 位补码系统中表示的是 `-2`。 



##### **计算**

###### 正数 ---> 负数

1. 符号位+其他位取反； + 1

###### 负数 ---> 正数

1. 取反 + 1 ;
2. 根据2^n算出数值（此时符号位不是符号位，是数值）

> 1000 0000 : 
>
> **符号位**（最高位）是 `1`，这表示这是一个负数。**剩余的 7 位**表示数值部分。
>
>  `1000 0000` 的取反是 `0111 1111`。  `0111 1111` + `1` = `1000 0000`。 回到了原始值。  
>
> 根据2^n算出128，那对应过去在补码系统中，`1000 0000` 表示的是最小的负数，即 `-128`。 

> 127 的二进制表示是 `0111 1111`。  最高位 `0` 表示这是一个正数。  剩余的 7 位表示数值 `127`。 



##### 溢出（overflow）

当加法或减法结果超出二进制系统能表示的范围

> 例如，当你使用 8 位（1 字节）来表示数时，最大正数是 127，最小负数是 -128。如果一个计算的结果超出了这些范围，溢出就会发生。 

> 溢出在二进制补码中很常见，需要程序检测并处理。 

###### 类型

- **正溢出**（Positive Overflow）：当加法结果超过了最大可表示的正数范围。
- **负溢出**（Negative Overflow）：当减法结果小于最小可表示的负数范围。

> 一正一负的运算不会导致**溢出**，这是因为溢出只会发生在**两个相同符号的数相加或相减**的情况下。  因为正负数的加法实际上是在“抵消”彼此，不会超出数值的表示范围。 

###### 检测规则

在二进制补码中，溢出通过**符号位**来检测。

> 因为补码使用最左边的一位（符号位）来表示正负号，当两个数相加或相减时，符号位的变化可以帮助我们判断是否发生了溢出。

- **正溢出**：当两个正数相加，结果应该是正数，但如果结果的符号位变成了 1（即负数），则发生了正溢出。
- **负溢出**：当两个负数相加，结果应该是负数，但如果结果的符号位变成了 0（即正数），则发生了负溢出。

> 当两个数相加时，如果产生进位，进位将被丢弃（因为进位会超出位数范围）。在补码系统中，这种进位处理不会影响最终结果，因为它相当于在环状数轴上回到正确的位置。 

###### 例子

在一个 4 位二进制系统中工作，范围是 -8 到 7。我们来计算 7+2。

- 7 的补码表示是：`0111`。
- 2 的补码表示是：`0010`。

```
  0111  (7)
+ 0010  (2)
---------
  1001  (-7)  -> 这个数在补码中表示 -7，而不是 9。 溢出！
  # 因为两个正数相加得到的结果是负数（符号位为 1），因此发生了溢出。
```

计算 −6+(−3)。

- -6 的补码表示是：`1010`。
- -3 的补码表示是：`1101`。

```
  1010  (-6)
+ 1101  (-3)
---------
  0111  (7)  -> 两个负数相加却得到了正数，溢出！
```



### Modular Arithmetic 模运算 

处理整数的运算方式，特别是在循环或周期性问题中非常有用。
$$
对于整数 a 和 b，以及正整数 m，我们说:\\
如果 (a - b) 可以被 m 整除,\text{ } a 和 b 在模 m 意义下是同余的\\
记作 a ≡ b \text{ }(\text{ }mod\text{ } m)
$$

> 基本思想是将数值限制在一个固定范围内，通常是从 0 到 m-1（其中 m 是**模数**）。



#### 同余关系

$$
a ≡ b (\text{ }mod\text{ } m) \\
当且仅当 a 和 b 的差 a - b 能被 m 整除。
$$



#### 运算规则

##### 模算术

`a mod b`  计算整数 `a` 除以整数 `b` 后的余数 
$$
a\text{ } mod \text{ }b = r\\其中 r 是余数，满足 0 ≤ r < b。\\
\text{ }\\
\text{a is dividend 被除数（或被模数）}\\
\text{b is modulus 模数 \ 除数（Divisor）}\\
\text{r is remainder 余数}\\
\text{商（quotient）被除数除以模数后的整数部分s}
$$

###### modulus

 模数 b 是模数运算中的除数。它设置了运算结果范围的上限。 指定余数的范围 [0, b-1] 



##### 加减乘除

$$
加法：
(a + b) \text{ } mod\text{ } m = [(a\text{ } mod\text{ } m) + (b\text{ } mod\text{ } m)] \text{ }mod\text{ } m\\
减法：
(a - b)\text{ } mod\text{ } m = [(a \text{ }mod\text{ } m) - (b \text{ }mod \text{ }m)] \text{ }mod\text{ } m\\
乘法：
(a * b)\text{ } mod\text{ } m = [(a \text{ }mod\text{ }m) * (b \text{ }mod \text{ }m)] \text{ }mod \text{ }m\\
\text{ }\\
除法（需要逆元）：
a / b ≡ a * b^{-1} (\text{ }mod\text{ } m)\\
其中 b^{-1} 是 b 的模 m 逆元，即满足 b * b^{-1} ≡ 1 (mod\text{ } m) 的值。
$$

>**循环**：
>
>- 模运算常用于计算周期性问题，例如日历计算、钟表时间等。比如，星期几的计算通常用模运算来处理，因为一周有 7 天。
>
>**密码学**：
>
>- 模运算在加密算法中非常重要，例如 RSA 加密算法，它使用模运算来处理大整数的加密和解密。
>
>**哈希函数**：
>
>- 哈希函数常常使用模运算来确保哈希值在固定范围内。

##### 模运算除法

 在模算术中，**除法**实际上是通过乘以**模逆元**来实现的。 

> 具体来说，对于两个整数 `a` 和 `b`，在模 `m` 的情况下，如果我们希望计算 `a / b`，我们实际上是计算 `a` 乘以 `b` 的模 `m` 逆元。 

###### 模逆元

$$
b⋅b^{−1}≡1(mod\text{ }m)
$$

> 使得一个数与其**逆元**的乘积在模 `m` 下等于 `1`  
>
> 模逆元存在的条件是 `b` 和 `m` 必须**互质**（即它们的最大公约数为 `1`）。如果 `gcd(b, m) ≠ 1`，则 `b` 的逆元不存在。

###### 例子

计算：`15 / 4` 在模 `7` 下的结果。 

1. 计算 `4` 的模 `7` 逆元：需要找到一个 `x`，使得 `4 * x ≡ 1 (mod 7)`。 使用扩展欧几里得算法或试错法可以找到 `4` 的模 `7` 逆元是 `2`。因为： 4⋅2=8 ； 8 mod  7=1。
2. 计算除法： 将 `15 / 4` 转换为 `15 * 4^{-1}`= `15⋅2(mod7)`= `30 mod 7`= `2 `

3. 所以，`15 / 4` 在模 `7` 下的结果是 `2`。 



# Module 2 **Statement Representation**

how two different statements may be logically equivalent.

"opposite statement".

- **Represent** English statements using formal mathematics
- **Evaluate** the truth of **compound** Boolean formulae
- **Negate** English statements and Boolean formulae
- **Prove** the **equivalence** of two Boolean formulae





## Terminology



### Boolean algebra

**Boolean algebra** is a branch of algebra that deals with logical operations and binary variables (typically represented as 1 for true and 0 for false). 

It was introduced by George Boole and is fundamental in computer science and digital logic design.

> 布尔代数是用来表示和操作逻辑表达式的一种数学结构, 通过这些运算来构造和简化逻辑表达式。
>
> **关键要素：**
>
> 1. 一个 **集合 A**，是一组符号或**逻辑变量**。
>
> 2. 两个 **二元运算**（运算涉及两个元素）\ 一个 **一元运算**（运算涉及单个元素）：
>
> - ∧ (**与**，AND) —— 两个元素的交集。
> - ∨ (**或**，OR) —— 两个元素的并集。
> - ¬ (**非**，NOT) —— 一个元素的否定或补集。
>
> 为了使集合 A 形成布尔代数，它必须满足一些定律（例如交换律、结合律、分配律等）。这个集合的元素可以表示逻辑值（真/假）或更抽象的符号。这些定律帮助我们简化逻辑表达式。常见定律包括：
>
> - **交换律**：A∧B=B∧A，A∨B=B∨A
> - **结合律**：(A∧B)∧C=A∧(B∧C)
> - **分配律**：A∧(B∨C)=(A∧B)∨(A∧C)
>
> **按照布尔代数的语法规则** (使用与（AND）、或（OR）和非（NOT）运算符组合这些元素) 构成的任何逻辑表达式都称为 **良构公式 (WWF, Well-Formed Formula)**。这些公式根据布尔代数的规则是有效的。
>
> **给定 A 的所有可能的良构公式的集合**形成了**布尔代数**。

>
>
>



#### Symbolic logic

**Symbolic logic** is the study of logic using symbols and formal methods to represent logical statements and arguments. It focuses on using variables and logical operators (like AND, OR, NOT, IF-THEN) to express propositions命题, enabling precise reasoning about truth, validity有效性, and logical relationships.



#### statements

a **declarative** sentence that is either true or false, but not both. 

> Simple Statements: basic statements that do not contain any logical connectives.

>Each statement has a truth value
>
>- **True (T)**: The statement is correct.
>- **False (F)**: The statement is incorrect.



#### predicate

a sentence with a number of **variables** which becomes a statement when the variables are replaced with specific values.

> Key features
>
> - **Variables**: A predicate contains one or more variables. For example, P(x) could represent "x is greater than 5."
> - **Domain of Discourse**: This is the set of values that the variables can take. 
> - **Truth Value**: A predicate can be evaluated as true or false depending on the specific values assigned to its variables.

>Types
>
>- **Unary Predicate**: A predicate with a single variable, e.g., P(x).
>- **Binary Predicate**: A predicate with two variables, e.g., Q(x,y) which could represent "x is less than y."

>Quantifiers
>
>Predicates often use quantifiers to express statements about multiple elements in the domain:
>
>1. **Universal Quantifier** (∀): Indicates that a predicate is true for all elements in the domain.
>   - Example: ∀x(P(x)) means "For all x, P(x) is true."
>2. **Existential Quantifier** (∃): Indicates that there exists at least one element in the domain for which the predicate is true.
>   - Example: ∃x(P(x)) means "There exists an x such that P(x) is true."



#### Compound Statements

**compound statements** are formed by combining two or more simple statements using **logical connectives**

> - **Conjunction** (AND, ∧)
> - **Disjunction** (OR, ∨)
> - **Negation** (NOT, ¬)
> - **Implication** (IF...THEN, →)
> - **Biconditional** (IF AND ONLY IF, ↔)



#### **Tautology重言式**

无论各个变量的真值是什么都**始终为真**的语句或布尔表达式。
$$
P∨¬P = 1
$$



#### well-formed formula (wff)

an expression that is constructed using specific rules

- **Basic Propositions**: Any propositional variable (like A or B) is a wff.
- **Negation**: If ϕ is a wff, then ¬ϕ (NOT ϕ) is also a wff.
- **Conjunction/Disjunction**: If ϕ and ψ are wffs, then ϕ∧ψ (AND) and ϕ∨ψ (OR) are wffs.
- **Parentheses**: If ϕ is a wff, then (ϕ) is also a wff.

>a syntactically句法上 valid expression in logic, constructed according to strict rules. It ensures that every logical statement is **meaningful** and **unambiguous**.
>
>1. **Clarity**: Wffs guarantee that logical expressions follow the correct structure, avoiding confusion.
>2. **Consistency**: They provide a standard format for interpreting logical operations.
>3. **Foundation for Proofs**: Wffs are the basis for constructing logical arguments, proofs, and mathematical reasoning.
>
>Without wffs, logical expressions would be chaotic and difficult to interpret systematically.

>a well-formed formula (wff) refers to the **rules** that govern the valid **combinations of logical statements** using logical operators. These rules define how statements (propositions, predicates, etc.) can be combined to form complex logical expressions.
>
>For example, in propositional logic:
>
>- A∧B is a valid combination (wff), as it follows the rules.
>- ∧AB is **not** a valid wff, as it doesn't follow the syntax rules.



#### **Normal Form**

将逻辑公式写成某种规范化的形式，以便更容易地进行分析、计算或证明。

>### 用途：
>
>- **自动化推理**：在自动定理证明、SAT求解等计算机逻辑处理任务中，公式常被转换为标准形式进行计算。
>- **复杂性分析**：很多逻辑问题（如 SAT 问题）在转换为 CNF 或 DNF 后，可以更容易进行复杂性分析，例如展示问题是 NP 完全的。
>- **简化逻辑电路**：在数字电路设计中，将布尔表达式转换为标准形式有助于优化和简化电路。

##### Conjunctive Normal Form, CNF

**主合取范式** 

一个逻辑公式写成**一组子句的合取 (AND)**。每个子句是**文字（原子命题或其否定）的析取 (OR)**。

a Boolean formula that is expressed as a conjunction (AND, `∧`) of multiple clauses, where each clause is a disjunction (OR, `∨`) of literals文字 (a variable or its negation).

> an “AND of ORs” structure: 多个以“或”连接的子句，用“与”连接在一起。

$$
(A∨¬B)∧(B∨C)∧(¬A∨C)
$$

##### Disjunctive Normal Form, DNF

**主析取范式**

一个逻辑公式写成**一组项的析取 (OR)**。每个项是**文字的合取 (AND)**。

Boolean formula is expressed as a disjunction (OR, `∨`) of multiple terms, where each term is a conjunction (AND, `∧`) of literals.

> an “OR of ANDs” structure: 多个以“与”连接的项，用“或”连接在一起。

$$
(A∧¬B)∨(B∧C)∨(¬A∧C)
$$

##### Simplify

**单位子句法（Unit Clause Method）**：当一个子句中只有一个未确定的字面量时，强制赋值使其为真。

**纯文字法（Pure Literal Method）**：如果某个字面量在所有子句中只以正或负形式出现，则可以赋值使其所有相关子句为真。

**分支限界法（Backtracking）**：系统地探索所有可能的赋值组合，剪枝不可能满足的路径。







#### NP-Hard 非确定性多项式困难

表示问题的难度级别非常高。

> 计算机科学中的问题可以分为很多类，其中最重要的两类是 **P** 和 **NP**

##### Polynomial Time (P 类问题)

可以在**多项式时间**内（即相对较快地）被解决的问题。也就是说，对于一个输入，存在一个算法可以在多项式时间内得出结果。

> 排序问题和求最短路径的问题都属于 **P 类**。

##### Nondeterministic Polynomial Time (NP 类问题)

虽然可能无法快速找到答案，但如果有人给了你一个答案，你可以**快速验证**答案是否正确。

> 数独问题就是一个 **NP 类**问题：找到解可能很难，但验证给定的解是否正确很容易。

###### NP-Complete

**NP** 类问题中最难的那些。具有 **NP-Hard** 的难度。

> 这个问题的难度和 **NP-Hard** 问题一样难，意味着**所有 NP 类问题都可以归约为这个问题**。换句话说，解决这个问题就相当于解决了所有 NP 类问题。

##### NP-Hard 问题

**非常难**的问题，它们至少和 **NP** 问题一样难，甚至可能更难。

不一定能在多项式时间内验证答案，也就是说，即使有人给了你一个答案，你也可能无法快速验证它是否正确。

> 解决 **NP-Hard** 问题非常困难，目前没有已知的高效算法可以快速解决这些问题。

##### “P=NP”问题的关键

如果我们能找到一个**高效的**方法来解决一个 **NP-Hard** 问题，那么所有 **NP** 问题也都可以被高效解决。这就是为什么 **NP-Hard** 问题那么重要。







### Digital Circuits

electronic circuits that operate on discrete signals, typically representing binary values (0 and 1). 

> Unlike **analog circuits**, which can handle a continuous range of values, digital circuits work with distinct levels, making them less susceptible to noise and interference.



#### Wire

a conductor导体 that provides a path for electric current to flow

> made of conductive materials like copper or aluminum, which have low resistance, allowing electricity to flow easily through them.

- **Conductivity导电性**: Wires are highly conductive, meaning they have **very low resistance**, allowing electricity to flow with minimal loss of energy.
- **Insulation绝缘**: Most wires are covered with an insulating material (like plastic or rubber) to prevent unintended contact with other conductive materials and protect against short circuits.
- **Gauge规格**: Wires come in different **thicknesses** (gauges), with thicker wires being able to carry more current.

>Applications:
>
>- Power Transmission: Wires carry electrical energy from power sources (like batteries or power supplies) to components in a circuit.
>- Signal Transmission: Wires are used to transmit electrical signals between parts of a circuit, such as from sensors to controllers.



#### Resistor电阻器

a **passive** electrical component that **resists** the flow of electric current

It is used to **limit or control the amount of current** in a circuit, provide a specific voltage drop, or dissipate energy in the form of heat. 

> fundamental component in almost all electronic circuits.

- **Resistance电阻 (R)**: Measured in **ohms (Ω)**, resistance defines how much the resistor opposes the current. A higher resistance value means less current flows through the circuit.
- **Ohm’s Law**: The relationship between voltage电压 (V), current (I), and resistance电阻 (R) is given by the formula: V=I×R. This means the voltage drop across a resistor is proportional to the current flowing through it and its resistance.

>**Types of Resistors**:
>
>- **Fixed Resistors**: Have a constant resistance value.
>- **Variable Resistors** (like potentiometers): Allow the resistance to be adjusted.
>
>**Applications**:
>
>- Current Limiting: preventing damage to sensitive components.
>- Voltage Division: In voltage divider circuits, resistors are used to create specific output voltages.
>- Heat Dissipation散热: convert electrical energy into heat, a useful property in power control circuits.





#### Switches

an electrical component that can control the flow of current in a circuit by opening or closing the circuit path.

>Relay继电器: An electrically operated switch that uses a small current to control a larger current in another circuit.
>
>Transistor as a Switch: A transistor can function as a switch in digital circuits, turning on or off based on the voltage applied to its gate or base.



#### Transistors

a semiconductor device that acts as a switch or amplifier in electronic circuits

> one of the most fundamental building blocks of modern electronic devices. A transistor is made of semiconductor materials (typically silicon)

A **transistor** can indeed be thought of as a **digital switch**, functioning similarly to a mechanical机械 light switch, but it operates electronically and at much higher speeds.

A “high” voltage (typically +5V) given as input to a transistor causes it to “close” and supply a “high” voltage to its output; similarly, a “low” voltage (typically 0V) given as input to a transistor causes it to remain “open” and supply no voltage (i.e., 0V) to its output.

> Why call it digital switches?
>
> In a household electrical circuit:
> - When you flip a **light switch** to the "on" position, it completes the circuit, allowing current to flow to the light bulb, turning it on.
> - When you flip the switch to the "off" position, it breaks the circuit, stopping the current flow, turning the light off.
>
> A **transistor** behaves in a similar way, but it **controls the flow of electrical current using a small voltage or current at one of its terminals.** It can either allow current to flow through it or block it, depending on the signal it receives.
>
> In Digital Circuits:
> - **On state (closed switch)**: When the transistor receives a small input signal (like a voltage applied to its **base** or **gate** terminal), it allows a larger current to flow between its **collector** and **emitter** terminals (in a **BJT**) or between **drain** and **source** terminals (in a **FET**). This is like turning the switch "on" and closing the circuit.
>   
>   In this state, the transistor acts as a **closed switch**, enabling the current to pass and representing a **binary 1** (high state).
>
> - **Off state (open switch)**: When no signal is applied to the base/gate terminal, the transistor stops the current from flowing. This is like turning the switch "off" and breaking the circuit.
>
>   In this state, the transistor acts as an **open switch**, blocking the current flow and representing a **binary 0** (low state).
>
> Because transistors switch very quickly between these two states, they are the key elements used to build **logic gates** (AND, OR, NOT, etc.), and ultimately, more complex circuits like processors and memory devices. This switching ability allows transistors to control digital signals, process information, and perform computations.

>control the flow of electrical current, enable complex operations like signal amplification, digital switching, and processing
>
>1. **Switching**: Transistors can turn current on or off, acting like a digital switch in circuits, which is essential for logic gates in digital electronics (e.g., in CPUs).
>2. **Amplification**: They can increase the strength of weak signals, which is important in analog circuits (e.g., in audio amplifiers).

>- Emitter (E)发射极: The source of the charge carriers (electrons or holes).
>- Base (B)基极: The control terminal that regulates the flow of charge carriers between the emitter and collector.
>- Collector (C)集电极: The terminal where charge carriers flow out.



#### **Logic Gates**

**Switches** can be **wired** together to **form** basic logic gates which are used to construct circuits which can manipulate numbers.

##### Basic Logic gates

> basic building blocks of digital circuits. 

The most common types of logical gates include:

1. **AND Gate**: Outputs true (1) only if all inputs are true (1).
2. **OR Gate**: Outputs true (1) if at least one input is true (1).
3. **NOT Gate**: Outputs the inverse of the input (0 becomes 1, and 1 becomes 0).

<img src="./pictures/1727034993_screenshot.png" alt="1727034993_screenshot" style="zoom:30%;" />

<img src="./pictures/1727035130_screenshot.png" alt="1727035130_screenshot" style="zoom:30%;" />

<img src="./pictures/NOT Gate.png" alt="NOT Gate" style="zoom:30%;" />

> Though we can construct circuit from all boolean formulae with just two-input AND, OR and NOT gates, our circuit drawing can be made much simpler if we allow **three-input AND and OR gates**. You can use these in your work for this course unless instructions say otherwise.



##### Derived Gates

specific types of combinational logic gates that are formed by combining basic gates.

###### XOR Gate (Exclusive OR)

Outputs true if an odd number of inputs are true (for two inputs, true if exactly one is true).

The XOR gate can <u>be constructed using a combination of AND, OR, and NOT gates.</u> The logic for XOR (for two inputs A and B) is:

- A XOR B = (A  AND  NOT  B)  OR  ( NOT  A  AND  B)

> This means that XOR outputs true (1) when either A or B is true, but not both.

<img src="./pictures/XOR.png" alt="XOR" style="zoom:50%;" />



###### XNOR Gate (Exclusive NOR) 同或

Outputs true if an even number of inputs are true (for two inputs, true if both are the same).

> derived from the **basic logic gates**: **AND**, **OR**, and **NOT**.

The XNOR gate is simply the complement (negation) of the XOR gate. It can be constructed by applying a NOT gate to the output of the XOR gate. The logic for XNOR (for two inputs A and B) is:

- A XNOR B=NOT(A  XOR  B)

Alternatively, breaking this down further:

- A XNOR B=(A  AND  B)  OR  ( NOT  A  AND  NOT  B)

This means that XNOR outputs true (1) when both inputs are either true or both are false (i.e., they are the same).

<img src="./pictures/XNOR.png" alt="XNOR" style="zoom: 67%;" />



##### Universal通用 Gates (Derived Gates)

gates that can be used to implement any logical function without needing to use any other gate type.

> NAND and NOR gates are **derived from** AND and OR gates combined with NOT operations. 

> Why they are called universal gates?
>
> they have **a special property**: either of them can be used to implement any other logic gate or any combinational logic circuit. This means that **using only NAND or NOR gates**, you can build circuits equivalent to AND, OR, NOT, XOR, XNOR, and even more complex circuits.

> they simplify circuit design and reduce the number of different gate types needed in a circuit.



###### NAND Gate

Outputs false (0) only when all inputs are true (1). It can be used to create any other gate, including AND, OR, and NOT.

> NAND = Negation of AND

A NAND gate can <u>be constructed from an AND gate</u> whose o<u>utput is attached to a NOT gate</u>.

<img src="./pictures/NAND Gate.png" alt="NAND Gate" style="zoom:50%;" />

1. The **NAND gate** is one of the simplest logic gates to construct using basic electronic components like **transistors**, **resistors**, and **wires**.

>In fact, a basic NAND gate can be constructed with **two transistors** (in a CMOS design, one NMOS and one PMOS transistor).
>
>Fewer components mean the NAND gate is more **cost-effective** and **efficient** to fabricate in large numbers, especially in **integrated circuits** (ICs), where space is at a premium.

2. The **NAND gate** is also considered **logically complete**, meaning that **any other logic gate** (AND, OR, NOT, NOR, XOR, XNOR, etc.) can be created using just NAND gates. 

> it implies that you can design **any digital circuit or truth table** entirely with NAND gates.
>
> - **NOT Gate**: A single NAND gate with both of its inputs tied together acts as a **NOT gate**, producing the complement of the input.
>
> $$
> A \text{ NAND } A = \overline{A} \\
> A \uparrow A  = \overline{A}
> $$
>
> - **AND Gate**: By using two NAND gates, you can construct an **AND gate**. The output of the first NAND gate is inverted using a second NAND gate (acting as a NOT gate).
>
> $$
> (A \text{ NAND } B)\text{ NAND } (A \text{ AND } B) = A \text{ NAND } B
> $$
>
> - **OR Gate**: By combining three NAND gates, you can also create an **OR gate**.
>
> $$
> (\text{NOT A})  \text{ NAND } (\text{NOT B}) = A \text{ OR } B\\
> \text{(A NAND A)} \text{ NAND } \text{(B NAND B)} = \text{A OR B}
> $$
>
> > where **NOT A** and **NOT B** are generated using single-input NAND gates.
>
> This ability to create any other gate from just NAND gates gives designers incredible flexibility and efficiency, especially in integrated circuits. Instead of using different types of gates, you can design a circuit using only NAND gates, simplifying manufacturing and design processes.



###### NOR Gate

Outputs true (1) only when all inputs are false (0). Like the NAND gate, it can also be used to construct any other gate.

A NOR gate can <u>be constructed from an OR gate</u> whose <u>output is attached to a NOT gate.</u>

> - NOR = Negation of OR

<img src="./pictures/NOR Gate.png" alt="NOR Gate" style="zoom:50%;" />

Since you can derive NOT, AND, and OR gates from NOR gates, it follows that you can construct any logical expression or truth table using just NOR gates. This makes the NOR gate **logically complete**, meaning you can design any digital circuit or system solely with NOR gates.

>**NOT Gate**: To create a NOT gate (inverter), you can connect both inputs of a NOR gate to the same input
>$$
>A \text{ NOR } A = \overline{A} \\
>A \downarrow A  = \overline{A}
>$$
>**OR Gate**: apply De Morgan’s Theorem. 
>$$
>A \text{ OR } B= \overline{\overline{A} \text{ NOR } \overline{B}}\\
>= ((A \text{ NOR } A )  \text{ NOR } (B \text{ NOR } B)) \text{ NOR } ((A \text{ NOR } A )  \text{ NOR } (B \text{ NOR } B))
>$$
>**AND Gate**: use De Morgan’s Theorem again
>$$
>A \text{ AND } B= \overline{A \text{ NOR } B}\\
>= (A \text{ NOR } B) \text{ NOR } (A \text{ NOR } B)
>$$



###### HOW TO CHOOSE

在构建数字电路时，选择 **NAND** 门还是 **NOR** 门通常取决于实际考虑因素，包括性能、效率和易于实施性。

1. **性能**：

- **传播延迟**：与 NOR 门相比，NAND 门通常具有较低的传播延迟。这意味着它们可以更快地切换状态，这在 CPU 和内存等高速电路中至关重要。
- **速度**：在许多技术中，尤其是 CMOS（互补金属氧化物半导体），NAND 门可以实现比 NOR 门更高的切换速度。

2. **功耗**：

- **更低功耗**：与 NOR 门相比，NAND 门在不切换时往往消耗更少的电量。这使得它们更适合能源效率至关重要的电池供电设备。

3. **电路复杂性**:

- **所需门更少**: 许多标准设计和架构都针对 NAND 门进行了优化。例如，使用 NAND 门实现触发器和锁存器更简单，从而降低了整体电路复杂性。
- **更简单的布局**: 使用 NAND 门设计电路通常会导致集成电路上的布局更紧凑，从而有助于降低制造成本。

4. **易于实现**:

- **逻辑系列中很常见**: NAND 门通常存在于各种数字逻辑系列中，使其成为电路设计的标准选择。
- **配置灵活**: NAND 门可以轻松配置以创建各种复杂功能，使其适用于不同的应用。

5. **历史偏好**:

- **既定标准**: 许多历史设计方法和标准都青睐 NAND 门，从而形成了围绕它们建立的知识和实践体系。这包括从教育材料到行业最佳实践的所有内容。

6. **集成电路设计**：

- **制造考虑**：集成电路 (IC) 通常围绕 NAND 门的特性进行设计，因为它们的结构更简单，并且在大型阵列中有效使用，使其有利于大规模集成。











#### CPUs

Actual **CPUs** constructed from circuits, logic gates, and ultimately transistors do not function physically like switches in that no transistor is actually ever “pushed.

> 由电路、逻辑门和晶体管构成的实际 CPU 在物理上并不像开关那样工作，因为实际上没有晶体管被“按下”。

A modern CPU is made up of **billions of transistors**. These transistors are arranged in complex circuits that implement everything from basic arithmetic to advanced data manipulation. 

> Despite functioning logically like switches, the transistors in CPUs work in a purely electronic way, using tiny, precisely controlled electrical signals.











## Resentation

### Boolean algebra

#### Statements

 (or propositions) are often represented using capital letters.(e.g., P,Q,R)

>### Lowercase Letters (p, q, r)
>
>- Specific Instances or Variables may be used to represent particular truth values or instances of propositions. This helps to differentiate between general statements and specific cases or values.
>  - Example: If P represents "It is raining," you might say p=True to indicate that the specific statement is true in a certain contexts

#### Predicates

are represented with variables and are usually denoted by **capital** letters, followed by the variables in parentheses, e.g., P(x),Q(x,y).

#### Equations

express relationships between quantities and typically use standard mathematical symbols (e.g., =,<,>,≠).

#### Function 

Functions are often represented **lowercase** as f(x) where f is the function and x is the variable.

#### Set

Sets are typically denoted with curly braces (e.g., S={1,2,3}).

#### multivariable equation/formula

$$
g(x, y) = x^2 + y^2\\
Q(x, y): \text{x teaches at y}
$$

#### Formula of Boolean Algebra

$$
(A \lor (B \land C)) \\
(x \and y)\lor \neg(y \lor z)\\
(x \lor y) \oplus z
$$

> Well-formed formulea
>
> 1. start with a set V of propositional variables. Eg.{V = {A, B, C} or V={u, v, x, y, z}
> 2. use these variables along with the basic operators and parentheses to form well-formed formulea [wffs]



### Digital Circuits

#### Gates & Circuits representation

![cs5001_hw2_text](./pictures/cs5001_hw2_text.png)

![Circuits symbol](./pictures/Circuits symbol.png)

- **逻辑“与”（AND）**运算用符号“·” / "∧"表示。例如，A1⋅B1 意味着 A1 和 B1 同时为真（1）。
- **逻辑“或”（OR）**运算用符号“+” / "∨"表示。例如，A1+B1 意味着 A1 或 B1 至少有一个为真（1）。
- **否定（Negation）**用“¬”或“∼”表示，表示对输入取反。
- **异或（XOR）**通常用“⊕”表示。
- **同或（XNOR）**通常用“⊙”表示。
- **与非（NAND）**通常用“↑”表示。
- **或非（NOR）**通常用“↓”表示。

> 在电路设计中，常用“⋅”表示“与”运算，用“+”表示“或”运算。





## Rules of Symbolic Logic

examining **mathematical notation** called **Boolean formulas**公式. 



### Logical Connectors/**Boolean Operators**

#### Basic Operators: AND, OR, NOT

| Boolean operators | Symbol | Circuits |
| ----------------- | ------ | -------- |
| conjuction        | ∧      | AND Gate |
| disjuction        | ∨      | OR Gate  |
| Negation          | ¬      | NOT Gate |

##### Not boolean operators: But/So

**"but"** is not a negation by itself. In logic, **"but"** is usually treated like **"and"** because it connects two statements while implying contrast, but both parts can still be true. Negation (**NOT**) is a separate operator that reverses the truth value of a statement. For example:

- **"P but Q"** is logically similar to **"P and Q"**.
- **Negation (¬P)** means **"not P"**.

> "but" contrasts ideas but doesn’t negate them.



#### Other Operators: exclusive OR, equivalence

| Boolean operators    | Symbol | Circuits  |
| -------------------- | ------ | --------- |
| Exclusive-OR "ex-or" | ⊕      | XOR Gate  |
| Equivalence "ex-nor" | ≡      | XNOR Gate |

> Why called XNOR?
>
> Equivalence (≡) is represented as **XNOR** in digital circuits because it performs the **inverse** of the **XOR** (Exclusive OR) operation. Equivalence means that **both inputs are either true or false for the output to be true**.
>
> Why use equivalence to refer XNOR?
>
> The term **equivalence** in logic refers to **two statements** having the **same truth value**—either both true or both false. This matches the behavior of the **XNOR** (Exclusive-NOR) operation in digital circuits, which outputs true only when both inputs are the same.

##### XOR's use

- Digital Logic Circuits: XOR is used in circuits like adders (e.g., for calculating sums in binary arithmetic).
- Error Detection: In checksums or parity bits, XOR is used to detect errors in data transmission.
- Cryptography: XOR is fundamental in encryption algorithms (e.g., one-time pad) because of its reversible nature.



### **Order of precedence**

1. **Parentheses** in logic (just like in arithmetic) are used to explicitly group expressions and control the order of operations. They override the standard order of precedence, ensuring that the operations inside the parentheses are performed first.
2. **Negation (¬)** has the highest precedence (like unary minus in algebra).
3. **Conjunction (∧)** comes next (like multiplication).
4. **Disjunction (∨)** has the lowest precedence (like addition).







### Circuits & Addition

#### **half adder circuits**

a simple digital circuit that adds **two single-bit** binary numbers. 

> but **cannot handle carry-in from a previous stage**, which limits its use to simple addition of two single bits.

<img src="./pictures/half add circuit.png" alt="half add circuit" style="zoom:50%;" />

It produces two **outputs**:

- **Sum (S)**: The result of the addition.
- **Carry (C)**: The carry output if the sum exceeds the value that can be represented by a single bit (i.e., 1 + 1 results in a carry of 1).

The half adder is built using **two basic logic gates**:

- **XOR Gate**: For the **sum** output. gives the proper output of the **least** significant bit in adding two bits
- **AND Gate**: For the **carry** output. gives the proper output of the **most** significant bit (or carry) in adding two bits.

> For handling multiple-bit additions, a **full adder** is used, which includes carry-in from previous bits.



#### full adder circuits

a digital circuit that adds **three single-bit** binary numbers: two input bits and a carry-in bit from a previous addition.

> **全加器（Full Adder）**是**波动进位加法器（Ripple-Carry Adder）**的基本组成单元。波动进位加法器是由多个全加器串联而成的，用于对多位二进制数进行加法运算。

<img src="./pictures/ripple adder circuit.png" alt="ripple adder circuit" style="zoom:50%;" />

输入是三位：两个被加数位（A 和 B）和一个进位输入（Carry-In）。

输出是：一个**和（Sum）**和一个**进位输出（Carry-Out）**。





#### **ripple-carry波纹进位 adder circuits**

a type of digital circuit used for **multi-bit** binary addition.

> It consists of a series of **full adders** connected in a sequence, where the **carry-out** of one full adder is fed into the **carry-in** of the next full adder. This configuration allows for the addition of binary numbers with more than one bit.

A ripple-carry adder **with n bits** consists of **n full adders**. 

<img src="./pictures/ripplr_carry_adder.jpg" alt="ripplr_carry_adder" style="zoom:50%;" />

The **least significant bit** (LSB) of the binary numbers is added using the first full adder.

>为什么波动进位加法器要从 LSB 开始？
>
>在波动进位加法器（Ripple-Carry Adder）中，加法是从二进制数的最低有效位（LSB, Least Significant Bit）开始的。最低有效位是二进制数最右边的位，代表二进制系统中的最小值
>
>就像十进制加法一样，我们从最右边的位开始相加，然后把进位（carry）传递到下一位。
>
>在多位加法器中（比如波动进位加法器），每个位的加法都要包括上一个位的进位。然而，在**最低有效位（LSB）**，因为这是加法的第一个位置，所以**没有进位输入**，因此进位通常设置为 0。

1. For each pair of bits from the numbers being added, a full adder computes the sum and the carry-out.
2. The carry-out from one full adder becomes the carry-in for the next full adder.
3. This process "ripples" through the entire chain of full adders, which is why it is called a **ripple-carry adder**.

>1. **第一个全加器（用于 LSB）**：
>
>   - 在**第一个全加器**中加 A0（1）和 B0（0），并且**进位输入为 0**（因为这是最低有效位）。
>   - 和 = A0⊕B0=1⊕0=1
>   - 进位输出 = A0⋅B0=1⋅0=0
>
>   因此，**最低有效位的和是 1**，并且**没有进位输出**。
>
>2. **第二个全加器（下一位）**：
>
>   - 现在，我们在第二个全加器中加 A1（1）和 B1（1），并且使用前一个全加器的进位输出（即 0）。
>   - 和 = A1 ⊕ B1 ⊕ Cin = 1⊕1⊕0 = 0
>   - 进位输出 = (A1⋅B1) + (A1⋅Cin) + (B1⋅Cin) = 1•1+1•0+1•0=1+0+0=1
>
>   因此，和是 0，进位输出为 1。
>
> 进位输出 Cout=(A1⋅B1)+(A1⋅Cin)+(B1⋅Cin): 必须在每一列中将每个输入数的相应位与任何输入进位位相加，从而产生一个输出位并可能产生一个进位位
>
>   **A1⋅B1**：
>
>   - 当 A1 和 B1 都为 1 时，它们的和超过了 1，因此必须产生进位输出。也就是说，两个被加数都是 1 时，必然会产生一个进位。
>
>   **A1⋅Cin**：
>
>   - 当 A1 为 1 且进位输入 Cin 也为 1 时，前一位的进位会影响当前位的加法，导致当前位的和超过 1，从而产生进位输出。
>
>   **B1⋅Cin**：
>
>   - 当 B1 为 1 且进位输入 Cin 也为 1 时，情况类似。如果前一位的进位和当前位的 B1 都为 1，也会导致进位输出。
>
>   **进位输出**的条件是至少有两个输入为 1。
>
>   | A1   | B1   | Cin  | Cout |
>   | ---- | ---- | ---- | ---- |
>   | 0    | 0    | 0    | 0    |
>   | 0    | 0    | 1    | 0    |
>   | 0    | 1    | 0    | 0    |
>   | 0    | 1    | 1    | 1    |
>   | 1    | 0    | 0    | 0    |
>   | 1    | 0    | 1    | 1    |
>   | 1    | 1    | 0    | 1    |
>   | 1    | 1    | 1    | 1    |
>
>   在这个真值表中，可以看到当至少有两个输入为 1 时，Cout 为 1，符合我们的公式。
>
>3. **第三个全加器**，依此类推……





### **Truth Tables**

a tool used in logic to represent the truth values of a compound statement for all possible combinations of truth values of its components.

> use a truth table to practice **determining if statements are true or false**.

| P    | Q    | ¬P   | P∧Q  | P∨Q  | P⊕Q  | P≡Q  | NAND | NOR  |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| T    | T    | F    | T    | T    | F    | T    | F    | F    |
| T    | F    | F    | F    | T    | T    | F    | T    | F    |
| F    | T    | T    | F    | T    | T    | F    | T    | F    |
| F    | F    | T    | F    | F    | F    | T    | T    | T    |

>### Explanation:
>
>- ¬P: NOT P (negation)
>- P∧Q: AND (both true is true)
>- P∨Q: OR (at least one true is true)
>- P⊕Q: XOR (exactly one true is true)

#### Meaning

Truth tables can represent the **arbitrary**任意 input/output behavior of Boolean (logical) formulae or **circuits**.

Truth tables represent the logical behavior of a Boolean formula or system, while circuits implement that behavior using physical logic gates.

>1. **Create a truth table** for the desired logical function, showing all possible input-output combinations.
>2. **Translate the table into a Boolean expression** (e.g., ¬p∧(q∨¬r)¬p∧(q∨¬r)).
>3. **Design a circuit** using logic gates (AND, OR, NOT, etc.) that implements this Boolean expression.

Truth tables define all possible input-output behaviors of a system. This allows us to understand how a system (or formula) behaves. Once we have the truth table, we can design circuits (using AND, OR, NOT gates, etc.) that perform exactly what the truth table describes. These circuits are used in computers, digital devices, and processors to perform operations like arithmetic (e.g., in adders) and decision-making tasks.

By translating truth tables into circuits, we can build reliable, real-world devices that process information logically.



#### **Converting into logic circuit** “按 1 构建 DBF”

Step 1: Identify Output Conditions. From the truth table, identify the rows where the output \( F(A, B) \) is true (1)

Step 2: Write the Minterms. For each row where the output is true, write the corresponding **minterm** (AND term)

Step 3: Combine Minterms Using OR. combine all the minterms using the OR operation.

Step 4: Create the Logic Circuit. To create the logic circuit based on the expression 

> If there are **a lot of rows with output 1**, the resulting DNF formula will be long. We can work **instead with the rows with output 0.**

##### Example

Consider a truth table for a function F(A,B)F(A,B):

| A    | B    | F(A, B) |
| ---- | ---- | ------- |
| 0    | 0    | 0       |
| 0    | 1    | 1       |
| 1    | 0    | 1       |
| 1    | 1    | 1       |

$$
1.\text{identify the rows where the output F(A,B) is true}\\
A=0,B=1\\
A=1,B=0\\
A=1,B=1\\
\text{ }\\

2.\text{Write the Minterms}\\
\text{For A=0,B=1: The minterm is: } \overline{A}B \\
\text{For A=1,B=0: The minterm is: } A\overline{B} \\
\text{For A=1,B=1: The minterm is: } AB\\
\text{ }\\

3.\text{combine all the minterms using the OR operation}\\
F(A, B) = \overline{A}B + A\overline{B} + AB\\
\text{ }\\

4.\text{Create the Logic Circuit}\\
\text{(1)Draw Inputs: Draw two inputs, A and B.}\\
\text{(2)NOT Gates: Use NOT gates to create }\overline{A} \space and \space \overline{B}\\
\text{(3)AND Gates: Create AND gates for each minterm }\overline{A}B \space A\overline{B} \space AB\\
\text{(4)connect the outputs of the three AND gates to an OR gate to get the final output F(A,B)}\\
$$









### **De Morgan’s Law and Other Boolean Laws**

#### De Morgan's Law

conversion between AND and OR operations with negations.

##### First Law (Converting AND to OR)

$$
\overline{A • B} = \overline{A} + \overline{B}
$$

the complement of an AND operation is equal to the OR of the complements of the individual terms

##### Second Law (Converting OR to AND)

$$
\overline{A + B} = \overline{A} • \overline{B}
$$

the complement of an OR operation is equal to the AND of the complements of the individual terms



#### Other Boolean Laws

##### Identity Law恒等律

某些运算如何保持变量不变

###### OR Identity

When you OR a variable with 0, the result is always the variable itself because 0 doesn't affect the outcome.
$$
\text{OR Identity: A + 0 = A}\\
$$

###### AND Identity

When you AND a variable with 1, the result is always the variable itself because 1 doesn’t affect the outcome.
$$
\text{AND Identity: A • 1 = A}
$$


##### **Domination Law支配律**/Null Law零律 / Annihilator湮灭  Law

将变量与 1 进行或运算或将变量与 0 进行与运算时会发生什么，从而有效地使变量变得无关紧要。

###### OR Null

When you OR a variable with 1, the result is always 1, since in an OR operation, any true condition makes the output true.
$$
A + 1 = 1
$$

###### AND Null

When you AND a variable with 0, the result is always 0, since in an AND operation, both conditions must be true for the output to be true.
$$
A • 0 = 0
$$


##### Idempotent Law幂等律

将变量与自身进行或运算或与运算不会改变其值。

> **幂等**是指数学和逻辑中的一个属性，即多次应用一个操作不会改变初次应用之外的结果。

###### OR Idempotent

将变量与自身进行或运算时，结果就是变量，因为将真条件与自身进行或运算不会改变结果。
$$
A + A = A
$$

###### AND Idempotent

将变量与自身进行与运算时，结果就是变量，因为将条件与自身进行与运算不会改变结果。
$$
A • A = A
$$


##### Complement Law补律

将变量与其补码进行“或”运算的结果为 1，将变量与其补码进行“与”运算的结果为 0。

###### OR Complement

变量及其补码涵盖所有可能的情况，因此无论变量的值如何，或运算的结果都是 1（真）。
$$
A + \overline{A} = 1
$$

###### AND Complement

变量及其补码不可能同时为真，因此 AND 运算的结果始终为 0（假）。
$$
A • \overline{A} = 0
$$


##### Commutative Law交换律

操作数的顺序不会影响 AND 或 OR 运算的结果。这意味着你可以交换变量，结果将保持不变。

###### OR Commutative

在 OR 运算中，无论先写A还是B先写，结果都是一样的。
$$
A+B = B+A
$$

###### AND Commutative

在 AND 运算中，变量的顺序不会影响结果。可以交换A和B，输出仍然相同。
$$
A•B = B•A
$$


##### Associative Law结合律

AND 或 OR 运算中变量的分组并不重要。

###### OR Associative

$$
A+(B+C) = (A+B)+C
$$

###### AND Associative

$$
A•(B•C) = (A•B)•C
$$



##### Distributive Law分配律

允许像代数一样对项进行分解或展开。

> ... Over ... refers to 其中一个运算可以分配到另一个运算上，类似于普通代数中乘法分配到加法上的方式。

###### AND over OR

AND 可以分配到 OR 上。
$$
A • (B+C) = (A•B) + (A•C)
$$

###### OR over AND

OR 可以分配到 AND 上。
$$
A + (B • C) = (A+B) • (A+C)
$$


##### Double Negation Law双重否定律

对变量取两次否定会返回原始变量，因为双重否定会抵消其效果。
$$
\overline{\overline{A}} = A
$$


##### Absorption Law吸收律

通过“吸收”冗余项来简化表达式

###### OR Absorption

如果A 已经为真，则附加项A⋅B 不会影响结果，因此表达式简化为A。
$$
A + (A•B) = A
$$

###### AND Absorption

如果A 已经为真，则附加项A+B 不会影响结果，因此表达式简化为A
$$
A•(A+B) = A
$$


##### Consensus Theorem共识定理

消除冗余项

> 共识定理有助于降低布尔表达式的复杂性，使逻辑电路更高效且更易于设计。

$$
A•B+\overline{A}•C+B•C = A•B+\overline{A}•C\\
\text{ }\\
\text{B⋅C 不会给表达式的输出添加任何新信息或影响。} \\
\text{它已经通过涉及A和} \overline{A} \text{的项来表示。}
$$



### **Boolean Equivalence**

two Boolean expressions that yield the same output **for all possible combinations of inputs**

> Boolean equivalence means the 2 expressions have the same truth table.

>Why Boolean Equivalence is Important
>
>- It is a foundational tool for simplifying logic circuits, reducing the number of gates and wires.
>- It helps create more efficient designs in both software logic and hardware circuits.

**Symbol**: A⇔BA⇔B (or sometimes A≡BA≡B)

**Meaning**: A⇔BA⇔B is true **if and only if** both AA and BB are either both true or both false.

>Why we use the same symbol for both Boolean equivalence and the XNOR gate?
>
>The reason is that they perform the same logical function:
>
>- Boolean equivalence checks whether two Boolean expressions have the same truth value.
>- XNOR checks whether two inputs to a digital circuit are the same (both true or both false).



##### Analysis: Normal Form

当我们试图分析布尔公式时，通常将公式写成标准形式或规范形式会有所帮助。

**真值表可用于生成 CNF 或 DNF**：从布尔公式的真值表中，可以构造公式的 CNF 或 DNF 表示。

> 使用**真值表**从布尔公式构造**合取范式 (CNF)**或**析取范式 (DNF)**，然后可以使用它们构建表示该公式的电路。
>
> 这种方法虽然通用，但**效率不高**，并且可能导致**复杂电路**，而这些电路不一定是最简单或最优化的版本。
>
> **指数复杂度**：如果公式有**N 个变量**，其真值表将有 \(2^N\) 行，这意味着将真值表转换为 CNF 或 DNF 的过程需要**指数时间**。随着变量数量的增加，计算成本会变得很高。





### **Propositional Logic命题逻辑**

Propositional logic, also known as sentential logic or statement logic, is a branch of logic that **deals with propositionsand their relationships**. 

> A **proposition** is a declarative statement that is either **true** or **false**. 

Propositional logic focuses on **how these propositions can be combined and manipulated using logical operators.**

>The concepts of **inverse**, **converse**, and **contrapositive** are crucial in logic and reasoning
>
>they help us explore the different ways statements can be related, revealing deeper insights into the structure of arguments and deductions.
>
>- In mathematical proofs and theorems, working with the **contrapositive** is often more convenient or simpler than working with the original statement.
>- Understanding the **inverse** and **converse** is also crucial in recognizing when certain assumptions or implications are incorrect.
>- The **converse** and **inverse** help in testing the robustness of an argument. Just because a statement P→Q is true doesn’t mean that the reverse statement (converse) or the negated forms (inverse) hold.
>- In **computer science** and **formal logic systems**, clearly distinguishing between **implications**, **converses**, **inverses**, and **contrapositives** helps design systems that accurately represent real-world logic.



#### Implications蕴涵, 原命题

An implication is a logical statement in the form P⇒Q, which reads "if P, then Q." 

- P is called the antecedent (or hypothesis). 前件（或假设）
- Q is called the consequent (or conclusion). 后件（或结论）

##### Negation

When you negate the implicationp→q, you're expressing that "it is **not true** that pp implies q." This is logically equivalent to stating that pp is true **but** q is false. 
$$
¬(p→q)≡p∧¬q
$$

>For the original implication p→q to be false, **the only scenario** where the implication fails is when p is true and q is false (look at the truth table). So, **negating p→q** means you are saying that p is true, but q does not follow, i.e., q is false



#### Inverses否命题

The **inverse** of an implication P⇒Q is formed by negating both P and Q, creating a new statement P‾⇒Q‾. This reads "if not P, then not Q."

- The inverse is **not logically equivalent to** the original implication P⇒Q, but it **follows a similar structure**, just with the opposite meanings of P and Q.

> If the original statement is "If it is raining, the ground is wet" (P⇒Q), the inverse would be "If it is not raining, the ground is not wet" (P‾⇒Q‾). 
>
> However, **this is not necessarily true**, since the ground could be wet for other reasons (like someone watering it).



#### Converse逆命题

The **converse** simply **reverses** the order of the implication without negating: Q⇒P



#### Contrapositives逆否命题

The **contrapositive** of an implication P⇒Q is formed by reversing and negating both P and Q, creating a new statement Q‾⇒P‾. This reads "if not Q, then not P."



#### Truth table

| p    | q    | p→q  | q→p (Converse) | ¬p→¬q (Inverse) | ¬q→¬p (Contrapositive) |
| ---- | ---- | ---- | -------------- | --------------- | ---------------------- |
| T    | T    | T    | T              | T               | T                      |
| T    | F    | F    | T              | T               | F                      |
| F    | T    | T    | F              | F               | T                      |
| F    | F    | T    | T              | T               | T                      |

- **Implication (p → q)**: This is true in all cases except when pp is true and qq is false.
- **Converse (q → p)**: This is the reverse of the implication. It’s true in all cases except when qq is true and pp is false.
- **Inverse (¬p → ¬q)**: This is the implication with both pp and qq negated. It’s false only when ¬p is true and ¬q is false (which happens when pp is false and qq is true).
- **Contrapositive (¬q → ¬p)**: This is logically equivalent to the original implication p→q. It’s true in all cases except when ¬q is true and ¬p is false, i.e., when p is true and q is false.

>The **contrapositive** is always logically equivalent to the original implication.
>
>The **inverse** and **converse** are **not** necessarily equivalent to the original implication.





### Quantifying Predicates

the use of **quantifiers** (like universal ∀∀ and existential ∃∃) to express statements about predicates in formal logic.

**Quantifiers** are symbols used in logic to specify how many elements of a domain satisfy a predicate.

When quantifying over a predicate, we must specify the **domain of discourse**, which is the set of all possible values for the variable xx. The truth of the quantified statement depends on this domain.



#### Universal Quantifier

a predicate holds for **every element** in a domain.

using the symbol ∀, which means **"for all"** or "for every."

##### general form

∀x P(x) This reads as: **"For all x, the predicate P(x) is true."**



#### Existential Qualifiers

express that **there exists at least one element** in a domain for which a certain statement or property holds.

using the symbol ∃, which means **"there exists"** or **"for some"**.

> The **domain of discourse** (the set of values that xx can take) is critical.

##### general form

∃x P(x) This reads as **"There exists at least one x such that P(x) is true."**

- ∃ is the **existential quantifier**.
- x is the **variable** in the domain.
- P(x) is a **predicate** (a statement) about x.



#### Usage

**Mathematical Existential Statement**: "There exists a number x such that x+3=7."

- Symbolic form: ∃x  (x+3=7)
- True because x=4 satisfies this equation.

**Contradictory Example**: "There exists a real number xx such that x^2=−1."

- Symbolic form: ∃x (x2=−1) over the domain of real numbers.
- False because no real number satisfies this condition. (In complex numbers, this would be true with x=i).

**In computer Science**

Formal verification: Proving that programs work correctly by defining predicates for certain conditions and checking them for all inputs (universal quantification) or for some inputs (existential quantification).

Database queries: SQL uses existential and universal quantifiers implicitly when retrieving data. For example, retrieving all rows satisfying a condition is like universal quantification over the rows.



#### In Propositions

**Combining Quantifiers**: combine quantifiers to make more complex statements about predicates.

>∀x∃yQ(x,y) means "For every x, there exists a y such that Q(x,y) is true."



#### Negation

The negation of an existential quantifier is a **universal quantifier**, and vice versa. This is known as **quantifier negation**.

> ¬(∃xP(x)) means "There does not exist an xx such that P(x) is true." This is equivalent to: ∀x ¬P(x), meaning "For all x, P(x) is false."
>
> ¬(∀xP(x)) becomes ∃x ¬P(x), which means "There exists an x such that P(x) is false."





## Nim Game

共有几堆物品（如石子、火柴等）。两名玩家轮流行动，每次可以从任意一堆中移除任意数量的物品，但至少要移除一件。不能跳过自己的回合。取走最后一件物品的玩家获胜。

胜利策略（XOR原理）： 如果在轮到你时，各堆物品的数量进行 XOR 之后的结果是 **0**，那你处于劣势。如果是非零，你可以通过合理的移除策略转化为对手的 XOR 结果为 0，从而让自己处于有利位置。 

> 计算多堆物品的 XOR 结果需要逐个对堆的数量进行 **按位异或（XOR）运算**。
>
> 异或的规则是：如果两个数相同（如0和0，或1和1），则结果为0；如果两个数不同（如1和0），则结果为1。 
>
> 将所有物品堆的数量转换为二进制表示。对每一堆的数量进行逐个数字的异或运算。
>
> ```shell
> # 假设有三堆石子，数量分别是：3、4、5。
> 011 ---> 3
> 100 ---> 4
> 101 ---> 5
> ----
> 010 ---> 最终的 XOR 结果
> # 如果最终 XOR 结果为 0，当前玩家处于劣势。如果最终 XOR 结果为非零，当前玩家处于有利位置，可以通过合理的策略让对手陷入劣势。
> ```



### Nim 博弈理论

XOR 操作的核心思想是通过对每一堆物品数量的二进制表示进行运算，揭示局势的**“对称性”和“非对称性”**。

> Nim 游戏中的每一堆物品可以用一个数表示，而整体的游戏局势可以通过所有堆的物品数进行异或（XOR）来描述。如果游戏的 XOR 结果为 0，这意味着当前的局面是“对称”的，玩家无论怎么选都会输；如果 XOR 结果不为 0，意味着局面是“非对称”的，当前玩家有办法采取必胜策略。 

> XOR 操作本质上是对每一堆物品的二进制位进行**按位比较**。 
>
> 通过逐位比较不同堆的物品数量，异或运算能让我们识别局势是否是“对称的”（即 Xor 结果为 0）。 
>
> 如果当前局面的 XOR 结果不为 0，说明局面非对称。这时，玩家可以通过按位异或找到一个合适的堆，通过移除适量物品将局面转化为对称局面（XOR 结果为 0），让对手陷入劣势。 

**XOR 结果为 0**：当前局面是劣势局面。如果轮到你时 XOR 结果为 0，你无论怎么操作都无法保证胜利，对手可以通过操作始终把局面维持为 XOR 结果为 0。

**XOR 结果不为 0**：当前局面是有利局面。如果轮到你时 XOR 结果不为 0，你可以通过调整某一堆的物品数量，使得对手面临的局面 XOR 结果变为 0，这样对手将处于劣势。

> 当 XOR 结果不为 0 时，你可以总是找到一个堆，通过合理取走物品，将局面的 XOR 结果变为 0。这样，对手在每次行动后只能面对劣势局面。如果你始终保持这个策略，最终会是你取走最后一个物品，赢得比赛。 



- 二进制数的每一位要么是 0 要么是 1，它们代表“关”和“开”的状态，因此，按位操作如 AND、OR、XOR 等可以逐位应用到二进制数上，简化对数字的处理。
- XOR 的**交换性和结合性** : 对于任何两个数 A 和 B，`A XOR B = B XOR A`。这意味着操作的顺序不影响结果。  对于三个数 A、B 和 C，`A XOR (B XOR C) = (A XOR B) XOR C`。这意味着可以先 XOR 任意两个数，再与第三个数进行 XOR 操作。 
- XOR的 **无进位加法**：XOR 本质上是模 2 加法，没有进位操作，这意味着它能够仅通过每一位的状态来揭示数字间的差异和对称性。 
- 当我们使用 XOR 时，如果 XOR 结果为 0，说明当前局面是对称的，玩家无法通过任何操作直接取胜；如果 XOR 结果不为 0，说明存在非对称性，玩家可以通过选择合适的堆并调整其中的物品数量，打破对称性，迫使对手进入不利局面。 


>如果将每个堆的数异或后加起来，最后的和只是一个总数，无法精确反映每一位上的对称与否。
>
>在 Nim 游戏中，我们需要知道每一位的状态，才能决定如何操作某一堆的物品。将数加起来则掩盖了这种逐位分析的能力，导致无法精确识别局面中的关键差异。



## Symbolic Logic or Boolean Algebra





# Module 3 **Set Theory**

Collection Representation

By the end of this module, you should be able to:

- 3-1: Define and represent a set using set builder notation
- 3-2: Operate on sets to create new sets using set difference, union, intersection, and power set

>{{A}, {B}, {C}, {A, B}, {A, C}, {B, C}, {A, B, C}} 7
>
>{{A}, {B}, {C}, {D}, {A, B}, {A, C}, {A, D} {B, C}, {B, D}, {C, D}, {A, B, C}, {A, B, D}, {A, C, D}, {B, C, D}, {A, B, C, D}} 15



## Sets

无序的、唯一的元素集合

- Elements in a set are **not repeated**
- Elements in a set have **no order**



### **VS. List**

A list is a collection of objects which has an ordering. 

> By ordering, we mean that the list has a first element, a second element, a third element, and so on. 
>
> It doesn’t necessarily mean that it is in alphabetical order or increasing numerical order, just that the position in the list matters.

- **集合**没有顺序，集合不允许重复元素。
- **列表**（或称为序列）是有序的，可以包含重复元素。The only distinguishing factor in a set is membership. This is not true for lists.

> 集合的操作（如并集、交集）通常针对元素的集合，而列表的操作（如排序、切片）则是基于位置和顺序。



### Logic & Predicates & Sets

There is a relationship between symbolic logic and predicates and sets

P(x) can be interpreted to mean {x | P(x)} which is {x Î P}

So P is the set of all x that satisfy the predicate P(x)

> Example: *Evens* is the set of all x that satisfy the predicate “x is even”

p can be interpreted to mean P(x), in other words {x is in P}

- (not p) means P’ 
- (p or q) means P union Q 
- (p and q) means P intersection Q



### Multiplicity

**多重集**是集合的一个推广，允许**元素出现多次**。也就是说，元素可以出现**不止一次**。

元素的总数，包括重复次数

#### 运算

##### 多重集并集

- 每个元素的多重性为各个多重集中的**最大**多重性。

M∪N={x∣max(M(x),N(x))}

> **示例**：M={1,2,2},N={2,3,3,3}
>
> M∪N={1,2,2,3,3,3}

##### 多重集交集

- 每个元素的多重性为各个多重集中的**最小**多重性。

M∩N={x∣min(M(x),N(x))}

> **示例**：M={1,2,2},N={2,3,3,3}
>
> M∩N={2}

##### 多重集差集

- 每个元素的多重性为在第一个多重集中的多重性减去在第二个多重集中的多重性（如果结果为正）。

M−N={x∣M(x)−N(x)（如果为正）}

> **示例**：M={1,2,2,3},N={2,3,3}
>
> M−N={1,2}













### **Cardinality**

- how to count the elements of a given set
- how to count elements when sets are combined in various ways
- counting overages using the pigeonhole principle.



#### Counting Unions

∣A∪B∣=∣A∣+∣B∣−∣A∩B∣



#### Counting Cartesian Products

**笛卡尔积** 描述多个集合之间所有可能的**有序组合**。

> 给定两个或多个集合，笛卡尔积就是这些集合中元素的所有可能的有序排列组合。

对于两个有限集合 A 和 B，其中：

∣A∣=m, ∣B∣=n, 则它们的笛卡尔积 A×B 中的元素数量为： ∣A×B∣=m×n

> **解释**：每个 A 中的元素可以与 B 中的每一个元素配对，因此总共有 m×n 种组合。

对于 k 个有限集合 A1,A2,…,Ak，其中：

∣A1∣=n1,∣A2∣=n2,…,∣Ak∣=nk, 则它们的笛卡尔积 A1×A2×…×Ak 中的元素数量为：∣A1×A2×…×Ak∣=n1×n2×…×nk

> **解释**：类似于两个集合的情况，每增加一个集合，元素的组合数量就乘以该集合的元素数量。









#### Inclusion-Exclusion Principle 容斥原理

a fundamental concept in combinatorics and set theory used to calculate the cardinality 基数 of the union of multiple sets.

##### Two Sets (n=2)

∣A∪B∣=∣A∣+∣B∣−∣A∩B∣

##### Three Sets (n=3)

∣A∪B∪C∣=∣A∣+∣B∣+∣C∣−∣A∩B∣−∣A∩C∣−∣B∩C∣+∣A∩B∩C∣

##### Four Sets (n=4)

∣A∪B∪C∪D∣= ∣A∣+∣B∣+∣C∣+∣D∣−∣A∩B∣−∣A∩C∣−∣A∩D∣−∣B∩C∣−∣B∩D∣−∣C∩D∣+∣A∩B∩C∣+∣A∩B∩D∣+∣A∩C∩D∣+∣B∩C∩D∣−∣A∩B∩C∩D∣

##### General Formula for n Sets

For any finite number of finite sets A1,A2,…,An, the cardinality of their union is given by:

In simpler terms:

1. **Add** the sizes of all individual sets.
2. **Subtract** the sizes of all pairwise intersections.
3. **Add** the sizes of all triple intersections.
4. **Subtract** the sizes of all quadruple intersections.
5. **Continue** this alternating pattern up to the intersection of all nn sets.





## Representation

用花括号 `{}` 表示，元素之间用逗号分隔。

>集合 A = {1, 2, 3}
>
>集合 B = {a, b, c, a} （注意：集合 B 中的元素 "a" 只算一次）

### **set builder notation 集合构建器符号**

通过指定其元素必须满足的属性或条件来描述集合。
$$
S=\{x∣condition\}
$$

- **S**: The name of the set.
- **{x∣condition}**: This reads as "the set of all x such that the condition is true."

> 通常在处理无限集或集合的元素不易列出时使用。

一般形式：A={x ∣ 满足某个条件}. 其中 x 是集合中的元素，后面的条件是对 x 的描述。

> 特定条件的集合
>
> A={x∈R ∣ x^2<4} 表示所有实数 x 使得 x^2<4。
>
> 范围限制的集合
>
> B={x∈R∣0<x<5} 表示 集合 B 包含所有在 0 和 5 之间的实数（不包括 0 和 5）。



### Typical sets

#### 自然数集 (N)

Set of natural numbers.

指非负整数或正整数，具体定义依赖于上下文。

> $$
> \mathbb{N}
> $$
>
> When writing the natural number set N, it is standard to use a double-struck (or blackboard bold) style to represent it, which is typically written with two vertical lines (also referred to as "double bars") in mathematical notation.

- 非负整数：N={0,1,2,3,…}
- 正整数：N^+={1,2,3,…}

> 自然数在加法和乘法下封闭，即两个自然数的和或积仍是自然数。

#### 整数集（Z）

Set of integers.

所有正整数、负整数和零，表示为：Z={…,−3,−2,−1,0,1,2,3,…}
$$
\mathbb{R}
$$

> 整数可以表示为有理数的形式，但不包括分数或小数。
>
> 整数集在加法、减法和乘法下封闭。

#### 有理数集（Q）

Set of rational numbers.

所有可以表示为两个整数之比的数，形式为：
$$
\mathbb{Q}=\{\frac{p}{q}∣p,q∈Z,q≠0\}
$$

> 有理数包括所有整数（可以看作是分母为1的分数）、有限小数和循环小数。
>
> 在加法、减法、乘法和除法下（除以零除外），有理数集是封闭的。

#### 实数集（R）

Set of real numbers.

所有有理数和无理数（即不能表示为两个整数之比的数），表示为： R=Q∪{无理数}
$$
\mathbb{Z}
$$

>实数可以表示为数轴上的点，包括正数、负数和零。
>
>实数包括有限小数、无限不循环小数（如 square root of 2, π 等）。
>
>实数集在加法、减法、乘法和除法下是封闭的。



### 元素符号

如果元素 x 属于集合 A，可以表示为 x∈A；如果不属于，可以表示为 x∉A。

### 空集合

没有元素的集合，用符号 ∅ 或 {} 表示。

### Venn diagram

集合之间关系的图形表示法

> 通常用于展示集合的交集、并集和差集等概念。

- **集合**：每个圆代表一个集合。
- **交集**：重叠部分表示两个集合的交集。
- **并集**：所有圆的区域合并表示两个集合的并集。
- **差集**：一个圆中不重叠的部分表示与另一个集合的差集。

### **Bitmap** **位图**

使用长度为 n 的二进制字符串来表示集合，其中 n 是全集中元素的数量。

1. 首先，我们固定一个任意的元素顺序。[先确定全集中元素的固定顺序，这一点至关重要，以确保表示的一致性。]
2. 然后，用 `1` 表示元素在集合中，`0` 表示元素不在集合中。

>**全集 U**：包含所有可能元素的集合。
>
>**位图（Bitmap）**：用于表示集合的**二进制字符串**。

> 将集合中的元素映射到二进制位（0和1），以简洁地表示集合的存在与否。
>
> 对于全集较小的集合非常高效。

#### 二进制字符串

假设我们有一个有限集合 A={a1,a2,a3,…,an}，其中 n 是集合中元素的个数。

一个长度为 n 的二进制字符串 b1b2b3…bnb1b2b3…bn 可以表示集合 A 的子集，其中：

- bi=1 表示元素 aiai 在集合中。
- bi=0 表示元素 aiai 不在集合中。

$$
% 使用二进制字符串表示集合
考虑集合 $A = \{1, 2, 3\}$，其二进制字符串表示如下：\\
空集 \emptyset： 000\\
只包含元素 1 的子集 \{1\}： 100\\
包含元素 1 和 2 的子集 \{1, 2\}： 110\\
包含所有元素的集合 \{1, 2, 3\}： 111\\
$$

#### 位图操作

$$
S_1 = 1010 \quad (\{a, c\})\\
S_2 = 0101 \quad (\{b, d\})\\
\text{ }\\
{并集}\\
S_1 \cup S_2 = 1111 \quad (\{a, b, c, d\})\\
\text{ }\\
{交集}\\
S_1 \cap S_2 = 0000 \quad (\emptyset)\\
\text{ }\\
{差集}\\
S_1 - S_2 = 1010 \quad (\{a, c\})\\
$$





## Types

### Subsets子集

一个集合的所有元素都包含在另一个集合中。

> This is a **statement** (in other words an **assertion**) not an **operator** on sets

> 设有集合 A 和 B，如果 A 的所有元素都在 B 中，则称 A 是 B 的子集，表示为 A⊆B。
>
> 包括两种情况：
>
> - **真子集**（Proper Subset）：如果 A 是 B 的子集，但不等于 B（即 A 是 B 的部分元素），记作 A⊂B。
> - **非真子集**（Not Proper Subset）：如果 A 等于 B（即 A 和 B 包含完全相同的元素），或者 A 是 B的部分元素，这种情况下可以写作 A⊆B。

#### proper subset

A set A is a **proper subset** of a set B if every element of A is also an element of B, and A is not equal to B. This means that B must contain at least one element that is not in A.

A⊂B

#### Not Proper Subset 非真子集

集合 A 如果是集合 B 的 **非真子集**，则意味着 A 满足以下条件之一：

1. A 等于 B（即 A 和 B 包含完全相同的元素），或者
2. A 包含 B 的部分元素，但并不是所有元素（这实际上也可以被称为子集，但不是非真子集的严格定义）。

如果 A 是 B 的非真子集，可以表示为：A⊆B

> 在这种情况下，A 可以等于 B，所以我们不能用 A⊂B 来表示，因为后者表示的是**真子集**。

>**非真子集**这个术语的“非”并不是说它不包括任何其他子集，而是强调了它的特点：“不是严格的真子集”
>
>它包括了两个方面的情况：要么是部分元素（真子集），要么是相等（并不满足真子集的条件）。就是说：
>
>- 如果 A 等于 B，那么 A 是非真子集；
>- 如果 A 是 B 的部分元素，则 A 是真子集。

### The Empty Set空集

一个不包含任何元素的集合，表示为 ∅ 或 {}。



### The Power Set幂集

一个集合的所有子集构成的集合。

> 设有集合 A，幂集表示为 P(A) 或 2^A。







## Operations/operators

### set equivalence

两个集合包含完全相同的元素。
$$
E \subseteq F \text{ and } F \subseteq E \iff E  \equiv F
$$


### intersection交集

所有在 A 和 B 中都存在的元素的集合，表示为 A∩B。



### union并集

所有在 A 或 B 中的元素的集合，表示为 A∪B。



### complement补集

在某个特定全集中，某个集合以外的所有元素。
$$
\text{the complement of A is } \overline{A}
$$

> 设有全集 U 和集合 A，则 A 的补集表示为 A′ 或 A‾。补集包含所有属于 U 但不属于 A 的元素。



### set difference 差集

集合 A 中去掉集合 B 中的元素，表示为 A−B。



#### Symmatric Difference

A triangle B = (A – B) union (B – A) = (A È B) intersection (A Ç B)’

 The set version of XOR !



### Cartesian Product of 2 sets

两个集合的所有有序对的集合。对于集合 A 和集合 B，笛卡尔积通常表示为 A×B。

对于集合 A 和 B，笛卡尔积 A×B 定义为：A×B={(a,b)∣a∈A 且 b∈B}. 每个元素是由集合 A 中的元素和集合 B 中的元素组成的有序对。

- **有序性**：笛卡尔积中的有序对是有顺序的，即 (a,b) 和 (b,a) 被视为不同的元素。



#### Counting Elements In The Cross Product

**元素数量**：如果集合 A 中有 m 个元素，集合 B 中有 n 个元素，则笛卡尔积 A×B 将有 m×n 个元素。

















## Relations

一个**关系** R 是两个集合 A 和 B 之间的有序对集合。我们说 R⊆A×B，即 R 是笛卡尔积 A×B的一个子集。

> 关系 R 是 A×B 的一个子集，因此它是一个有序对集合 (a,b)，其中 a∈A 且 b∈B。

It might not include all the ordered pairs in A X B

### Domain & Range

- A is called the **domain** of R
- B is called the **range** of R
- Some people call it the **codomain** of R

>- **A** 被称为关系 R 的**定义域**（Domain）。定义域是所有能够作为有序对第一个元素 aa 的集合。
>- **B** 被称为关系 R 的**值域**（Range）。值域是所有能够作为有序对第二个元素 bb 的集合。
>
>有时，**B** 也被称为**陪域**（Codomain）。

### General relation R

在一般关系 R 中：

- **定义域**中的每个元素可能对应于关系 R 中的零个、一个或多个有序对。
- **值域**中的每个元素也可能对应于关系 R 中的零个、一个或多个有序对。

> 在一般关系中，没有限制每个定义域中的元素可以对应多少个有序对。比如，某个元素可以对应于多个有序对，或者根本不对应任何有序对。





### Multiplicity（多重性）

在一个关系中，一个元素在定义域中可能对应多个输出元素（即多个有序对）。在这种情况下，我们可以说这个元素的多重性是大于1。

>在关系 R 中，若元素 x 对应于多个有序对，比如 (x,y1) 和 (x,y2)，则我们称 x 的多重性为 2。

**关系**可以具有多重性，允许一个定义域中的元素对应多个值域中的元素。

**函数**不允许多重性。每个输入都必须映射到唯一的输出。如果有一个输入对应多个输出，则该关系不是函数。

>在数据库中，关系的多重性可以表示数据的冗余性或复用性。
>
>在编程中，函数通常要求输入返回唯一的输出，以确保逻辑的可预测性和可靠性。



### Types

- **多对一**（如母亲关系）：多个输入元素（孩子）可以对应到同一个输出元素（母亲）。
- **一对一**（如首都关系）：每个输入元素（国家）对应唯一的输出元素（首都）。
- **多对多**（如最爱食物关系）：多个输入元素（学生）可以对应到多个输出元素（食物）。







### Function

当定义域中的每个元素恰好对应于一个有序对时，称该关系为**函数**。

- **唯一性**：每个定义域中的元素对应于一个且仅一个有序对。这意味着函数的每个输入（定义域中的元素）都只能产生一个输出（值域中的元素）。
- **映射**：函数将定义域中的每个元素映射到值域中的一个元素。

> 将每个定义域中的元素映射到一个唯一的值域中的元素
>
> - 函数要求定义域中的每个元素只能对应于一个有序对。
> - 函数为定义域中的每个元素提供一个唯一的输出。

在函数中，每个定义域中的元素（输入）只能对应一个值域中的元素（输出）。这意味着函数的多重性为1。

#### one-to-one correspondence

如果定义域中的每个元素与值域中的唯一元素相对应，则该函数称为**一一对应**

- **一对一**：每个定义域中的元素都映射到值域中的一个唯一元素。
- **到达性**：值域中的每个元素都由定义域中的某个元素映射。

##### invertible可逆

由于一一对应的性质，函数是**可逆的**，这意味着我们可以找到一个**逆函数**。

在一一对应的情况下，定义域和值域的基数（cardinality）是相同的。这意味着两者中元素的数量是一样的。

##### **双射**（bijection）

一一对应的函数

squares:{正整数}↔{完全平方数}

- **单射（Injective）**：没有两个不同的元素映射到同一个元素。
- **满射（Surjective）**：每个元素都被映射到。

###### Prove

- Prove that for each element in the domain there is one element in the range
- Also prove that for each element in the range there is one element in the domain



##### isomorphic**同构**

在一一对应的情况下，定义域和值域被称为**同构**（isomorphic），因为它们之间存在一种一对一的关系。









## Properties

### 交集性质

1. **交换律**：A∩B=B∩A
2. **结合律**：A∩(B∩C)=(A∩B)∩C
3. **与空集合的交集**：任何集合与空集合的交集都是空集合，即 A∩∅=∅

### 并集性质

1. **交换律**：A∪B=B∪A
2. **结合律**：A∪(B∪C)=(A∪B)∪C
3. **与空集合的并集**：任何集合与空集合的并集都是它自己，即 A∪∅=A

### 补集性质

1. **全集的补集**：全集 U 的补集是空集合，即 U′=∅。
2. **空集合的补集**：空集合的补集是全集，即 ∅′=U。
3. **补集的双重**：某个集合的补集的补集是它自己，即 (A′)′=A。

### 子集性质

1. **任意集合的子集**：每个集合都是它自己的子集，即 A⊆A。
2. **空集合是子集**：空集合是任何集合的子集，即 ∅⊆A。

### 空集合性质

1. **子集**：空集合是任何集合的子集。
2. 并集与交集：
   - 与任何集合的并集是该集合本身，即 A∪∅=A。
   - 与任何集合的交集是空集合，即 A∩∅=∅。

### 幂集性质

1. **元素个数**：如果集合 A 有 n 个元素，则其幂集有 2^n 个元素。
2. **空集合的幂集**：空集合的幂集是包含空集合本身的集合，即 P(∅)={∅}。
3. **包含空集和原集合**：幂集中一定包括空集 ∅∅ 和原集合 AA 本身。



### **Laws**

#### Identity Law恒等律

$$
A \cap U = A\\
A \cup \empty = A
$$

#### Domination Law支配律

$$
A \cup U = U\\
A \cap \empty = \empty
$$

#### Idempotent Law幂等律

$$
A \cup A = A\\
A \cap A = A
$$

#### Commutative Law

$$
A \cup B = B \cup A\\
A \cap B = B \cap A
$$

#### Associative Law

$$
(A \cup B)\cup C = A \cup (B \cup C)\\
(A \cap B)\cap C = A\cap (B\cap C)
$$

#### Distributive Law

$$
A\cup (B\cap C) = (A\cup B)\cap (B\cup C)\\
A\cap (B\cup C) = (A\cap B)\cup (B\cap C)
$$

#### Absorption Law

$$
A \cup (A\cap B) = A\\
A \cap (A\cup B) = A
$$

#### De Morgan's Law

$$
\overline{A \cup B} = \overline{A} \cap \overline{B}\\
\overline{A \cap B} = \overline{A} \cup \overline{B}\\
$$







# Module 4 **Writing Proofs: formal proofs**



## Terminology

### Assertion

Any statement can be called an **Assertion**. We don’t necessarily know whether it is true or false

### Assumption

a statement we believe to be true without proving it

> There are several kinds of assumption:
>
> - An **Axiom** or **Law** is something universally agreed to be true **[**DeMorgan’s Law / “Every integer is either even or odd”**]**
>
> - A **Definition** that Are Universally Agreed , EITHER **a Law:** 
>   •Let Z be the set of integers
>
>   •p XOR q means (p or q) and not (p and q)
>
>   •p ⇒ q means (not p) or q
>
>   •P(S) means the powerset of S
>
>   •∅ means the empty set
>
>   **something we declare as a convenience:**
>   •Let S be the set of numbers divisible by 4
>
>   •Suppose n is an even number. Then there exists an integer k such that n = 2k
>
>   •Suppose we want to assign n pigeons to k holes 
>
> - A statement we make during a proof, knowing it is yet to be proven. Usually we say “Suppose X. Then …” We will prove it is true or not
>
> - •Let’s prove: There are no two integers x and y such that x2 + y2 = 2023
>
>   ```txt
>   For all integers n, n mod 4 must be one of {0, 1, 2, 3}
>                           
>    Now suppose n mod 4 = 0
>                           
>    blah blah blah – *here we can assume n mod 4 is 0*
>                           
>    Now suppose n mod 4 = 1
>                           
>    blah blah blah – *here we can assume n mod 4 is 1*
>                           
>    Now suppose n mod 4 = 2
>                           
>    Now suppose n mod 4 = 3
>                           
>    Therefore, …
>   ```



### Conclusion

something we have proven

also call it a **Theorem** or **Lemma** if we want to use it in the future

#### Theorem 

定理是一个经过证明的数学命题。它通常由一个前提和一个结论构成，可以表述为“如果...那么...”的形式。



### Conjecture推测

a statement whose truth we do not know





## What is a proof?

a mathmatical argument or reason to show something is true

proof: 数学论证或推理，用于展示某个命题或定理的真实性。它通过逻辑推理和已知事实来支持一个数学声明。

> Jury: 陪审团. 一群被选中听取和评估法律案件中的证据并根据该证据作出裁决的个人。



### Belief phase

对待证明的命题形成一个初步的理解和信念。需要明确自己对该命题的看法。

### proof idea

为证明选择的方法或策略。例如，您可能决定采用直接证明、反证法（间接证明）或数学归纳法等。



## How Do We Figure Out A Proof?

1. Start with a clear statement
2. Play with the ideas until we see a line of reasoning that works
3. Write up this line of reasoning as a Proof



## What Does A Proof Look Like?

1. First we **state a Conjecture**. We will try to prove it.
2. There are several standard approaches to writing a proof. If we are kind to the reader we will **tell them what approach we will be using.**
3. We **state our assumptions**. Our most important Definitions need to be stated here. Usually we don’t bother to state the “universally agreed on” Laws and Definitions
4. Then we **reason** by applying our assumptions …… until we prove that our assumptions result in the **truth of our Conjecture**
5. “**Therefore**” the Conjecture is true. “QED” (we sometimes put this, it means roughly “it is proven”)



## How Rigorous Does A Proof Have To Be?

Can you use that as an assumption in a proof? It all depends on the audience for whom your proof is written!!

One person may say, we all know this is true, fine, use it and move along. Another person may say, well, is this really true? Prove it before you use it









## Common **Types of proof**

- **直接证明（Direct Proof）**：通过逻辑推理直接从假设得出结论。
- **间接证明（Indirect Proof）**：又称反证法，假设结论为假，推导出矛盾，从而得出结论为真。
- **归纳证明（Inductive Proof）**：通过数学归纳法，首先证明基础情况（通常是最小值），然后证明如果对某个数成立，则对下一个数也成立。



### Disproof by **Counterexample**

Disprove an assertion by finding one example where it is false

>Assertion: “It rains every day in Seattle.”
>
> Find one day where it did not rain in Seattle
>
> Therefore, the assertion must be False

1. **Write the statement**  Assertion: If x and y are real numbers then **xy** **> 0**
2. **Describe your proof**  Disproof by counterexample
3. **Provide counterexample**  Suppose x = 3 and y = -2. Then xy = -6 < 0
4. **Conclude**  Therefore the assertion is False





### **Direct proof**

Frequently the most obvious way to write a proof. Usually for proofs of the form “premise Þ conclusion”

Start by assuming (supposing) the premise is true. Derive the conclusion from the premise by equivalence or by implication

>“If n is an odd integer, then n2 is odd”
>
>Suppose n is an odd integer
>
>There must be some integer k such that n = 2k+1 *by definition of odd integers*
>
>So n2 = (2k+1)2 = 4k2 + 4k + 1 *by algebra*
>
>Let j = 2k2 + 2k. Then n2 = 2j + 1 *by algebra*
>
>Therefore n2 is odd *by definition of odd integers*

通过逻辑推理一步步地从假设推导出结论。直接证明通常包含以下步骤：

**Write the statement Assertion:** “The sum of two odd integers is even”

**Suppose the premise** Suppose x and y are both odd integers

**Derive the conclusion** For some j and k, x=2j+1 and y = 2k+1

> **justifying each step** by the definition of odd integers
>
> The sum x+y = 2j+1+2k+1 = 2j+2k+2 = 2(j+k+1) by algebra
>
> 2(j+k+1) is even  by the definition of even integers

**Conclude** Therefore the sum of two odd integers is even



#### Tautology重言式

a statement that is true.

> 当一个命题的逻辑形式在所有可能的情况下都为真时，我们称它为重言式。

When the assertion allows you to derive True, you have a Tautology

当一个命题经过推导或转换后能够导出**True**，我们称该命题为重言式。即，不管其前提或组成部分如何，结果始终为真。

> It can be derived by transforming an assertion to True
>
> 我们可以通过逻辑等价变换，将某个命题转换为一个总为真的命题，从而确定其为重言式。
>
> 通过逻辑推理或真值表，也可以验证某一命题是否是重言式。如果在真值表的每一行都为真，那么这个命题就是重言式。



#### 证明过程

在正式的数学证明中，您需要有一个结构化的过程。通常包括以下几个部分：

- **引入相关定义**：为使论证清晰，您可能需要定义一些关键术语。
- **列出假设**：在证明开始时，明确列出所有已知的条件和假设。
- **推导结论**：逐步推理，使用数学逻辑和已知的定理，最终到达所要证明的结论。



### Proof by **Contradiction**

通过假设命题的结论不成立（即假设它的反面为真），并推导出矛盾，从而证明最初的命题是正确的。

First, assume the premise is True

Now, assume the conclusion is False and show it is impossible

> You do this by deriving a contradiction of the premise, i.e. that the premise is False
>
> This shows that the conclusion cannot be False

Therefore, the conclusion is True

Therefore, if the premise is True, then the conclusion must also be True



#### 基本步骤

1. **假设命题的反面为真：** 假设你要证明的命题为 P，则你首先假设 P 为假，也就是说假设 ¬P\neg P¬P 为真。
2. **推导出矛盾：** 根据这个假设（即 ¬P\neg P¬P），使用已知的事实、定理或逻辑推理来进行推导，直到出现一个明显的矛盾。这个矛盾可以是逻辑上的不可能事件（如 AAA 和 ¬A\neg A¬A 同时为真），或与已知事实冲突的结论。
3. **得出结论：** 因为假设 ¬P\neg P¬P 导致了矛盾，所以这个假设必定是错误的。因此，可以得出 PPP 为真，也就是最初想要证明的命题成立。

*State assertion* **Assert: If 3n+2 is odd, then n is odd**

*Assume premise* **Suppose 3n+2 is odd**

*Negate conclusion* **Suppose n is even**

*Derive contradiction* **Then 3n is even and 3n+2 is also even**

> **This contradicts the premise**
>
> **Therefore, it cannot be true**

*State conclusion* **Therefore n must be even**

> **Therefore, if 3n+2 is odd, then n is odd**





### Proof by **Contrapositive**

通过证明命题的 **逆否命题** 来证明原命题，因为一个命题和它的逆否命题是等价的。

You can prove “premise Þ conclusion”. Assume conclusion is false, and show that the premise must be false

**命题的形式**：如果 P，那么 Q。

- 原命题的形式是： P→Q。

**命题的逆命题**：如果 Q 不成立，那么 P 也不成立。

- 逆命题的形式是： ¬Q→¬P。



### Proof of Equivalence

p ⟺ q means “p **equals** q” or “p **if and only if** q” or “p **iff** q”

双条件命题也可以表示为“**当且仅当**”或“**p等价于q**”。

#### 证明 p  ⟹  q 和 ¬p  ⟹  ¬q

基于**对称性**来进行证明。

通过证明 p 导致 q 并且 ¬p 导致 ¬q，我们可以表明 p⟺q 的正确性。

>思路是：如果一个命题为真，那么它的否命题也应该在对称情况下保持一致。
>
>1. **证明 p⟹q**：先证明如果 p 为真，那么 q 必然为真。
>2. **证明 ¬p⟹¬q**：再证明如果 p 为假，那么 q 也必然为假。
>
>如果这两步都能证明，则 p  ⟺  q 成立。

#### 证明 p⟹q 和 q⟹p

更直接的双向证明方法。

通过证明 p 导致 q，并且 q 导致 p，我们可以确认 p⟺q 成立

> 思路是，p 和 q 彼此蕴含对方。
>
> **证明 p⟹q**：证明如果 p 为真，那么 q 必然为真。
>
> **证明 q⟹p**：再证明如果 q 为真，那么 p 也必然为真。
>
> 如果这两步都能证明，则 p⟺q 成立。

**第一种方法**适合那些否定式命题较为简单或者容易推导的情况下，因为你可以通过证明 ¬p 和 ¬q 之间的关系来得到对称性。

**第二种方法**通常更直观，因为只需要分别证明正向和逆向的蕴含即可。





### Proof By Cases

Sometimes there are a small number of different cases. But we know that one of these cases must be true. Then if we can prove the assertion for each of the cases, we have a complete proof. So list the cases and make a proof for each case

在面对一个复杂命题时，可以将问题拆解为多个互斥的子情况（cases），每个子情况都能涵盖所有可能性。通过逐个证明这些子情况中的命题为真，我们就能证明整个命题的正确性。

#### 证明步骤

1. **列出所有可能的情况**：首先，确定你需要处理的所有子情况。确保这些情况是**互斥**的，并且**穷尽**了所有可能性。
2. **分别证明每种情况**：对于每个子情况，单独证明命题在该情况成立。
3. **总结**：如果每个子情况的证明都成立，那么整个命题在所有情况下都成立，完成证明



#### When To Use It?

当命题比较复杂，无法直接通过一步推导来证明整个命题，这时可以考虑将问题分解为多个容易处理的小情况进行分析。

如果涉及到的情况是有限的、简单的，并且可以逐一处理，那证明工作就相对容易。

- **列举有限的情况**：例如，只有几个可能的值，或者有限的情境。例如，真或假、正或负、偶数或奇数等，这些二分法很常见。
- **前提中包含简单的 OR、XOR、或 EQUALS 关系**：如果前提中涉及到简单的逻辑运算，比如 P∨Q 或 P⊕Q，我们可以对每个子情况分别进行处理。









## 逻辑 expressing

### 连接词

在证明中，使用逻辑连接词可以帮助清晰地表达推理过程。例如：

- **如果...那么...（If... then...）**：用于表示条件关系。
- **且（And）**：用于连接两个同时成立的条件。
- **或（Or）**：用于连接至少一个条件成立的情况。
- **非（Not）**：用于表示否定。

### 结构

通常包括：

- **引言**：简要介绍要证明的命题。
- **假设**：明确列出所有已知的条件。
- **推导过程**：逐步推理，使用逻辑和定义。
- **结论**：清晰地总结证明的结果。

### 技巧

- **使用定义**：在推导过程中，始终参考相关的数学定义，这有助于确保您的推理是正确的。
- **实例**：在必要时使用具体的例子来说明您的推理。
- **对称性和反转性**：在处理集合、数列或其他数学对象时，考虑它们的对称性或反转性可能会提供额外的见解。

### Habits

- using we than I: 正式的数学证明中，通常用“我们”来强调集体的思维过程，表明这是一个普遍适用的推理，而不仅仅是个人的观点。这种用法使得证明更加客观和严谨。
- Ending with little bos and a x in it or Q.E.D: 证明的最后，通常会用某种符号或短语来表示证明结束。





## **Pigeonhole Principle**

### 鸽巢原理

如果有 n 只鸽子要放进 m 个鸽巢，并且 n>m，那么至少有一个鸽巢中会有至少两只鸽子。

#### Proof by Contradiction

**假设：** 有 n 只鸽子放入 m 个鸽巢中，且 n>m。假设每个鸽巢中至多只有一只鸽子。

**推论：** 如果每个鸽巢中至多只有一只鸽子，那么最多只能放入 m 只鸽子。

**推导过程：**

1. **假设每个鸽巢中至多有一只鸽子：**
   - 每个鸽巢容纳 0 或 1 只鸽子。如果所有 m 个鸽巢都至少有 1 只鸽子，那么总共可以容纳的鸽子数最多为 m 只。
2. **与已知条件对比：**已知有 n>m 只鸽子。意味着有 n 只鸽子需要放入 m 个鸽巢。
3. **得出矛盾：**根据假设，每个鸽巢最多容纳 1 只鸽子，总共最多只能容纳 m 只鸽子。
   - 但实际需要容纳的是 n>m 只鸽子。
   - 这导致矛盾，因为 n>mn > mn>m 表明有更多鸽子需要放入鸽巢，而每个鸽巢最多只能放一只。
4. **结论：**
   - 假设每个鸽巢中至多只有一只鸽子是不成立的。
   - 因此，至少有一个鸽巢中必须有至少两只鸽子。

**因此，基本鸽巢原理得证。**



### 一般鸽巢原理（General Pigeonhole Principle）

如果有 n 只鸽子要放进 m 个鸽巢，并且 n>k×m，那么至少有一个鸽巢中会有至少 k+1 只鸽子。其中，k 是一个非负整数。

#### 证明

**假设：** 有 n 只鸽子放入 m 个鸽巢中，且 n>k×m。假设每个鸽巢中至多只有 k 只鸽子。

**推论：** 如果每个鸽巢中至多只有 k 只鸽子，那么最多只能放入 k×m 只鸽子。

**推导过程：**

1. **假设每个鸽巢中至多有 k 只鸽子：**
   - 每个鸽巢容纳 0 到 k 只鸽子。
   - 如果所有 m 个鸽巢都至多有 k 只鸽子，那么总共可以容纳的鸽子数最多为 k×m 只。
2. **与已知条件对比：**
   - 已知有 n>k×m 只鸽子。
   - 这意味着有 n 只鸽子需要放入 m 个鸽巢。
3. **得出矛盾：**
   - 根据假设，每个鸽巢最多容纳 k 只鸽子，总共最多只能容纳 k×m 只鸽子。
   - 但实际需要容纳的是 n>k×m 只鸽子。
   - 这导致矛盾，因为 n>k×m 表明有更多鸽子需要放入鸽巢，而每个鸽巢最多只能放 k 只。
4. **结论：**
   - 假设每个鸽巢中至多只有 k 只鸽子是不成立的。
   - 因此，至少有一个鸽巢中必须有至少 k+1 只鸽子。



# **Permutations and Combinations**

- Determine when order matters

- Determine when repetitions are allowed 

- Count combinations

- Count orderings


|                          | **Without Replacement**                                      | **With Replacement**                                         |
| ------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Order Matters**        | **Permutations**  Select k things from a set of n  **P(n,k)  = n! / (n-k)!** | **Permutations With Repetition**  Select from n groups k times  (independently)  **n****k |
| **Order Doesn’t Matter** | **Choosing** /  Combinations  Choose k things from a set of n  **C(****n,k****)  = n! / k! (n-k)!**  **(****■(****n@k))** | **Choosing With Repetition**  Distribute k objects into n groups  Same as choosing a group k times  There are n-1 “separators” between  groups  Balls (k) in Bins (n)  Stars (k) and Bars (n-1)  **C(k+n-1, k) = (n+k-1)! / k!  (n-1)!** |

## Permutations

Counting Choice When Order Matters, No Repetitions

将一组对象按特定顺序进行排列的方式。

- **n-permutation**: A permutation of *n* distinct objects.
- **r-permutation**: A permutation of *r* objects selected from a set of *n* distinct objects.



### Concepts

**阶乘 (Factorial, n!)**：所有正整数从 1 到 *n* 的乘积。它在计算排列和组合中起到基础作用。

**组合 (Combination, n 选 r)**：从 *n* 个对象中不考虑顺序地选择 *r* 个对象。

**二项式系数 (Binomial Coefficient)**：表示组合，记作
$$
(_r^n)
$$
**置换群 (Permutation Group)**：在抽象代数学中，所有集合排列组成的群，群的运算是排列的复合。

**循环排列 (Circular Permutations)**：顺序是环形的排列，旋转视为相同。

- *n* 个不同对象的循环排列数量：(n−1)!
- **例子**：围坐在圆桌周围的人数排列。





### Formula

The number of **permutations** of *n* distinct objects is given by:

P(n)=n!   Where: n! (n factorial) = n×(n−1)×(n−2)×⋯×1

For **r-permutations** (arrangements of *r* objects from *n*), the formula is:
$$
P(n, r) = \frac{n!}{(n-r)!} = _nP_k
$$


### With Repetitions

When objects can be repeated, the number of permutations changes.

The number of **r-permutations with repetition** from *n* distinct objects is: 
$$
n^r
$$

> 使用数字 0-9（允许重复）组成 3 位数密码的数量：
> $$
> 10^3 = 1000
> $$



### **Multisets**

When the set contains repeated elements, the number of distinct permutations is reduced.

对于一个包含 n 个元素的多重集，其中有 n1 个元素是同一种类，n2 个是另一种类，依此类推，直到 nk 个元素是第 k 种类的元素。那么，这个多重集的不同排列数目 P 由以下公式给出：
$$
\frac{n!}{n_1! * n_2! * n_3! * ... * n_k!}\\
\text{ }\\
n = 对象总数\\
n_1, n_2, n_3, ... , n_k = 每种类型的不可区分对象的数量
$$
当集合中有重复元素时，直接使用 n! 会多计一些排列，因为交换相同元素的位置不会产生新的排列。因此，需要将这些重复情况的排列数除去。

假设有 n1 个相同的元素，这些元素之间可以互相交换，而不改变整体排列。因此，这些重复的排列数是 n1!。同理，对于 n2, n3,…,nk 个相同元素，也需要分别除以它们的阶乘。

>单词 "BALLOON" 的不同排列数量：
>
>总字母数：7
>
>B:1, A:1, L:2, O:2, N:1
>$$
>\frac{7!}{1! * 1! * 2! * 2! * 1!} = \frac{5040}{4} = 1260
>$$

















## Combinations

Counting Choice When Order Doesn’t Matter, No Repetitions

**组合 (Combination)**：从一个集合中选择若干个元素，且不考虑选择的顺序。

**n 选 r (Combination of n choose r)**：从 *n* 个不同对象中选择 *r* 个对象的所有可能方式。



### Formula

选择 *r* 个对象从 *n* 个不同对象的组合数由以下公式给出：
$$
C(n, r) = (_r^n) = \frac{n!}{(n-r)!r!}\\
\text{ }\\
n! （n 的阶乘）= n×(n−1)×(n−2)×⋯×1\\
(_r^n) \text{ is read as "n choose r}
$$




### Characteristics

顺序无关: 选择项目的顺序不影响组合的唯一性。

对称性: 选择 *r* 个元素与选择剩余的 n−r 个元素的组合数相同。

递推公式: C(n,r) = C(n−1,r−1) + C(n−1,r) 组合数的基本递推关系，基于是否选择第一个元素。

> **组合恒等式**：如 Pascal 三角形中的递推关系 C(n,r)=C(n−1,r−1)+C(n−1,r)

边界条件: 当 r=0 或 r=n 时，C(n,r)=1; 当 r>n 时，C(n,r)=0





### With Repetitions

从一个更大的集合中选择若干项，其中不考虑选择的顺序，并且每个项目可以被多次选择。

组合数由以下公式给出：
$$
C_{rep}(n, r) = (_{r}^{n+r-1}) = \frac{(n+r-1)!}{r! * (n-1)!}\\
\text{ }\\
n = 不同项目的数量。\\
r = 要选择的项目数量。\\
(_{r}^{n+r-1}) \text{表示“n + r - 1 选 r”}
$$


#### Multisets

允许元素多次出现的集合。带重复的组合通常在多重集的上下文中考虑。

在带重复的组合中，我们实际上是在从多重集中选择元素。



#### **Stars and Bars Theorem**

一个视觉化的方法来理解带重复的组合

- **星 ( * )** 代表要选择的项目。
- **条 ( | )** 代表不同类型项目之间的分隔符。

##### 推导步骤

假设我们有 n 种不同的元素，想要选择 r 个元素，允许重复选择同一个元素。我们需要计算有多少种不同的选择方式。

- 用 r 个星（*）表示要选择的 r 个元素。
- 用 n−1 个条（|）将 n 种不同的元素分隔开。例如，对于 3 种元素 A, B, C，可以用 **|** 将它们分隔为 A | B | C。

通过排列 r 个星和 n−1 个条，我们可以得到所有可能的带重复组合。
$$
C_{rep}(n, r) = (_{r}^{n+r-1}) = \frac{(n+r-1)!}{r! * (n-1)!}\\
$$

##### Example

例如，从 2 种类型（A 和 B）中选择 3 个项目：

- ∗∗∗∣ 表示 3 个 A 和 0 个 B。
- ∗∣∗∗ 表示 1 个 A 和 2 个 B。

总符号数为 r+n−1（星加条），排列这些符号的方式数即为带重复的组合数。

```
将 5 个相同的糖果分给 2 个孩子，有多少种分配方式？
n=2（孩子）
r=5（糖果）
*****| （5 个糖果给孩子 1，0 给孩子 2）
****|* （4 给孩子 1，1 给孩子 2）
***|** （3 给孩子 1，2 给孩子 2）
**|*** （2 给孩子 1，3 给孩子 2）
*|**** （1 给孩子 1，4 给孩子 2）
|***** （0 给孩子 1，5 给孩子 2）
```



## Binomial Coefficients

fundamental components in combinatorics, algebra, and probability theory.









### Pascal’s Triangle





# **Probability**

某事件发生的可能性



## Concepts



### Experiments/Observations/trial

A situation whose future or truth we do not know 

> a situation with one or more possible outcomes

在控制条件下进行的观察或测量过程，以获得数据或信息。

> 实验通常用于研究某些现象或测试假设。

实验可以是随机的，即其结果受到随机因素的影响。

The result of the trial must either be A or ~A

### outcome

Each possible result of the experiment 

### Events

A significant set of outcomes 

something that might happen

在实验或观察中可能发生的结果的集合。

每个事件可以由一个或多个结果组成。事件可以是简单的（单个结果）或复合的（多个结果）。

### Sample Space

The set of all possible outcomes 

所有可能结果的集合，通常用字母 S 表示。

在概率论中，实验的结果构成样本空间。

### Probabilities

a real number in the range of [0, 1]

某事件发生的可能性，通常用 P(A) 表示，其中 A 是事件。概率的值范围在 0 到 1 之间：

- P(A) = 0 表示事件 A 不会发生。
- P(A) = 1 表示事件 A 必定发生。

> write the probability of an event **Pr(event)**

The probability of A is defined as:  **lim┬(N→∞)⁡〖(number of times A occurs)/(N trials)〗**

> Probability is a dimensionless ratio. Even with known probability, there is uncertainty in any trial or set of trials







## Fallacies to Avoid

**Assuming Equal Likelihood of Outcomes**: We could start to go around thinking everything has a 50% chance of happening because there are “two outcomes” - either it does happen, or it doesn’t.

我们可能会开始认为所有事件都有 50% 的发生概率，因为“结果有两个”——要么发生，要么不发生。然而，这种思维方式是错误的，因为许多情况下，事件的结果并不是均等可能的。

在概率论中，仅仅计算事件的结果是不够的，特别是当结果的可能性不均等时。在这种情况下，简单地将结果视为均等可能会导致误导性的结论。

只有在所有被计数的结果均等可能的情况下，计数才能产生合理的概率。

在进行概率分析时，务必避免假设所有结果的均等可能性。了解具体情境中的可能性，并考虑相关的影响因素，可以帮助我们更准确地计算和理解概率。





## Counting: calculate simple probability



### Sampling

抽样（Sampling）

通常分为两种情况：**有放回抽样（Sampling With Replacement）**和 **无放回抽样（Sampling Without Replacement）**。

#### With Replacement

每次抽样后，抽取的对象会被放回原来的总体中。因此，每次抽样的结果是独立的。

#### Without Replacement

抽样后不会将对象放回总体，因此每次抽样的结果会影响下一次抽样的可能性。

> 因此需要逐步计算。





### **Partitions分区**

A **partition** is a set of mutually exclusive events that covers the sample space

Every outcome is in exactly one of the events

>**划分**（partition）在概率论中指的是一组互斥事件，它们的并集覆盖整个样本空间。也就是说，每个样本点（试验的结果）只能属于其中一个事件，而且这些事件的总和涵盖了所有可能的结果。
>
>假设样本空间为 SS，划分 A1,A2,...,An 是互斥事件集合的一个划分，当且仅当：
>
>1. **互斥性**：对于所有 i≠j，Ai∩Aj=∅，即任何两个事件不可能同时发生。
>2. **覆盖样本空间**：所有事件的并集是整个样本空间，即 A1∪A2∪...∪An=S。
>3. **每个结果仅属于一个事件**：每个样本空间中的元素只属于一个事件。

A1, A2, …, An form a partition if (Ai and Aj = None) and A1orA2or… orAn = S



### **Discrete Sample Space**

In a discrete sample space, there is a finite set of outcomes {si}, where Us_i = S

**离散样本空间**（Discrete Sample Space）是指包含有限或可数多个可能结果的样本空间。在概率论中，样本空间是所有可能结果的集合，而如果这些结果是**离散的**，则称为离散样本空间。

> Notice that these outcomes are mutually exclusive, so {si} is a partition

1. **有限或可数**：样本空间中的元素是有限的，或可以通过枚举来列出。例如，掷硬币的结果是离散的（正面或反面），投骰子的结果也是离散的（1 到 6）。
2. **每个结果独立且可区分**：离散样本空间中的每个结果都是相互独立且互不重叠的。这意味着每个结果都可以单独确定且没有模糊性。

在离散样本空间中，每个结果 sisi 的概率 P(si) 满足以下条件：

1. 每个结果的概率都是非负的： P(si)≥0
2. 所有结果的概率之和为1： ∑P(si)=1

•Let A be an event consisting of a set of outcomes {s1, s2, …, sk}. Then Pr(A) = p1 + p2 + … + pk



### Counting Probabilities

In a discrete sample space, if all outcomes are equally likely, we can count outcomes to determine the probability of an event:

Probability of A = `(the number of outcomes in A)/(the total number of outcomes in S)` = `|A|/|S|` 



### **Axioms of Probability**

Kolmogorov Axioms of Probability

**An Axiom** or Postulate is defined as a statement that is accepted as true and correct.

> An **Axiom** presents itself as self-evident, on which you can base any arguments or inference. These are universally accepted as a general truth. 

- 公理 1：有效概率在区间 [0, 1] 之间
- 公理 2：所有互斥事件的概率和为 1
- 公理 3：互斥事件的概率相加: P(A∪B)=P(A)+P(B). 如果事件 A 和 B 不是互斥的（即有交集），则需要调整公式为：P(A∪B)=P(A)+P(B)−P(A∩B)

#### Non-Negativity Axiom

对于任何事件 A，它的概率 P(A) 都是非负数：P(A)≥0

> 意味着任何事件发生的概率不能为负数。概率总是一个大于或等于 0 的数。

#### Total Probability Axiom

在样本空间 S 中，样本空间包含了所有可能的结果，因此样本空间 S 的概率总和等于 1：P(S)=1

> 意味着某些事情一定会发生（即事件发生在样本空间内）。

#### Additivity Axiom

对于两个互斥事件 A 和 B（即 A∩B=∅，两者不会同时发生），它们的联合事件的概率等于它们各自概率的和：P(A∪B)=P(A)+P(B) 如果 A∩B=∅

> 意味着，如果两个事件是互斥的，它们同时发生的概率为 0，那么它们发生的联合概率等于每个事件发生概率的简单相加。

If A1, A2, … An are pairwise **disjoint** events ∀_i ∀_j (Ai Ç Aj = f), then the probability of their union is the sum of their probabilities: `Pr (A1 or A2 or … or An) = Pr(A1) + Pr(A2) + … + Pr(An)`



#### Some consequences:

- P(f) = 0
- If A is a subset of B, then Pr(A) £ Pr(B)
- Some notation: `A union B means “A or B”`;  `A intersection B means “A and B”`



### **Calculus of Probabilities**

- Pr(A or B) = Pr(A) + Pr(B) – Pr(A and B)
- Pr(A) + Pr(~A) = 1
- Pr(A) = Pr(A and B) + Pr(A and ~B) [Law of Total Probability]

>The prob. that you’re sickis the sum of the prob. 
>
>that you are sick and test positive,
>
>and the prob. that you are sick and test negative



## Independence and Conditional Probability

分析事件之间的关系，尤其是当事件的发生是否相互影响时。

### **Exclusive & Independent Events**

- Events are called **exclusive** if they cannot occur together: Pr(A and B) = 0
- Events are called **independent** if their probabilities are the same, regardless of whether the other event occurs: Pr(A and B) = Pr(A) x Pr(B)

> Notice that **exclusive events are not independent !!!!**
>
> **互斥事件**是指两个事件不能同时发生。如果一个事件发生了，另一个事件就不可能发生。例如，在掷骰子时，事件“掷出1”和“掷出2”是互斥的，因为在一次掷骰中不可能同时掷出1和2。
>
> **独立事件**是指两个事件的发生与否相互没有影响。也就是说，一个事件的发生不会改变另一个事件发生的概率。例如，连续两次掷骰子的结果是独立的，因为第一次的结果不会影响第二次的结果。
>
> **为什么互斥事件不是独立的？**
>
> 因为如果两个事件是互斥的（不能同时发生），那么其中一个事件发生意味着另一个事件一定不会发生，因此它们的发生之间存在依赖关系。





### **Law of Total Probability**

P(B)=P(B∣A)⋅P(A)+P(B∣not A)⋅P(not A)

计算一个事件的概率，该事件可以通过多个互斥事件的组合来实现。

> 将一个复杂的事件拆解为更简单的、已知概率的事件。

设 A 是我们感兴趣的事件，B1,B2,…,Bn 是一组互斥且完备的事件（即至少有一个事件发生），那么全概率公式可以表示为：

P(A)=P(A∣B1)P(B1)+P(A∣B2)P(B2)+…+P(A∣Bn)P(Bn)

- P(A∣Bi) 是在事件 Bi 发生的条件下事件 A 发生的概率。
- P(Bi) 是事件 Bi 的概率。
- 所有的 Bi 事件必须是互斥的，并且其概率的和为 1（即 P(B1)+P(B2)+…+P(Bn)=1P(B1)+P(B2)+…+P(Bn)=1）。





### Independence & joint probabilities

两个事件之间的关系，其中一个事件的发生与否**不会影响**另一个事件发生的概率。

事件 A 和事件 B 是独立的，当且仅当：P(A∩B)=P(A)×P(B)

> 意味着，如果事件 A 和事件 B 互相独立，那么它们的联合概率等于各自概率的乘积。



### Conditional Probability

在已知某个事件 B 已经发生的前提下，另一个事件 A 发生的概率。

The conditional probability is the fraction of the probabilities for B that also include

It is defined this way:
$$
P(A|B) = \frac{P(A \cap  B)}{P(B)}, \text{  }P(B)>0
$$

> 给定事件 B 已经发生的条件下，计算事件 A 同时发生的概率。
>
> **注意，**条件概率要求 P(B)>0，即事件 B 必须是有可能发生的。

#### 独立性与条件概率

当两个事件 A 和 B 是独立的，条件概率 P(A∣B) 其实和 P(A) 相同，因为 A 和 B 互相不影响。

在独立事件的情况下，有：P(A∣B)=P(A)

#### 条件概率与非独立事件

如果事件 A 和 B 不是独立的，那么条件概率就反映了事件 B 对事件 A 的影响。

> 通常我们会通过条件概率公式来计算某个事件在已知另一个事件发生后的调整后的概率。







## **Bayes' Theorem**

>•The definition of conditional probability is:
>
>   Pr(A|B) = Pr(A and B) / Pr(B)
>
>•We can rewrite this as:   Pr(A and B) = Pr(A|B) x Pr(B)
>
>•Therefore   Pr(A and B) = Pr(A|B) x Pr(B) = Pr(B|A) x Pr(A)
>
>•Now we have Bayes’ Theorem:  Pr(A|B) = Pr(B|A) x Pr(A) / Pr(B)
>
>•Bayes’ theorem allows us to get Pr(A|B) if we already know Pr(B|A)

计算给定某个条件下的事件发生的概率

> 帮助我们根据新证据 B 来调整对某事件 A 的概率估计。提供了一种从先验知识到后验知识的更新过程。

$$
P(A|B) = \frac{P(B|A) * P(A)}{P(B)}, \text{ }P(B)>0\\
\text{}\
P(A∣B) : 在已知事件 B 发生的条件下，事件 A 发生的后验概率（\text{posterior probability}）。\\
P(B∣A) : 在已知事件 A 发生的条件下，事件 B 发生的似然函数（likelihood）。\\
P(A) : 事件 A 发生的先验概率（\text{prior probability}），即在没有考虑事件 B 时，事件 A 的概率。\\
P(B) : 事件 B 发生的边际概率（\text{marginal probability}），即事件 B 不依赖于 A 是否发生的概率。
$$

- **先验概率** P(A)：我们对事件 A 在没有任何额外信息时的最初估计。
- **似然函数** P(B∣A)：在事件 A 已经发生的条件下，事件 B 的可能性。
- **边际概率** P(B)：事件 B 发生的总体概率。
- **后验概率** P(A∣B)：在事件 B 发生后，更新了我们对事件 A 的概率估计。

#### prior probability

•If {Ai} is a partition, then for any event B:

Pr(B) = Pr(A1ÇB) + Pr(A2 ÇB) + … + Pr(AnÇB)

•And we have: Pr(AiÇB) = Pr(B|Ai) x Pr(Ai)

•So:

Pr(B) = Pr(B | A1) x Pr(A1)

​     \+ Pr(B | A2) x Pr(A2)

​     \+ …

​     \+ Pr(B | An) x Pr(An)

#### marginal probability

•We saw this before: Pr(B) = Pr(A and B) + Pr(~A and B)

•Now we also know: Pr(A and B) = Pr(B|A) x Pr(A)

•So if we put these together:

 Pr(B) = Pr(B|A) x Pr(A) + Pr(B|~A) x Pr(~A)





### Used For Evaluating Evidence

![Bayes](./6.CS 5002/Module 7/Bayes.png)

When we apply Bayes' rule, the numbers we calculate **tell us which hypothesis is most likely**, but they are not the true probabilities. 

To get the actual probabilities, we will need to divide each quantity by Pr(evidence). Recall that the probability of the evidence can be computed as:
$$
Pr(evidence) =  Pr(evidence \wedge hypothesis1) +  Pr(evidence \wedge hypothesis2) + ...  + Pr(evidence \wedge hypothesisN)
$$
Which, by definition, is
$$
Pr(evidence) = Pr(evidence | hypothesis1)Pr(hypothesis1) +  Pr(evidence | hypothesis2)Pr(hypothesis2) + ... Pr(evidence | hypothesisN)Pr(hypothesisN)
$$
Thus, to get the true probabilities we will need to divide each of our results by the sum of the results. However, this step is unnecessary for deciding which of the hypotheses is most likely because they will still have the same rank ordering. To see this clearly, let’s look at the following example that shows how to calculate exact probabilities:

I just rolled a die that was drawn at random from a bag containing an **equal** number of 6-sided dice (numbered 1-6) and 20-sided dice (numbered 1-20). I tell you the die roll is a 6. What is the probability of each hypothesis in light of the evidence (6-sided vs 20-sided)?

We don’t need to know the exact number of dice of either type because I told you we have an equal number. This means we can represent the prior for both 6-sided and 20-sided as ½. This gives us:



### Bayes’ Rule For Partitions

•We have Bayes’ Rule: Pr(A|B) = Pr(B|A) x Pr(A) / Pr(B)

•And the Law of Total Probability: Pr(B) = Pr(B|A1) x Pr(A1) + Pr(B|A2) x Pr(A2) + … + Pr(B|An) x Pr(An)

•Putting these together: Pr(Ai|B) = 

Pr(B|Ai) x Pr(Ai) / 

Pr(B|A1) x Pr(A1) + Pr(B|A2) x Pr(A2) + … + Pr(B|An) x Pr(An)





## Probability function

概率论中，**概率函数**（Probability Function）描述的是随机变量取不同值的可能性。

对于离散随机变量，常用**概率质量函数（PMF）**来表示随机变量取特定值的概率；

对于连续随机变量，使用的是**概率密度函数（PDF）**。

> 我们通常感兴趣的是计算与该随机变量相关的期望值（Expectation）和方差（Variance）。



### Expectation: expected value of a probability function

**期望值**（Expected Value），也称作**均值**，是随机变量可能取值的加权平均值。

它是概率分布的一个重要特征，表示从长远来看，随机变量的平均值会趋向于某个特定值。

**离散随机变量的期望值**：如果随机变量 X 的值为 x1,x2,...,xn，并且其对应的概率为 P(X=x1),P(X=x2),...,P(X=xn)，则期望值 E(X)定义为: `E(X)=∑i=1 nxi⋅P(X=xi)`

> 即每个取值乘以它发生的概率，并求和。

**连续随机变量的期望值**：如果随机变量 XX 的概率密度函数为 f(x)f(x)，则期望值 E(X)E(X) 定义为：

`E(X)=∫−∞~∞x⋅f(x) dx`



### variance of a distribution

**方差**（Variance）表示随机变量的取值偏离其期望值的程度，衡量数据的离散程度。它反映了结果的波动性。

**离散随机变量的方差**：随机变量 X 的方差 Var(X) 是其与期望值之差的平方的期望值。



### Standard Deviation

**标准差**（Standard Deviation）是方差的平方根，常用来衡量数据的波动性。它与方差有相同的量纲，通常用来比较不同数据集的离散程度。





## **Random Variables**

- Calculate the expected value of a probability function
- Calculate the variance of a distribution

**Here are the three "big ideas" for this module.**

- The expected value of a probability function
- How expected value is linear 期望值如何呈线性
- The variance of a probability distribution, which is the square of the "standard deviation". 



### Random Variables

the outcomes of a random experiment in a numerical format

#### Definition

A random variable (often denoted as X, Y, etc.) is a function that assigns a numerical value to each outcome of a random experiment.

> if you roll a die, a random variable XX could represent the outcome of the roll (1 through 6).

#### Types

- **Discrete Random Variables**: Take on a finite or countable number of possible values. 
- **Continuous Random Variables**: Take on an infinite number of possible values within a range.



##### Independent Random Variables

- X and Y are **independent** if for all x and y, Pr(X=x and Y=y) = Pr(X=x) Pr(Y=y)

 

#### Probability Distribution

For each random variable, we can define a probability distribution that tells us the likelihood of each possible value.

- For **discrete random variables**, this is represented as a **probability mass function (PMF)**, which assigns probabilities to individual outcomes.
- For **continuous random variables**, this is represented as a **probability density function (PDF)**, which describes the relative likelihood of values within a continuous range.

#### Independent Random Variables

Two random variables XX and YY are independent if knowing the value of one does not change the probability distribution of the other.

#### Conditional Expectation

Sometimes, we want to know the expectation of a variable given that we know something else (like a condition or event). This is useful in situations where we have partial information.



### Expected Value: Expectation (Mean)

https://brilliant.org/wiki/expected-value/

The **expected value** (or mean) of a random variable gives the average outcome if an experiment is repeated many times.

E(X)=∑x⋅P(X=x)(for discrete variables)

E(X)=∫x⋅f(x) dx(for continuous variables)



#### 线性性

期望值的总和等于每个期望值的相加。这表示多个独立随机变量的期望值总和等于各个期望值相加。

https://brilliant.org/wiki/linearity-of-expectation/

##### 证明

线性期望的证明本质上依赖于期望值的分布性质。线性期望的核心在于期望值的加法性，即**总期望等于各部分期望值的和**。

对于两个随机变量 X 和 Y，我们可以写出它们的和的期望值：**E(X+Y)=E(X)+E(Y)**. 利用分配律，我们可以将整个表达式重写，以便逐项计算。无论各自值如何变动，它们的期望值相加可以得到总的期望。



##### 线性期望在计算机科学中的应用

在许多算法中，不同步骤可能包含随机性。根据线性期望，总的执行时间等于每个步骤的时间相加。这意味着，我们可以将算法的分析简化为各个步骤的时间期望分析。



#### Rules

- For constant a, a can be considered a random variable with value a: E(a) = a
- E(a + bX) = a + bE(X)
- E(X + Y) = E(X) + E(Y)

##### Linearity of Expectation

- E(aX + bY) = aE(X) + bE(Y)

  - This is called Linearity of Expectation

  > Note there is no assumption above that X and Y must be independent

##### independent Random Variables

If X and Y are independent, then E(XY) = E(X)E(Y)

- In fact, if X and Y are independent, then you can apply any functions g and h to them: `E[g(X) h(Y)] = E[g(X)] E[h(Y)]`

> Note that in general E(1/X) ≠ 1/E(X)

#### Conditional Expectation

E(X|A) of X given event A is: `E(X|A) = sum over all x of  x Pr(X=x | A)`

##### Rules

- Linearity applies: E(bX+cY | A) = bE(X|A) + cE(Y|A)
- Law of Total Expectation: If {Ai} is a partition of S, then `E(X) = E(X|A1)Pr(A1) + E(X|A2)Pr(A2) + … + E(X|An)Pr(An)`







### Variance

https://brilliant.org/wiki/variance-definition/

The **variance** of a random variable describes how much the values vary around the mean: 

Var(X) = E[(X−E(X))^2]

> Variance helps measure the spread or “dispersion” of the random variable’s possible values.

- **方差**衡量随机变量的结果在平均值周围的分散程度。方差越大，分布越分散，表示结果变化幅度越大。

#### 证明

Var(X) = E(X^2) − (E(X))^2

方差可以通过随机变量的平方的期望和期望的平方之差来计算。

#### Properties

- Var[a] = 0
- Var[aX+b] = a^2 Var(X)

If { X1, X2, …, Xn } are pairwise independent random variables, then

1. Var(X1 + X2 + … + Xn) = Var(X1) + Var(X2) + … + Var(Xn)
2. Var(a1X1 + a2X2 + … + anXn) = a1^2Var(X1) + a2^2Var(X2) + … + an^2Var(Xn)



### Standard Deviation

- The **standard deviation** σ_X =  `√Var(X)`
  - This is the Greek letter sigma

方差的平方根称为**标准差**，表示平均偏离的量级。例如，方差为9时，标准差为3，方便对数据进行直观理解。

> Most values will be within ±1σ of E(X)

























### Covariance

协方差（Covariance）用于衡量两个随机变量之间的关系。

> 理解当一个变量变化时，另一个变量是否有类似的变化趋势。

#### 定义

设有两个随机变量 X 和 Y，它们的协方差记为 Cov(X,Y)，定义如下：

Cov(X,Y) = E{ [X – E(X)] E[Y – E(Y)] } = E[(X−E(X))(Y−E(Y))]

Alternate formula: Cov(X,Y)=E(XY)−E(X)E(Y). [X 和 Y 的乘积的期望减去各自期望的乘积]

- E(X) 和 E(Y) 分别是 X 和 Y 的期望值。
- 协方差表示 X 和 Y 在均值附近偏离方向上的共同变化。

**正协方差**：当 Cov(X,Y)>0 时，表示 XX 和 YY 通常会在相同方向上偏离其均值（例如，当 XX 增大时，YY 也倾向于增大）。

**负协方差**：当 Cov(X,Y)<0 时，表示 XX 和 YY 倾向于在相反方向上偏离其均值（例如，当 XX 增大时，YY 倾向于减小）。

**零协方差**：当 Cov(X,Y)=0Cov(X,Y)=0 时，表示 XX 和 YY 之间没有线性关系，虽然它们可能仍然有更复杂的非线性关系。

> This is zero iff X and Y are independent
>
> - Note Cov(X,X) = Var(X)

if X and Y are independent, Var(X+Y) = Var(X) + Var(Y)

For any X and Y (not necessarily independent): `Var(X + Y) = Var(X) + Var(Y) – Cov(X,Y)`



# **Sequences, Series, and Induction**

- Determine if a given series/sequence is arithmetic, quadratic, or geometric and calculate next term or sum

- Prove mathematical properties using induction

- Evaluate recurrence relations 递归




## Sequences 序列

Sequence. 一个按照特定顺序排列的数据集合。序列中的数据元素通常是有序的，可以是数字、字母或其他类型的数据。每个元素在序列中都有固定的位置（通常从第一个元素开始编号为1）。

A sequence is a function between a subset Natural numbers to a set of numbers.

按特定顺序排列的一系列数，可以是有限的或无限的。

每个数称为“项”。

### Types

- **Arithmetic Sequence** **算术序列**：元素之间的差相同。例如，2, 4, 6, 8, … 是一个等差数列，差为2。Defined by a **starting value** and the **common difference**
  $$
  a_{n+1} = a_n + d\\
  \text{ }\\
  \text{The general formula for the n-th term: }\\
  t(n) = a + (n-1) d\\
  $$

- **Geometric Sequences** **几何序列**：元素之间的比相同。例如，3, 6, 12, 24, … 是一个等比数列，公比为2。In a geometric sequence, each term is the previous term times a constant. A geometric sequence is defined by a **starting value** and a **common ratio**. 
  $$
  a_{n+1} = a_n * r\\
  \text{ }\\
  \text{n-th term is}\\
   t(n) = ar^{n-1}
  $$

  >If |r| < 1 the sequence **converges**; if |r| > 1 the sequence **diverges**
  >
  >Try computing 0.99^(100000) or 1.001^(100000)

- **二次（或平方）序列**：相邻项的**差值**会以恒定的步长变化，这通常表现为**差的差值是恒定的**。例如，序列 1,4,9,161,4,9,16 的项分别是平方数 12,22,32,4212,22,32,42，因此是一个二次序列。The second difference is a constant! 
  $$
  \text{The general form: }\\
  T(n) = an^2 + bn + c \text{ }\text{   T(n) 是第 n 项，a、b、c 是常数。}\\
  \text{ }\\
  a = \text{second difference} / 2\\
  b = t2 – t1 – 3a\\
  c = t1 – a – b 
  $$

  >Analyzing Quadratic Sequences
  >
  >It has the general form tn = an2 + bn + c
  >
  >Consider tn, tn+1, and tn+2
  >
  > an2 + bn + c; a(n+1)2 + b(n+1) + c; a(n+2)2 + b(n+2) + c
  >
  >- Subtract them to get the first differences = 2an+a+b 2an+3a+b
  >- Subtract these to get the second difference = 2a
  >
  >With further algebra:
  >
  >- second difference = t1 + t3 – 2t2 = 2a ---> a = (t1 + t3 – 2t2) / 2
  >- t2 – t1 = 3a + b  --->  b = t2 – t1 – 3a
  >- t1 = a + b + c  --->  c = t1 – a - b

  > 计算下一个项较为复杂。若知道二次序列的表达式（例如 an=n^2），可以直接求值；或者继续按二阶差来预测下一个项。
  >
  > 根据二次差值确定 a 的值：二次差值等于 2a。用已知项代入序列中的数值来解出 b 和 c。

- **字符序列**：如字符串"ABCDEF"，它是字母的有序序列。

给定序列的前几项，可以用以下方法来判断：

- **算术序列**：如果相邻项的差 d 是恒定的，那么它是一个算术序列。
- **几何序列**：如果相邻项的比 r 是恒定的，那么它是一个几何序列。
- **二次序列**：如果相邻项差的差（称为二阶差）是恒定的，那么它是一个二次序列。

### example

#### Square Numbers

 1, 4, 9, 16, 25, 36, 49, … f(n) = n2

#### Prime Numbers

 2, 3, 5, 7, 11, 13, 17, 19, … f(n) = ?

#### Triangular Numbers

 1, 3, 6, 10, 15, 21, 28, … f(n) = 1 + 2 + … + n  = n(n+1)/2

#### Fibonacci Numbers

 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, …

 f(0) = 0 f(1) = 1 f(n) = f(n-2) + f(n-1)

Any function defined on the integers can be used to define a sequence



## Series数列

是序列的项的和，通常表示为 Sn=a1+a2+a3+...+an。

When you add up the terms of a sequence, you get a series

- If it’s infinite and you add the whole thing, you have an **infinite series**
- If it’s finite or you just add up part of it, you have a **finite series** or **partial sum**

You can just put + signs in between the terms instead of commas:

 1, 2, 3, 4, 5  ---> 1 + 2 + 3 + 4 + 5

You can also use a notation called sigma notation:
$$
\sum^{n}_{i=1}𝑡_𝑖\\
\text{Read this as:  	“The sum, for i = 1 to n, of }t_i\text{ ”}\\
\text{It means: }		t_1 + t_2 + t_3 + … + t_n
$$

### Sigma Notation

$$
\sum^{n}_{i=1}𝑡_𝑖\\
\sum^{n}_{i=1}2𝑖 \text{ means }2x_1 + 2x_2 + 2x_3 + … + 2x_n\\
\sum^{n}_{i=1}(2𝑖+3) \text{ means }(2x_1+3) + (2x_2+3) + (2x_3+3) + … + (2x_n+3)\\
\sum^{∞}_{i=4}𝑡_𝑖 \text{ means } 2*4 + 2*5 + 2*6 + … … …\\
$$

#### rules

$$
\sum^{n}_{i=m}c𝑡_𝑖 = c\sum^{n}_{i=m}𝑡_𝑖  \text{: pull out a constant factor}\\
\sum^{n}_{i=m}(𝑡_𝑖 + u_i) = \sum^{n}_{i=m}𝑡_𝑖 + \sum^{n}_{i=m}u_𝑖  \text{: split up things you add}\\
$$





### Types

- **算术序列**：元素之间的差相同。例如，2, 4, 6, 8, … 是一个等差数列，差为2。
  $$
  S_n = \frac{n}{2} * (2a + (n-1)d) \text{ 其中 a 是第一项, d 是公差。}
  $$

- **几何序列**：元素之间的比相同。例如，3, 6, 12, 24, … 是一个等比数列，公比为2。
  $$
  S_n = a \frac{1-r^n}{1-r} \text{ 其中 a 是第一项, r是公比。}
  $$

  > 如果 r 的绝对值小于 1（即 −1<r<1），当 n 无限增大时，r^n 会趋近于 0. 公式简化为：
  > $$
  > S = \frac{a}{1-r}
  > $$

- **二次（或平方）序列**：相邻项的**差值**会以恒定的步长变化，这通常表现为**差的差值是恒定的**。例如，序列 1,4,9,161,4,9,16 的项分别是平方数 12,22,32,4212,22,32,42，因此是一个二次序列。
  $$
  T(n) = an^2 + bn + c \text{ }\text{   T(n) 是第 n 项，a、b、c 是常数。}
  $$
  

  > **二次序列的前 n 项和**：通常需要利用公式或已知表达式来求解。





## Proof By Induction

一种证明方法，通常用于证明关于自然数 n 的命题。



### steps

You have a conjecture P(n) about integers n

- First, you prove the **base case** P(1)
- Then you prove the **inductive step** P(n) Þ P(n+1)

Now you have proven P(n) for all n >= 1

#### 基础步骤

首先，证明命题在n=1 时成立。这是归纳法的基础，因为它是归纳过程的起点。

#### 归纳步骤

假设对于某个自然数 k，命题成立，即假设 P(k) 为真。然后，证明在 k+1 的情况下也成立，即 P(k+1) 也为真。

如果这两个步骤都完成了，就可以得出结论：对于所有自然数 n，命题 P(n) 都成立。



### Proof by Contradiction

Suppose P(1) and P(n) Þ P(n+1)

Now suppose there is a positive integer k such that not P(k). 

Then not P(k-1), so not P(k-2), etc., so not P(1). 

But P(1) is true. This is a contradiction.

So there cannot be a positive integer k such that P(k) is false.







## Strong Induction

一种数学归纳法的扩展，通常用于证明所有自然数 nn 满足某种性质 P(n)。

Sometimes P(n) is not enough to prove P(n+1)

In some cases, P(1) and P(2) and … and P(n) is enough to prove P(n+1)

In other words, if you know P(k) were true for all k = n, then you could prove P(n+1)

You still start with proving P(1)

Then you use an inductive step {P(1) and P(2) and … and P(n)} ==> P(n+1)

This is called **strong induction**

> 通常用于证明所有自然数 n 满足某种性质 P(n)。
>
> 在一些问题中，仅仅使用 P(k) 推导 P(k+1) 不足以完成证明，需要借助更多的前置信息。这时，强归纳法的假设可以让我们利用更多的 P(i) 来确保 P(k+1) 成立。

1. **基步（Base Step）**：验证某个最小自然数（如 n=1 或 n=0）使得性质 P(n) 成立。
2. **归纳假设（Induction Hypothesis）**：假设对于从基步开始的某个自然数 k 之前的所有数都成立，即假设 P(1),P(2),…,P(k) 全部为真。
3. **归纳步骤（Induction Step）**：在归纳假设的基础上，证明 P(k+1) 成立。这一步允许我们用之前的任意多个 P(i)（即 P(1),P(2),…,P(k)）来证明 P(k+1)，而不仅仅局限于 P(k)。

强归纳法的关键在于扩展归纳假设的适用范围，利用更多的前提条件来完成证明。这在涉及复杂构造或多个前置条件的情况下非常有效。

> *Discrete Structures,* Chapter 12 - This chapter works through proof by induction.



## Recurrences

递推关系 一种描述序列中各项之间关系的数学表达式，通常用于定义一个序列中的每一项是如何由前几项生成的。

Recurrence is a definition of a function in terms of itself

> 递推关系广泛应用于算法分析、动态规划、数列定义等领域。

### Structure

一个递推关系通常包含两个部分：

1. **递推式（Recurrence Relation）**：描述一个数列的通项如何通过前面的项来计算。例如：an=f(an−1,an−2,…,an−k)。
2. **初始条件（Initial Condition）**：给出序列的起始项（或前几项），便于计算出后续的项。

> 斐波那契数列\阶乘\合并排序的时间复杂度



### Recursive Functions

When a function is recursive, we can frequently get a recurrent definition of how long it takes to run

```python
def Factorial (n):
  if n ==1:
  	return 1
  return Factorial(n-1) * n
```

> The running time will be f(n) = f(n-1) + 1

It has a **recursive term** f(n-1) and a **non-recursive term** 1



#### Binary Search

Given a sorted list, we want to find a value x

- We look at the middle value m. If m = x we are done!
- Else if m < x we look in the left half; otherwise we look in the right half

>This is the same search, but the list is half as long

We need to do a compare operation, then a search in a list of half the length

So the general running time is T(n) £ 1 + T(n/2)



### solution

Usually when we are given a recurrent function definition, we seek a solution

A solution is **a “closed-form” (i.e. non-recurrent) definition for that function**

> This will allow us to directly compute any value

> Unfortunately, there is no magic way to get a closed-form solution for every recurrence



There are several approaches that might work, most are beyond this class

#### 递推展开（Unrolling the Recurrence）

逐步展开递推式，寻找一个模式并得到一个一般形式。

#### 代入法（Substitution Method）

假设递推关系的解形式，然后通过代入验证假设是否成立。

#### 主定理（Master Theorem)

主定理用于一种特定格式的递推式：
$$
T(n) = aT(n/b) + O(n^d)
$$

> 可以快速判断出递推的渐近时间复杂度。

通过主定理，能直接判断这个递推关系的时间复杂度。只需检查 nlog⁡banlogba 和 ndnd 的大小关系，来得到答案。这种方法非常快速。

#### 特征方程法（Characteristic Equation Method) 

主要用于线性递推关系。将递推式转化为一个“特征方程”来求解其通解。

> 例如，比如，斐波那契数列用特征方程法就可以得到一个闭式解，帮助我们直接计算序列的任意项。



# Sorting and Algorithm Performance

*Discrete Structures* Chapter 10. This reading introduces searching and sorting as a context for analyzing algorithms.

- examine relations and functions with a focus on their growth rate.
- consider various sorting functions and compare their growth rates
- order functions by their rate of asymptotic growth, as well as relevant terms for their growth, including Big O, Little o, Big Omega, Little Omega, and Theta.





## **Sorting**



### Insertion Sort

将元素逐个插入到前面已经排好序的部分中，找到合适位置插入。

#### Process

1. 从**第二个元素开始**：将第二个元素看作是待插入的元素。假设第一个元素已经在正确的位置上。
2. 与已排序部分进行比较：将**待插入元素**与已排序部分的元素进行比较，**从后向前找**到合适的位置，将待插入元素插入到这个位置。

3. **移动部分已排序部分的元素**：在插入待插入元素的过程中，可能需要将已排序部分的元素向后移动，以为待插入元素腾出位置。
4. 重复过程：将下一个元素作为待插入元素，重复上述过程，直到所有元素都被插入到合适的位置。

#### Time Complexity

- The worst-case time complexity of Insertion Sort is O(n^2).
- The best-case time complexity occurs when the array is already sorted, making it O(n).
- The average-case time complexity is also O(n^2).

#### Space Complexity

Insertion Sort is an in-place sorting algorithm, meaning it does not require additional memory proportional to the size of the input.

#### Stability

Insertion Sort is stable, meaning that the relative order of equal elements remains unchanged during sorting.





### Merge Sort

采用分治法。将数组不断分为两部分，分别排序后再合并。

> a divide-and-conquer sorting algorithm

#### Process

1. **分解（Divide）**：将待排序的数组分解成两个大小相等的子数组，递归地对这两个子数组进行排序。
2. **合并（Merge）**：将两个已排序的子数组合并成一个有序的数组。
3. **递归（Recursion）**：在分解步骤中，继续递归地将子数组分解，直到每个子数组只包含一个元素（此时已排序）。

#### Time Complexity

The time complexity of Merge Sort is O(nlog⁡n) in all cases (worst-case, average-case, and best-case). This makes Merge Sort highly efficient for large datasets.

> The list is divided into two halves, which takes constant time: \(O(1)\).
>
> Recursively sorting the two halves involves log(n) levels of recursion.
>
> At each level, the total work done is proportional to \(n\), where \(n\) is the size of the input. In this example, \(n = 10\).
>
> So, the time complexity for the conquer step is O(nlog⁡n)

#### Space Complexity

Merge Sort has a space complexity of O(n) due to the need for additional space to store temporary sublists during the merging process.

#### Stability

Merge Sort is a stable sorting algorithm, meaning that the relative order of equal elements is preserved during the sorting process.





### Summary

| Sorting Algorithm  | Best Case | Average Case | Worst Case |
| ------------------ | --------- | ------------ | ---------- |
| **Bubble Sort**    | O(n)      | O(n2)        | O(n2)      |
| **Insertion Sort** | O(n)      | O(n2)        | O(n2)      |
| **Merge Sort**     | O(nlog⁡n)  | O(nlog⁡n)     | O(nlog⁡n)   |
| **Quick Sort**     | O(nlog⁡n   | O(nlog⁡n)     | O(n2)      |
| **Heap Sort**      | O(nlog⁡n   | O(nlog⁡n)     | O(nlog⁡n)   |



## Asymptotics渐近线 and Big O

>给出一个表达式，并要求我们找到一个常数 cc，使得 c⋅n2c⋅n2 能够“压制”或“包住”原式 7n^2+8n+2的增长率，从而满足大O的定义。
>
>我们有一个表达式 7n^2+8n+2，并希望证明它的增长率是 O(n^2)
>
>**大O定义**： 对于函数 f(n)，如果我们可以找到一个常数 c 和一个正整数 n0，使得当 n≥n0 时，f(n)≤c⋅g(n)，我们就可以说 f(n)=O(g(n))。

### Asymptotic Analysis 渐近分析 

渐近分析是用来描述算法在输入规模 n 无限增大时的表现。

渐近分析的主要目的是**描述函数增长的趋势**。growth trend

>它帮助我们理解算法在大规模数据下的性能，而不必关心精确的执行时间。

### Big O Notation

渐近分析的主要工具，用来描述**算法的最坏情况时间复杂度**，即在最差情况下输入规模增大时算法的增长速率。

**定义**：对于一个函数 f(n)，如果存在正整数常数 c 和 n0，使得当 n≥n0 时，始终有 f(n)≤c⋅g(n)，那么我们可以写 f(n)=O(g(n))。

> **大O符号**专注于算法的上界，即它保证了算法在最坏情况下不会增长得比 g(n) 更快。
>
> 除了大O，还有一些其他的渐近表示法：
>
> - **Big Omega (Ω)**：描述算法的**下界**，即算法的最优表现情况。
> - **Theta (Θ)**：描述算法的**紧确界**，即上下界同时满足的情况。
> - **Little o (o)** 和 **Little ω (ω)**：表示严格的上界和下界。

> **Growth rate, or asymptotic渐近 behavior, of a function** refers to how the function behaves as the input size n grows. This is essential in algorithm analysis to determine performance and **efficiency** across different input sizes. The most common asymptotic notations are: 
>
> - **Big O** (O): Upper bound, describes the worst-case growth rate.
> - **Little o** (o): Upper bound (strict), describes functions that grow slower than a given upper bound.
> - **Big Omega** (Ω): Lower bound, describes the best-case growth rate.
> - **Little Omega** (ω): Lower bound (strict), describes functions that grow faster than a given lower bound.
> - **Theta** (Θ): Tight bound, describes functions that grow at the same rate, both upper and lower bounds.
>
> ****
>
> **Asymptotic Notations in Sorting Analysis**
>
> - **Best-Case**: Minimum time required, e.g., Insertion Sort on a sorted array has a best-case time complexity of Ω(n).
> - **Average-Case**: Expected time complexity for average input configurations, e.g., Quicksort generally performs in Θ(nlogn) in its average case.
> - **Worst-Case**: Maximum time required, e.g., Bubble Sort has a worst-case time complexity of O(n^2).





## Ordering Functions



### Little o Notation

描述了一个**严格上界** upper bound，表示 f(n) 的增长速度小于 g(n)。

- **定义**：如果对于任何正数常数 c，当 n→∞ 时，f(n)<c⋅g(n)，那么 f(n)=o(g(n))。
- 小o表示法关注的是一种更严格的上界，比大O更精确。换句话说， f(n)=o(g(n)) 表示 f(n)的增长速度比 g(n) 更慢。



### Big Omega Notation

大Ω表示法描述一个函数的**下界**，即描述算法的最佳表现情况。

- **定义**：如果存在一个常数 c>0 和 n0，使得对于所有 n≥n0，都有 f(n)≥c⋅g(n)，那么 f(n)=Ω(g(n))。
- 大Ω描述了最小的增长率，确保算法的增长至少和 g(n) 一样快。



### Little omega Notation

小ω表示法描述了一个函数的**严格下界**，即 f(n) 的增长速度比 g(n) 快。

- **定义**：如果对于任意正数常数 c，当 n→∞ 时，总是 f(n)>c⋅g(n)，那么 f(n)=ω(g(n))。
- 这表示 f(n) 的增长速率严格超过 g(n)。

- **大O**（上界）： f(n)=O(g(n)) 表示 f(n) 的增长不会快于 g(n)。
- **小o**（严格上界）： f(n)=o(g(n)) 表示 f(n)f(n) 的增长速度严格小于 g(n)。
- **大Ω**（下界）： f(n)=Ω(g(n)) 表示 f(n) 的增长速度至少和 g(n) 一样快。
- **小ω**（严格下界）： f(n)=ω(g(n)) 表示 f(n)f(n) 的增长速度严格快于 g(n)。



### Ordering Functions by Asymptotic Growth Rates

how quickly they increase as n increases.

- **Constant Time**: O(1)
- **Logarithmic Time**: O(log⁡n) Binary search.
- **Linear Time**: O(n)
- **Linearithmic Time**: O(nlog⁡n) Efficient sorting algorithms like **Merge Sort**, **Heapsort**, and **Quicksort** (average case).
- **Quadratic Time**: O(n^2) Simpler sorting algorithms like **Bubble Sort**, **Selection Sort**, and **Insertion Sort** (worst case).
- **Cubic Time**: O(n^3)
- **Exponential Time**: O(2^n)
- **Factorial Time**: O(n!)





# Graphs and Trees



## Graphs

### Definition

In **discrete mathematics**, a **graph** is defined as an **ordered pair** G=(V,E), where:

1. **V** is a non-empty set of **vertices** (also called **nodes** or points).
2. **E** is a set of **edges**, where each edge is an unordered or ordered pair of vertices from V.

- In mathematics and computer science, a graph is **a collection of nodes (vertices) and edges that connect pairs of nodes.** Graphs are used to **model relationships between entities.**
- In a more general sense, "graph" can refer to any visual representation that shows the relationship between different elements.



#### Types

##### Directed and Undirected

- **无向图（Undirected Graph）**：边没有方向，连接是双向的。例如 (u,v) 表示 uu 和 vv 互相连接。
- **有向图（Directed Graph）**：边有方向，用箭头表示，例如 (u,v) 表示从 uu 指向 vv。

##### Weighted and Unweighted

- **加权图（Weighted Graph）**：边带有权值，用来表示连接的成本、距离或权重。

  >A **weighted graph** is a graph in which each edge is assigned a numerical value, called a **weight**. These weights often represent quantities like cost, distance, time, or capacity, depending on the context of the problem.
  >
  >Formally, a **weighted graph** is represented as:
  >
  >G=(V,E,w)
  >
  >where:
  >
  >- V is the set of vertices (nodes).
  >- E is the set of edges (connections between vertices).
  >- w:E  → R is a weight function that assigns a **real number w(e)** to each edge e∈E
  >
  >

- **无权图（Unweighted Graph）**：边没有权值，通常表示简单的连接关系。

> Both vertices and edges can have **labels**. A numeric label is called a **weight**.
>
> 在图论中，**顶点（vertices）** 和 **边（edges）** 可以附加上某些“**标签（labels）**”来表示它们的属性或特性。
>
> - **标签（Label）**：顶点可以附加一个标识，比如一个名字、编号或者其他属性。
> - **权重（Weight）**：如果顶点的标签是数字，我们称之为权重。权重通常表示与这个顶点相关的一些属性值。
>
> The sum of all the weights is called the **weight of the graph**.

>使用边的权重，我们可以解决**最短路径问题**（如 Dijkstra 算法）。
>
>使用顶点的权重，我们可以解决**资源分配问题**或**最小代价问题**。

##### Dense and Sparse

- **稠密图（Dense Graph）**：边的数量接近节点数的平方（ ∣E∣ ≈ ∣V∣^2）。
- **稀疏图（Sparse Graph）**：边的数量远小于节点数的平方（ ∣E∣ ≪ ∣V∣^2）。



##### Bipartite Graph 二分图

A **bipartite graph** is a type of graph whose vertex set can be divided into two **disjoint subsets**, U and V, such that:

- **Every edge** connects a vertex in U to a vertex in V.
- There are **no edges** between vertices within the same subset.

> Formally, a graph G=(V,E) is bipartite if there exists a partition of V into U and V where:  E⊆{(u,v)∣u∈U,v∈V}.

###### Characteristics

**Two-colorable**:

- A bipartite graph can be **colored using two colors** such that no two adjacent vertices share the same color.

**No Odd-length Cycles**:

- A graph is bipartite if and only if it contains **no odd-length cycles** **无奇环**.

**Complete Bipartite Graph**:

- Denoted as Km,n, where:
  - m=∣U∣m=∣U∣: Number of vertices in one subset.
  - n=∣V∣n=∣V∣: Number of vertices in the other subset.
  - Each vertex in UU is connected to every vertex in VV, and vice versa.

###### Check if a Graph is Bipartite

**Two-colorable**

1. Breadth-First Search (BFS) Algorithm:
   - Color the starting vertex with one color.
   - Alternate colors as you traverse to adjacent vertices.
   - If a vertex is revisited with the same color, the graph is **not bipartite**.
2. DFS Approach:
   - Similar to BFS but uses recursion to color vertices and check adjacency.

图染色法（BFS/DFS）我们尝试为图的每个节点染色，使用两种颜色（例如红色和蓝色），并保证相邻的两个节点有不同的颜色。如果能够成功完成染色，则是二分图；如果发现冲突（即相邻节点出现相同颜色），则不是二分图。

1. 任选一个起点节点，将其染为红色。
2. 遍历该节点的所有邻居，将它们染为蓝色。
3. 继续对邻居的邻居染色（红色和蓝色交替）。
4. 如果在染色过程中出现冲突（某节点的邻居被染成了相同的颜色），则不是二分图。

**判断是否存在奇环（Odd-length Cycle）**

如果图中存在奇数长度的环，则不是二分图。

可以通过 BFS 或 DFS 来检测是否存在奇数环：在遍历过程中，检查当前节点是否和它的祖先节点（环中的一个节点）有相同颜色。

###### 应用场景

1. **匹配问题**：如最大匹配问题（在二分图中找到最大数量的匹配边）。
2. **网络流问题**：如使用二分图求解最大流问题。
3. **调度问题**：例如将任务分配给工人，任务和工人可以看作二分图的两组节点。





#### Loops

A **loop** is an edge that starts and ends at the same vertex

#### Multiple Edges and Multigraph

A **multiple edge** is **a set of edge**s that start at the same vertex, and end at the same vertex

> 图中的特殊边集。
>
> 主要出现在**多重图（multigraph）**中，因为在简单图（**simple graph**）中，不允许两个顶点之间有多于一条的边。
>
> - **简单图（Simple Graph）**：不允许多重边和自环（一个节点连接自身的边）。
> - **多重图（Multigraph）**：允许多重边，但可以选择是否允许自环。

#### simple graph

A graph with no loops or multiple edges 



#### Characteristics

##### Degree/in-degree/out-degree/isolated vertex

The **degree** of a node is the number of edges connected to that node

In a directed graph, each node has an **in-degree** and an **out-degree**

A vertex with degree = 0 is called an **isolated vertex**

##### Adjacency

In an undirected graph, two vertices are **adjacent** if there is an undirected edge between them

In a directed graph, we will use the definition that **vertex v is adjacent to vertex u if there is an arc (directed edge) from u to v**. 

> **V is adjacent to U**, but U is not adjacent to V

##### Walks

A walk is the most general definition of how we can move around a graph.

A **walk** starts at a vertex and moves along edges to vertices in a sequence.

> In a simple graph (no loops or multiple edges), we can simply write the vertices on the order we visit them.
>
> In a directed graph we only can walk in the direction of each edge.

The **length** = how many edges 

###### Trails

A **trail** is a walk that does not repeat any edges

###### Paths

A path is a walk that does not visit any vertex more than once (except at the start and end)

> A path is always also a trail (no repeated edges)

###### Open and Closed / Circuit and Cycle

- A walk is called **open** if the first and last vertices are different. 
- A walk is called **closed** if the first and last vertices are the same

- A closed trail is also called a **circuit**.
- A closed path is also called a **cycle**.

##### Connected

Two vertices are **connected** if there is a path from one to the other.

In a **connected graph** all pairs of vertices are connected.

###### Fully Connected / complete

In a **fully connected** or **complete** graph, every vertex is adjacent to every other vertex by an edge

###### component

A maximum connected subset of a graph (subgraph) is a **component**.

> 在图论中，**component（连通分量）**是图的一种特定结构，它表示图中的一个**最大连通子图**。
>
> 在一个无向图中，如果任意两个顶点之间都可以通过某条路径相连，那么这两个顶点所在的子图是连通的。连通的子图是包含所有这些顶点的边和点的集合。
>
> 一个连通分量必须是**最大化的**，即无法再添加更多的点或边来保持连通性。如果你还能加入点或边，那么这个子图还不是一个完整的分量。
>
> 一个图可能由多个连通分量组成，尤其是在图是**非连通的**情况下。每个分量都是图中独立的一部分。



##### Isomorphic 同构

Two graphs G1 and G2 are **isomorphic** if there exists a one-to-one correspondence (bijection) between their vertex sets such that the adjacency relationship is preserved. 

- 节点之间的连接关系在两个图中是相同的。
- G1 和 G2 的结构一致，但节点的名称可能不同。

This means that you can "relabel" the vertices of one graph to make it identical to the other graph.

If two graphs are isomorphic:

- They have the **same number of vertices**.
- They have the **same number of edges**.
- The structure (connections between vertices) is identical under some relabeling.

###### Steps to Determine

1. **Check Basic Properties:**

   - Same number of vertices.
   - Same number of edges.
   - Same degree distribution (each vertex in G1G1 must have a corresponding vertex in G2G2 with the same degree).

   If these don't match, the graphs are **not isomorphic**.

2. **Compare Degree Sequences:**

   - List the degrees of all vertices in both graphs in descending order.
   - If the degree sequences are different, the graphs are **not isomorphic**.

3. **Match Neighborhoods:**

   - Check if vertices with the same degree have the same neighborhood structure (adjacent vertices).
   - If neighborhoods differ, the graphs are **not isomorphic**.

4. **Try Relabeling:**

   - Find a bijection (mapping) between the vertices of G1G1 and G2G2 such that the adjacency relationship is preserved. This is usually done by trial-and-error for small graphs or using algorithms for larger ones.

5. **Automated Methods (for Larger Graphs):**

   - Use graph isomorphism algorithms like **Nauty** or **VF2** for efficient checking.









### Graph Path

In graph theory, a **path** is a sequence of vertices connected by edges in which **each edge is traversed only once**, and no vertex (except possibly the starting and ending vertex) is repeated.

A **path** P in a graph G=(V,E) is defined as:

P=(v1,v2,…,vk)

where:

1. v_i∈V for i=1,2,…,k
2. (vi,vi+1)∈E. for i=1,2,…,k−1
   - In an undirected graph, {vi,vi+1}∈E.
3. No vertex is repeated except when forming a **cycle**.



#### Types of Paths

1. **Simple Path**:
   - A path where no vertex is repeated.
   - Example: P=(A,B,C), assuming no loops or repeated vertices.
2. **Closed Path (Cycle)**:
   - A **simple** path where the starting and ending vertices are the same.
   - Example: P=(A,B,C,A).
3. **Directed Path**:
   - A path in a directed graph where all edges follow the direction of traversal.
   - Example: P=(A,B,C), where (A,B) and (B,C) are directed edges.
4. **Weighted Path**:
   - A path in a weighted graph where the **path weight** is the sum of the weights of the edges in the path.
   - Example: If w(A,B)=3, w(B,C)=2, then the total weight of P=(A,B,C) is 3+2=5.



#### Cycles

A **cycle** in a graph is a **closed path** where:

1. The path starts and ends at the same vertex.
2. All edges and vertices (except the starting/ending vertex) are distinct.
3. A cycle must have at least three vertices.

Formally, in a graph G=(V,E), a cycle is a sequence of vertices:

C=(v1,v2,…,vk,v1)

where:

- v1=vk (the starting and ending vertices are the same).
- (vi,vi+1)∈E for i=1,2,…,k−1.
- All vi are distinct for 1≤i≤k−1.

##### Eulerian Cycle

An **Eulerian Cycle** is a cycle in a graph that **traverses every edge exactly once** and returns to the starting vertex.

>- If it is a closed trail it is called a **Eulerian circuit**
>- If a graph has a Eulerian circuit, it is called a **Eulerian graph**

Conditions for Existence:

- Undirected Graph
  - All vertices must have an **even degree**.
  - The graph must be **connected** (ignoring isolated vertices).
- Directed Graph
  - All vertices must have the same **in-degree** and **out-degree**.
  - The graph must be **strongly connected** (every vertex is reachable from any other vertex).

##### Hamiltonian Cycle

A **Hamiltonian Cycle** is a cycle that **visits every vertex exactly once** and returns to the starting vertex.

>If it is a closed path (start = end) it is called a **Hamiltonian cycle**
>
>If a graph has a Hamiltonian cycle, it is called a **Hamiltonian graph**

**Conditions for Existence**:
There are no straightforward necessary/sufficient conditions, but some general criteria include:

- **Dirac's Theorem**: If every vertex in an n-vertex graph has a degree ≥n/2, then the graph has a Hamiltonian cycle.
- **Ore's Theorem**: If for every pair of non-adjacent vertices u,v, the sum of their degrees deg(u)+deg(v)≥n, the graph has a Hamiltonian cycle.



### Representation

#### adjacency matrix

An **adjacency matrix** is a 2D matrix where Aij is 1 if nodes i and j are adjacent

一个 n×n 的矩阵，用来表示 n 个顶点之间的连接关系。

若顶点 i 和 j 之间有边，则 matrix [i] [j]=1(或边的权重）；否则为 0。

> 无向图的邻接矩阵是对称的（ matrix [i] [j]=matrix [j] [i]）。We usually require a simple graph (no loops or multiple edges) when using an adjacency matrix
>
> 对于有向图，方向会影响矩阵值。

Adjacency Matrix For Directed Graph: An **adjacency matrix** is a 2D matrix where Aij is 1 if node j is adjacent to node i. Remember that means there is an arc from node i to node j

![Adjacency Matrix for Directed Graph](./pictures/Adjacency Matrix for Directed Graph.jpg)

If you multiply an adjacency matrix by itself, you get how many paths of length 2 exist between nodes i and j

**邻接矩阵 A** 表示的是图中**直接相邻（长度为1）的路径**。当我们将 A 自乘（A⋅A）时，得到的新矩阵 B 表示**长度为2的路径的数量**。

![Adjacency Matrix for Directed Graph multiply itself](./pictures/Adjacency Matrix for Directed Graph multiply itself.jpg)

矩阵乘法的规则是：
$$
B[i][j] = \sum_{k=1}^{n} A[i][k] * A[k][j]
$$
B[i] [j] 是所有从 i 到 j 经过中间节点 k 的路径数量之和。

> A[i] [k]=1 表示节点 i 和 k 是直接相连的。
>
> A[k] [j]=1 表示节点 k 和 j 是直接相连的。
>
> 因此，A[i] [k]⋅A[k] [j]=1 表示存在一条从 i 到 j **经过 k** 的长度为2的路径。
>
> 将所有可能的 kk 相加，就得到了从 ii 到 jj 的**所有长度为2的路径的数量**。

If you multiply an adjacency matrix by itself n times = A^n, you get how many paths of length n exist between nodes i and j!

![Adjacency Matrix for Directed Graph multiply itself n times](./pictures/Adjacency Matrix for Directed Graph multiply itself n times.jpg)

















#### adjacency list

An **adjacency list** is a list of all the nodes adjacent to this one

用一个数组表示每个顶点的邻居列表。

每个顶点存储一个链表或列表，记录其直接相连的顶点编号。

> 更适合稀疏图（边较少的图），因为节省空间。
>
> NOT GOOD WHEN SEARCH A SINGLE EDGE

In object-oriented programming, each node can be an object

The adjacency list could be stored as a property in the node

It would be a list of links to the adjacent node objects (Sometimes you might also store the edges as objects)

> 在面向对象编程（Object-Oriented Programming，简称 OOP）中，可以通过将**节点（Node）**和**边（Edge）**建模为对象，来实现图的表示。这种方法利用了 OOP 的特性（如**封装**、**继承**和**多态**），让我们能够更自然地模拟现实中的图结构。

**节点（Node）作为对象**: 每个节点可以用一个对象表示，包含以下信息：

- **节点值**（如名称、ID等）。
- **邻居节点列表**（即与该节点相邻的其他节点）。
- **其他属性**（如节点的权重、颜色等，可选）。

**边（Edge）作为对象**: 如果边需要存储额外的信息（例如权重、方向等），可以将边表示为对象。

- **起点和终点节点的引用**。
- **边的元数据**（例如权重、方向等）。

**图（Graph）类**: 

- 维护所有节点的集合。
- 提供添加/删除节点和边的方法。
- 执行图上的各种操作（如遍历、搜索等）。

```python
class Node:
    def __init__(self, value):
        self.value = value  # 节点的值
        self.adjacency_list = []  # 邻居节点的列表

    def add_neighbor(self, neighbor):
        """向当前节点添加一个邻居节点"""
        self.adjacency_list.append(neighbor)

    def __str__(self):
        """返回节点的字符串表示"""
        neighbors = [neighbor.value for neighbor in self.adjacency_list]
        return f"Node({self.value}) -> Neighbors: {neighbors}"


class Edge:
    def __init__(self, source, target, weight=1):
        self.source = source  # 起点节点
        self.target = target  # 终点节点
        self.weight = weight  # （可选）边的权重

    def __str__(self):
        return f"Edge({self.source.value} -> {self.target.value}, weight={self.weight})"


class Graph:
    def __init__(self):
        self.nodes = {}  # 用字典存储节点，键为节点值

    def add_node(self, value):
        """向图中添加一个新节点"""
        if value not in self.nodes:
            self.nodes[value] = Node(value)

    def add_edge(self, source_value, target_value, weight=1):
        """在两个节点之间添加一条边"""
        if source_value not in self.nodes:
            self.add_node(source_value)
        if target_value not in self.nodes:
            self.add_node(target_value)
        source = self.nodes[source_value]
        target = self.nodes[target_value]
        source.add_neighbor(target)  # 添加邻居节点
        # （可选）创建边对象以存储权重或其他数据
        return Edge(source, target, weight)

    def __str__(self):
        """打印图的结构，显示所有节点及其邻居"""
        return "\n".join(str(node) for node in self.nodes.values())


# 示例使用
graph = Graph()
graph.add_edge("A", "B")  # 添加边 A -> B
graph.add_edge("A", "C")  # 添加边 A -> C
graph.add_edge("B", "D")  # 添加边 B -> D

print(graph)  # 显示图的结构
```

```
Node(A) -> Neighbors: ['B', 'C']
Node(B) -> Neighbors: ['D']
Node(C) -> Neighbors: []
Node(D) -> Neighbors: []
```



### Graph Traversals

visit every node called **traversing** the graph



#### Depth-First Search

**DFS** is a **recursive** algorithm that explores as far as possible along a branch of the graph before backtracking. 

It starts at a given node, explores the first adjacent unvisited vertex, then recursively explores that vertex’s neighbors, and so on, until it reaches a dead end (no unvisited adjacent vertices). After hitting a dead end, it backtracks to the most recent visited vertex that still has unvisited neighbors and continues exploring from there.



#### Breadth-First Search

**BFS** explores the graph level by level. 

It starts at a given vertex, then visits all adjacent vertices (neighbors) at the current level before moving on to the next level. 

> BFS is typically implemented using a **queue** data structure, which ensures that nodes are visited in the order they were discovered.





### Shortest Path: Dijkstra’s Algorithm

Dijkstra's Algorithm, a well-known algorithm used to find the shortest path between two points (or vertices) in a graph. 

> Dijkstra's algorithm is particularly useful for graphs with non-negative edge weights, and it efficiently computes the shortest path from a starting vertex to all other vertices in the graph.

>Dijkstra 算法适用于 **非负权重图**，因为负权重会导致错误的结果。
>
>如果需要处理负权重图，应该考虑使用 **Bellman-Ford** 算法。

**Source vertex**: The starting point from which we want to find the shortest path to all other vertices.

#### Steps

1. **Initialization**:
   - Set the distance to the source vertex as **0** and to all other vertices as **infinity** (∞), indicating they are unreachable at the start.
   - Mark all vertices as **unvisited**. The goal is to visit each vertex and find the shortest path to it.
   - Create a **priority queue** (or a min-heap) that will store vertices and their current shortest distance from the source.
2. **Process the Current Vertex**:
   - Start with the source vertex, and look at all its neighbors (connected vertices). For each neighbor, calculate the **tentative distance** as the sum of the distance to the current vertex and the weight of the edge connecting the two vertices.
   - If the calculated tentative distance is smaller than the current known distance to that neighbor, update the neighbor’s distance with this smaller value.
3. **Mark the Current Vertex as Visited**:
   - After all neighbors of the current vertex have been processed, mark the current vertex as visited (it will not be checked again).
4. **Choose the Next Vertex**:
   - From the set of unvisited vertices, choose the one with the smallest tentative distance, and repeat the process for that vertex.
5. **Repeat**:
   - Continue the process until all vertices have been visited, or the smallest tentative distance among the unvisited vertices is infinity (which means the remaining unvisited vertices are not reachable from the source).
6. **Shortest Path**:
   - Once all vertices are visited, the algorithm has found the shortest path to all vertices from the source.

#### Time Complexity

Dijkstra 算法的时间复杂度取决于以下两个关键操作：

1. **找到最小的节点**（使用优先队列或堆来优化）。
2. **更新邻居节点的距离**（取决于图的表示方式）。

##### 1. 使用普通数组实现优先队列

时间复杂度分析：

- **找到最小的节点**：
  每次需要线性扫描所有未处理的节点来找到最小距离的节点，耗时为 O(V)，其中 V 是节点数。
- **更新邻居节点的距离**：
  对于每条边进行更新操作，耗时为 O(E)，其中 E 是边数。

总时间复杂度：对于 V 个节点和 E 条边，找到最小节点需要执行 V 次，每次耗时 O(V)，加上所有边的更新，复杂度为：O(V^2+E). 当图是稠密图时（即 E≈V^2），复杂度为 O(V^2)。

##### 2. 使用最小堆实现优先队列

时间复杂度分析：

- **找到最小的节点**：
  使用最小堆，找到最小节点的操作复杂度为 O(logV)。
- **更新邻居节点的距离**：
  更新操作涉及调整堆，复杂度为 O(logV)。对于每条边，这个操作会被执行一次，因此总复杂度为 O(ElogV)。

总时间复杂度：对于 V 个节点，最小节点操作执行 V 次，每次耗时 O(logV)，加上边的更新，复杂度为：O((V+E)logV)

| 图的表示 & 优化 | 找到最小节点 | 更新邻居距离 | 总复杂度     | 适用场景         |
| --------------- | ------------ | ------------ | ------------ | ---------------- |
| 普通数组        | O(V)         | O(1)         | O(V^2)       | 稠密图           |
| 最小堆          | O(log⁡V)      | O(log⁡V)      | O((V+E)log⁡V) | 稀疏图和大规模图 |

##### 不同图结构下的时间复杂度

- **稀疏图**（边较少，E≪V^2）：
  使用堆时，复杂度为 O((V+E)log⁡V)。由于 E≈V，简化为 O(Vlog⁡V)。
- **稠密图**（边较多，E≈V^2）：
  使用堆时，复杂度为 O((V+E)log⁡V)。由于 E≈V^2，简化为 O(V^2log⁡V)。
- **完全图**（每两个节点之间都有边，E=V(V−1)/2）：
  若使用普通数组实现优先队列，则复杂度为 O(V^2)。















### Bridges of Königsberg

The challenge is to find a walk (known as an *Eulerian path*) that crosses each of the seven bridges in the city of Königsberg **exactly once**, without retracing any steps.

The problem can be modeled as a graph where:

- **Landmasses** (two islands and two banks of the river) are represented as **vertices**.
- **Bridges** connecting these landmasses are represented as **edges**.

Here’s the graph representation:

- There are **4 vertices** (A, B, C, and D, representing the two islands and two riverbanks).
- There are **7 edges**, one for each bridge.

#### Euler's Criterion for an Eulerian Path

Euler determined that:

1. A graph has an *Eulerian path* (a walk crossing each edge exactly once) **if and only if it has exactly 0 or 2 vertices of odd degree** (degree = number of edges connected to a vertex).
2. A graph has an *Eulerian circuit* (a closed walk crossing each edge exactly once, starting and ending at the same vertex) **if and only if all vertices have even degree**.

#### Applying Euler's Criterion

Let’s calculate the degree of each vertex:

- Vertex A: **3 bridges** connect to A → Degree = 3 (odd).
- Vertex B: **3 bridges** connect to B → Degree = 3 (odd).
- Vertex C: **3 bridges** connect to C → Degree = 3 (odd).
- Vertex D: **3 bridges** connect to D → Degree = 3 (odd).

All **4 vertices have odd degrees**.

#### Conclusion

Since there are more than 2 vertices with odd degrees (in fact, all 4 vertices are odd), it is **impossible to find an Eulerian path**. Thus, you cannot walk through all 7 bridges exactly once.

>### Proof
>
>Euler's criterion is both necessary and sufficient:
>
>1. **Necessity**: Any Eulerian path must have 0 or 2 odd-degree vertices because the walk enters and exits each vertex. Odd-degree vertices can only serve as the start or end of the path, so having more than 2 odd-degree vertices makes it impossible to satisfy this condition.
>2. **Sufficiency**: If a graph has 0 or 2 odd-degree vertices, an Eulerian path exists, and it can be constructed algorithmically.
>
>Since the graph for Königsberg violates the necessary condition, the result is proven: there is no Eulerian path for the Bridges of Königsberg.







## Trees



### Definition

A **tree** is a special type of graph that is connected and acyclic. 

> A tree is an **undirected** graph that is **connected** and **acyclic** (has no cycles)
>
> 在图论中，树被看作一种纯粹的结构：它描述的是节点和节点之间的连接关系，而不是节点之间的方向性。这种无向表示更通用。图论中的树本质上并不关心哪个节点是“父”，哪个是“子”，它只要求节点之间是连通且无环的。
>
> 如果需要表示“方向”，我们可以进一步扩展树，构造**有向树**（directed tree），例如用于表达父子关系的结构化数据。在许多实际应用中，比如二叉树（binary tree）或多叉树，我们会人为规定一个节点为“根节点”（root），然后约定从“根”向下到达其子节点的方向。这种约定是基于树的结构化应用，而不是图论中的基本定义。

A tree T=(V,E) satisfies the following properties:

1. **Acyclic**: A tree contains no cycles.
2. **Connected**: There is a path between any two vertices.
3. Edges and Vertices
   - If ∣V∣=n, ∣E∣=n−1 (a tree with nn vertices always has n−1 edges).

#### Characteristics of Trees

1. **Unique Path**:
   - There is exactly one path between any two vertices in a tree.
2. **Acyclic**:
   - Removing any edge from a tree will disconnect it, proving it has no cycles.
3. **Adding an Edge Forms a Cycle**:
   - If you add any edge to a tree, it will create a cycle.
4. **Rooted Tree**:
   - A tree can be rooted by designating one vertex as the "root."
   - In a rooted tree, vertices have parent-child relationships.

#### Types of Trees

1. **Rooted Tree**:
   - A tree with a designated root where edges have a direction pointing away from the root.
2. **Binary Tree**:
   - A rooted tree where each vertex has at most two children.
3. **Binary Search Tree (BST)**:
   - A binary tree where the left subtree contains values less than the parent, and the right subtree contains values greater than the parent.
4. **Spanning Tree**:
   - A subgraph of a graph that is a tree and connects all the vertices of the graph.



### **Tree Traversals**

Tree traversal is the process of visiting all nodes of a tree systematically. Common types include:

1. **Pre-order Traversal**:
   - Visit root → Traverse left subtree → Traverse right subtree.
   - Example (Binary Tree): A→B→D→E→C→F→G
2. **In-order Traversal**:
   - Traverse left subtree → Visit root → Traverse right subtree.
   - Example: D→B→E→A→F→C→G
3. **Post-order Traversal**:
   - Traverse left subtree → Traverse right subtree → Visit root.
   - Example: D→E→B→F→G→C→A
4. **Level-order Traversal**:
   - Visit nodes level by level from top to bottom.
   - Example: A→B→C→D→E→F→G























### Binary tree

A **binary tree** is a type of tree in which each node has **at most two children**, referred to as the **left child** and the **right child**.

A **binary tree** T=(V,E) is defined as a tree where:

- Each node has at most two children.
- Each node can have 0, 1, or 2 children, where:
  - **Left child**: The left subtree rooted at that node.
  - **Right child**: The right subtree rooted at that node.

#### Properties

1. **Number of Nodes**:
   - A binary tree with nn nodes has at most n−1n−1 edges, just like any tree.
2. **Height**:
   - The **height** of a binary tree is the length of the longest path from the root to a leaf node. It can be calculated as the number of edges on the path from the root to the deepest node.
   - The height of a tree with a single node is 0, and the height of a tree with no nodes is -1.
3. **Depth**:
   - The **depth** of a node is the number of edges from the root node to that node. The depth of the root node is 0.
4. **Interval:** 
   - 
5. **Full Binary Tree**:
   - A binary tree is **full** if every node has exactly 0 or 2 children.
   - Height = h, has 2^h leaves. 总节点数可以用叶节点表示： N=2L−1
6. **Complete Binary Tree**:
   - A binary tree is **complete** if all levels of the tree are fully filled, except possibly for the last level, which is filled from left to right.
7. **Perfect Binary Tree**:
   - A binary tree is **perfect** if all internal nodes have exactly two children, and all leaf nodes are at the same level.

#### Types

1. **Binary Search Tree (BST)**:
   - A binary search tree is a binary tree where:
     - The left child of a node contains only nodes with values less than the parent node.
     - The right child of a node contains only nodes with values greater than the parent node.
   - This property makes BSTs useful for searching, insertion, and deletion operations.
2. **Balanced Binary Tree**:
   - A balanced binary tree ensures that the heights of the two subtrees of every node differ by no more than one. This is crucial for maintaining efficiency in search operations.
3. **AVL Tree**:
   - An AVL tree is a self-balancing binary search tree where the difference between the heights of left and right subtrees of any node is at most one.
4. **Red-Black Tree**:
   - A red-black tree is another self-balancing binary search tree where each node has an extra bit for determining its color (either red or black) to ensure the tree remains balanced during insertions and deletions.







### Forest

A **forest** is a collection of **disjoint trees**. In other words, a forest is a graph that contains no cycles and is not necessarily connected. Each connected component of a forest is a tree.

A **forest** F=(V,E) is a graph where:

- **Each connected component** is a tree (i.e., connected and acyclic).
- There are no cycles in the graph.
- A forest with nn vertices will have at most n−1 edges, just like trees. However, since there may be multiple disconnected trees, the total number of edges will be less than n−1.

In mathematical terms, a graph is a forest if it is acyclic and the graph can be split into disjoint subgraphs, each of which is a tree.

#### Key Characteristics

1. **Acyclic**:
   - A forest, like a tree, contains no cycles.
2. **Disconnected**:
   - A forest may consist of one or more disconnected components (trees). Each component is itself a tree.
3. **Edges and Vertices**:
   - If a forest has nn vertices, it has at most n−1n−1 edges in total, because each tree in the forest has exactly m−1m−1 edges where mm is the number of vertices in that tree.
4. **Relation to Trees**:
   - A **tree** is a special case of a forest with only one connected component (i.e., a single tree).
   - A forest is simply a set of disjoint trees.

#### Applications of Forests

1. **Spanning Forest**:
   - A **spanning forest** of a graph is a forest that includes all the vertices of the original graph. It is essentially a collection of spanning trees for each connected component of the graph.
2. **Cycle Detection**:
   - A forest is useful for detecting cycles. If you repeatedly add edges to a graph that is initially a forest and at some point a cycle is formed, then the graph is no longer a forest.
3. **Graph Decomposition**:
   - A forest can be used in certain graph algorithms, such as for decomposing a graph into its connected components, especially in union-find or disjoint-set operations.
4. **Minimum Spanning Forest**:
   - In some cases, when working with disconnected graphs, finding a minimum spanning tree for each component is essential. This forms a **minimum spanning forest**.







































































