ranks = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
scores = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]
total = 0
credits = 0
for x in range(20) :
    subject, score, rank = [*input().split()]
    if (rank != 'P') : 
        total += scores[ranks.index(rank)] * float(score)
        credits += float(score)
print(total / credits)