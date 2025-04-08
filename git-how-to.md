# Git/GitHub Quick Start Guide

## 1. Generating an SSH Key

bash
# Create an ED25519 key (recommended)
ssh-keygen -t ed25519 -C "your.email@example.com"

# For older systems, you can use RSA:
# ssh-keygen -t rsa -b 4096 -C "your.email@example.com"

# Simply press Enter to accept the default location (~/.ssh/)
# Optional: Add a passphrase for extra security

# Verify the creation:
cat ~/.ssh/id_ed25519.pub
2. Adding the Key to GitHub
Copy the public key:

bash
Copy
# Linux/Mac
cat ~/.ssh/id_ed25519.pub | pbcopy  # Mac
cat ~/.ssh/id_ed25519.pub | xclip -sel clip  # Linux

# Windows (Git Bash)
cat ~/.ssh/id_ed25519.pub | clip
GitHub Settings:

Navigate to the SSH settings in your GitHub account.

Click "Add SSH Key"

Title: Personal Device (or another descriptive name)

Paste the key into the "Key" field.

Click "Add SSH Key".

Verify the connection:

bash
Copy
ssh -T git@github.com
# Successful message: "Hi username! You've successfully authenticated..."
3. Cloning a Repository
bash
Copy
# Get the SSH URL from the GitHub repo page (Code -> SSH)
git clone git@github.com:username/repo-name.git

# Navigate to the cloned repository:
cd repo-name

Helpful Tips:

Use ssh-add ~/.ssh/id_ed25519 to add your key to the SSH agent.

Managing multiple keys? Create a ~/.ssh/config file for host aliases.

First time setup? Configure Git:

bash
Copy
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com
/
