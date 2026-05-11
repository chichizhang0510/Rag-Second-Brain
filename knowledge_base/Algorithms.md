https://excalidraw.com

# 2025.9.5 

## 斐波那契数列

```python
def fib(n):
  if n == 0 or n == 1:
    return n
  return fin(n-1) + fib(n-2)
```



### Running Time Analysis

- Speed: Time Complexity
- Space: Space Complexity （data structure + call stack if using recursion [how many levels in the recursion tree] ）
- If easy to understand

> Call stack only push the unfinished function

#### Recursion Tree Calculation

T(n) = T(n-1) + T(n-2) + 1

What is this calculation? Recursion Tree

T(n) = run time to compute fib(n)

```
         T(n) +1
        /    \
     T(n-1)  T(n-2)
 .......................
```

> n -> full level of tree has sum(2^n) nodes





### Improve Recursion

using something to remember it, only calculate it once

#### Memorization

递归 + 记忆数组。

```python
def fib(n, memo={}):
    if n <= 1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]
```

先用递归写出问题的递归结构（分治思想），在每次计算子问题时，把结果存到一个缓存（数组/哈希表）里，下次再遇到相同子问题时直接取缓存。

- 递归调用，自顶向下。
- 常用在容易写成递归的题（如斐波那契数列）。
- 会跳过不必要的子问题（只算真正需要的）。

递归层数太深可能会导致栈溢出（stack overflow）。



#### Tabulation

迭代 + DP 表。

```python
def fib(n):
    if n <= 1:
        return n
    dp = [0] * (n+1)
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
```

从最小的子问题开始，逐步计算并存到表里，最后得到目标问题的答案。

- 迭代实现，自底向上。
- 通常用数组作为 DP 表。
- 所有子问题都会算到（即使有些不是必须的）。

可能会计算到一些用不上的子问题，效率上略低，但更安全。

> #### 动态规划（DP）的本质
>
> 动态规划的核心并不是 表格，而是：
>
> - 把一个复杂问题拆分成子问题（overlapping subproblems）；
> - 利用子问题的最优解构成原问题的最优解（optimal substructure）；
> - 避免重复计算。
>
> 只要你的算法满足这三个条件，它就是 DP，至于用递归还是用循环，只是实现形式的不同。
>
> 记忆化（Memoization）其实就是“带缓存的递归 DP”。普通递归时每次遇到子问题都重新算 → 会爆炸性重复计算。记忆化给每个子问题开个缓存（数组/哈希表），算过一次后直接取 → 避免重复。



### Improve Time Complexity better than O(n)

O(log) -> Binary Search 

Using Matrix to Calculate Fibnacci Number

A^n includes a_n which is what we need.

Using A_n/2 * A_n/2 to achieve A^n and soing the same break until touching A. This is log(n) Time. We nned to identify the odd and even circumstance.



## Asymptotic Analysis 渐进分析

Big O Notation Analysis

### Anotation

- **Big O**  ->  f(n) = O(g(n)) :  <=  means g(n) grows faster or equal.

  > 表示算法运行时间的上界（upper bound）算法的最坏情况不会比某个函数快得多。

- **Little o**  ->  f(n) = o(g(n)):   < means g(n) grows faster

  > 表示 严格上界，意思是 f(n) 增长得比 g(n) 慢很多，永远追不上 f(n)。

- **Big Theta**  -> f(n) = θ(g(n))  :  = means they grows equal

  > 表示算法运行时间的紧确界（tight bound），即同时有上界和下界。算法的时间复杂度和 f(n) 同阶增长。

- **Big Omega**  ->  f(n) = Ω(g(n)) :  >= means g(n) grows slower or equal

  > 表示算法运行时间的下界（lower bound）。算法至少需要这么多时间，不可能比它更快。

- **Little Omega**  -> f(n) = ω(g(n))  :  > means  g(n) grows slower

  > 表示 严格下界，意思是 f(n) 增长得比 g(n) 快很多，最终远超 f(n)。

### Analysis

- 如果增长率一致，那么三种big都能用

  > exponential 里面常数的变化就会造成增长率的变化，得用 little o

- 如果是有小于的关系，那么O 和 o都行

- 大于同理

### Compare

logarithm < polynomial < exponential

> Polynomial（多项式） 指的是由若干个 常数 × 变量的幂 相加组成的表达式。



## Solving Recursions

Recursive Solution's 时间复杂度分析方法，主要有两种经典工具：

- Masters Theorem
- Recursion Tree

> 这两个方法经常用来分析分治类算法，比如 二分查找、归并排序、快速排序 等。



### Masters Theorem

$$
T(n) = aT(\frac{n}{b}) + n^c
$$

> 特别要求 **b > 1**，也就是说子问题的规模要真的缩小，递归才有意义。

We need to compare:
$$
log_b a \space VS.  \space c
$$
有三种情况：
$$
log_b a \space < \space c  \space :  \space T(n) = \theta(n^c)  \space \text{合并/划分比递归更耗时}\\
log_b a \space = \space c  \space :  \space T(n) = \theta(n^c logn)  \space \text{递归子问题和合并操作平衡}\\
log_b a \space > \space c  \space :  \space T(n) = \theta(n^{log_b a})  \space \text{递归子问题更耗时}
$$

> ###### 为什么在 Master Theorem 里当 log_b a = c 时，复杂度会多出一个 log n 
>
> 每一层的总代价
> $$
> n^c
> $$
> 树的高度大约是
> $$
> log_b n
> $$
> 总代价
> $$
> n^c logn
> $$

### Recurtion Tree









# 2025.9.12



## Sorting

Because of CPU sppeed, sorting is very important.

- Bubble Sort
- Selection Sort (recursive version) -> in-place
- Insertion Sort
- Merge Sort (recursive version) -> not in-place
- Quick sort (recursive version) -> in-place
- Heap Sort
- Counting Sort
- Radix Sort
- Bucket Sort



## Template of each method

### Selection Sort

T(n) = n + T(n-1) -> Recursion Tree -> n^2

```
# sudo code
arr = []
n = length of arr

# pointer point to the 1st element in arr
for i in range(n):
    # assume the current index is the minimum
		min_index = i
		
		# iterate unsorted part of arr and find the minimum
		for j in range(i+1, n):
				if arr[j] < arr[min_index]:
						min_index = j
		# swap the minimum with the first element
		swap arr[i] and arr[min_index]
```

```python

```



### Merge Sort

Divide & Conquer

- Divide: mid
- Conquer: merge

Do split and merge seperately

T(n) = 2T(n/2) + n -> Master Theorem -> nlog(n)

```
arr = []
n = length

# split
split(arr, start, end):
		if end == start:
				return [arr[start]]
		mid = (start + end) // 2
		left = split(arr, start, mid)
		right = split(arr, mid+1, end)
		return merge(left, right)

# merge
merge(arr1, arr2):
		res = []
		n1, n2 = length(arr1), length(arr2)
		p1, p2 = 0, 0
		
		while p1 < n1 and p2 < n2:
				if arr1[p1] < arr2[p2]:
						res.append(arr1[p1])
						p1 += 1
				else:
				    res.append(arr1[p2])
				    p2 += 1
		
		while p1 < n1:
		    res.append(arr1[p1])
				p1 += 1
	  
	  while p2 < n2:
		    res.append(arr2[p2])
				p2 += 1
		
		return res
```

```python

```



### Quick sort

Divide & Conquer

- Divide: pivot
- Conquer: put smaller and bigger -> shuffle -> partition

The shuffle method is important

- **Partition** -> O(n)
- Quick_sort -> O(logn)

T(n) = n + 2T(n') 

> n' is decided by how we choose the pivot
>
> The format is not master theorem, so use recursion tree to calcualte the runtime
>
> T(n) = n + T(n/3) + T(2n/3) -> if the tree is unbalanced, find a lower bound and upper bound to limit the real runtime

> ##### Why pick the last is a good strategy?
>
> When the input is random values list, the possibility of choose any number is 1/n.
>
> ##### When the input is not random, what strategy we should choose?
>
> pick the middle one in the list. When the list is random, this strategy is also ok.

About the possibility

The operation is easier than merge sort, you just need to traverse once. no need to allocate.

```
arr = []

partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            swap arr[i] and arr[j]
    
    swap arr[i+1] and arr[high]
    return i+1  # index of pivot

quicksort(arr, low, high):
		if low < high:
		    pivot = partition(arr, low, high)
		    quicksort(arr, low, pivot-1)
		    quicksort(arr, pivot+1, high)
```



```python
def partition(arr, low, high):
    # 选择最后一个元素作为 pivot
    pivot = arr[high]
    i = low - 1   # i 表示 ≤ pivot 区间的末尾下标

    # 遍历 low ~ high-1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # 把 ≤ pivot 的元素换到左边
    # 扫描完后，把 pivot 放到正确位置
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1   # 返回 pivot 的最终下标


def quicksort(arr, low, high):
    if low < high:
        # 分区，把 pivot 放到正确位置
        pi = partition(arr, low, high)
        # 递归排序 pivot 左右两边
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)


# 测试
arr = [13, 19, 9, 5, 12, 8, 7, 4, 11, 2, 6, 21]
print("原始数组:", arr)
quicksort(arr, 0, len(arr) - 1)
print("排序结果:", arr)
```











### Heap Sort

Relationships between Priority queue and Heap

- Insert
- Delete_max
- Heapify



#### heap

##### What is max-heap?

- Almost full binary tree
- Parent >= children

##### How to build a heap?

- Parent_index
- Child1_index = Parent_index * 2
- Child2_index = Parent_index * 2 + 1

Find the parent: i // 2

Find the left child: i * 2

Find the right child: i * 2 + 1

> 0-based indexing（根在下标 0）
>
> - 父节点：`parent(i) = (i - 1) // 2` （i>0 时才有父亲）
> - 左孩子：`left(i) = 2 * i + 1`
> - 右孩子：`right(i) = 2 * i + 2`



#### Build Heap

1. 假设有一个数组（任意顺序）。
2. 从最后一个非叶子节点开始，依次对每个节点调用 **Heapify**（下沉调整）。
   - 最后一个非叶子节点下标是 `(n//2 - 1)`（0-based）。
3. 一直往上调整到根节点。

时间复杂度：O(n)。
>- 整个 `build_heap`：摊销下来是 O(n)。
>- 单次 `heapify`（针对一个节点）：最坏 O(log n)。
>
>在 Python 里，`heapify` 是在 `heapq` 模块里的函数，作用是：把一个无序数组原地调整成一个合法的最小堆。
>
>- `heapify`（整体建堆）：复杂度是 O(n)。虽然单个节点下沉最坏要 $O(\log n)$，但大部分节点都在底层，摊下来总成本是线性的。
>
>- 单次 `heappush` / `heappop` / `siftup` / `siftdown`：每次操作堆的大小为 n，代价最多是调整一条路径（高度 $\log n$）。所以复杂度是 O(log n)。
>
>-  `heapq.nsmallest(k, iterable, key=None)` 返回 可迭代对象 `iterable` 中最小的 k 个元素，结果是一个 已排序列表（从小到大）。还可以传 `key` 函数，就像 `sorted` 一样，用来指定比较的依据。时间复杂度大约是 O(n log k)，比全量排序 O(n log n) 更省，尤其当 k 远小于 n 的时候。
>
>  ```python
>  import heapq
>  
>  arr = [7, 2, 9, 4, 1, 8]
>  print(heapq.nsmallest(3, arr))   # [1, 2, 4]
>  
>  words = ["python", "c", "java", "rust", "go"]
>  print(heapq.nsmallest(2, words, key=len)) # ['c', 'go']
>  ```
>
>-  `heapq.nlargest(k, iterable, key=None)` 找出最大的 k 个元素，返回结果是降序列表。
>
>  ```python
>  arr = [7, 2, 9, 4, 1, 8]
>  
>  print(heapq.nlargest(3, arr))  
>  # [9, 8, 7]
>  
>  # 第 k 大
>  print(heapq.nlargest(3, arr)[-1])  
>  # 7
>  ```
>
>  当 k 很小时，`heapq` 版本更快。

```
arr = []
n = len(arr)

heapify(arr, n, i):
    left = i * 2 + 1
    right = i * 2 + 2
    largest = i
   
    if left < n and arr[left] < arr[largest]:
    		largest = left
    
    if right < n and arr[right] < arr[largest]:
        largest = right
    
    if largest != i:
        swap arr[i] and arr[largest]
        heapify(arr, n, largest)

# 把一个任意数组调整成合法的堆
build_heap(arr):
    n = len(arr)
    
    # start from last no-leaf node
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
```



##### Implement 3 heap method

在这个 已经是堆的数组 上，进行 动态操作。

- Get_max: return arr[0]

- Insert: put the value in the last position, the find its parent and compare, if bigger swap; continue until stop. O(log n)
  >```
  >insert(value):
  >		arr.append(x)
  >		index = len(arr) - 1
  >		
  >		while index > 0:
  >				parent = (index - 1) // 2
  >				if arr[index] > arr[parent]:
  >						swap arr[i], arr[parent]
  >						index = parent
  >			  else:
  >			      break
  >```
  >
  >时间复杂度：O(log n)

- Delete_max: get the last number in arr, put it in the heap's top. Swap it with bigger child if its value is samller than bigger child until cannot swap. O(log n)
  >```
  >delete_max():
  >		if len(arr) == 0:
  >        return None
  >    
  >    max_value = arr[0]
  >    arr[0] = arr[-1]
  >    arr.pop()
  >    n = len(arr)
  >    
  >    index = 0
  >    while True:
  >    		largest = index
  >    		left = index * 2 + 1
  >    		right = 2 * index + 2
  >    		
  >    		if left < n and arr[left] > arr[largest]:
  >    				largest = left
  >    		
  >    		if right < n and arr[right] > arr[largest]:
  >    				largest = right
  >    		
  >    		if largest != index:
  >    				swap arr[largest], arr[i]
  >    				index = largest
  >    		else:
  >    				break
  >```
  >
  >时间复杂度：O(log n)



#### Heapify -> How to achieve it in code?

How to achieve heapify function? 从一个无序的子树出发，调整它成为一个满足堆性质（大顶堆或小顶堆）的合法堆。

核心思想：**从下往上**，依次让每个节点都变成“父节点比子节点更大（或更小）”的结构。

- Recursion: Do heapify to each node in the tree from leaves to root
- Assumption: for each node we will do heapify, we will assume that the children are all subtrees which is already a heapified tree.

>- heapify 单次调用复杂度：`O(log n)`，因为可能递归到树高。
>- build_heap 构建堆复杂度：`O(n)`，因为多数节点在下层，实际花费比逐个插入少。

Heapify(i) 的步骤：

1. 找出 `i` 的 **左孩子** 和 **右孩子**（在二叉堆里）。
2. 找出三者里最大的节点。
3. 如果最大值不是 `i`，就把 `i` 和那个最大孩子交换。
4. 递归调用 Heapify(最大孩子位置)。

```python
def max_heapify(arr, n, i):
    """
    调整以 i 为根的子树，使它满足最大堆性质
    arr : 堆数组
    n   : 堆的大小
    i   : 当前根节点索引
    """
    largest = i          # 假设当前 i 是最大值
    left = 2 * i + 1     # 左孩子索引
    right = 2 * i + 2    # 右孩子索引

    # 如果左孩子存在且比当前大
    if left < n and arr[left] > arr[largest]:
        largest = left

    # 如果右孩子存在且比当前大
    if right < n and arr[right] > arr[largest]:
        largest = right

    # 如果发现孩子更大，就交换，并继续往下沉
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # 交换
        max_heapify(arr, n, largest)                 # 递归：继续往下检查
        

def build_max_heap(arr):
    n = len(arr)
    # 从最后一个非叶子结点开始
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)


# 测试
arr = [5, 3, 17, 10, 84, 19, 6, 22, 9]
print("原始数组:", arr)
build_max_heap(arr)
print("建堆完成:", arr)
```



##### 单个节点的 heapify 过程

1. 取当前节点 `i`，找到它的左孩子 `l = 2*i + 1`，右孩子 `r = 2*i + 2`（0-based 索引）。
2. 找出 `i`、`l`、`r` 中最大值的索引。
3. 如果最大值不是 `i`，交换 `i` 和那个最大值，然后 递归 对被交换下去的子节点继续 heapify。

```python
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)  # 递归向下调整
```



##### 构建整个堆

叶子节点天然满足堆性质，因此只需从**最后一个非叶子节点**开始。

最后一个非叶子节点索引为 `n//2 - 1`。从这个索引一路向上调用 `heapify`。

```python
def build_heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
```



#### Code

- How to achieve a heap sort?

- How to make a max heap? -> fast_version: from i = n/2 to 1, continue to do the heapify

  > 从最后一个非叶子节点开始，依次向上对每个节点做 heapify。
  >
  > 1. 完全二叉树中，叶子节点天然满足堆性质。最后一个非叶子节点的下标是 `n/2 - 1`（0-based），或 `n/2`（1-based）。
  >    - 数组长度为 `n`，下标范围是 `[0, n-1]`。一个节点 `i` 有左孩子的条件：`2*i + 1 < n`。令 `2*i + 1 = n - 1`（恰好是最后一个位置）⇒ `i = (n - 2)/2`。向下取整：`i = n//2 - 1`。从这个下标往前的节点都是非叶子节点，其后都是叶子。
  > 2. 依次对下标 `i = n/2 - 1` 到 `0`（0-based）做 `heapify`。每次 `heapify` 保证以 `i` 为根的子树满足最大堆性质。
  >    - 我们已经知道最后一个非叶子节点的下标是 `n//2 - 1`。根节点的下标是 `0`。所以所有非叶子节点的下标就是从 `n//2 - 1` 一直递减到 `0`。
  > 3. 所有节点都调整完毕后，整个数组就是一个合法的大顶堆。

- Why space complexity is O(log(n))?







## Linear Sorting

> ##### Therom: Any comparison based sorting algorithm runs in Ω(nlogs)
>
> 传统比较排序（如 Quick Sort、Merge Sort）下界是 **Ω(n log n)**。

线性排序（Linear Sorting）指的是一类平均与最坏情况时间复杂度可以做到 O(n) 的排序算法，

- **不依赖元素之间的比较**，而是利用数据的结构特征来排序。
- 线性排序打破 Ω(nlogs) 下界的前提是：**利用输入数据的“值域特性”**，直接按数据的分布或数位进行分类。

| 算法                          | 核心思想                                         | 适用条件                               | 时间复杂度                | 稳定性         |
| ----------------------------- | ------------------------------------------------ | -------------------------------------- | ------------------------- | -------------- |
| **Counting Sort**（计数排序） | 统计每个值的出现次数，并利用累积计数确定最终位置 | 数据范围 k 不大，且可映射为整数        | O(n + k)                  | ✔ 稳定         |
| **Radix Sort**（基数排序）    | 从低位到高位（或反向）逐位进行稳定排序           | 数据可以分解成“位”，如整数、定长字符串 | O(d*(n + k))，d 为位数    | ✔ 稳定         |
| **Bucket Sort**（桶排序）     | 将数据划分到多个桶中，对每个桶内局部排序再合并   | 数据分布较均匀                         | 平均 O(n + k)，最坏 O(n²) | 取决于桶内排序 |





### Counting Sort

计数排序 -> 非比较型排序

核心思想：“出现次数 + 相对顺序 = 排序结果”。

1. 扫描数组，记录每个数值出现的次数。
2. 将频次数组转成“前缀和”，用来确定每个元素在结果中的最终位置。
3. 从原数组逆序遍历，根据累积计数把元素放入输出数组，并相应减少计数值，保证**稳定性**。

```
arr = [4, 2, 2, 8, 3, 3, 1]
```

> ① 先找到最小值与最大值（这里最小值 1，最大值 8），创建 count 数组长度 = 8 - 1 + 1 = 8：
>
> | 索引（表示数值） | 1    | 2    | 3    | 4    | 5    | 6    | 7    | 8    |
> | ---------------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
> | count 初始       | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    |
> | 统计后           | 1    | 2    | 2    | 1    | 0    | 0    | 0    | 1    |
>
> ② 前缀和（累积计数）把 count 数组改成累积次数，表示“小于等于该数的元素总数”：
>
> | 索引   | 1    | 2    | 3    | 4    | 5    | 6    | 7    | 8    |
> | ------ | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
> | 累积后 | 1    | 3    | 5    | 6    | 6    | 6    | 6    | 7    |
>
> ③ 逆序遍历原数组，稳定放置。从右往左扫描 `arr`，根据当前值在累积计数中的位置放到结果数组中，同时 count 对应值减 1（if loop from left to right, it will change the relative order of items）
>
> | 原数组值 | 对应 count 位置 | 放入输出数组索引 | 输出数组变化          |
> | -------- | --------------- | ---------------- | --------------------- |
> | 1        | 1               | 0                | [1, _, _, _, _, _, _] |
> | 3        | 5               | 4                | [1, _, _, _, 3, _, _] |
> | 3        | 4               | 3                | [1, _, _, 3, 3, _, _] |
> | 8        | 7               | 6                | [1, _, _, 3, 3, _, 8] |
> | 2        | 3               | 2                | [1, _, 2, 3, 3, _, 8] |
> | 2        | 2               | 1                | [1, 2, 2, 3, 3, _, 8] |
> | 4        | 6               | 5                | [1, 2, 2, 3, 3, 4, 8] |

- 时间复杂度 `O(n + k)` = `O(n)+O(k)+O(n)`
- 空间复杂度 `O(n + k)` = `O(k)+O(n)+O(1)`

>使用条件: 
>
>1. 整数或可离散化的值，因为需要直接用值当作索引。
>2. 数值范围（k）不大 -> 若 k ≫ n，空间成本会过高。

>计数排序可以看成是一种“特殊的桶排序”，每个桶对应一个具体的整数值，桶的范围是离散的并且已经排好顺序。
>
>#### 为什么还要多做“前缀和 + 逆序填充”？取决于你对“排序结果”的要求
>
>1. 只要值本身有序 -> 这种情况下，第一步统计完直接输出就可以，和简单的桶排序几乎一样。
>
>   - 只输出纯数字（比如单纯的统计报表），
>   - 不需要保持原数组中相同元素的相对顺序，
>   - 也不需要带着其他信息（比如 ID、对象引用）一起排序，
>
>2. 需要稳定排序 或 要排序的不是单一数字
>
>   - 例如每个元素除了 key 还有其他字段（ID、结构体、记录等），
>   - 相同 key 的记录必须保持原来的相对顺序，
>
>   这时就必须用累积计数 + 逆序填充：
>
>   - 累积计数给出每个 key 最后一个元素应放的精确索引，
>   - 逆序填充确保相同 key 按原顺序排列。

```
arr = []
n = len(arr)
min_value = min(arr)
max_value = max(arr)
min_max = max_val - min_val + 1

# get frequency
count = [0] * min_max
for i in range(min_max):
		count[arr[i] - min_value] += 1

# get prefix
for i in range(0, min_max):
		count[i] += count[i-1]

# get result
res = [0] * min_max
for i in range(n-1, -1, -1):
    value = arr[i]
    position = count[val - min_val] - 1
    res[position] = value
    count[val - min_val] -= 1

return res
```







### Radix Sort

> **Radix** 是数学里“进制、基数”的意思（如十进制、二进制中的“10”“2”就是 radix）。
>
> 这个算法的本质是：按某个进制（radix）把数从最低位到最高位分解出来，然后逐位进行稳定排序。

基数排序 -> 非比较型排序

核心思想：“低位优先 + 稳定排序 = 全局有序”。

先把所有元素按个位排一次，再按十位排一次……一直排到最高位。因为每一轮都用**稳定排序**（如计数排序 Counting Sort），之前低位的相对顺序不会被破坏，所以最后整体是有序的。

```python
arr = [170, 45, 75, 90, 802, 24, 2, 66]
```

> ① 按个位 (ones place) 做稳定排序
>
> | 数字 | 个位 |
> | ---- | ---- |
> | 170  | 0    |
> | 90   | 0    |
> | 802  | 2    |
> | 2    | 2    |
> | 24   | 4    |
> | 45   | 5    |
> | 75   | 5    |
> | 66   | 6    |
>
> ```python
> # 仅按个位排，十位百位顺序仍未处理。
> [170, 90, 802, 2, 24, 45, 75, 66]
> ```
>
> ② 按十位 (tens place) 做稳定排序
>
> | 数字 | 十位 |
> | ---- | ---- |
> | 170  | 7    |
> | 90   | 9    |
> | 802  | 0    |
> | 2    | 0    |
> | 24   | 2    |
> | 45   | 4    |
> | 75   | 7    |
> | 66   | 6    |
>
> ```python
> # 个位顺序被稳定地保留下来，比如个位相同的 802 和 2 依旧保持先 802 后 2 的顺序。
> [802, 2, 24, 45, 66, 170, 75, 90]
> ```
>
> ③ 按百位 (hundreds place) 做稳定排序
>
> | 数字 | 百位 |
> | ---- | ---- |
> | 802  | 8    |
> | 2    | 0    |
> | 24   | 0    |
> | 45   | 0    |
> | 66   | 0    |
> | 170  | 1    |
> | 75   | 0    |
> | 90   | 0    |
>
> ```python
> [2, 24, 45, 66, 75, 90, 170, 802]
> ```
>
> 已整体有序。
>
> - 3 位数字：d = 3
> - 每位稳定排序 O(n + k)（十进制 k=10）
> - 总时间复杂度：O(d·(n + k)) ≈ O(3·(8 + 10)) → 线性级别。
> - 空间复杂度：O(n + k)。

```
arr = []
n = len(arr)

radix_sort(arr, n):
		max_val = max(arr)
		exp = 1  # start from tenth digit
		
		while max_val // exp > 0:
				counting_sort(arr, n, exp)
				exp = exp * 10

count_sort(arr, n, exp):
		count = [0] * 10
		res = [0] * n
		
		# get frequency
		for i in range(n):
				digit = (arr[i] // exp) % 10
				count[digit] += 1
		
		# get prefix
		for i in range(1, 10):
				count[i] += count[i-1]
		
		# for i in range(n-1, -1, -1):
				digit = (arr[i] // exp) % 10
				position = count[digit] - 1
				res[position] = arr[i]
				count[digit] -= 1
		
		for i in range(n):
				arr[i] = res[i]
```



Radix Sort = d 轮稳定排序（通常用 Counting Sort）：

1. 取出当前位的数字：O(n)
2. 一轮计数排序：O(n + k) -> 每一位都要做一次

$$
T(n) = d \times O(n + k) = O(d \cdot (n + k))
$$

- 若 k 是常数（如十进制 k=10），复杂度接近 O(d·n)。
- 如果最大值有 log₍k₎(M) 位（M 为最大数值），d ≈ O(log₍k₎ M)。例如十进制整数，d ≈ O(log₁₀ M)。
- 当 d 和 k 相对较小（典型场景），整体接近线性时间 O(n)。

每一轮稳定排序（例如计数排序）需要：

- 计数数组：O(k)
- 输出数组：O(n)
- 其他辅助变量：O(1)

$$
S(n) = O(n + k)
$$

这部分空间在每轮可以复用，所以总空间复杂度依然是 O(n + k)，而不是 O(d·(n + k))。

> 适合：整数、字符串等可以拆成“位”的数据。
>
> 数据范围：位数不宜过大，每一位的取值范围要比较小（方便做稳定排序）。



#### 为什么一定要“稳定”？

假设我们要按个位、十位、百位依次排序：

- 先排个位时，把个位相同的元素顺序固定。
- 下一轮排十位时，如果十位相同，元素的相对顺序要保持 **之前个位排序的顺序**。
- 这样当我们排到最高位时，十位、个位的顺序仍然正确——整体升序。

若这一轮排序不稳定，十位相同的元素的个位顺序可能被打乱，前几轮的工作就白做了。



#### 如何做稳定排序？

假设我们这一轮要对某一位（例如十位）的数字进行排序。步骤与普通计数排序相同，只是统计的值是“该位上的数字”。

1. 统计出现次数：遍历数组，提取当前位数字 `d`，count[d]++。
2. 前缀和（累积计数）：将 count 改成前缀和，表示 ≤ d 的元素总数。
3. 逆序遍历原数组并填入输出
   - 从右往左看原数组，提取当前位数字 d。
   - 在 count[d] 中找到它应放的位置，count[d]--。
   - 把该元素（整个原始记录，不只是那一位）放到输出数组相应位置。
   - 逆序保证相同 d 的元素保持原有相对顺序。
4. 把输出数组复制回原数组：准备进入下一轮（下一位）的排序。



#### 如何取出当前要比较的那一位数字？

把数值在“位”的意义上拆开。

在十进制，假设我们现在要处理“第 k 位”，这里的“位”从个位开始数：

- **个位**是第 0 位
- **十位**是第 1 位
- **百位**是第 2 位

$$
digit = (\frac{num}{10^k}) \text{ } mod  \text{ } 10 \\
\\
如果是基数 b，公式同理：\text{  }digit = (\frac{num}{b^k}) \text{ } mod  \text{ } b
$$

如果是定长字符串（例如 “apple”、“pear”）：

- 第 k 位字符：直接用下标取 `s[k]`。
- 如果需要转成数字（例如 'a'→0，'b'→1），用 ASCII：

```python
digit = ord(s[k]) - ord('a')
```



#### How to choose which method we should use?

什么时候我们选择radix sort更好，什么时候选择counting sort.

##### Counting Sort 适用场景

- k 和 n 同阶或者比 n 小很多，比如 k ≤ 10⁶、n 也在百万级。k 不会远大于 n。

  > 如果 k ≫ n（比如要排序的数只有几十个，但值域是 0~10¹²），count 数组会非常大，空间浪费且时间也会变成 O(k) → 不适合。

- 数据类型是整数或可直接离散化成整数索引。

- 对稳定性有要求

- 需要一次性直接得到有序结果

##### Radix Sort 适用场景

- 数据可以拆成多“位”，例如十进制整数、二进制整数、定长字符串。
- 每一位的取值范围（k）小，例如十进制一位 k=10，二进制一位 k=2。
- 数值范围很大，但“位数” d = O(log₍k₎ M) 相对较小。
- 适合排序 大整数、长字符串、固定长度 key，不希望开超大计数数组。



#### Use Computer bit language to calcualtion Time Complexity





#### Bit Operation

在实现 radix sort 时：

- 取某一位：位运算比除法快。
  - 取最低 r 位：`num & ((1 << r) - 1)`。
  - 右移 r 位：`num >> r`。

这些都是 **O(1)** 的操作，比用 `/` `%` 快。

```python
r = 8  # 每次处理8位
mask = (1 << r) - 1  # 0xFF
digit = (num >> (pass_num * r)) & mask
```

这样直接提取当前轮要比较的那 r 位。





### Bucket Sort

1. 根据元素值域和分布，将元素映射到若干区间（桶）中。
2. 每个桶内部单独排序。常用插入排序或其他适合小数据量的排序。
3. 按桶的顺序依次把桶内元素合并。

假设 **数据分布均匀** 且 **桶数量足够**：

- 平均每个桶 O(1) 或很少元素，
- 分桶 O(n)，
- 桶内排序总成本近似 O(n)。

期望时间复杂度： `O(n+k)`。其中 k 是桶的数量，若 k ≈ n 则近似 O(n)。

但**最坏情况**：所有数据都落在同一个桶里 → 退化到桶内排序算法的复杂度（如 O(n²)）。





# 2025.9.19 Divide and Conquer

一种算法设计范式（Algorithm Design Paradigm），与动态规划、贪心、回溯并列。

> 依赖递归与子问题独立性，也是分析递归复杂度（主定理、递归树法）的核心应用场景。

1. **Divide（分）**：把规模为 `n` 的问题拆成若干个**规模更小**的子问题（一般同构、规模约 `n/b`）。
2. **Conquer（治）**：递归解决子问题；当规模足够小时直接求解（base case）。
3. **Combine（合）**：把子问题的解**合并**成原问题的解（如归并排序里的“归并”）。



## 典型递推模型

$$
T(n) = a * T(n/b) + f(n) \\
\text{a：子问题个数}\\
\text{n/b：单个子问题规模}\\
\text{f(n)：分解与合并的开销}\\
$$



## 复杂度怎么分析：递归树 & 主定理



### Recursion Tree

把递归展开成树：

- 第 0 层：成本 `f(n)`
- 第 1 层：有 `a` 个子问题，每个成本 `f(n/b)`，总成本 `a·f(n/b)`
- …
- 第 k 层：`a^k · f(n/b^k)`
- 叶子层深度约 `log_b n`，把各层成本相加即总复杂度。



### Master Theorem







## Order Statistics

在一个含 n 个元素的无序数组中：

- **第 k 小元素**（the k-th order statistic） = 按升序排列后排在第 $k$ 个位置的元素。
  - k=1：最小值（minimum）。
  - k=n：最大值（maximum）。
  - k=n/2：中位数（median）。

所以 最小值、最大值、中位数 都是 Order Statistics 的特例。



### 常见问题

1. 找最小/最大：O(n)，只需扫描一遍数组。
2. 同时找最小和最大：可以优化成 approx 1.5n 次比较（成对比较）。
3. 找第 k 小元素（最重要）：
   - 排序法：排序后取第 k 个，时间 O(n log n)。
   - heap法：全部构建 或者 构建size为k的heap。从空间复杂度的角度考虑，限定size为k的方法更好。
   - 改进算法：不需要全排序，只找第 k 小，能做到 线性时间。



### Partition -> Divide & Conquer

Find kth smallest number

```
find_kth_smallest(arr, k):
		pivot_index = partition(arr)
		if pivot_index == k-1:
				return arr[pivot_index]
		elif pivot_index > k-1:
				return find_kth_smallest(arr[:pivot_index], k)
		else:
				return find_kth_smallest(arr[pivot_index + 1:], k - (pivot + 1))
```

```
partition(arr, low, high):
		pivot = arr[high]
		i = low
		for j in range(low, high):
		    if arr[j] <= pivot:
		    		arr[i], arr[j] = arr[j], arr[i]
		    		i += 1
		arr[i], arr[high] = arr[high], arr[i]
		return i

find_kth_smallest(arr, low, high, k):
		if low <= high:
        pivot_index = partition(arr, low, high)
        if pivot_index == k - 1:
            return arr[pivot_index]
        elif pivot_index > k - 1:
            return quickselect(arr, low, pivot_index - 1, k)
        else:
            return quickselect(arr, pivot_index + 1, high, k)
```





## Count inversions

在一个数组 `arr` 中，如果一对元素满足：
$$
i < j \text{并且 } arr[i] > arr[j]
$$
就称 `(i, j)` 是一个 逆序对 (inversion)。

>例子： `arr = [2, 4, 1, 3, 5]`
>
>- 逆序对有 `(2,1), (4,1), (4,3)`
>- 总数 = 3



### Merge -> Divide & Conquer

```
split(arr):
		if len(arr) == 1:
				return arr, 0
		
		mid = len(arr) // 2
		left, left_count = split(arr[:mid])
		right, right_count = split(arr[mid:])
		
		merged, merged_count = merge(left, right)
		
		return merged, left_count + right_count + merge_count

merge(arr1, arr2):
		count = 0
		res = []
		p1, p2 = 0, 0
		n1, n2 = len(arr1), len(arr2)
		
		while p1 < n1 and p2 < n2:
				if arr[p1] <= arr2[p2]:
						res.append(arr[p1])
						p1 += 1
				else:
						res.append(arr2[p2])
						count += n1 - p1
						p2 += 1
		
		res.extend(arr1[p1:])
		res.extend(arr2[p2:])
    return res, count
						

count_inversion(arr):
		_, count = split(arr)
		return count
```



T(n) = 2 T(n/2) + nlogn 推理过程？





# 25.10.3 Divide & Conquer 



## Large Integer Multiplication

如何在编程里处理超出机器整型范围的数相乘。

- int 32
  >最小值：−2³¹ = −2,147,483,648
  >
  >最大值：2³¹ − 1 = 2,147,483,647

- int 64
  >最小值：−2⁶³ = −9,223,372,036,854,775,808
  >
  >最大值：2⁶³ − 1 = 9,223,372,036,854,775,807

`int32`、`int64` 都有上限，一旦超过就会溢出，所以需要专门的方法。

> 模拟乘法（字符串实现）在不支持大整数的语言（比如 C 里只有 `int64`），就需要用字符串 + 模拟竖式乘法：
>
> - 把两个大数用字符串存储；
> - 每一位逐个相乘，然后进位处理；
> - 最后得到结果字符串。
>
> $$
> T(n)=O(n^2)
> $$

对于特别大的整数（上百万位），普通竖式乘法太慢，需要更高级的算法：

- Karatsuba 算法：分治思想，把大数拆成小块，复杂度降到 O(n^1.585)。
- Toom-Cook 算法：进一步推广 Karatsuba。
- FFT (Fast Fourier Transform) 快速傅里叶变换乘法：把乘法转化为卷积，复杂度降到 O(n log n)。
- NTT (Number Theoretic Transform)：FFT 在整数域的变体，用模数运算保证精度。

这些算法就是现代大整数库（如 GMP、Java BigInteger 内部）在背后实现的优化。



### 数的进制展开（Positional Notation / 基数展开）

$$
x = 1234 = 12 * 10 ^ 2 + 34\\
\\
12 -> \text{2 digits}\\
10^2 -> \text{shifting digits}\\
34 -> \text{2 digits}
$$

把一个整数按位数（digit）进行拆分：数的进制展开（Positional Notation / 基数展开）

> 任何整数都可以写成某个基数（base）的展开式，这种“拆成高位 × 基数^位数 + 低位”的方法，本质上就是进制展开的一种分块方式。

$$
1234=1×10^3+2×10^2+3×10^1+4×10^0
$$





### 大整数乘法（Karatsuba Algorithm）优化过程

$$
\text{假设有两个 n 位数，可以写成：}\\
x=a×10^m+b\\
y=c×10^m+d\\
\text{其中 a,c 是高位，b,d 是低位。} \\
\\
\text{做乘法时，可以利用这种拆分减少计算量: }\\
x * y \\
= (a×10^m+b) * (c×10^m+d)\\
= ac×10^{2m}+(ad+bc)×10^m+bd\\
\text{这里一共要算 4 次乘法：}\\
ac, \\ad, \\bc, \\bd.\\ \text{再加上一些加法和移位}\\
T(n) = 4 * T(\frac{n}{2}) + O(n) = o(n^2)\\
\\
\text{但是 ad+bc=(a+b)(c+d)−ac−bd} \\
\text{也就是说，我们不用单独算 ad 和 bc，只要多算一次 (a+b)(c+d)，然后减去 ac 和 bd 就行了。}\\
\text{于是，整个乘法只需要 3 次乘法：}\\ 
ac, \\bd, \\(a+b)(c+d)\\ \text{再加上一些加法和移位}\\
T(n)=3T(\frac{n}{2}) + O(n) = O(n^{log_23}) = O(n^{1.585})
$$





### RSA（Rivest–Shamir–Adleman）

最经典的公钥加密算法之一。

RSA 的关键点在于**加密和解密用的是不同的密钥**：

- 公钥 (public key)：对外公开，用来加密。
- 私钥 (private key)：自己保管，用来解密。

安全性依赖于 **大整数因数分解的困难性**。给一个几百位、上千位的大整数 `N = p × q`，想要分解出它的质因数 `p` 和 `q`，在计算上几乎不可能（经典计算机在可接受时间内做不到）。



#### 密钥生成

1. 选择两个大质数 `p` 和 `q`（一般几百位甚至上千位）。因为后面用到的欧拉函数 φ(N) = (p-1)(q-1) 在质数情况下公式最简单。

2. 计算 `N = p × q`，这个就是模数，公钥和私钥都会用到。

3. 计算欧拉函数 `φ(N) = (p-1)(q-1)`。
   >φ(N) 的定义是：小于 N 的数中，有多少个数与 N 互质。
   >
   >但对于 N = p×q（p、q 为质数），公式可以简化为：
   >$$
   >φ(N)=(p−1)(q−1)
   >$$
   >

4. 选择一个整数 `e`，满足 `1 < e < φ(N)` 且 `gcd(e, φ(N)) = 1`。（常用 `e = 65537`，既安全又高效）。

5. 计算 `d = e^(-1) mod φ(N)`，也就是 `e·d ≡ 1 (mod φ(N))`。

- 公钥就是 (N, e)
- 私钥就是 (N, d)





## Binary Search Tree





### BST

```python
class TreeNode:
  def __init__(self, key):
    self.key = key
    self.left = left
    self.right = right
```

```python
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    # 插入
    def insert(self, key):
        self.root = self._insert(self.root, key)
    
    def _insert(self, node, key):
        if node is None:   # 找到空位置插入
            return TreeNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        # 如果相等，可以选择忽略 或 允许重复（这里忽略）
        return node
    
    # 查找
    def find(self, key):
        return self._find(self.root, key)
    
    def _find(self, node, key):
        if node is None:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self._find(node.left, key)
        else:
            return self._find(node.right, key)
    
    # 删除
    def delete(self, key):
        self.root = self._delete(self.root, key)
    
    def _delete(self, node, key):
        if node is None:
            return None
        
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:  
            # 找到节点，分情况
            if node.left is None:   # 只有右子树或无子树
                return node.right
            elif node.right is None:  # 只有左子树
                return node.left
            else:
                # 有两个子树：找右子树的最小节点替代
                min_larger_node = self._minValueNode(node.right)
                node.key = min_larger_node.key
                node.right = self._delete(node.right, min_larger_node.key)
        return node
    
    def _minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
```

| 操作              | 时间复杂度 (平衡树 O(log n)) | 时间复杂度 (最坏 O(n)) | 空间复杂度                |
| ----------------- | ---------------------------- | ---------------------- | ------------------------- |
| `insert`          | O(log n)                     | O(n)                   | O(h) = O(log n) ~ O(n)    |
| `delete`          | O(log n)                     | O(n)                   | O(h)                      |
| `find`            | O(log n)                     | O(n)                   | O(h)                      |
| `Min` / `Max`     | O(log n)                     | O(n)                   | O(1) (迭代) / O(h) (递归) |
| `findPredecessor` | O(log n)                     | O(n)                   | O(h)                      |
| `findSuccessor`   | O(log n)                     | O(n)                   | O(h)                      |





#### find

```python
def find(k, root):
  if not root:
    return False
  
  if k == root.val:
    return True
  elif k < root.val:
    return find(k, root.left)
  return find(k, root.right)
```

O(h) -> h is the height of the binary search tree

- 平均情况（树平衡）：O(log n)
- 最坏情况（树退化成链表）：O(n)



#### insert

```python
def insert(key, root):
  if not root:
    return Node(key)
  
  if key == root.val:
    return root
  elif key < root.val:
    root.left = insert(key, root.left)
  else:
    root.right = insert(key, root.right)
  
  return root
```

- 时间：`O(h)` → 平衡时 `O(log n)`，最坏 `O(n)`
- 空间：`O(h)`（递归栈）





#### min/max

```python
def Min(key, root):
  if not root:
    return root.value
 	
  return min(key, root.left)
```

```python
def Max(key, root):
  if not root:
    return root.value
 	
  return max(key, root.right)
```

- 时间：`O(h)`
- 空间：`O(1)`（迭代版） / `O(h)`（递归版）



#### delete

删除操作的三种情况

- 没有子节点（叶子）直接删掉 → 返回 `None`。
- 只有一个子节点 -> 用子节点替换自己。
- 有两个子节点，不能直接删，否则会断开一部分树。-> 找 右子树的最小值 (inorder successor)，替换当前节点的值，再在右子树递归删除那个最小值。（也可以用左子树的最大值，效果一样）。

```python
def delete(key, root):
  if not node:
    return None
  
  if key < root.value:
    root.left = delete(key, root.left)
  elif key > root.value:
    root.right = delete(key, root.right)
  else:
    # find the target node: 真正的删除
    # 分情况讨论
    if not root.left and not root.right:
      return None
    elif not root.left:
      return root.right
    elif not root.right:
      return root.left
    else:
      min_larger_node = Min(root.right)
      root.val = min_larger_node.val
      root.right = delete(min_larger_node.val, root.right)
  
  return root
```

- 先查找目标节点：`O(h)`
- 处理三种情况：
  1. 无子节点：`O(1)`
  2. 一个子节点：`O(1)`
  3. 两个子节点：需要找右子树最小值 → `O(h)`

**复杂度：**

- 时间：`O(h)` → 平衡时 `O(log n)`，最坏 `O(n)`
- 空间：`O(h)`（递归栈）





#### find predecessor & successor of any node

- 前驱 predecessor：比当前节点小的最大值
- 后继 successor：比当前节点大的最小值

这其实就是在 中序遍历序列 下，一个节点的前一个和后一个节点。

要找 `node` 的前驱：

- 如果 有左子树 → 前驱 = 左子树里一路向右走的最大节点。
- 如果 没有左子树 → 前驱一定在它的祖先里，往上找 最后一个比 node 小的祖先。

要找 `node` 的后继：

- 如果 有右子树 → 后继 = 右子树里一路向左走的最小节点。
- 如果 没有右子树 → 后继一定在它的祖先里，往上找 最后一个比 node 大的祖先。

```python
def findPredecessor(root, key, pre=None):
    if not root:
        return pre
    
    if key == root.val:
        # 如果有左子树，前驱是左子树的最大值
        if root.left:
            tmp = root.left
            while tmp.right:
                tmp = tmp.right
            return tmp
        return pre
    
    elif key < root.val:
        # 去左子树，前驱不变
        return findPredecessor(root.left, key, pre)
    else:
        # 去右子树，当前 root 可能是前驱
        return findPredecessor(root.right, key, root)
```

- 按 BST 性质查找 `key` → `O(h)`
- 如果有左子树，还要往左子树里一路右走 → `O(h)`

**复杂度：**

- 时间：`O(h)`
- 空间：`O(h)`（递归栈）

```python
def findSuccessor(root, key, suc=None):
    if not root:
        return suc
    
    if key == root.val:
        # 如果有右子树，后继是右子树的最小值
        if root.right:
            tmp = root.right
            while tmp.left:
                tmp = tmp.left
            return tmp
        return suc
    
    elif key < root.val:
        # 去左子树，当前 root 可能是后继
        return findSuccessor(root.left, key, root)
    else:
        # 去右子树，后继不变
        return findSuccessor(root.right, key, suc)
```

和前驱完全对称，也是：

- 时间：`O(h)`
- 空间：`O(h)`





### Tree Traversal

```python
res = []
def pre_prder(root):
  if not root:
    return
  
  res.append(root)
  pre_prder(root.left)
  pre_prder(root.right)
```

```python
res = []
def in_prder(root):
  if not root:
    return
  
  in_prder(root.left)
  res.append(root)
  in_prder(root.right)
```

```python
res = []
def post_prder(root):
  if not root:
    return
  
  post_prder(root.left)
  post_prder(root.right)
  res.append(root)
```



### Construct 还原

- LeetCode 105. Construct Binary Tree from Preorder and Inorder Traversal

- LeetCode 106. Construct Binary Tree from Inorder and Postorder Traversal

- LeetCode 889. Construct Binary Tree from Preorder and Postorder Traversal

- eetCode 1008. Construct Binary Search Tree from Preorder Traversal

- LeetCode 654. Maximum Binary Tree






### Balanced BST

普通 BST 的所有操作复杂度取决于树的高度 `h`。如果树退化成链表，高度 = `n`，操作就变成 **O(n)**，很差。

平衡 BST 通过保持树的高度接近 `O(log n)`，保证所有操作都能在对数时间内完成。



#### 平衡条件

不同的平衡树用不同的规则保持“平衡”：

##### AVL 树

- 每个节点的左右子树高度差 ≤ 1

- 插入/删除时可能要旋转（左旋、右旋）来恢复平衡

- 查找非常快，接近完美平衡


##### 红黑树 (Red-Black Tree)

- 每个节点是红/黑色
- 保证从根到叶子路径上的黑色节点数相同
- 比 AVL 树稍微“松一点”，旋转次数更少 → 插入/删除更高效

> 实际上很多库里的 `map` / `set`（如 C++ STL、Java TreeMap/TreeSet）就是红黑树实现

##### B-Tree / B+Tree

- 用于磁盘和数据库索引（MySQL 索引就是 B+Tree）
- 一个节点能存多个 key，减少磁盘 IO

##### Treap / Splay Tree

- Treap：结合堆和 BST，利用随机化保持平衡
- Splay Tree：每次访问后通过旋转把节点“拉到根”，适合有访问局部性的数据



#### Rotation

旋转 (Rotation) 是平衡 BST（AVL、红黑树等）里最核心的操作，用来在插入或删除后“拉直”树。

##### Right Rotation



##### Left Rotation



##### 双旋转

- LR 型 (Left-Right)：先左旋 `x` 的左子树，再右旋 `y`
- RL 型 (Right-Left)：先右旋 `y` 的右子树，再左旋 `x`







## Hashing

- BST = 基于排序的动态集合结构
- Hashing = 基于数组映射的动态集合结构

> BST 用二叉搜索树来存数据，能做 insert / delete / find，时间复杂度取决于高度。普通 BST 最坏 O(n)，Balanced BST (AVL、红黑树) 能做到 O(log n)。
>
> Hashing (哈希) 用哈希函数把 key 映射到一个数组下标。理论上 find/insert/delete 都是 O(1) 平均时间。可能有冲突（collision），需要链表、开放寻址等方法处理。

Map/Set 在编程语言的库实现里：

- 基于 BST 的实现：
  - Java `TreeMap` / `TreeSet` = 红黑树
  - C++ STL `map` / `set` = 红黑树
  - 特点：支持有序遍历（中序遍历就是排序结果），复杂度 O(log n)
- 基于 Hash 的实现：
  - Java `HashMap` / `HashSet`
  - C++ `unordered_map` / `unordered_set`
  - 特点：平均 O(1) 查找，但无序

这几块其实都是在回答同一个问题：如何存一堆 key，并且支持快速的 insert / delete / find？

- 最简单：数组（无序/有序），但是效率差
- 升级版：BST（动态，支持排序）
- 更高效：Balanced BST（O(log n)）
- 另一种思路：Hashing（平均 O(1)）

最终抽象：Map / Set 接口，具体实现可能用 BST，也可能用 Hash





### Map & Set

```
Map<k, v>
Set<k>

dynamic set of keys
- insert
- delete
- find

# 无序数组 (Unsorted Array) -> 插入快，查找/删除慢。
- insert  O(1)
- delete  O(n)
- find    O(n)

# 有序数组 (Sorted Array) -> 查找快，插入/删除慢。
- insert  O(n)
- delete  O(n)
- find    O(log n)
```

>- 普通的 Map / Set Map<K,V>: 一组 键–值对，键唯一，每个键对应一个值。
>- Multimap / Multiset: 允许 同一个键出现多次，一个键可以对应多个值。数据库一对多关系，比如“一个学生可以选多门课”



### Pre-hash

把任意类型的 key 转换成一个整数。

- uniqueness
- simple & fast

```
Pre-hash: key (string/obj) → big integer
```

> 用数组下标来快速存取 key，但 key 可能不是整数（比如字符串、对象）。

- 如果 key 已经是整数（比如学号 20231001），可以直接用。

- 如果 key 是字符串（比如 "Alice"），就要把它转换成整数
  >1. 按字符编码（ASCII/Unicode）转成数字
  >
  >2. 再用某种方法组合，比如：
  >
  >   ```
  >   "abc" → (97 * 31^2 + 98 * 31^1 + 99 * 31^0)
  >   ```
  >
  >   这里的 `31` 是常见的多项式 hash 基数（Polynomial rolling hash）。



#### **Functions**

- ASCII / Unicode 累加: 把字符串每个字符转成整数（ASCII/Unicode），再相加。
  >```
  >"abc" → 97 + 98 + 99 = 294
  >```
  >
  >缺点：顺序信息丢失，容易冲突（不满足unique的要求）。

- **多项式 Rolling Hash（最常见）**: 给字符串一个进制系数 `p`（常用 31 或 131），逐位累积：
  
  >```
  >"abc" → 97 * p^2 + 98 * p^1 + 99 * p^0
  >```
  >
  >保留了顺序，冲突率比单纯加和低。很多编程语言和算法里用这个，比如 Rabin–Karp 字符串匹配。
  >
  >
  >
  >多项式哈希 (Polynomial Hash) 用质数，最典型的例子就是字符串的 rolling hash：
  >$$
  >H(s) = (s_0*p^{n-1} + s_1*p^{n-2} + ··· + s_{n-1}) \text{ } mod \text{ } M
  >$$
  >
  >- `p`：一般取一个 质数基数，比如 31、131、257。
  >- `M`：通常是一个大质数模数，比如 $10^9+7$、$2^{61}-1$。Pre-hash function do not include `mod m`.
  >
  >
  >
  >为什么要用 prime？
  >
  >保证不同组合更容易产生不同结果（减少冲突）。如果 p 不是质数，可能出现“分解重复”的情况（类似代数里质因数分解的唯一性）。用 prime 可以让 hash 分布更均匀。
  >
  >如果你用 `mod M`，而 M 是质数，数学上会构成一个 有限域 (finite field)。在这个域里，乘法/加法/逆元都有良好的性质。避免很多“周期性冲突”。如果 M 不是质数（比如 1000），很多不同的数模 M 会更容易撞在一起。
  
- 乘法散列 (Multiplicative Hash): 适用于整数
  >```
  >h(k) = floor(m * (k * A mod 1))
  >```
  >
  >其中 `A` 是 [0,1) 的无理数常数，比如黄金比例 (√5 - 1)/2。理论上分布比较均匀。

- 系统级函数: 很多语言库里都有内置的 pre-hash
  >- Java → `Object.hashCode()`
  >- Python → `hash()`
  >- C++ → `std::hash`



#### operations

- +: 把 key 的各部分数值直接加起来。
- xor: 常用在整数和 bit 层级的哈希。把不同字段的值 XOR 起来，达到混合的效果。XOR 有对称性和可逆性，比加法更能区分不同组合。还是可能冲突，顺序依旧不敏感。
- prime number: 把 key 的不同部分按顺序乘以质数再累加。质数在模运算下更容易保证 hash 分布均匀，避免不同组合重复分解，减少冲突。







### **Hash**

**哈希函数 (hash function)** 就是把大整数压缩到数组范围内：

```
h(k) = (prehash(k)) mod m
```

- `prehash(k)` = 预哈希结果（大整数）
- `m` = 数组大小（通常取素数，比如 1009）
- `h(k)` = 哈希表里的索引

> 预哈希得到的整数可能非常大，不能直接作为数组下标。
>
> ```
> "abc" → prehash = 1234567 → h("abc") = 1234567 mod 1009 = 777
> ```
>
> 把任意 key 映射到 `[0, m-1]` 的下标范围。



#### 均匀分布

哈希函数的本质就是：**把大范围的整数压缩映射到小范围 `[0, m-1]`，同时尽量保证均匀分布**。

如果分布不均匀 → 一些槽位特别拥挤，另一些槽位空着。那么冲突（collision）就会很多，性能退化。理想情况是每个槽位的 key 数量差不多。



#### 装载因子 (load factor) 

$$
α= \frac{n}{m}
$$

- `n` = 当前存储的 key 数
- `m` = 哈希表大小（槽位数）

一般要求：

- `α` 太大 → 冲突太多，性能退化
- `α` 适中（比如 0.5 ~ 0.75） → 查找和插入仍然接近 O(1)

如果 `m` 是质数：`(prehash(k) mod m)` 的分布更均匀，避免很多整数模式导致集中映射

> 判断哈希表的利用率（load factor, α）是否合理？
>
> 其实就是判断装载因子 (load factor) 有没有超过经验阈值。利用率 α = n/m，越接近 1 越容易冲突；通常保持在 0.5~0.75 之间。
>
> 假设：
>
> - `n` = 已插入元素数（当前键数量）
> - `m` = 哈希表的槽位数（数组长度）
>
> 只要你知道这两个值，就能即时算出 α。如果只知道「表中剩余空位」或「碰撞情况」，可以估算：利用率 ≈ 已用槽位 / 总槽位，平均链表长度 ≈ α，在链地址法中，每个槽挂的链表平均长度就是 α。
>
> | 哈希表类型                    | 推荐 α 最大值        | 说明                              |
> | ----------------------------- | -------------------- | --------------------------------- |
> | 开放寻址（Open Addressing）   | ≤ 0.5                | 因为冲突导致线性探测变慢          |
> | 链地址法（Separate Chaining） | ≤ 0.75               | 每个槽可挂链表，但太满仍会退化    |
> | Java HashMap                  | 0.75                 | 默认阈值（`DEFAULT_LOAD_FACTOR`） |
> | C++ unordered_map             | 默认 1.0，可手动设定 |                                   |

监控 α，一旦超过阈值 → 触发扩容（rehash）。



#### How To choose m?

**尽量取质数**：避免 `key mod m` 出现周期性冲突。保证 m ≈ n / α_target

> 比如希望 α ≤ 0.75，且预计最多插入 900 元素，则：
>
> ```
> m ≈ 900 / 0.75 = 1200
> ```
>
> 再取一个接近 1200 的质数，比如 1201。

 `m`（哈希表大小）应该是**动态的**

> 假设哈希表容量（`m`）固定：当不断插入元素时，`n` 逐渐增大；而 `m` 不变 ⇒ `α` 不断上升；`α` 越大，冲突（collision）就越多。
>
> 冲突多了会造成什么后果？
>
> - 链地址法（chaining）每个槽位挂一个链表；冲突越多，链表越长；查找/插入平均复杂度从O(1) → O(α) → 最坏 O(n)（全挤在一个链表里）。
> - 开放寻址法（open addressing）插入时一旦冲突，要不断线性探测、二次探测；当表“快满”时，空槽越来越少；探测序列越来越长，性能急剧下降。
>
> 不动态调整 `m`，哈希表性能会从近似 O(1) 退化成 O(n)。





### Design Hash Function

#### Division Method

最简单、最常用的哈希函数形式：
$$
h(k)=k\text{ }mod\text{ }m
$$
其中：

- `k`：键值（key）
- `m`：哈希表的大小（槽位数）

直接对 key 取模，将结果映射到 `[0, m-1]` 的范围。



##### **如何选 `m`?**

关键点：如何选 `m`

选不好 `m`，容易产生模式冲突（pattern collision）： 一般建议 取质数（prime number），尤其当 key 分布具有某种线性或周期规律时更安全。
$$
m ≈ 质数，且略大于预计元素数 / 负载因子
$$




#### Multiplication Method

利用 key 的小数部分分布来均匀映射：
$$
h(k) = [m * (kA\text{ }mod\text{ }1)]
$$
其中：

- `A` 是一个 0～1 之间的常数（通常取 **无理数**，例如黄金比例相关值）；
- `(kA mod 1)` 表示取 `kA` 的小数部分；
- `m` 是哈希表大小。
- `k`：键值

$$
\text{乘法法的计算机实现形式}\\
h(x)=a×x \text{ } mod\text{ }2^{32}
$$

计算机不能直接用浮点数去取小数部分，也不会真的去算 “`mod 1`”。所以在实现时，我们把它变形成纯整数运算版本。相当于取：x 乘以一个固定常数 a 的低 32 位部分。这正是 `(kA mod 1)` 在整数世界的对应操作！

在 32 位机器上，整数的计算会自动 mod 2^{32}，也就是说：任意 32 位整数乘法的结果，只保留低 32 位。所以 “`a * x mod 2^32`” 实际上是“取乘积的低 32 位”。

> Knuth（《The Art of Computer Programming》）建议：
> $$
> A=\frac{\sqrt{5} - 1}{2} ≈ 0.6180339887
> $$
> 这样 `(kA mod 1)` 的分布非常均匀。

> 分布更均匀，对模式冲突不敏感
>
> 需要浮点乘法和取整，略慢于除法法





##### **How to choose table size (m)?**

对 `m` 的要求不高（不需要是质数）

> 在 除法法（Division Method） 中，`h(k) = k mod m` 的结果直接依赖于 `m` 的数值特性（尤其是二进制低位或周期性模式）。所以：如果 `m` 是 2 的幂 → 容易让低位模式重复，分布不均。需要选择质数 `m` 才能打破这种模式。
>
> 而在 乘法法 中：`kA` 先被乘上一个无理数 `A`；再取小数部分 `(kA mod 1)`；小数部分的分布几乎与 `m` 无关，是均匀的。`m` 只是把这个 `[0,1)` 区间划分成 m 份。
>
> - `m` 越大 → 区间划分越细（哈希表槽位更多，分辨率更高）；
> - `m` 越小 → 区间划分越粗（可能多个 key 落入同一个槽）；
>
> 但不管 `m` 是多少，这些点在 [0,1) 上的分布仍然是均匀的。这<u>意味着哈希值的随机性主要由 `A` 提供</u>，而不是由 `m` 控制。因此 `m` 只决定了映射的“分辨率”，而不会影响均匀性。

| 目标                                | 建议选择                                       |
| ----------------------------------- | ---------------------------------------------- |
| 想让计算更快                        | 取 2 的幂：`m = 2^p `（常取 2 的幂以加快计算） |
| 想要更细的分布控制                  | 任意整数都行，比如 1000, 1024, 2048            |
| 实现上与内存对齐方便（如底层C实现） | `m = 2^p` 更高效，因为可以用位运算代替乘除     |

>若使用 乘法法 + m = 2^p：
>$$
>h(k)=⌊2p×(kA \text{ }mod\text{ } 1)⌋
>$$
>或者更常见的实现变形：
>$$
>h(k)=(k×A_{fixed})≫(w−p)
>$$
>其中：
>
>- `A_fixed` 是把 `A` 的小数部分编码进整数的常数；
>- `w` 是字长（例如 32 位或 64 位）；
>- `>> (w - p)` 表示右移取高位。
>
>右移操作 (`>>`) 在硬件层面非常快，比除法快得多。当 `m = 2^p` 时，可以：
>
>- 用位移代替乘除；
>- 用掩码代替取模（`k & (m - 1)`）；
>- 大幅降低 CPU 指令开销。





### Uniqueness & Collision

理想情况下，我们希望 每个 key 经过哈希函数后，都能映射到唯一的位置。这样的话，`insert` / `find` / `delete` 都是 O(1)，完美无缺。但问题是：数组大小有限，而 key 的空间无限大。

> 为什么一定会有 Collision
>
> ```
> h(k) = prehash(k) mod m
> ```
>
> 即使 prehash(k) 不一样，取模之后可能结果相同。这就是 鸽笼原理 (Pigeonhole Principle)：如果有更多的鸽子（key）要放进比鸽子数量少的鸽笼（数组槽位），一定会有多个鸽子挤在同一个笼子里。

处理 Collision 常见的方法有两大类：

- 链地址法 (Chaining) 每个数组槽位放一个 链表/动态数组。冲突的元素都挂在同一个链表里。查找时只要扫描该槽位的链表。平均复杂度 O(1)，最坏 O(n)。

- 开放寻址法 (Open Addressing) 不用链表，所有元素直接存数组里。如果位置被占，就找下一个位置（根据某种规则）。

  >线性探测 (Linear Probing)：往后找 `h(k)+1, h(k)+2 ...`
  >
  >平方探测 (Quadratic Probing)：往后跳 `+1², +2² ...`
  >
  >双重哈希 (Double Hashing)：用第二个哈希函数来决定步长。



#### **Handle Collision**

当两个不同的 key 通过哈希函数映射到了同一个槽位（index）时，就发生了冲突 (collision)。我们需要“碰撞解决策略”：

| 方法                          | 思想                       | 例子                             |
| ----------------------------- | -------------------------- | -------------------------------- |
| 链地址法（chaining）          | 每个槽挂一个链表           | Java HashMap                     |
| 开放寻址法（open addressing） | 冲突时往下找空位           | C++ `unordered_map` 内部策略之一 |
| 双重哈希（double hashing）    | 冲突时用第二个哈希函数跳探 | Hash probing                     |



##### chaining

在开放寻址法里，最常见的探测方式是：
$$
h_i(k) = (h(k) + i)\text{ } mod\text{ } m
$$
这里 `m` 是哈希表的大小。如果 `m` 选得不好，比如是 `2^p`，则 `(h(k) + i) mod m` 的探测序列可能会陷入循环，不能遍历到所有槽位。

当 `m` 是质数时：模运算 `(h(k) + i) mod m` 能保证在探测时遍历表中所有槽位；不会出现提前循环；冲突分布更均匀。

> 常用的质数表长会选 23、31、37、41……



###### len of linked list

在链地址法中：
$$
\alpha = \frac{n}{m}
$$
其中：

- n：表中存储的元素总数（所有 key 的总数）
- m：哈希表中“槽位”的个数（即链表的数量）

那么：

> 平均每条链表的长度 = α

| 操作 | 平均时间复杂度 | 最坏情况 | 说明                   |
| ---- | -------------- | -------- | ---------------------- |
| 插入 | ( O(1) )       | ( O(n) ) | 插入到链头             |
| 查找 | ( O(1 + α) )   | ( O(n) ) | 平均只需扫描 α 个元素  |
| 删除 | ( O(1 + α) )   | ( O(n) ) | 需遍历链表查找目标节点 |





##### open addressing

当插入一个 key 时，如果它的槽位已经被占用（发生冲突），就 “继续往下找空位” 来存放这个 key。

> 整个哈希表就是一个大数组，所有元素都存放在这个数组里，不再使用链表。如果被占了，就往下找下一个空格。

$$
设初始哈希位置为：\\
h_0(k) = h(k)\\
\\
若槽位已占，则第 i 次探测位置：\\
h_i(k) = (h(k)+f(i))\text{ }mod\text{ }m
$$

其中：

- `f(i)` 是探测序列函数；
- `m` 是表长；
- `i` 从 0 开始。

| 探测方式                      | 探测函数 f(i)      | 特点                               |
| ----------------------------- | ------------------ | ---------------------------------- |
| 线性探测（Linear Probing）    | `f(i) = i`         | 简单但易聚集（primary clustering） |
| 平方探测（Quadratic Probing） | `f(i) = i²`        | 缓解聚集问题，但需 m 特定选取      |
| 双重哈希（Double Hashing）    | `f(i) = i * h2(k)` | 分布最均匀，性能最好               |



###### insert

当插入键 `k` 时，从初始槽位开始探测，
 遇到：

- 空槽（`EMPTY`）→ 插入；
- 相同 key → 覆盖（更新）；
- 已删除槽（`DELETED`）→ 可作为候选插入点；
- 否则继续往下探测。

```
def insert(key, value):
    for i in range(m):
        j = (h(key) + i) % m
        if table[j] is EMPTY or table[j] is DELETED:
            table[j] = (key, value)
            return
        elif table[j].key == key:
            table[j].value = value  # update
            return
    raise OverflowError("Hash table is full")
```



###### find

探测路径与插入一致：

- 若在探测中遇到 key → 找到；
- 若遇到空槽（`EMPTY`）→ 说明 key 不存在；
- 若遇到 `DELETED` → 继续往下探测（不能停止！）。

```
def find(key):
    for i in range(m):
        j = (h(key) + i) % m
        if table[j] is EMPTY:
            return None  # 不存在
        elif table[j] is not DELETED and table[j].key == key:
            return table[j].value
    return None
```



###### delete

不能直接把槽设为空（`EMPTY`），否则查找可能提前终止（破坏探测链）。所以要用一个特殊标记：**墓碑（tombstone）** 表示“这个位置之前有元素，但被删除了”。

```
def delete(key):
    for i in range(m):
        j = (h(key) + i) % m
        if table[j] is EMPTY:
            return  # key 不存在
        elif table[j] is not DELETED and table[j].key == key:
            table[j] = DELETED
            return
```

>###### 如果在哈希表（开放寻址法）中删除一个中间的元素，要不要把后面的元素往前“推”来填空？
>
>不能推！只能打上“删除标记”（tombstone）。删除元素时，不是真的清空格子，而是打上一个特殊标记：`DELETED`（表示这个位置以前有人，但现在空了）。
>
>- 查找（find） 时，遇到 `DELETED` 不停止，继续往下探测。 → 所以仍能找到 `24`。
>- 插入（insert） 时，遇到 `DELETED` 可以复用这个位置。→ 所以以后可以在 4 号位重新放新元素。
>
>在 开放寻址法（Open Addressing） 中，每个元素都是通过一条固定的“探测序列”找到自己位置的。如果你“删除 17”然后把 24 往前推，那么问题出现了：24 的哈希位置是 3（`24 mod 7 = 3`），查找时程序会从槽 3 开始找，探测顺序是 3→4→5，但当它到 4 时，认为“4 不是原来的 24 的探测路径”，结果可能跳过或提前停止，导致查找失败！
>
>也就是说，一旦你移动了元素的位置，整个“探测链”就被破坏，哈希表的逻辑失效。

soft delete（软删除）对应了开放寻址哈希表中那种“打墓碑标记（tombstone）”的做法。

>当你“删除”一个元素时，不真的移除它，而是给它打一个特殊标记（例如 `DELETED`、`isDeleted=true`），表示它逻辑上被删除，但物理上仍留在数据结构中。
>
>在开放寻址法（Open Addressing）中，这种标记就是我们前面说的 “墓碑 tombstone”。

>###### 为什么要用软删除（而不是直接删除）?
>
>在开放寻址中，如果你直接把槽位设为空（`EMPTY`），查找时遇到空位就会停止，导致错误。



###### 哈希表性能

在开放寻址（Open Addressing）中，平均需要多少次探测 (probe) 才能找到一个空槽。
$$
平均探测次数（插入时）≈ \frac{1}{1-alpha}
$$
当装载因子为
$$
\alpha = \frac{n}{m}
$$
也就是表中已有 n 个元素、总槽位数 m，

假设我们在进行 线性探测（linear probing），并且哈希函数足够随机，那么：

- 当前表的“空槽比例”为 1 - alpha；
- 每次探测命中空槽的概率 = 1 - \alpha；
- 每次探测失败（撞到已有元素）的概率 = alpha。

所以要找到一个空位，本质上是在重复独立试验：“试到一个空槽为止”。

> 这是一个几何分布（geometric distribution）：
> $$
> P\text{(first empty after k probes)}=(α)^{k−1}(1−α)
> $$
> 于是期望探测次数：
> $$
> E[probe]=∑^{∞}_{k=1}k(α)^{k−1}(1−α)=\frac{1}{1−α}
> $$
>
> | α (装载因子) | 表填充比例 | 平均探测次数 |
> | ------------ | ---------- | ------------ |
> | 0.5          | 半满       | 2 次         |
> | 0.75         | 75% 填充   | 4 次         |
> | 0.9          | 90% 填充   | 10 次        |
> | 0.99         | 99% 填充   | 100 次！     |

当表接近满时，探测次数急剧上升，性能迅速退化。所以我们通常在 α ≈ 0.7~0.8 时就会触发 扩容（rehash）。

> 这只是插入（或查找失败）时的平均探测次数。如果是查找一个已存在的元素，平均探测次数不同：
> $$
> \frac{1}{2}(1+\frac{1}{1-\alpha})
> $$





#### Rehash / resize







## Balanced BST VS. HashTable

insert, find, delete

| 操作   | 平衡二叉搜索树（Balanced BST，如 AVL / Red-Black） | 哈希表（Hash Table）     |
| ------ | -------------------------------------------------- | ------------------------ |
| insert | (O(log n))                                         | 平均 (O(1))，最坏 (O(n)) |
| find   | (O(log n))                                         | 平均 (O(1))，最坏 (O(n)) |
| delete | (O(log n))                                         | 平均 (O(1))，最坏 (O(n)) |

### Balanced BST

- 数据按 键值有序 存储；
- 插入、查找、删除都要沿树路径（高度为 $O(\log n)$）；
- 若每次插入后进行平衡调整（rotation），树高始终保持 $\log n$。

因此三种操作都是 O(log n)。

支持排序、范围查询。

- 有序性
- 范围查询 (range query)
- 最小/最大值



### Hash Table

- 元素位置直接由 哈希函数 h(key) 决定；
- 理论上查找、插入、删除都只需 一次访问 → O(1)；
- 但若发生冲突（collision），就需要额外探测或链表查找。

平均仍是 O(1)，但最坏情况（哈希函数差或冲突严重）退化为 O(n)。







# 25.10.10 - Dynamic Programming





## Recursion Design



### Naive recursion -> bad



## Trading space for time



### Bottom up



### Top down





## What type of problems?

- Optimization problems: longest/shortest/max/min
- Counting
- Feasibility



### **longest common subsequence**

#### Thinking

```
A = [1, 3, 2, 5, 4]

subsequence -> subset of A
[1, 2], [], [1, 3, 2, 5, 4]
[2, 1] is not

Given A and B, can you find some common subsequence in A and B?

-> What is larger problem? What is smaller problem?

-> What is the size of the problem?
	 (the size of A, the size of B)
	 try to optimize the length of the LCS
	 f(n, m) = length of longest common subsequence of A[n], B[m]
	 
-> How to make the size of the problem smaller?
	 if we only consider the last element of both arr, check A[n] == B[m] ?
	 - 1.A[n] == B[m]: f(n, m) = f(n-1, m-1) + 1
	 - 2.A[n] != B[m]: f(n, m) = max(f(n, m-1), f(n-1, m))
   
-> What is the base case?
	 - first arr is empty: f(0, m) = 0
	 - second arr is empty: f(n, 0) = 0
```

#### Recursion

```python
def lcs(arr1, arr2):
  #. base case
	if not arr1 or not arr2:
    return 0
  
  # special case
  n, m = len(arr1), len(arr2)
  if arr1[n-1] == arr2[m-1]:
    return 1 + lcs(arr[:n-1], arr2[m-1])
  
  # compare case -> cannot find specific result
  return max(lcs(arr, arr2[m-1]), lcs(arr[:n-1], arr2))

'''
每次比较最后一个元素，
- 如果相等 → 只递归一次；
- 如果不相等 → 递归两次。

所以最坏情况是每层都进入两个递归分支：T(n,m)=T(n−1,m)+T(n,m−1)
边界条件：T(0, m) = T(n, 0) = O(1)

递归树规模 -> 等价于一棵二叉递归树，其节点数大约为：
O(2^{min(n, m)})

空间主要来自 递归调用栈。递归深度最多为 n + m（每次至少减少一个长度）。
'''
```

#### Tabulation -> Bottom up

用一个二维表 `dp[n+1][m+1]` 存结果，可以避免重复计算
$$
dp[i][j] =
\begin{cases}
0, & \text{若 } i = 0 \text{ 或 } j = 0 \\[8pt]
dp[i-1][j-1] + 1, & \text{若 } arr1[i-1] = arr2[j-1] \\[8pt]
\max(dp[i-1][j],\ dp[i][j-1]), & \text{否则}
\end{cases}
$$

- 表格初始化：第一行和第一列都设为 0（因为空串与任何串的 LCS = 0）
- 填表顺序：由于 `dp[i][j]` 依赖 `dp[i-1][j]`、`dp[i][j-1]`、`dp[i-1][j-1]`，我们从左上到右下依次填表。

```python
def lcs(arr1, arr2):
  for i in range(n):
    dp[i][0] = 0
  for j in range(n):
    dp[0][j] = 0
  
  for i in range(1, n):
    for j in range(1, m):
      if arr1[i] == arr2[j]:
        dp[i][j] = dp[i-1][j-1]
      else:
        dp[i][j] = max(dp[i-1][j] + dp[i][j-1])
```

| 类型             | 复杂度                    |
| ---------------- | ------------------------- |
| 时间复杂度       | (O(n * m))                |
| 空间复杂度       | (O(n * m))                |
| 若优化为滚动数组 | 空间可降为 (O(min(n, m))) |

##### 滚动数组（rolling array）Space Optimization

当前状态只依赖于前一行（或前一列）。
$$
dp[i][j] =
\begin{cases}
0, & \text{若 } i = 0 \text{ 或 } j = 0 \\[8pt]
dp[i-1][j-1] + 1, & \text{若 } arr1[i-1] = arr2[j-1] \\[8pt]
\max(dp[i-1][j],\ dp[i][j-1]), & \text{否则}
\end{cases}
$$
计算 `dp[i][j]` 时，只需要三个位置的值：

- `dp[i-1][j-1]`（左上）
- `dp[i-1][j]`（上）
- `dp[i][j-1]`（左）

既然只依赖上一行的值，那么整张 `n×m` 表根本不需要保存。只要我们在计算第 `i` 行时：

- 保留一份上一行的结果（称为 `prev[]`）；
- 同时构建当前行的结果（称为 `curr[]`）；

那计算完这一行后：

- 下一次循环再让 `curr` 变成新的 `prev`，
- 继续计算下一行。

两行数组（prev 与 curr）在计算过程中不断交换角色。

```python
def longestCommonSubsequence(arr1, arr2):
    n, m = len(arr1), len(arr2)
    dp = [[0] * (m + 1) for _ in range(2)]

    for i in range(1, n + 1):
        curr = i % 2
        prev = (i - 1) % 2
        for j in range(1, m + 1):
            if arr1[i - 1] == arr2[j - 1]:
                dp[curr][j] = dp[prev][j - 1] + 1
            else:
                dp[curr][j] = max(dp[prev][j], dp[curr][j - 1])
    return dp[n % 2][m]
```



#### Memoization -> Top Down

```python
def main(arr1, arr2):
  n, m = len(arr1), len(arr2)
  for i in range(n):
    for j in range(m):
      dp[i][j] = -1
  
  return lcs(arr1, arr2, dp)


def lcs(arr1, arr2, dp):
  i, j = len(arr1), len(arr2)
  if i == 0 or j == 0:
    return 0
  
  # check if the solution exists
  if dp[i][j] != -1:
    return dp[i][j]
  
  if arr1[n-1] == arr2[m-1]:
    dp[i][j] = 1 + lcs(arr[:n-1], arr2[m-1])
  else:
    dp[i][j] = max(
      lcs(arr1[i-1], arr2[j], dp),
      lcs(arr[:i], arr2[:j-1], dp)
    )
```



#### Reconstruction

在 `dp` 表填好之后，从右下角 反向回溯路径。

- 如果 `arr1[i-1] == arr2[j-1]` → 当前字符属于 LCS；
- 当当前两个字符不相等时，我们要根据 `dp` 表里的数值，判断 LCS 是来自上方还是左方，从而选择往哪边回溯。

$$
dp[i][j] =
\begin{cases}
0, & \text{若 } i = 0 \text{ 或 } j = 0 \\[8pt]
dp[i-1][j-1] + 1, & \text{若 } arr1[i-1] = arr2[j-1] \\[8pt]
\max(dp[i-1][j],\ dp[i][j-1]), & \text{否则}
\end{cases}
$$

当两个字符不相等时，我们就取“上方”和“左方”中较大的那个值。

```python
i, j = n, m
lcs = []

while i > 0 and j > 0:
    if arr1[i - 1] == arr2[j - 1]:
        lcs.append(arr1[i - 1])
        i -= 1
        j -= 1
    elif dp[i - 1][j] >= dp[i][j - 1]:  # same, any one is ok
        i -= 1
    else:
        j -= 1

return lcs.reverse()
```

- O(m+n)
- O(min(m,n))





## Zero-one Knapsack

给定：

- `n` 个物品，每个物品有：
  - 重量 `w[i]`
  - 价值 `v[i]`
- 背包容量为 `W`

要求：从中选择若干个物品放入背包，使得总重量不超过 `W`，且总价值最大。 每个物品最多只能选 一次（“0-1” 的含义）。



### Recursion

最“人脑直觉”的想法确实就是用 回溯（Backtracking / Recursion）：尝试每个物品的“选”或“不选”两种决策，一旦超出容量就剪枝（停止向下探索）。

```python
def knapsack_recursive(weights, values, capacity):
    n = len(weights)

    def dfs(i, remaining):
        # base case：物品都选完 or 背包已满
        if i == n or remaining <= 0:
            return 0

        # 不选当前物品
        not_take = dfs(i + 1, remaining)

        # 选当前物品（前提是放得下）
        take = 0
        if weights[i] <= remaining:
            take = values[i] + dfs(i + 1, remaining - weights[i])

        return max(take, not_take)

    return dfs(0, capacity)
```

**时间复杂度**

每个物品都要考虑“选 / 不选”，且每条路径都可能完整遍历到深度 `n`。
$$
T(n) = 2 ^ n
$$
即使存在“超出容量直接剪枝”的情况，最坏情况下（所有物品都能放下），仍然需要遍历所有组合，所以最坏复杂度依然是 O(2ⁿ)。

**空间复杂度**

空间由 递归调用栈 决定。栈的最大深度 = `n`（每一层对应一个物品）每层只保存局部变量（常数级空间）. 所以`S(n)=O(n)`



### Greedy

另一个经典思路：Greedy（贪心算法）。

在背包问题中，我们得非常清楚地区分它 在哪种背包问题中可行、在哪种不行。

| 类型                                | 是否可部分拿取 | 典型名称               | 是否能用贪心   |
| ----------------------------------- | -------------- | ---------------------- | -------------- |
| **0-1 背包（0-1 Knapsack）**        | 不能拆分物品   | 每个物品要么拿要么不拿 | 贪心不保证最优 |
| **分数背包（Fractional Knapsack）** | 可拆分物品     | 可以取物品的一部分     | 贪心最优       |

贪心的想法通常是：先拿价值密度（value/weight）最高的物品。但在 0-1 背包中，这样做可能会错失组合更优的结果。

> 贪心算法能不能用，是靠“贪心选择性质”与“最优子结构”是否同时成立。
>
> 任何贪心算法想要正确，必须同时满足：
>
> 1. 贪心选择性质（Greedy Choice Property）局部最优选择能导向全局最优解。换句话说，你在每一步“只看当前最好的选择”，就能保证最后整体也是最好的。
> 2. 最优子结构（Optimal Substructure）一个问题的最优解包含它的子问题的最优解。也就是“子问题独立”，不会因为后面决策不同而改变前面子问题的最优性。贪心要求每次选择“当前最优”不会影响未来的最优性。
>
> ##### 为什么 0-1 背包破坏了“贪心选择性质”?
>
> | 物品 | 重量 | 价值 | 价值密度 |
> | ---- | ---- | ---- | -------- |
> | A    | 1    | 2    | 2        |
> | B    | 2    | 3    | 1.5      |
> | C    | 3    | 4    | 1.33     |
>
> 背包容量 W = 3
>
> 贪心按密度排序，会：
>
> - 先拿 A（剩余容量2，价值=2）
> - 然后拿 B（容量刚好3，价值=5）
>
> 但最优解是直接拿 C（容量3，价值=4）。 因为当物品 不可分割 时，“局部最优”未必能组合成“全局最优”。你选了一个高密度的轻物品，看似最划算，但它占了重量空间，导致后面无法放入价值更高的物品。这就是破坏了 贪心选择性质。
>
> 在 0-1 背包中：选择某个物品，会改变剩余容量；而剩余容量决定了后续能不能选别的物品；所以每一步的选择与未来决策强相关，不是独立的。也就是说违反了最优子结构（Optimal Substructure）准则。



### Analyze

```python
'''
What is the bigger problem? What is the smaller problem?
- 2 dimensions: the number of items / the valu of items

f(i, j) = max value with item 1 to i and knapsack capability j

Think about the last item? What decision you will make about it?
- If I will take it?
-- w[i] <= j, I will take it. v[i] + f(i. j-w[i])
-- not take it. f(i. j)
Compare these 2 options, Which one is better, take which one.

What is base case?
- When there is no items or there is no knapsack, this is the base case = 0
'''
```

```python
def knapsack(v[1...i], w[1...j], j):
  if (i == 0) or j == 0:
    return 0
  
  if w[i] > j:
    return knapsack(v[1...i-1], w[1...j-1], j)
  else:
    return max(
      knapsack(v[1...i-1], w[1...j-1], j), 
      knapsack(v[1...i-1], w[1...j-1], j-w[i]) + v[i]
    )
```

```
                           knapsack(n, W)
                           /            \
         不选第n个物品 → knapsack(n-1, W)   选第n个物品 → knapsack(n-1, W - w[n]) + v[n]
                        /       \                     /         \
           不选n-1 → knapsack(n-2, W)    选n-1 → knapsack(n-2, W - w[n-1]) + v[n-1]
                        ⋮                           ⋮
                        ⋮                           ⋮
                knapsack(1, W)             knapsack(1, W - w[1]) + v[1]
                      / \
             (0,W)=0   (0,W-w[1])+v[1]

# n levels -> 2^n
```



### Bottom up

在递归版本中，我们是自顶向下（Top-down）：每次调用 `knapsack(i, j)` 会递归计算子问题 `knapsack(i-1, j)` 和 `knapsack(i-1, j-w[i])`；也就是从「大问题 → 小问题」；存在大量重复子问题。

Bottom-up 的思路恰好反过来：从最小的子问题（base case）出发，一层一层往上构建，直到得到最终答案 `dp[n][W]`。

#### Definition

`dp[i][j] = 前 i 个物品在容量 j 时的最大价值`

- `i` ∈ [0, n] 表示前 i 个物品；
- `j` ∈ [0, W] 表示容量；
- `dp[0][*] = dp[*][0] = 0`（无物品或无容量 → 无价值）。

#### State Transfer Function

$$
dp[i][j] =
\begin{cases}
0, & \text{若 } i = 0 \text{ 或 } j = 0 \\[8pt]
dp[i-1][j], & \text{若 } w[i-1] > j \\[8pt]
\max \big( dp[i-1][j],\ dp[i-1][j - w[i-1]] + v[i-1] \big), & \text{若 } w[i-1] \le j
\end{cases}
$$

#### Code

```python
def knapsack(weights, values, W):
    n = len(weights)
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, W + 1):
            if weights[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(
                    dp[i - 1][j],
                    dp[i - 1][j - weights[i - 1]] + values[i - 1]
                )
    return dp[n][W]
```

`T(n,W)=O(n×W)`



#### Rolling Array

用 `dp[2][W+1]` 保存当前行与上一行：

- `curr = i % 2`
- `prev = (i - 1) % 2`

```python
def knapsack(weights, values, W):
    n = len(weights)
    dp = [[0] * (W + 1) for _ in range(2)]

    for i in range(1, n + 1):
        curr = i % 2
        prev = (i - 1) % 2
        for j in range(1, W + 1):
            if weights[i - 1] > j:
                dp[curr][j] = dp[prev][j]
            else:
                dp[curr][j] = max(
                    dp[prev][j],
                    dp[prev][j - weights[i - 1]] + values[i - 1]
                )
    return dp[n % 2][W]
```

**一维滚动数组（真正的压缩版）**

当我们在第 `i` 行计算 `dp[j]` 时，只依赖于「上一行的 dp[j]」与「上一行的 dp[j - w[i-1]]」。

若我们从右往左更新（即 j 递减），可以让“上一行的旧值”在使用前不会被新值覆盖。
$$
dp[j] = 
\begin{cases}
dp[j], & w[i-1] > j \\[8pt]
\max(dp[j],\ dp[j - w[i-1]] + v[i-1]), & w[i-1] \le j
\end{cases}
$$

```python
def knapsack_optimized(weights, values, W):
    n = len(weights)
    dp = [0] * (W + 1)

    for i in range(n):
        for j in range(W, weights[i] - 1, -1):  # 从右往左更新
            dp[j] = max(dp[j], dp[j - weights[i]] + values[i])
    return dp[W]
```

> 为什么要“从右往左”更新？
>
> 如果你从左往右更新，当计算 `dp[j]` 时，`dp[j - w[i]]` 可能已经被本轮更新覆盖，导致你使用了新值而非上一轮的旧值，相当于「一个物品被重复使用」——那就是完全背包逻辑。
>
> <u>0-1 背包必须从右向左更新，完全背包则从左向右更新。</u>
>
> - 它们的核心区别就在于：每种物品是否能被重复使用。





### Top down

Top-down 的出发点与暴力递归一样：从大问题出发，拆分成两个子问题

- 不选当前物品；
- 选当前物品（如果放得下）。

但不同之处在于：我们会把每个子问题的结果缓存下来（memoization），避免重复计算，从而把指数级复杂度降为多项式级。

#### Definition

`f(i,j)=前 i 个物品在容量 j 时的最大价值`

#### State Transfer Function

$$
f(i, j) =
\begin{cases}
0, & \text{若 } i = 0 \text{ 或 } j = 0 \\[8pt]
f(i-1, j), & \text{若 } w[i-1] > j \\[8pt]
\max\big(f(i-1, j),\ f(i-1, j - w[i-1]) + v[i-1]\big), & \text{若 } w[i-1] \le j
\end{cases}
$$

#### Code

```python
def knapsack(weights, values, W):
    n = len(weights)
    memo = {}  # (i, j) -> 最大价值

    def dfs(i, j):
        # base case
        if i == 0 or j == 0:
            return 0
        
        # if it is not the first time, return directly
        if (i, j) in memo:
            return memo[(i, j)]

        # if it is the first time. compute, return
        if weights[i - 1] > j:
            res = dfs(i - 1, j)
        else:
            res = max(
                dfs(i - 1, j),
                dfs(i - 1, j - weights[i - 1]) + values[i - 1]
            )

        memo[(i, j)] = res
        return res

    return dfs(n, W)
```



### Reconstruction

从 `dp` 表里倒推回去，找出那组最优物品。

$$
dp[i][j] =
\begin{cases}
0, & \text{若 } i = 0 \text{ 或 } j = 0 \\[8pt]
dp[i-1][j], & \text{若 } w[i-1] > j \\[8pt]
\max \big( dp[i-1][j],\ dp[i-1][j - w[i-1]] + v[i-1] \big), & \text{若 } w[i-1] \le j
\end{cases}
$$
当前 `dp[i][j]` 的值是从哪个分支来的？

从 `i = n, j = W` 开始往上走：

- 如果 `dp[i][j] == dp[i-1][j]` → 当前物品 没被选。→ 向上移动：`i -= 1`
- 否则 → 当前物品 被选 → 记录物品 i → 减去它的重量 `j -= w[i-1]` → 再往上 `i -= 1`

直到 `i == 0` 或 `j == 0` 为止。

```python
selected = []
i, j = n, W
while i > 0 and j > 0:
    if dp[i][j] != dp[i - 1][j]:
        selected.append(i - 1)  # 第 i 个物品被选
        j -= weights[i - 1]
    i -= 1

selected.reverse()  # 物品编号从小到大
return dp[n][W], selected
```





## **Complete Knapsack**

n types of items. For each type, there is infinity number of copies. 

有 `n` 种物品，每种物品都有：

- 重量 `w[i]`
- 价值 `v[i]`

现在有一个容量为 `W` 的背包，每种物品有无限个副本（infinity number of copies），即每种物品可以被选任意次（包括 0 次）。

问：在不超过总容量 `W` 的前提下，我们最多能获得的总价值是多少？



### Recursion

对于每一个物品：我可以选择 `0 个、1 个、2 个、...`，只要总重量不超过 W。

```python
def dfs(i, cap):
    if i == n or cap <= 0:
        return 0  # 没物品可选 or 超出容量

    res = dfs(i + 1, cap)  # 不选当前物品

    if w[i] <= cap:
        res = max(res, dfs(i, cap - w[i]) + v[i])  # 选当前物品（注意这里仍是 i，不是 i+1）
    
    return res
```

- “选物品0”这条分支可以反复调用自身；

- 每次递归都在“减少容量”；一旦超重（`cap < 0`），就直接返回；

- 每次回溯时记录当前组合的总价值，更新全局最大值。


指数级回溯：每个物品可以被选任意次；对每个物品的选择次数从 0 到 `W / w[i]`；所以大约复杂度为：
$$
O(W^{n})
$$
递归深度 = `n`（每层对应一个物品），所以空间复杂度：`S(n) = O(n)`



### Analyze

```python
'''







- if w[i] <= j: v[i] + f(j-w[i]) -> max(all of possibilities), take the max one
'''
```





### Bottom up











#### Definition

`dp[i][cap]=当处理第 i个物品，剩余容量为 cap 时的最大价值`

- `i` 表示当前正在考虑的物品；
- `cap` 表示当前剩余容量；
- 函数返回「从 i 开始能得到的最大价值」。

#### State Transfer Function

$$
dp[i][j] =
\begin{cases}
0, & \text{若 } i = 0 \text{ 或 } j = 0 \\[6pt]
dp[i+1][j], & w[i] > j \\[8pt]
\max(dp[i+1][j],\ dp[i][j - w[i]] + v[i]), & w[i] \le j
\end{cases}
$$

#### Code

```python
dp = [[0] * (W + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(W + 1):
        if w[i-1] > j:
            dp[i][j] = dp[i-1][j]
        else:
            # 完全背包：注意是 dp[i][j - w[i-1]]
            dp[i][j] = max(dp[i-1][j], dp[i][j - w[i-1]] + v[i-1])
```





## Exercise

### Final

0-1 Knapsack Problem

- n problems need to solve
- problem i, score[i], time[i]
- T

```
f(i, j) -> first i problems, use j time

dp[] -> if give up
give up -> f(i-1, j)
not give up ->  score[i] + f(i-1, j-time[i])

max 2 options
```





### Coin Change

Complete Knapsack Problem

- 1 5 10 25 cents
- M -> Want make change of this amount
- Goal is to minimize the number of coins that I make changes of M

```
f(j) = 1 + f(j-d[i])
j -> amount to change
d -> the amount of each coin choice

f(j) = min(
					1 + f(j-d[1])
					1 + f(j-d[2])
					...
					1 + f(j-d[n])
			 )
```

```
for ( i = 1 ... C ) {
	dp[i] = 
	
	for (k = 1 ... n ) {
		if (dp[k] <= i) {
			dp[i] = min(dp[i], i+dp[i-d[k]])
		}
	}
}

return dp[C]
```





## **Longest Increasing Subsequence**



```
A = [1, 5, 2, 3]
```

```
f(i) = length of longest increasing subsequence given A[1:i]
-> i is the length of arr
-> A[1:i]: slice of the input A


f(i) = max(
				 1 + f(i-1) if A[i-1] < A[i]
				 1 + f(i-2) if A[i-2] < A[i]
				 ...
				 1 + f(1) if A[1] < A[i]
				 1
       )

f(1)
f(2)
f(3)
...
f(n)
```

```
# optimization
dp[]

for (i = 1 .. n) {
	dp[i] = 1;
	
	for (k = 1 .. i-1) {
		if (A[k] < A[i]) {
			dp[i] = max(dp[i], 1+dp[k]);
		}
	}
}

return max(dp[])
```





## **Max Subarray Sum**

```
f(i) = max sub arr sum W/A[1:i]


```





# 25.10.24 - DP





## Matrix Chain Multiplication

`A1 * A2 * A3 * A4 * A5 * ... * An`

```
A -> p*q
B -> q*r
A * B -> O(pqr)

A1(50, 10), A2(10, 100), A3(100, 5)
(A1 * A2) * A3
-> 50 * 10 * 100 = 50,000
-> (50 * 100) 
-> 50 * 100 * 5 = 25,000
-> total = 50,000 + 25,000 = 75000

A1 * (A2 * A3)
-> 10 * 100 * 5 = 5,000
-> (10 * 5) 
-> 50 * 10 * 5 = 2,500
-> total = 5,000 + 2,500 = 7,500

So different combination will cause different time complexity.
```

```
If there is a maxtrix chain we will multipy, How can we get result with minimal cost?

  A1  *  A2  *  A3  *  A4
p0,p1  p1,p2  p2,p3   p3,p4
How many different kinds of type of combination about the multiplication?
6
-> ((A1 * A2) * A3) * A4
-> (A1 * (A2 * A3)) * A4
-> ((A1 * A2) * (A3 * A4))
-> A1 * (A2 * (A3 * A4))
-> A1 * ((A2 * A3) * A4)

Which one should be the last one when multiplying?
A4
A1
(A1 * A2) * (A3 * A4)

f(1, 4) = min (
						0 + f(2, 4) + p0*p1*p4,
						f(1,2) + f(3. 4) + p0*p2*p4,
						f(1, 3) + 0 + p0*p3*p4
    			)
```

```
  A1  *  A2  *  A3  *  A4  *  ...  *  An
p0,p1  p1,p2  p2,p3   p3,p4         pn-1,pn

(j - i) times multiplication

f(i, j) = min (
						0 + f(i+1, j) + pi-1*pi*pj,
						f(i,i+1) + f(i+2, j) + pi-1*pi+1*pj,
						f(i,i+2) + f(i+3, j) + pi-1*pi+2*pj,
						f(i,i+3) + f(i+4, j) + pi-1*pi+3*pj,
						...
						f(i, j-1) + 0 + pi-1*pj-1*pj
    			)
    	  = min {f(i, k) + f(k+1, j) + pi-1*pk*pj}  # k {i...j-1}

# base case
f(i, i) = 0  # nothing to multiply

# What we want in the end?
dp[1,n]

# what data structure we can use?
dp[[]] -> 2 dimentional array

dp[i,j] = f(i,j)
1. The diagonal line will be filled with 0 -> base case
...... the order we fill the 2d table
```

```
# psudocode
for (i=1...n) dp[i,i] = 0

for (j=2, ..., n) {
	for (i=j-1, ... ,1) {
		dp[i,j] = + infinity
		
		for (k=i, ... j-1) {
			dp[i,j] = min(dp[i,j], dp[i,k]+dp[k+1,j]+pi-1*pk*pj)
		}
	}
}

return dp[1, n]
```



## Types of Recursion Pattern

1. LCSubsequence / LCSubstring
2. LIS / Subarray Sum / Palindrome
3. Knapsack 01 / complete
4. Matrix Multiplication -> intervals







# 25.10.31 - DP



## Longest Common Substring



### 暴力思路

1. 枚举所有 `s1` 的子串。
2. 对于每一个子串，检查它是否也出现在 `s2` 中。
3. 如果出现，就更新最长长度。



### Recursion

```
f(i, j) -> the length of LCS given s[1:i], t[1:j]


```



```
lcs(s1, s2, i, j, count)
```

从 s1 的第 i 个字符、s2 的第 j 个字符开始，以当前位置为结尾的最长公共子串长度（count 是当前连续匹配的长度）。

- **如果 i 或 j 越界**，返回当前计数 `count`；
- **如果 s1[i-1] == s2[j-1]** → 当前字符匹配，递归求解 `lcs(s1, s2, i-1, j-1, count+1)`；
- **否则字符不匹配** → 子串被打断，必须重新从 0 开始计数：分别尝试 `(i-1, j)` 和 `(i, j-1)` 两个方向；

返回三个结果的最大值。

```python
def lcs_recursion(s1, s2, i, j, count):
    # 递归终止条件
    if i == 0 or j == 0:
        return count
    
    # 如果当前字符匹配，向前延伸
    if s1[i - 1] == s2[j - 1]:
        count = lcs_recursion(s1, s2, i - 1, j - 1, count + 1)
    
    # 无论匹不匹配，都要尝试其他分支
    count = max(count,
                lcs_recursion(s1, s2, i - 1, j, 0),
                lcs_recursion(s1, s2, i, j - 1, 0))
    
    return count
```

- 时间复杂度：O(2^(n+m))，因为每个递归分支都可能分裂成两个方向。
- 空间复杂度：O(n+m)，递归栈深度。



### 记忆化递归

```python
memo = {}

def lcs_recursion(s1, s2, i, j, count):
    # 递归终止条件
    if i == 0 or j == 0:
        return count
    
    if (i, j, count) in memo:
      return memo[(i, j, count)]
    
    # 如果当前字符匹配，向前延伸
    same_count = count
    if s1[i - 1] == s2[j - 1]:
        same_count = lcs_recursion(s1, s2, i - 1, j - 1, count + 1)
    
    # 无论匹不匹配，都要尝试其他分支
    res = max(same_count,
                lcs_recursion(s1, s2, i - 1, j, 0),
                lcs_recursion(s1, s2, i, j - 1, 0))
   	memo[(i, j, count)] = res
    return res
```

- 时间复杂度: `O(n * m)`

- 空间复杂度: `O(n×m)`




### Tabulation

```python
n, m = len(s), len(t)
dp = [[0] * (m+1) for _ in range(n+1)]
max_len = 0

for i in range(1, n+1):
  for j in range(1, m+1):
    if s[i-1] == t[j-1]:
      dp[i][j] = dp[i-1][j-1] + 1
      max_len = max(max_len, dp[i][j])
    else:
      dp[i][j] = 0

return max_len
```

- 时间复杂度: `O(n * m)`
- 空间复杂度: `O(n×m)`







## Palindrome Partitioning

```
f(i) -> given s[:i], minimum number of palindromes
```



### Brute Force

列举出所有可能的切割方式（2^(n-1) 种），对每种切割方式检查：每个子串是不是回文。

1. 对长度为 `n` 的字符串，每两个字符之间都有一个“切”或“不切”的选择 → `2^(n-1)` 种组合；
2. 生成所有切割方案；
3. 对每个方案，逐个判断子串是否是回文；
4. 如果整组子串全是回文 → 加入结果。

```python
def partition(s):
    res = []
    path = []

    def is_palindrome(sub):
        return sub == sub[::-1]

    def backtrack(start):
        # 递归终点
        if start == len(s):
            res.append(path[:])
            return

        # 尝试所有切割点
        for end in range(start + 1, len(s) + 1):
            sub = s[start:end]
            if is_palindrome(sub):  # 剪枝：只对回文继续递归
                path.append(sub)
                backtrack(end)
                path.pop()  # 回溯：撤销上一步选择

    backtrack(0)
    return res
```

- 时间复杂度：`O(n × 2^n)`

- 空间复杂度：`O(n)`


>##### backtrack 难加 memo？
>
>这里 `path` 是全局变量（存放当前路径），所以递归返回的是副作用结果（直接改动 `res`）。这类函数返回值是 `None`，并不是函数式的“输入 → 输出”关系。所以你没法直接说“`memo[start] = backtrack(start)`”，因为它没有返回值。
>
>要能 memo，就要“函数式”化：让 `dfs(start)` 返回结果。
>
>- 输入唯一（start） → 输出唯一（该位置开始的所有回文划分）
>
>这才可以缓存结果。`memo_part[start]` 就表示：从 start 开始切，所有可能的回文划分列表





### Memoization

```python
n = len(s)

memo_judge = {}
def is_palindrome(l, r):
	if (l, r) in memo_judge:
		return memo_judge(l, r)
  
  substring = s[l: r]
  memo_judge[(l, r)] = substring == substring[::-1]
  return memo_judge[(l, r)]

memo_part = {}
def dfs(start):
  if start == n:
    return [[]]  # 表示这条路径的后半部分是空的，但它是一个有效的结束方案。
  
  if start in memo_part:
    return memo_part[start]
  
  res = []
  for end in range(start+1, n+1):
    if is_palindrome(start, end):
      for sub_partition in dfs(end):
        res.append([s[start:end]] + sub_partition)
        # [s[start:end]] + tail ⇒ ["b"] + [] ⇒ ["b"]
        # 所以上一层返回 [["b"]]
        # 再往上一层拼接 "a" + ["b"] → ["a","b"]
        # 最上层得到 ["a","a","b"]
  
  memo_part[start] = res
  return memo_part[start]
```

- 时间复杂度 O(n²)

- 空间复杂度 O(n²)




### Tabulation

```python
n = len(s)

# Check if palindrome
if_palindrome = [[False] * (n) for _ in range(n)]

for i in range(n):
    is_pal[i][i] = True
    
for i in range(n-1, -1, -1):
  for j in range(i+1, n):
    if s[i] == s[j] and (j-i <= 2 or if_palindrome[i+1][j-1]):
      if_palindrome = True

# fill out all possibility that dp[i] means 从下标 i 开始的所有回文划分方案
dp = [[] for _ in range(n+1)]
dp[n] = [[]]

for i in range(n-1, -1, -1):
  for end in range(i+1, n+1):
    if if_palindrome[start][end]:
      for tail in dp[end]:
        dp[i].append([[s[i:end]] + tail])

return dp[0]
```

- 时间复杂度 O(n²)
- 空间复杂度 O(n²)







# 25.11.7 - Graph



## Basic

- **Directed**
- **Undirected**
- **Degree**
- **Indegree**
- **self-loop**
- **Sparse**
- **Dense**
- **Complete**
- **DAG Directed Acyclic Graph**









## Representation









## Search



### DFS





### BFS











## **Topological Sort**













































































































# 25.11.14 / 21 - Graph







## How do you detect cycles in directed graph?

**Kahn’s Algorithm** 如果一个有向图是 DAG，那么拓扑排序一定能排完全部节点；否则某些节点始终有入度 > 0。

1. 计算每个点的入度。
2. 把所有入度为 0 的点入队。
3. 不断出队 → 更新后继节点入度 → 发现新的 0 入度点入队。
4. 若最终弹出的节点数 < 总节点数 ⇒ 有环。

```

```

**White/Gray/Black DFS 三色标记法**：如果 DFS 遍历时遇到一个 灰色节点，说明发现 **回边（back edge）** → 有环。

```

```





## Word ladders

Input:

- dictionary
- start word
- target word

Output:

- the sequence that start word gradually change into target word by changing a character one time.

关键在于：把单词看成图里的节点

- 节点（vertex） = dictionary 中的每个单词

- 边（edge） = 两个单词差一个字符。每对差 1 个字符的单词之间画一条无向边。得到的就是一个 无向图（graph）。


所以问题变成：找从 start 到 target 的 **最短路径**（每条边权重是 1）







## Puzzle 8

Input:

- 3 * 3 board
- Numbers 1-8
- 一个空格（通常记作 0）

Action:

- Move the numbers into the right sequence. 每一步只能把空格 `_` 和它上下左右的数字交换


```
1 2 3
4 5 6
7 8 _
```

Output:

- 找到从初始状态移动到目标状态的 **步骤序列**。

图论经典建模：

- 每个状态是一个 vertex。每一个棋盘布局 = 图中的一个节点
- 每次移动（上下左右）是 edge。一次合法移动 = 一条边


得到状态图（State Graph），找最短步数 = 图论 shortest path。



### Encode the board

- String：把 3×3 展平成字符串（string encoding）【天然可哈希、判断 visited 简单】
- Vector array: prehash function
- Int：9 位数组编码成整数（int / long）【占空间小、哈希速度快、生成邻居时仍要转回二维坐标】

```
vector<int> state
→ prehash(state) = "123456708"
→ 哈希表计算 hash("123456708")
→ 存储到 bucket
```

> 为什么 8 Puzzle 特别需要 prehash？
>
> 因为 BFS/DFS 必须记录 visited 状态：`visited.insert(board_state);`
>
> - board 是二维数组
> - vector<int> 也不是 hashable by default（C++）
>
> 所以必须先做：**board → 编码（prehash） → 放进 visited**





## Multiply Adjacency Matrix

将邻接矩阵 A 与它自身做矩阵乘法：A × A = A²

> ##### 为什么要做邻接矩阵相乘？
>
> `Aⁿ[i][j]` 表示从 i 到 j 的长度为 n 的路径条数。
>
> - `A²[i][j]` = 所有从 i 到 j 走两步的路径数
> - `A³[i][j]` = 所有从 i 到 j 走三步的路径数
> - …
>
> ##### 典型用途
>
> - ① 计算两点之间的 k 步可达性
> - ② 判断图是否存在环
> - ③ 计算图的路径总数
> - ④ 动态规划求路径数量（Graph Counting）
> - ⑤ 用矩阵快速幂（binary exponentiation）加速搜索

```python
def matmul(A, B):
    n = len(A)
    m = len(B[0])
    k = len(B)

    C = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            s = 0
            for t in range(k):
                s += A[i][t] * B[t][j]
            C[i][j] = s

    return C
```







## **Shortest Path**



### Single Source Shortest Path

给定：

- 一个图 G = (V, E)
- 一个起点节点 source

要求：找到从 source 到所有其他节点的最短距离（shortest distance）。

根据「边权」不同分为两种情况

- 情况 A：无权图 (Unweighted Graph)，最适合 BFS

- 情况 B：有权图 (Weighted Graph)
  - 所有边权 ≥ 0 → 使用 *Dijkstra* 算法
  - 边权可以负数，但没有负环 → 使用 *Bellman-Ford* 算法
  - 图中有负环 → 最短路径不存在

```
Is G a DAG?
- Yes: SP on DAG（拓扑排序 + 松弛）
- No: 
  - 非负权重 -> Dijkstra's
  - 负权重   -> Bellman-Ford
```



#### relax（松弛）

检查一条边是否能让当前的最短路径变得更短，并在变短时更新它。

```python
if dist[v] > dist[u] + w(u, v):
    dist[v] = dist[u] + w(u, v)
```

可以把最短路径想象成橡皮筋：初始全是松的（dist 很大）。每次找到更短路径，就把它“拉紧”一点，最终所有距离都被“拉到最紧”的状态。

> Bellman–Ford 每一轮扫描所有边做 relax，（最多做 V−1 轮，保证所有路径都到最短）
>
> ```
> for _ in range(V-1):
>     for (u, v, w) in edges:
>         relax(u, v, w)
> ```
>
> Dijkstra 每次从未确定的点中选距离最小的点 u，然后 relax 所有 u 的邻居：
>
> ```
> for v in adj[u]:
>     relax(u, v, weight)
> ```
>
> DAG shortest path 按照拓扑序，从前向后 relax：
>
> ```
> for u in topo_order:
>     for v in adj[u]:
>         relax(u, v, w)
> ```





#### SP on DAG

问题设定：

- 有一个 有向无环图 $G = (V, E)$
  - Directed：边有方向
  - Acyclic：没有从某点出发最终又回到自己的环
- 每条边有一个权重 w(u, v)，可以是正数，也可以是负数（注意：负数是允许的，跟 Dijkstra 不同）
- 给定一个起点 `source`
- 目标：求 `source` 到图中每个点的 最短路径长度（Single Source Shortest Path on DAG）。

DAG强力工具：**拓扑排序（topological order）**。在 DAG 中，你可以把所有点排成一个线性顺序，对于任何一条边 u → v，u 一定出现在 v 前面。按照「前驱在前，后继在后」的顺序，从前到后依次更新最短路。这就是 SP on DAG 的核心。

假设拓扑序为：v₁, v₂, ..., vₙ。对于每条边 u → v：
$$
dist[v] = \min(dist[v], \; dist[u] + w(u, v))
$$
因为是拓扑序，当你处理到 v 时，所有能到 v 的前驱 u 都已经更新完成，所以这个递推是安全的。





time complexity: O(n+m)



for sparse graph -> running time O(n)

for dense graph -> running time O(n^2)





#### Dijkstra's Algorithm



- pure -> O(mlogn)
- Heap -> 

- boolean array -> O(n^2)






#### Bellman Ford Algorithm

不断放松（relax）所有边，每次最多增加一条边的长度（hop 数）。

- 一开始你只知道源点 s 自己的距离为 0，其他为 ∞；每做一轮“对所有边的松弛”，就允许路径“多走一步 edge”。因为图中无环的最短路径最多 n−1 条边（即简单路径），所以做 n−1 轮松弛就足够了。

```python
# 外层做 n-1 轮 → O(n)
for i in range(n-1):
  # relax all edges
  # 第二层和第三层循环一起覆盖所有 edge → O(m)
	for u in range(n):
    for v in graph.neighbors(u):
      relax(u, v)
```

- 时间复杂度：O(n*m)

**Bellman-Ford 的逻辑基础之一**

Claim: After relaxing all edges k times, the shortest distance from s to u is distance[u] if the number of hops on this shortest path <= k.

因为每一轮松弛，可以让使用到 k 条边的路径被正确传递到 dist 中。因此，只要 k 轮松弛 ≥ hop 数，答案就会正确。

**Negatively weighted cycles** -> infinity decrease weight in the path。

路径可以不断绕这个环，每绕一圈 sum 变小一点。如果最短路径包含负权环，则最短路径不存在（趋向 -∞）。

这时候 Bellman-Ford 的检测方式是：再做一轮松弛（第 n 轮）。如果第 n 轮还能进一步松弛 → 说明存在负权环 reachable from s。

>Can we relax all edges 1 more time? -> it is depends on if we have negatively weighted cycles。

**Simple Path** means no cycles on this path.

Bellman-Ford 依赖一个重要性质：任意两点之间，如果无负权环，其最短路径一定是一条 simple path（不重复结点）。

一旦路径里出现环且环权重 ≥ 0，则去掉环更短；若环权重 < 0，则短得无穷无尽 → 最短路径不存在。因此只需要考虑 simple path，它最多有 n−1 条边。





### SSSP：Currency Exchange

从某个货币（例如 USD）到其他货币的最大可兑换金额（最佳路径）是否存在套利（arbitrage）

```python
USD → EUR → JPY → USD # 最后比一开始更多
```

其实就是在图上找最大乘积路径 / 检测是否存在乘积 > 1 的环。



#### 取 log

图论的最短路无法直接处理“乘积”，所以我们要做数学变换，把乘法路径变成加法路径。

```python
value_new = value_old × rate

# 为了用最短路，我们希望变成相加：
log(value_new) = log(value_old) + log(rate)

# 但最短路需要 加起来变小，而最大汇率需要 乘起来变大。
# 用 -log(rate) 当边权！
log(product) 越大 → product 越大
-log(product) 越小 → product 越大

weight(u → v) = -log(rate[u → v])
# 最大乘积路径 = 最短路径（因为权重变“越小越好”）
```

把汇率 r 转成边权 w = -log(r)。最大兑换路径 → 最短路径（Bellman–Ford）。

- 若存在负权环，存在套利，即Bellman–Ford 第 n 轮仍能松弛，有套利机会。

>##### 为什么 Bellman–Ford 而不是 Dijkstra？
>
>因为汇率转换后会出现 **负边**（因为 -log(rate) 常常是负数），必须检测负环（套利）。



#### code

1. 读入汇率
2. 构图（使用 -log(rate)）
3. Bellman–Ford 求最短路
4. 第 n 轮松弛检测套利（负环）

```python
import math

def bellman_ford_currency(n, edges, source):
    """
    n: 货币数量
    edges: [(u, v, rate), ...]
    source: 源货币编号
    """

    # Step 1: 构造权重（用 -log(rate)）
    graph = []
    for u, v, rate in edges:
        w = -math.log(rate)
        graph.append((u, v, w))

    # Step 2: 初始化 dist
    INF = float('inf')
    dist = [INF] * n
    dist[source] = 0

    # Step 3: 做 n-1 轮松弛
    for _ in range(n - 1):
        updated = False
        for u, v, w in graph:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                updated = True
        if not updated:
            break  # 提前收敛

    # Step 4: 第 n 轮松弛检查负环（套利）
    arbitrage = False
    for u, v, w in graph:
        if dist[u] + w < dist[v]:
            arbitrage = True
            break

    return dist, arbitrage
```



#### Path Reconstruction

```python
import math

def bellman_ford_currency_with_path(n, edges, source):
    """
    n: 货币数量
    edges: [(u, v, rate), ...]
    source: 起点货币编号
    """

    # Convert rates to weights: -log(rate)
    graph = []
    for u, v, rate in edges:
        graph.append((u, v, -math.log(rate)))

    INF = float('inf')
    dist = [INF] * n
    parent = [-1] * n        # for path recovery

    dist[source] = 0

    # ----------- Regular Bellman-Ford (n-1 rounds) -------------
    for _ in range(n - 1):
        updated = False
        for u, v, w in graph:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u
                updated = True
        if not updated:
            break

    # ----------- Cycle Detection in nth round -------------
    cycle_start = -1
    for u, v, w in graph:
        if dist[u] + w < dist[v]:
            cycle_start = v        # cycle exists
            parent[v] = u
            break

    # ----------- Recover arbitrage cycle path -------------
    arbitrage_cycle = []
    if cycle_start != -1:
        # move cycle_start ahead n times to ensure it's inside cycle
        x = cycle_start
        for _ in range(n):
            x = parent[x]

        # now extract cycle
        cycle = []
        cur = x
        while True:
            cycle.append(cur)
            cur = parent[cur]
            if cur == x:
                break
        cycle.reverse()
        arbitrage_cycle = cycle

    return dist, parent, arbitrage_cycle
```





### All Pair Shortest Path

对图中每个节点 s，都计算所有顶点 v 的最短距离。即输出一个 **n × n** 的矩阵：
$$
dist[i][j] = \text{the shortest path from i to j}
$$

| 算法                | 图类型             | 时间复杂度     | 能处理负边吗 | 能处理负环吗 |
| ------------------- | ------------------ | -------------- | ------------ | ------------ |
| Floyd–Warshall      | 任意图（邻接矩阵） | O(n³)          | ✔            | ✔            |
| Dijkstra × n 次     | 无负权图           | O(n·(m log n)) | ✘            | ✘            |
| Bellman–Ford × n 次 | 任意图             | O(n² m)        | ✔            | ✔            |

>##### 什么时候用 APSP?
>
>- 要求所有点到所有点
>- 图规模不大（n ≤ 400）
>- 有负边（不能用 Dijkstra）
>- 需要检测任意负环
>- 需要路径恢复
>
>有负边 → Floyd–Warshall
>
>无负边 → Dijkstra × n 次
>
>边很多且负边 → Bellman–Ford × n 次





#### SSSP * n times

- **SP on DAG** O(n^2+mn) -> dense graph: n^2 to n^3
- **Dijkstra** O(mnlogn) / O(n^3) -> dense graph: n^2*logn to n^3
- **Bellman-Ford** O(n^2*m) -> dense graph: n^3 to n^4



#### Floyd–Warshall

用每一个点 k 作为“中间点”，尝试更新所有 i→j 的最短路径。
$$
dist[i][j] = min(dist[i][j],dist[i][k]+dist[k][j])
\\
\\
\text{负环判断 : }dist[i][i]<0\\
\text{如果 dist[i][i] < 0 → i 可达一个负权环。}\\
\text{因为自己到自己本应该为 0，如果出现 <0，说明存在让路径变更短的环 → 即负权环。}
$$

```python
for k in 0..n-1:
  for i in 0..n-1:
    for j in 0..n-1:
        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
```

$$
f^k(u, v) \text{ \{1, 2, 3, 4, 5, ..., k\}}\\
f^0(u, v)\\
f^1(u, v)\\
f^2(u, v)\\
...\\
f^{k-1}(u, v)\\
\\
\begin{flalign*}
& \text{Compare 2 cases: }\\
& \text{Have a mid node k: } & f^k(u, v) = f^{k-1}(u, k) + f^{k-1}(k, v)& \\
& \text{Connect directly: } & f^{k-1}(u, v)& 
\end{flalign*}
$$



##### Using adjacency matrix

```python
def FW(G):
  A = G.adjacency_matrix
  
  for k in range(n):
    for u in range(n):
      for v in range(n):
        if A[u, k] + A[k, v] < A[u, v]:
          A[u, v] = A[u, k] + A[k, v]
  
  return A
```





##### Code

```python
def floyd_warshall(n, edges):
    # 1. 初始化 dist 矩阵
    dist = [[float("inf")] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    
    # 2. 处理每条边 (u, v, w)
    for u, v, w in edges:
        dist[u][v] = min(dist[u][v], w)   # 允许多重边，取最小权重

    # 3. 主算法（三层循环）
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # 如果经过 k 更短，则更新
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    # 4. 负环检测
    for i in range(n):
        if dist[i][i] < 0:
            print("Warning: graph contains a negative cycle")

    return dist
```

```python
INF = float('inf')

def floyd_warshall(n, edges):
    # 初始化距离矩阵
    dist = [[INF] * n for _ in range(n)]
    nxt = [[None] * n for _ in range(n)]   # 用于路径恢复

    for i in range(n):
        dist[i][i] = 0

    for u, v, w in edges:
        dist[u][v] = w
        nxt[u][v] = v

    # 三层循环
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    nxt[i][j] = nxt[i][k]   # 路径恢复关键

    return dist, nxt


def recover_path(u, v, nxt):
    if nxt[u][v] is None:
        return []

    path = [u]
    while u != v:
        u = nxt[u][v]
        path.append(u)
    return path
```

- 时间复杂度 = O(n³)
- 空间复杂度 = O(n²)







## **Minimum Spanning Tree**

- Undirected Graph G



### Spanning Tree

对于一个 连通无向图 G(V, E)：Spanning Tree 是一个包含所有顶点、且恰好有 n−1 条边、并且无环的子图。

- 覆盖所有节点（spanning）
- 是一棵 树（tree）
- 没有环。
- 边数 = n − 1，既不能少也不能多。
- 连通

> - “极大无环”：再加一条边就会出现环
> - “极小连通”：删掉任何一条边都会断开图

一个图可以有很多 Spanning Trees

任意一次 DFS 或 BFS 的搜索树，就是一棵 Spanning Tree。

#### 生成树数量

连通图的 spanning tree 个数可以用 Kirchhoff Matrix Tree Theorem 计算。
$$
完全图 𝐾_n 的生成树数量： n^{n−2}
$$


### MST

所有 Spanning Trees 中权重最小的一棵

- 不能用于有向图
- MST 和最短路没有关系
- MST 不能处理负边

#### Cut Property（割性质）

给定一个图的任何“割”（把节点分成两部分 S 和 V−S）：跨割的所有边中，权重最小的那一条边，一定在某个 MST 中。

#### Cycle Property（环性质）

若在图中形成一个环：这个环中最重的那条边一定不会属于 MST。

#### 是否唯一？

- 若图中存在两个或更多“相同权重”的替代边 → MST 可能不唯一
- 若权重都互不相同 → MST **唯一**





### Kruskal's Algorithm

适用 Sparse（稀疏图），实现简单，但是需要排序边

（排序边 + 并查集）

1. 把所有边按 w 从小到大排序
2. 维护一个空的 MST 集合
3. 对每条边 (u, v)：
   - 如果 u 和 v 不在同一个组件 → 加入 MST（并查集合并）
   - 否则跳过
4. 当 MST 边数 = n−1 时停止

```python
def kruskal(n, edges):
    """
    n: number of vertices (0 ~ n-1)
    edges: list of (w, u, v)
    """

    # ----- Union-Find (Disjoint Set Union) -----
    parent = list(range(n))
    rank = [0] * n

    def find(x):
        if parent[x] == x:
          return x  # 路径压缩
        return find(parent[x])

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return
        if rank[ra] < rank[rb]:
            parent[ra] = rb
        else:
            parent[rb] = ra
            if rank[ra] == rank[rb]:
                rank[ra] += 1

    # ----- Kruskal 核心 -----
    edges.sort()        # 按权重排序
    mst = []
    total_weight = 0

    for w, u, v in edges:
        # 如果两个端点 u 和 v 已经属于同一个连通组件（即 find(u) == find(v)），那么加入这条边会形成环
        if find(u) != find(v):        # 不在同一集合 → 不成环
            union(u, v)               # 合并
            mst.append((u, v, w))     # 加入 MST
            total_weight += w
            if len(mst) == n - 1:
                break

    return total_weight, mst
```

- 时间复杂度：`O(mlogm)=O(mlogn)`

>Kruskal 的核心本质：排序 + 检测环 + 加边。
>
>并查集（Union-Find）只是其中一种“检测环”的方法，本质上 Kruskal 不依赖并查集，它依赖的是一种能快速判断一条边加入后是否会形成环的机制。
>
>Union-Find 单次判环复杂度 近似 O(1)。排序边 O(E log E) + 并查集操作 O(E·α(V)) ，整体为 O(E log E)。其中 α(V) 是反 Ackermann 函数，远小于 O(log V)，在所有实际输入中都 < 5，所以视为常数。
>
>- 按秩合并 → 树高度接近平衡 → find 的复杂度 = O(log n)。适用于单纯使用按秩合并（union by rank/size）不加路径压缩的情况。
>
>- 路径压缩（path compression）直接把树“打平”。find 的复杂度就不是 log n，而是O(α(n))（逆 Ackermann 函数），是已知最快的动态连通性数据结构（除了复杂得离谱的结构）。
>  >Ackermann 函数：
>  >
>  >- 比指数大
>  >- 比塔函数大
>  >- 比超级指数还大
>  >- 几乎宇宙级别
>  >
>  >在所有现实输入中，α(n) ≤ 4。
>  >
>  >| n                  | α(n) |
>  >| ------------------ | ---- |
>  >| 100                | 3    |
>  >| 10^6               | 4    |
>  >| 10^18              | 4    |
>  >| 10^(10^18)         | 5    |
>  >| 宇宙所有原子的数量 | 4    |
>  >
>  >所以我们说 `amortized find() ≈ O(1)`，是学术意义上的“几乎常数时间”。
>
>其他判环方法也可以用，比如：
>
>- 拓扑排序只适用于 有向无环图 DAG，MST是无向图。
>- 三色染色法（针对有向图）动态维护三色染色会非常复杂且慢
>- DFS visited + parent 检测：每次 DFS = O(V + E)，Kruskal 最多加 E 次边 → 总复杂度 = O(E(V + E))。
>
>##### 为什么 最终只有并查集真正适合 Kruskal？
>
>Kruskal 算法中，随着加入的边逐渐构造森林、最终成为 MST。所以它维护的是“不断增长的若干颗树”。
>
>在这个过程中，图结构是 动态变化的，每插入一条边都必须高效地判断是否让两个节点已经连通，除了并查集外，而其他方法在“动态图上的环检测”性能都不够好。



### Prim's Algorithm

适用 Dense（稠密图），不必排序所有边，但是需堆结构

（类似 Dijkstra 的扩展树）

从任意一点开始，每次选择连向“外部”的最小权重边，把新节点加入树。

1. 任意选择一个起点（如 0）
2. 把所有与起点相连的边放进最小堆
3. 每次从堆里取最小边
4. 若该边的目标节点未加入 MST → 加入，并把它的所有新边加入堆
5. 重复直到所有节点加入

```python
import heapq

def prim(n, graph):
    """
    graph[u] = [(v, w), ...]
    """
    visited = [False] * n
    min_heap = [(0, 0)]  # (权重, 节点)
    mst_weight = 0
    edges = []

    while min_heap:
        w, u = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        mst_weight += w

        for v, weight in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (weight, v))
                edges.append((u, v, weight))

    return mst_weight, edges
```

- 时间复杂度：`O(mlogn)`





## 



















