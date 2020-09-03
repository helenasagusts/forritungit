#Biðja notanda um tölu fyrir lengdina á sequence
n = int(input("Enter the length of the sequence: ")) # Do not change this line

num_1 = 1
num_2 = 2
num_3 = 3
num_4 = 4

print(num_1)
print(num_2)
print(num_3)

for i in range(1, n-2):
    num_4 = num_1 + num_2 + num_3
    num_1 = num_2
    num_2 = num_3
    num_3 = num_4
    print(num_4)