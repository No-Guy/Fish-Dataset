import os
from tqdm import tqdm
cwd = os.getcwd()

# List all files in the current working directory
files = os.listdir(cwd)
ClassCounts = {}
# Filter and print only .txt files
for file in tqdm(files):
    if file.endswith('.txt'):
        with open(file, 'r') as f:
            for line in f:
                #print(line)
                labelclass = int(line.split(' ')[0])
                if(not labelclass in ClassCounts):
                    ClassCounts[labelclass] = 0
                ClassCounts[labelclass] += 1
classes = ["fish","clownfish","mantaray","jellyfish","seaturtle","dolphin","shark","seal","swordfish","butterflyfish"]
sum = 0
for Key in ClassCounts:
    print(f"{classes[Key]} : {ClassCounts[Key]}")
    sum += ClassCounts[Key]
print(f"Total Objects {sum}")