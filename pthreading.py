import threading
import random
import time

# Create an array X of 1 million random numbers between 1-100
X = [random.randint(1, 100) for i in range(1000000)]

# Define a function to calculate the sum of a given range of elements in X
def calculate_sum(start, end):
    sum = 0
    for i in range(start, end):
        sum += X[i]
    return sum

# Part 1
start_time = time.time()
total_sum = calculate_sum(0, len(X))
end_time = time.time()
print("PART 1:-")
print("The sum of elements in X using standard programming is:", total_sum)
print("Time taken to execute this program (function) is", end_time - start_time, "sec!!!")
# Part 2

def thread_sum(start, end, result):
    result[0] = calculate_sum(start, end)

# Create 2 symmetric threads
result1 = [0]
result2 = [0]
t1 = threading.Thread(target=thread_sum, args=(0, 500000, result1))
t2 = threading.Thread(target=thread_sum, args=(500000, 1000000, result2))

start_time1 = time.time()
t1.start()
start_time2 = time.time()
t2.start()


t1.join()
end_time1= time.time()
t2.join()
end_time2= time.time()


total_sum = result1[0] + result2[0]
print("PART 2:-")
print("The sum of the first 500000 elements of X using one of the threads:", result1[0])
print("The sum of the first 500000 elements of X using one of the threads:", result2[0])
print("the execution time taken by thread 1 is", end_time1 - start_time1, "sec!!!")
print("the execution time taken by thread 2 is", end_time2 - start_time2, "sec!!!")

# Part 3

result1 = [0]
result2 = [0]
t1 = threading.Thread(target=thread_sum, args=(0, 300000, result1))
t2 = threading.Thread(target=thread_sum, args=(300000, 1000000, result2))

start_time1 = time.time()
t1.start()
start_time2 = time.time()
t2.start()


t1.join()
end_time1= time.time()
t2.join()
end_time2= time.time()

total_sum = result1[0] + result2[0]
print("PART 3:-")
print("The sum of the first 300000 elements of X using one of the threads:", result1[0])
print("The sum of the first 700000 elements of X using one of the threads:", result2[0])
print("the execution time taken by thread 1 is", end_time1 - start_time1, "sec!!!")
print("the execution time taken by thread 2 is", end_time2 - start_time2, "sec!!!")


# Part 4

result1 = [0]
result2 = [0]
result3 = [0]
result4 = [0]
t1 = threading.Thread(target=thread_sum, args=(0, 250000, result1))
t2 = threading.Thread(target=thread_sum, args=(250000, 500000, result2))
t3 = threading.Thread(target=thread_sum, args=(500000, 750000, result3))
t4 = threading.Thread(target=thread_sum, args=(750000, 1000000, result4))

start_time1 = time.time()
t1.start()
start_time2 = time.time()
t2.start()
start_time3 = time.time()
t3.start()
start_time4 = time.time()
t4.start()

t1.join()
end_time1= time.time()
t2.join()
end_time2= time.time()
t3.join()
end_time3= time.time()
t4.join()
end_time4= time.time()

total_sum = result1[0] + result2[0] + result3[0] + result4[0]
print("PART 4:-")
print("The sum of the first 250000 elements of X using one of the threads:", result1[0])
print("The sum of the second 250000 elements of X using one of the threads:", result2[0])
print("The sum of the third 250000 elements of X using one of the threads:", result3[0])
print("The sum of the fourth 250000 elements of X using one of the threads:", result4[0])
print("the execution time taken by thread 1 is", end_time1 - start_time1, "sec!!!")
print("the execution time taken by thread 2 is", end_time2 - start_time2, "sec!!!")
print("the execution time taken by thread 3 is", end_time3 - start_time3, "sec!!!")
print("the execution time taken by thread 4 is", end_time4 - start_time4, "sec!!!")

# Part 5

result1 = [0]
result2 = [0]
result3 = [0]
result4 = [0]
t1 = threading.Thread(target=thread_sum, args=(0, 100000, result1))
t2 = threading.Thread(target=thread_sum, args=(100000, 300000, result2))
t3 = threading.Thread(target=thread_sum, args=(300000, 700000, result3))
t4 = threading.Thread(target=thread_sum, args=(700000, 1000000, result4))

start_time1 = time.time()
t1.start()
start_time2 = time.time()
t2.start()
start_time3 = time.time()
t3.start()
start_time4 = time.time()
t4.start()

t1.join()
end_time1= time.time()
t2.join()
end_time2= time.time()
t3.join()
end_time3= time.time()
t4.join()
end_time4= time.time()

total_sum = result1[0] + result2[0] + result3[0] + result4[0]
print("PART 5:-")
print("The sum of the first 100000 elements of X using one of the threads:", result1[0])
print("The sum of the second 200000 elements of X using one of the threads:", result2[0])
print("The sum of the third 400000 elements of X using one of the threads:", result3[0])
print("The sum of the fourth 300000 elements of X using one of the threads:", result4[0])
print("the execution time taken by thread 1 is", end_time1 - start_time1, "sec!!!")
print("the execution time taken by thread 2 is", end_time2 - start_time2, "sec!!!")
print("the execution time taken by thread 3 is", end_time3 - start_time3, "sec!!!")
print("the execution time taken by thread 4 is", end_time4 - start_time4, "sec!!!")
