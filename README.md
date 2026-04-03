# 📘 List Comprehension in Python

This file contains **10 important List Comprehension tasks** with examples and expected outputs.
List comprehension provides a concise way to create lists.

---

## 🔹 What is List Comprehension?

List comprehension is a short and readable way to create lists in Python.

### ✅ Syntax:

```python
[expression for item in iterable if condition]
```

---

# 🔥 Tasks

---

## 1️⃣ Square Numbers

👉 Create a list of squares from 1 to 10

```python
square_list = [i**2 for i in range(1, 11)]
print(square_list)
```

✅ Output:

```
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

---

## 2️⃣ Even Numbers

👉 Create a list of even numbers from 1 to 20

```python
even_list = [i for i in range(1, 21) if i % 2 == 0]
print(even_list)
```

✅ Output:

```
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

---

## 3️⃣ Odd Numbers

👉 Create a list of odd numbers from 1 to 15

```python
odd_list = [i for i in range(1, 16) if i % 2 != 0]
print(odd_list)
```

✅ Output:

```
[1, 3, 5, 7, 9, 11, 13, 15]
```

---

## 4️⃣ Multiply List Elements

👉 Multiply each element by 5

```python
original_list = [1, 2, 3, 4]
multi_list = [i * 5 for i in original_list]
print(multi_list)
```

✅ Output:

```
[5, 10, 15, 20]
```

---

## 5️⃣ Convert to Uppercase

👉 Convert names to uppercase

```python
names = ["rahul", "pavan", "raj"]
upper_names = [name.upper() for name in names]
print(upper_names)
```

✅ Output:

```
['RAHUL', 'PAVAN', 'RAJ']
```

---

## 6️⃣ Filter Positive Numbers

👉 Keep only positive numbers

```python
mix_list = [2, -3, 4, -1, 0]
pos_list = [i for i in mix_list if i > 0]
print(pos_list)
```

✅ Output:

```
[2, 4]
```

---

## 7️⃣ Length of Each Word

👉 Find length of each word

```python
words = ["apple", "banana", "kiwi"]
length_list = [len(word) for word in words]
print(length_list)
```

✅ Output:

```
[5, 6, 4]
```

---

## 8️⃣ Flatten Nested List

👉 Convert nested list into single list

```python
nested = [[1, 2], [3, 4], [5, 6]]
flat_list = [x for sub in nested for x in sub]
print(flat_list)
```

✅ Output:

```
[1, 2, 3, 4, 5, 6]
```

---

## 9️⃣ Numbers Divisible by 3

👉 Get numbers divisible by 3 (1–30)

```python
div3 = [i for i in range(1, 31) if i % 3 == 0]
print(div3)
```

✅ Output:

```
[3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
```

---

## 🔟 Conditional Expression

👉 Replace even → "Even", odd → "Odd"

```python
nums = [1, 2, 3, 4, 5]
result = ["Even" if i % 2 == 0 else "Odd" for i in nums]
print(result)
```

✅ Output:

```
['Odd', 'Even', 'Odd', 'Even', 'Odd']
```

---

# 🚀 Conclusion

* List comprehension makes code **short, clean, and readable**
* Useful for **filtering, mapping, and transforming data**
* Common in **interviews and real-world coding**

---

⭐ Practice daily to master Python!
