# Concurrency   
Concurrency can greatly improve the performance of network automation tools by allowing python scripts to run more efficiently by doing multiple tasks at once. 

For Example, rather than interating through a list of devices one by one (synchronously) to run show commands, we can connect to all of the devices in the list concurrently(asynchronously) and run the commands all at once, greatly reducing how much time it takes for the script to run.

There are different techniques to choose from in Python. Which one you use depends on the use case.

The three available techniques are:   
1. Multiprocessing - Enables running a Python module using multiple processes.
2. Multithreading - Enables the more efficient use of a CPU
3. Async (ideal for network automation)   


## Multiprocessing   


## Threading   


## Async   




https://leimao.github.io/blog/Python-Concurrency-High-Level/