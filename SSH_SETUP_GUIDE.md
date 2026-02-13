# 🔐 GitHub SSH Setup Guide

Your portfolio is ready to upload! Follow these steps to complete the process:

## Your SSH Public Key (COPY THIS)
```
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIMp5a9/CpPRV4CTdSk1DSxYq5RsVBnxRYA2wXFl/oMMm achraf.berouih@gmail.com
```

## Step 1: Add SSH Key to GitHub
1. Go to: https://github.com/settings/keys
2. Click "New SSH key"
3. Title: "MacBook Portfolio"
4. Key type: "Authentication Key"
5. Paste the SSH public key above
6. Click "Add SSH key"

## Step 2: Push to GitHub
Once you've added the SSH key, run:
```bash
cd /tmp/portfolio
git push -u origin main
```

## Step 3: Verify Upload
- Go to: https://github.com/ACHRAF484/portfoliio
- You should see all your portfolio files

## Step 4: Enable GitHub Pages (Optional)
1. Go to Settings → Pages
2. Select "main" branch
3. Click "Save"
4. Your site will be live at: https://achraf484.github.io/portfoliio/

---

### Current Status:
- ✅ Git initialized
- ✅ All files committed
- ✅ SSH key generated
- ⏳ Waiting for SSH key to be added to GitHub
- ⏳ Ready to push

### Files Ready to Upload:
- index.html
- style.css
- script.js
- images/profile.jpg
- README.md
- .gitignore