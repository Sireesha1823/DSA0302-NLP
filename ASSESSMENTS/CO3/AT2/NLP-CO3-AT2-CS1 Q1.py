# Q1: Maximum Likelihood Estimate (MLE)

count_data_science = 3
count_data = 3

probability = count_data_science / count_data

print("P(science | data) =", probability)
print("Percentage =", probability * 100, "%")

if probability == 1:
    print("Interpretation: After 'data', 'science' is predicted with 100% probability.")
