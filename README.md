# CPU Scheduling C++/Python
Scheduling is a process to finish work on time. CPU scheduling is a process that allows on e-process to use the CPU while the another process is delayed due to unavailability of any resources. Whenever the CPU becomes idle, the operating system must select one of the processes in the line ready for launch. The selection process is done by a temporary (CPU) scheduler. The Scheduler selects between memory processes ready to launch and assigns the CPU to one of them. For this project, we will utilize process scheduling as a multi process manager handling the removal of an active process from the CPU and selecting the other process based on a specific strategy involving data structures and algoirthms.

## What is a process?
 In computer science, a process is the insurance of a computer program that is being executed by one or many threads. It contains the programming code and its usage/activity. The algorithms used in this project are designed specifically for x86_64 GCC, G++, and clang compilers.
 
 ## Using process memory for efficient algorithms
 The process memory is divided into 4 catgeories:
  ## Text:
    Integrated program code read from fixed storage when the program is launched.
  ## Data:
    Global and static variables distributed from executed programs.
  ## Heap:
   Data structure used for dynamic memory allocation and is managed by calls through CRUD
  ## Stack:
   Used for local variables. The space in the stack data structure is reserved for local variables.

## Process Scheduling and why we do it
  Scheduling:
    
