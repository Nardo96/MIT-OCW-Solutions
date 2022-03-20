# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    perms = []
    if len(sequence) > 1:
        smaller_perms = get_permutations(sequence[1:]) #get permunations of sequence with the first character removed
        for elem in smaller_perms:
            for i in range(len(elem)+1):
                perms.append(elem[:i] + sequence[0] + elem[i:])
                
        return perms
    else: perms.append(sequence)
    return perms
                
    

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    example_input1 = 'abc'
    print('Input:', example_input1)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input1))

    example_input2 = 'df'
    print('Input:', example_input2)
    print('Expected Output:', ['df', 'fd'])
    print('Actual Output:', get_permutations(example_input2))
    
    example_input3 = 'g'
    print('Input:', example_input3)
    print('Expected Output:', ['g'])
    print('Actual Output:', get_permutations(example_input3))


