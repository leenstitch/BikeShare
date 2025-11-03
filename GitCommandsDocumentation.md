\# Git Commands Documentation

#GitHub Profile GitHub Profile:
[GitHub Profile](https://github.com/leenstitch)


\-\--

\# 1 Initialize Local Repository \`\`\`bash git init \`\`\` \# 2 Add
Files to Staging \`\`\`bash git add . \`\`\`

\# 3 Commit Changes Locally \`\`\`bash git commit -m \"Initial commit\"
\`\`\`

\# 4 Connect Local Repository to GitHub #Links the local repository to
the remote repository on GitHub. \`\`\`bash git remote add origin
https://github.com/leenstitch/BikeShare.git \`\`\`

#Pushes the files for the first time to the main branch on GitHub.
\`\`\`bash git push -u origin main \`\`\`

\# 5 Create New Branches \`\`\`bash git checkout -b documentation git
checkout -b refactoring \`\`\`

\# 6 Add, Commit, and Push Changes in Documentation Branch \`\`\`bash
git checkout documentation git add README.md GitCommandsDocumentation.md
git commit -m \"Added project documentation\" git push -u origin
documentation \`\`\`

\# 7 Add, Commit, and Push Changes in Refactoring Branch \`\`\`bash git
checkout refactoring git add bikeshare.py git commit -m \"Refactored
bikeshare.py for efficiency\" git push -u origin refactoring \`\`\`

\# 8 Update Main Branch \`\`\`bash git checkout main git add README.md
bikeshare.py git commit -m \"Updated README.md and bikeshare.py\" git
push \`\`\`

\# 9 Switch Between Branches \`\`\`bash git checkout main git checkout
documentation git checkout refactoring \`\`\`

\# 10 Check Branches \`\`\`bash git branch -a \`\`\`
