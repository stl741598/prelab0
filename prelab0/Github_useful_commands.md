# GitHub Common Commands

## 🔑 Set Up SSH Key

### Step 1: Create Your SSH Key
```bash
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```
- Replace `"your_email@example.com"` with your GitHub email.  
- Press **Enter** to accept default save location (`~/.ssh/id_rsa`).  
- Set passphrase (optional).  

### Step 2: Start SSH Agent and Add Key
```bash
bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa
exit
```

### Step 3: Copy Public Key
```bash
cat ~/.ssh/id_rsa.pub
```
- Copy the entire output (starts with `ssh-rsa`).  

### Step 4: Add Key to GitHub
1. Go to [GitHub SSH Settings](https://github.com/settings/keys).  
2. Click **New SSH key**.  
3. Enter a title (e.g., "CentOS Server").  
4. Paste the key, then save.  

### Step 5: Test SSH Connection
```bash
ssh -T git@github.com
```
Expected response:
```
Hi your-username! You've successfully authenticated, but GitHub does not provide shell access.
```

---

## 📂 Clone Repository
```bash
git clone git@github.com:your-username/your-repo.git
```

---

## 📌 Common Git Commands

### Check Repository Status
```bash
git status
```

### Add Files to Staging
```bash
git add filename         # Add specific file
git add .                # Add all changes
```

### Commit Changes
```bash
git commit -m "your commit message"
```

### Push to Remote
```bash
git push origin main     # Push to main branch
```

### Pull Latest Changes
```bash
git pull origin main
```

### Create & Switch to New Branch
```bash
git checkout -b branch-name
```

### Switch Branch
```bash
git checkout branch-name
```

### Merge Branch into Main
```bash
git checkout main
git merge branch-name
```

### View Commit History
```bash
git log --oneline --graph --decorate --all
```

---

✅ With this setup, you can securely use SSH for GitHub and quickly run the most common commands.
