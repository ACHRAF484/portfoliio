#!/bin/bash

# GitHub Push with Personal Access Token
# GitHub no longer supports password authentication
# We'll use a Personal Access Token instead

cd /tmp/portfolio

echo "🔐 GitHub Authentication Setup"
echo "================================"
echo ""
echo "GitHub requires a Personal Access Token (not your password)"
echo ""
echo "Steps to create a token:"
echo "1. Go to: https://github.com/settings/tokens/new"
echo "2. Token name: Portfolio-Upload"
echo "3. Expiration: 30 days (or Custom)"
echo "4. Scopes: Check 'repo' only"
echo "5. Click 'Generate token'"
echo "6. COPY the token immediately (you won't see it again!)"
echo ""
echo "================================"
echo ""

# Read token from user
read -sp "Paste your Personal Access Token: " token
echo ""
echo ""

if [ -z "$token" ]; then
    echo "❌ No token provided. Exiting."
    exit 1
fi

# Update remote URL with token
echo "🔗 Configuring Git with token..."
git remote set-url origin "https://ACHRAF484:${token}@github.com/ACHRAF484/portfoliio.git"

# Push to GitHub
echo "📤 Pushing to GitHub..."
if git push -u origin main; then
    echo ""
    echo "✅ SUCCESS! Portfolio uploaded to GitHub!"
    echo "🌐 https://github.com/ACHRAF484/portfoliio"
    
    # Reset URL to remove token from config
    echo ""
    echo "🔒 Removing token from local config..."
    git remote set-url origin "https://github.com/ACHRAF484/portfoliio.git"
    echo "✅ Token removed from config (stored securely in memory only)"
else
    echo ""
    echo "❌ Push failed. Please check:"
    echo "   - Token is correct and not expired"
    echo "   - Repository exists at: https://github.com/ACHRAF484/portfoliio"
    echo "   - You have push access to the repository"
    exit 1
fi