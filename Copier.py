import os
import shutil
cwd = os.getcwd()
exts = ['.jpg','.jpeg','.png']
Statistics = {'Paired':0,'Copied':0,'Not Paired':0}

CopyfromPath = r"D:\Guy\Uni\Project\ClownfishImages"
# Iterate over all files in the directory
for filename in os.listdir(cwd):
    # Check if the file is a text file
    if filename.endswith(".txt"):
        # If it's a text file, do something with it
        
        skip = False
        for ext in exts:
            base, _ = os.path.splitext(os.path.join(cwd,filename))
            if(os.path.exists(base + ext)):
                skip = True
                break
        if(not skip):
            suc = False
            base, _ = os.path.splitext(filename)
            for ext in exts:
                base, _ = os.path.splitext(os.path.join(CopyfromPath,filename))
                fullpath = base + ext
                if(os.path.exists(fullpath)):
                    suc = True
                    shutil.copyfile(fullpath, os.path.splitext(os.path.join(cwd,filename))[0] + ext)
                    Statistics['Copied'] += 1
                    break
            if(not suc):
                print(filename)
                Statistics['Not Paired'] += 1

        else:
            Statistics['Paired'] += 1
print(Statistics)
        # For example, you can open and read the file
