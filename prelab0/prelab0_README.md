# Project Basics
This is your first assignment. You are given this assignment to make sure you can easily work with GitHub and GitHub Classroom, please refer to Github_useful_commands.md for commonly used Github commands. Your next assignments will be harder!

## Description
You are going to write a C++ program (arbitrary.cpp) that takes two argument. They are address of the input and output file respectively (with same names but in different folders). In the first file, there are two positive integers `a` and `b` separated by a single space. In the output, you should write five lines like below (update the first line to your info). 

```
<FirstName>, <LastName>, <StudentNumber>
1> a, b
2> a+b, a-b
3> a%b, a*b 
4> That's it! 
```

## Sample 1

### Run Command:
```
mkdir build && cd build
cmake ..
make
./arbitrary ../input/test1.txt ../output/test1.txt
```
#### Content of input/test1.txt
```
1 3
```

### Content of output/test1.txt after run:
```
<FirstName>, <LastName>, <StudentNumber>
1> 1, 3
2> 4, -2
3> 1, 3
4> That's it!
```

## Test
To test your code with all test cases in the `output/`, run this command in the main directory.
```
python3 test.py
```
