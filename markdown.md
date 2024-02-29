## Version Control System

### Centralised vs distributed 

A Centralised Version Control System is a version control system where a central repository stores the entire history of the project. Developers check out a working copy of the code from the central repository onto their local machines, make changes locally, and then commit those changes back to the central repository.  

A Distributed Version Control System is a version control system that does not rely on a central repository. Instead, each developer has a complete copy of the repository, including the entire project history, on their local machine. Developers can work independently, committing changes to their local repository and later pushing those changes to share with others.

![img.png](img.png)

## Git

### Check your Git version
To check your version of Git:
```commandline
git --version
```

### The Three Stages in Git:

1. **Untracked:** modified files/folders that have not been staged.
2. **Tracked:** modified files/folders that have been staged.
3. **Committed:** modified files/folders that have been committed.

### Command workflow of commands:

- `git init` - to initialise Git.
- `git status` - to see if something if there's an existing git repo OR to view the status of changes as untracked, modified, or staged.
- `git add .` to stage changes.
- `git commit -m "[desired-message]"` - to commit changes with a message. 

    <br> Note: If you need to remove a file or directory from the Git index (i.e., the staging area) without deleting them from the working directory, run either:

    - `git rm --cached [your-file]` to remove files from the staging area.
    - `git rm --cached -r [your-directory]/` to remove a directory recursively from the staging area (including all its contents), using the the -r or --recursive flag.
  
        For example, run the following to remove the **.venv** directory:
        ```
      git rm --cached -r .venv/
      ```
    Note: Best practice is to add the **.venv** folder to the **.gitignore** file before performing any staging and commits.

### .gitignore

The purpose of `.gitignore` is to tell Git which files and patterns to exclude when staging changes or creating commits. It helps keep your repository clean, avoids unnecessary clutter, and prevents sensitive information from being accidentally committed.

## Dealing with different versions
It's important to take snapshots of your versions using `git commit` command. 

**git log** <br>
If you wanted to compare two commits (i.e. two versions/snapshots), you can copy the commit IDs – which you can retrieve by running:
```commandline
git log
```

### Difference between versions
**git diff**<br>
Run the command to show the differences:
```commandline
git diff [old-commitID] [new-commitID]
```
> Example: Let's say the commit ID for version 1 is 12345 and the commit ID for version 1 is 67890.
The command to run would be `git diff 12345 67890`

Any new additions will start with a plus sign (+) and any deletions will start with a minus sigh (-).



### Viewing different versions

To view different versions you can run the following:

```
git checkout [commitID]
```

To view the latest version of that branch (which is called 'main' in this case):
```
git checkout main
```

To do a hard reset where the risk:
```
git checkout main
```

git reset
explain branching briefly

