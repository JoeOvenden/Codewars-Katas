# There is a queue for the self-checkout tills at the supermarket. Your task is write a function to calculate the total time required for all the customers to check out!

# input
# customers: an array of positive integers representing the queue. Each integer represents a customer, and its value is the amount of time they require to check out.
# n: a positive integer, the number of checkout tills.
# output
# The function should return an integer, the total time required.

def queue_time(customers, n):
    time_taken = 0
    tills = [0 for i in range(n)]
        
    while customers != []:
        # Assign customers to empty tills
        for i in range(n):
            if tills[i] == 0:
                try:
                    tills[i] = customers.pop(0)
                except IndexError:
                    break
                
        # Jump ahead to when the next till clears
        time_increase = min(tills)
        time_taken += time_increase
        tills = [t - time_increase for t in tills]
        
    # The queue has finished so wait for all the tills to be cleared and then return time
    time_taken += max(tills)
    return time_taken