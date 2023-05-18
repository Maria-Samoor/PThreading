Write a pthread program using  c/c++ or java code to calculate the sum of an arrays X of 1 million random numbers (between 1-100). Design  your program to have the following output:



part 1: The sum of elements in X using standard programing is : 76876987678

Time taken to execute this program ( function)  is 16 sec !!!


part 2: Now Using 2 symetric threads, 

The Sum of the first 500000  elements of X is using one of the threads:  76876


The Sum of the first 500000  elements of X is using one of the threads:  76876

the execuation time taken by thread 1 is 9 sec !!!
the execution time taken by thread 2 is 8 Sec !!


Part 3: Now Using 2 asymmetric  threads, 

The Sum of the first 300000  elements of X is using one of the threads:  76876


The Sum of the first 700000  elements of X is using one of the threads:  76876

the execution time taken by thread 1 is 3 sec !!!
the execution time taken by thread 2 is 12 Sec !!

part 4: repeat part 2 using 4 threads
part 5: repeat part 3 with 4 threads ( 100000 thread 1, 200000, thread 2, 400000 thread 3, and 300000 thread 4)
