def CalculateWaitingTime(at, bt, N):
 
    # Declare the array for waiting
    # time
    wt = [0]*N;
    wt[0] = 0;
 
    print("P.No.\tArrival Time\t" , "Burst Time\tWaiting Time");
    print("1" , "\t\t" , at[0] , "\t\t" , bt[0] , "\t\t" , wt[0]);
 
    # Calculating waiting time for
    # each process from the given
    # formula
    for i in range(1,5):
        wt[i] = (at[i - 1] + bt[i - 1] + wt[i - 1]) - at[i];
        print(i + 1 , "\t\t" , at[i] , "\t\t" , bt[i] , "\t\t" , wt[i]);
     
    average = 0.0;
    sum = 0;
 
    # Loop to calculate sum of all
    # waiting time
    for i in range(5):
        sum = sum + wt[i];
     
    # Find average waiting time
    # by dividing it by no. of process
    average = sum / N;
 
    # Print Average Waiting Time
    print("Average waiting time = " , average);
 
 # Driver code
if __name__ == '__main__':
    # Number of process
    N = 5;
 
    # Array for Arrival time
    at = [ 0, 1, 2, 3, 4 ];
 
    # Array for Burst Time
    bt = [ 4, 3, 1, 2, 5 ];
 
    # Function call to find
    # waiting time
    CalculateWaitingTime(at, bt, N);
