#!/bin/bash

# GitHub Push Script with Token Support

cd /tmp/portfolio

echo "📤 Pushing portfolio to GitHub..."
echo ""
echo "⚠️  You will be prompted for GitHub credentials."
echo "   - Use your GitHub username"
echo "   - Use a Personal Access Token instead of your password"
echo ""
echo "To create a Personal Access Token:"
echo "1. Go to: https://github.com/settings/tokens"
echo "2. Click 'Generate new token'"
echo "3. Select 'repo' scope"
echo "4. Copy and paste the token when prompted"
echo ""

git push -u origin main --verbose

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ SUCCESS! Portfolio pushed to GitHub!"
    echo "🌐 Repository: https://github.com/ACHRAF484/portfoliio"
    echo "📍 Local: http://localhost:8000"
else
    echo ""
    echo "❌ Push failed. Please check your GitHub credentials."
fi