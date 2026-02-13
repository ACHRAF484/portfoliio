# 📤 Push to GitHub - Two Methods

Your portfolio is committed locally but the GitHub repo is empty. Choose one method:

## ✅ Method 1: Personal Access Token (Easiest)

### Step 1: Create a Personal Access Token
1. Go to: https://github.com/settings/tokens/new
2. Token name: "Portfolio Upload"
3. Expiration: 30 days
4. Scopes: Check only "repo" (for Full control of private repositories)
5. Click "Generate token"
6. **COPY the token** (you won't see it again!)

### Step 2: Push using the token
Replace `YOUR_TOKEN` with the token you copied:

```bash
cd /tmp/portfolio
git remote set-url origin https://ACHRAF484:YOUR_TOKEN@github.com/ACHRAF484/portfoliio.git
git push -u origin main
```

After push, you can reset the URL:
```bash
git remote set-url origin https://github.com/ACHRAF484/portfoliio.git
```

---

## ✅ Method 2: SSH Key (More Secure)

You already have an SSH key generated. Just add it to GitHub:

1. Go to: https://github.com/settings/keys
2. Click "New SSH key"
3. Title: "MacBook Portfolio"
4. Paste this key:
   ```
   ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIMp5a9/CpPRV4CTdSk1DSxYq5RsVBnxRYA2wXFl/oMMm achraf.berouih@gmail.com
   ```
5. Click "Add SSH key"
6. Wait 30 seconds for GitHub to process
7. Then run:
   ```bash
   cd /tmp/portfolio
   git push -u origin main
   ```

---

## Which method to use?
- **Method 1 (Token)**: Faster, works immediately
- **Method 2 (SSH)**: More secure for future use

**I recommend Method 1 for quick upload, then Method 2 for future work.**