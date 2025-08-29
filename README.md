# Devops-practice
git-learning 

## Basic Git Commands  

- git init → make current folder a Git repo  
- git clone <repo-url> → copy repo from remote to local  
- git remote add origin <repo-url> → connect local repo to remote  
- git add . → move all changes to staging  
- git commit -m "message" → save changes in local repo  
- git push origin main → send commits to remote repo  
- git pull origin main → fetch + merge updates from remote  
- git fetch → download updates from remote (no merge)  

## Branching & Merging  

- git branch → list branches  
- git branch <name> → create new branch  
- git checkout <branch> → switch branch  
- git switch <branch> → (new way) switch branch  
- git checkout -b <name> → create + switch branch
- git diff <branch name> → to compare commits, branches, files and more 
- git merge <branch name > → merge branch into current (megrge two branch)
- git rebase <branch> → reapply commits on top of another branch
   

## Status & History  

- git status → show current state of files  
- git log → show commit history  
- git log --oneline → compact history  
- git show <commit-id> → details of a commit  
- git diff --staged → show changes staged for commit  

## Undo / Fix  

- git restore <file> → undo changes in file (before staging)  
- git reset <file> → unstage file (keep changes)  
- git reset --hard <commit-id> → reset repo to old commit (⚠ deletes changes)  
- git revert <commit-id> → make new commit that undoes given commit  
- git amend -m "new message" → change last commit message  

## Collaboration  

- git pull → get latest changes from remote  
- git fetch → fetch remote changes (no merge)  
- git stash → save uncommitted changes temporarily  
- git stash pop → restore stashed changes  

## File States in Git  

- Untracked → new file, not yet tracked  
- Modified → file changed  
- Staged → file ready to commit  
- Unmodified → no changes (already committed)  


