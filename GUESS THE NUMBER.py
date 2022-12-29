

#variables for game
runs = 0
wickets = 0
overs = 0

# constants for game
MAX_RUNS = 300
MAX_OVERS = 50
MAX_WICKETS = 10

# Welcome  message
print("Welcome to the Cricket Game!")

# while loop runs till all wickets are out or maximum overs are completed
while (wickets < MAX_WICKETS and overs < MAX_OVERS):
    # each over has 6 balls
    for ball in range(1,7):
        print("This is ball number ",ball)
        # take input from user
        runs_scored = int(input("Enter runs scored in this ball: "))

        #add runs scored to total runs
        runs += runs_scored

        #check if all runs are completed
        if runs >= MAX_RUNS:
            print("All runs completed!")
            break
        # check if wicket falls
        wicket_fallen = input("Did a wicket fall (yes/no): ")
        if wicket_fallen == 'yes':
            wickets += 1
    overs += 1

#print final score
print("Final Score: ", runs,"/",wickets,"in",overs,"overs")