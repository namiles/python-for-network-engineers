# Concurrency   
Concurrency can greatly improve the performance of network automation tools by allowing python scripts to run more efficiently by doing multiple tasks at once. 

For Example, rather than interating through a list of devices one by one (synchronously) to run show commands, we can connect to all of the devices in the list concurrently (asynchronously) and run the commands all at once, greatly reducing how much time it takes for the script to run.

There are different techniques to choose from in Python. Which one you use depends on the use case.

The three available techniques are:   
1. Multiprocessing - Enables running a Python module using multiple processes.
2. Multithreading - Enables the more efficient use of a CPU
3. Asynchronous Input/Output (asyncio)   

**CPU-bound** tasks are tasks that are bound by the efficiency of a machines CPU. Examples could be calculations or machine learning.   

**I/O-bound** tasks are tasks that are bound by having to wait for external information to continue processing. Network autmation is a good example of an I/O bound task.   

## Multiprocessing   
- Form of concurrency that works in parralell, meaning all at the same time.
- Achieves paralellism by creating multiple processes that can be spread across different CPU cores.
- Best for CPU bound/intensive tasks

## Threading   
- 

## Asyncio   
- 



https://leimao.github.io/blog/Python-Concurrency-High-Level/