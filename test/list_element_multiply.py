#encoding=utf-8

"""
Consider the following code snippet:

1. list = [ [ ] ] * 5
2. list  # output?
3. list[0].append(10)
4. list  # output?
5. list[1].append(20)
6. list  # output?
7. list.append(30)
8. list  # output?
What will be the ouput of lines 2, 4, 6, and 8? Explain your answer.


"""

list = [ [ ] ] * 5
print(list)  # output?
list[0].append(10)
print(list)  # output?
list[1].append(20)
print(list)  # output?
list.append(30)
print(list)  # output?

"""

The output will be as follows:

[[], [], [], [], []]
[[10], [10], [10], [10], [10]]

Here’s why:

The first line of output is presumably intuitive and easy to understand; i.e., list = [ [ ] ] * 5 simply creates a list
 of 5 lists.

However, the key thing to understand here is that the statement list = [ [ ] ] * 5 does NOT create a list containing 5
distinct lists; rather, it creates a a list of 5 references to the same list. With this understanding, we can better
understand the rest of the output.

list[0].append(10) appends 10 to the first list. But since all 5 lists refer to the same list, the output is:
[[10], [10], [10], [10], [10]].

Similarly, list[1].append(20) appends 20 to the second list. But again, since all 5 lists refer to the same list, the
output is now: [[10, 20], [10, 20], [10, 20], [10, 20], [10, 20]].

In contrast, list.append(30) is appending an entirely new element to the “outer” list, which therefore yields the
output: [[10, 20], [10, 20], [10, 20], [10, 20], [10, 20], 30].

"""