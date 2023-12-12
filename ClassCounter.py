import os
cwd = os.getcwd()

# List all files in the current working directory
files = os.listdir(cwd)
ClassCounts = {}
# Filter and print only .txt files
for file in files:
    if file.endswith('.txt'):
        with open(file, 'r') as f:
            for line in f:
                #print(line)
                labelclass = int(line.split(' ')[0])
                if(not labelclass in ClassCounts):
                    ClassCounts[labelclass] = 0
                ClassCounts[labelclass] += 1
classes = ["fish","clownfish","mantaray","jellyfish","seaturtle","dolphin","shark","seal","swordfish","butterflyfish"]
for Key in ClassCounts:
    print(f"{classes[Key]} : {ClassCounts[Key]}")