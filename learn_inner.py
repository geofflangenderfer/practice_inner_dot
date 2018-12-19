import numpy as np
import os 



def print_matrices(inner = False):

    A = np.random.randint(10, size = (2,2))
    B = np.random.randint(10, size = (2,2))
    if inner:
        print("What's the inner product of A and B?")
    else:
        print("What's the dot product of A and B?")

    print("A = \n", A)
    print("B = \n", B)

    return  A, B


def take_input():

    prompt = ("\nInput your answer as comma seperated values i.e.:\n" 
             + "Answer = a, b, c, d --> Answer = [[a, b],\n"  
             + "                                  [c, d]]\n\n" 
             + "Answer =")

    answer = input(prompt)
    a = []
    for num in answer.split(','):
        a.append(int(num))

    a = np.array(a).reshape(2,2)

    return a
    

def check(m1, m2, input_ans, inner = False):


    if inner:
        correct = np.inner(m1, m2).flatten()
        inp = input_ans.flatten()
    else:
        correct = np.dot(m1, m2).flatten()
        inp = input_ans.flatten()

    for i in range(len(correct)):
        if correct[i] != inp[i]:
            return False

    return True



if __name__ == '__main__':

    # while I want to practice
        # clear screen
        # display both matrices
        # prompt for answer
        # check if correct and show answer
    os.system("clear")
    which_to_learn = input("0 to learn dot product, 1 for inner product: ")
    which_to_learn = int(which_to_learn)

    while True:
        os.system("clear")

        if which_to_learn == 0:
            A, B = print_matrices()
            input_answer = take_input()
            correct = check(A, B, input_answer)
        else:
            A, B = print_matrices(inner = True)
            input_answer = take_input()
            correct = check(A, B, input_answer, inner = True)

        if correct:
            print("Correct!")
        else:
            if which_to_learn == 0:
                print("Incorrect. Here's the answer:\n", np.dot(A, B))
            else:
                print("Incorrect. Here's the answer:\n", np.inner(A, B))

        ready = input("Press enter for the next problem")

