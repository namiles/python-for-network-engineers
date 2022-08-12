# Version Control with Git   
Version Control, Git in this case, is an extremely useful tool to learn when doing development work. This section covers some essential Git basics.

## Installing Git and Setup 
Documentation for intalling Git can be found [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)   

### User Setup   
Git can be configured with users globally on a system, or local to a repository:
```
git config --global user.name "User Name"
git config --global user.email youremail@example.com
git config --local user.name "User Name"
git config --local user.email youremail@example.com
```

To view Git config, use ```git config --list```

### Initializing a Git Repository   
To initialize a new Git repository, you can use ```git init```.     
To view the status of Git repository, use ```git status```.   
 - Git status can show the current status of a local git repostiroy, such as uncomitted changes, untracked files, and commmits ready to be pushed.   
To add files to be tracked by Git, use the ```git add``` command.   
 - To track a specific file, use ```git add {file}```   
 - To add any files within a driectory, use ```git add .```   
To make a commit, use ```git commit -m {comment}```   
 - The "-m" option is used to add a comment to the commit.   



## Git Logs   
