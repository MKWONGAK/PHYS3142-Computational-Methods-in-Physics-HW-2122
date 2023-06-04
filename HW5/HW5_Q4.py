population = 7.403e6
confirmed = 538602
false_pos = 0.03

prob_infect = confirmed/population

#equation from lecture note
actual_prob = prob_infect*(1-false_pos)/(prob_infect*(1-false_pos)+(1-prob_infect)*false_pos)

print("The probability is", prob_infect)
print("The actual probability is", actual_prob)