# Q6: HMM Probability

p_book_given_vb = 0.6
p_book_given_nn = 0.4

p_start_vb = 0.5
p_start_nn = 0.5

# HMM likelihood
vb_probability = p_start_vb * p_book_given_vb
nn_probability = p_start_nn * p_book_given_nn

print("Probability of book as VB =", vb_probability)
print("Probability of book as NN =", nn_probability)

print()

if vb_probability > nn_probability:
    print("HMM selects VB")
else:
    print("HMM selects NN")
