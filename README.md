# CPU Scheduling C++/Python
Scheduling is a process to finish work on time. CPU scheduling is a process that allows on e-process to use the CPU while the another process is delayed due to unavailability of any resources. Whenever the CPU becomes idle, the operating system must select one of the processes in the line ready for launch. The selection process is done by a temporary (CPU) scheduler. The Scheduler selects between memory processes ready to launch and assigns the CPU to one of them. For this project, we will utilize process scheduling as a multi process manager handling the removal of an active process from the CPU and selecting the other process based on a specific strategy involving data structures and algoirthms.

## What is a process?
 In computer science, a process is the insurance of a computer program that is being executed by one or many threads. It contains the programming code and its usage/activity. The algorithms used in this project are designed specifically for x86_64 GCC, G++, and clang compilers.
 
## Using process memory for efficient algorithms
 The process memory is divided into 4 catgeories:
 * Text: Integrated program code read from fixed storage when the program is launched.
 * Data: Global and static variables distributed from executed programs.
 * Heap: Data structure used for dynamic memory allocation and is managed by calls through CRUD.
 * Stack: Used for local variables. The space in the stack data structure is reserved for local variables.

## Process Scheduling and why we do it
 * Scheduling: An important area when it comes to computer environments. Scheduling allows programs to work on the CPU through the Operating System of the computer.

 * Process Scheduling: Let's the OS allocate CPU time for each process i.e. algorithms. Another reason why we use the process scheduling is due to tha fact that it keeps the CPU busy at all times which will allow us to get accurate estimates when we measure for performance. 
    
# Design Patterns for Scheduling Algorithms
* Preemptive Scheduling :
 Used when a process switches from running state to ready state or from waiting state to the ready state.
* Non-Preemptive Scheduling:
 Used when a process terminates or when a process switches from running state to waiting state.
 
1. First Come First Serve (FCFS):
* Simple operating system scheduling algorithm. First come first serve scheduling algorithm states that the process that requests the CPU first allocated the CPU first and is implemented by using FIFO Queue.

2. Shortest Job First (SJF):
* Is a scheduling process that selects the waiting process with the smallest execution time to execute next. This scheduling method may or may not be preemptive. Significantly reduces the average waiting time for other processes waiting to be executed. The full form of SJF is Shortest Job First.

3. Longest Job First (LJF):
* Scheduling process is just opposite of shortest job first (SJF), as the name suggests this algorithm is based upon the fact that the process with the largest burst time is processed first. Longest Job First is non-preemptive in nature.

4. Round Robin:
* Round Robin is a CPU scheduling algorithm where each process is cyclically assigned a fixed time slot. It is the preemptive version of First come First Serve CPU Scheduling algorithm. Round Robin CPU Algorithm generally focuses on Time Sharing technique. 

5. Shortest Remaining Time First:
* Is the preemptive version of the Shortest job first which we have discussed earlier where the processor is allocated to the job closest to completion. In SRTF the process with the smallest amount of time remaining until completion is selected to execute.

6. Longest Remaining Time First:
*  Is a preemptive version of the longest job first scheduling algorithm. This scheduling algorithm is used by the operating system to program incoming processes for use in a systematic way. This algorithm schedules those processes first which have the longest processing time remaining for completion.

