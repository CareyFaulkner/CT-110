# Carey Faulkner
# 13 April 2025
# P4HW1
# Score Analyzer

# Step 1: Ask user how many scores they want to enter
num_scores = int(input("How many scores would you like to enter? "))

# Step 2: Collect valid scores in a list
score_list = []
for i in range(num_scores):
    while True:
        try:
            score = float(input(f"Enter score #{i+1}: "))
            if 0 <= score <= 100:
                score_list.append(score)
                break
            else:
                print("Invalid score. Please enter a value between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Step 3: Process scores
lowest_score = min(score_list)
modified_scores = score_list.copy()
modified_scores.remove(lowest_score)
average = sum(modified_scores) / len(modified_scores)

# Step 4: Determine letter grade
if average >= 90:
    letter = 'A'
elif average >= 80:
    letter = 'B'
elif average >= 70:
    letter = 'C'
elif average >= 60:
    letter = 'D'
else:
    letter = 'F'

# Step 5: Display results
print("\n----- Results -----")
print(f"Lowest score: {lowest_score}")
print(f"Modified score list (lowest removed): {modified_scores}")
print(f"Average of scores: {average:.2f}")
print(f"Letter grade: {letter}")