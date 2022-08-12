# Version Control with Git   
Version Control, Git in this case, is an extremely useful tool to learn when doing development work. This section covers some essential Git basics.

## Installing Git and Setup 
Documentation for intalling Git can be found [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)   

### User Setup   
Git can be configured with users globally on a system, or local to a repository:
```
Global
git config --global user.name "User Name"
git config --global user.email youremail@example.com

Local
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
 - To track all untracked files in the current directory, use ```git add .```   

To make a commit, use ```git commit -m {comment}```   
 - The "-m" option is used to add a comment to the commit.   

In the below example, I add some changes to be tracked, create a commit, then push it to the remote repostiroy on Github.
```zsh
python-for-network-engineers % git status
On branch master
Your branch is up to date with 'origin/master'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   git/README.md

no changes added to commit (use "git add" and/or "git commit -a")
python-for-network-engineers % git add .
python-for-network-engineers % git status
On branch master
Your branch is up to date with 'origin/master'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	modified:   git/README.md

python-for-network-engineers % git commit -m "update git README"
[master 28d6a24] update git README
 1 file changed, 31 insertions(+)
python-for-network-engineers % git status
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
python-for-network-engineers % git push origin master
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 10 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (4/4), 1.50 KiB | 1.50 MiB/s, done.
Total 4 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/namiles/python-for-network-engineers.git
   08a5be3..28d6a24  master -> master
python-for-network-engineers %
```

## Git Logs   
Git logs can be used to see the record of changes made, or commits, in a repository. To view the log, use ```git log```. To view the git log in a more concise format, use ```git log --oneline```.    
- Shows the commit checksum, author, date of the commit, and the commit message.
- The git commit checksum can be used to "go back in time" to when that commit was done.

## Git Branches   
Git branches are one of the main reasons why using version control is so useful. With branches, you can create a "Copy" of a local repositry, but in a seaprate workspace. They are commonly used to make experimental changes, or work on new features without interfering with the main branch code.   

To see existing branches, use ```git branch``` in a local repostiroy.   
- The main branch is usually caleld either "main" or "master".   

To create a new branch, use ```git branch {name}```.   
To switch to a branch, use ```git checkout {branch}```.   
To create AND switch to a branch, use ```git checkout -b {branch}```.
To FORCE delete a branch, use ```git branch -D {branch}```.   

In the below example, I create and switch to a new branch called "new_feature_branch", list the branches, switch back to the master branch, then delete the "new_feature_branch" branch.
```zsh
python-for-network-engineers % git branch
* master
python-for-network-engineers % git checkout -b new_feature_branch
Switched to a new branch 'new_feature_branch'
python-for-network-engineers % git branch
  master
* new_feature_branch
python-for-network-engineers % git checkout master
M	git/README.md
Switched to branch 'master'
Your branch is up to date with 'origin/master'.
python-for-network-engineers % git branch -D new_feature_branch
Deleted branch new_feature_branch (was 08a5be3).
```   

## Git Merge and Git Rebase   
Git merge and git rebase are both commands that can be used to move changes from branches to the master/main branch. However, each one has different uses.   

### Git Merge   
To merge changes in a branch to the master/main branch, you want to be in the master branch, or where you want the changes to be brought to.   
Then, use ```git merge {branch}```. This will merge any changes in the specified branch into the master/main branch.

```zsh
python-for-network-engineers/git (git_merge_readme) » git checkout master                                                                                       nmiles@Nicks-MacBook-Pro
Switched to branch 'master'
Your branch is up to date with 'origin/master'.

python-for-network-engineers/git (master) » git merge git_merge_readme                                                                                          nmiles@Nicks-MacBook-Pro
Updating 8868b9d..35838ce
Fast-forward
 git/README.md | 11 ++++++++++-
 1 file changed, 10 insertions(+), 1 deletion(-)
```

### Git Rebase   
The main difference betweeen **git merge** and **git rebase** is that when using git merge, all of the separate commits are brought over into the master/main branch, which can make the git log muddy and difficult to follow.   
Git rebase helps keep the git timeline clean, and actually re-writes the the git history for it to be linear and easy to read.   

The general rule of thumb is to use rebase if using a private repository, and merge when using public repositories.

### The .gitignore File
.gitignore is a special file in Git repositories that can be used to prevent Git from tracking certain files or directories within the local repository. For example, if you have a file that you are only using for testing, you can add it to a .gitignore file and Git will not asssociate it with the repository.  

In the .gitignore file for this repository, I have the below files/directories:
```zsh
python-for-network-engineers (master*) » cat .gitignore
__pycache__
.venv/
```
