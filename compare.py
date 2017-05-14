import os

# normalizes inputFile1 of whitespace

with open('neo3_ecs_rules_only_latest.txt') as inputFile1, open('normalized_inputFile1.txt', 'w') as outputFile1:
    for line in inputFile1:
        outputFile1.write(line.strip(' \t\n\r'))  # get rid of whitespace
        outputFile1.write('\n')

with open('normalized_inputFile1_final.txt', 'w') as outputFile1_final:
    outputFile1_final.write(os.linesep.join([l for l in open(
        "normalized_inputFile1.txt", "r").read().splitlines() if l]))  # get rid of blank lines

# normalizes inputFile2 of whitespace

with open('Neo_1412_ECS_Rule_Final.txt') as inputFile2, open('normalized_inputFile2.txt', 'w') as outputFile2:
    for line in inputFile2:
        outputFile2.write(line.strip(' \t\n\r'))  # get rid of whitespace
        outputFile2.write('\n')

with open('normalized_inputFile2_final.txt', 'w') as outputFile2_final:
    outputFile2_final.write(os.linesep.join([l for l in open(
        "normalized_inputFile2.txt", "r").read().splitlines() if l]))  # get rid of blank lines

# opens normalized inputFile1 to compare
with open('normalized_inputFile1_final.txt') as file1list:
    file1l = file1list.read().splitlines()

# opens normalized inputFile2 to compare
with open('normalized_inputFile2_final.txt') as file2list:
    file2l = file2list.read().splitlines()

# assigns files to sets
set1 = file1l
set2 = file2l

# Prints everything in set b that's not in set a


def difference(a, b):
    return list(set(b).difference(set(a)))

list_diff = difference(set1, set2)

print('\n============================')
print('Delta - infile1 vs. infile2')
print('============================\n')
print(list_diff)
print('\n')
