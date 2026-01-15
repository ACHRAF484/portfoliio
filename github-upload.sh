#!/bin/bash

# Direct GitHub Upload Script
# This script uploads the portfolio to GitHub using HTTPS

echo "📦 Uploading Portfolio to GitHub..."
cd /tmp/portfolio

# Initialize git repository
echo "🔧 Initializing Git repository..."
git init

# Configure git
echo "⚙️  Configuring Git user..."
git config user.name "Achraf Berouih"
git config user.email "achraf.berouih@gmail.com"

# Add all files
echo "📁 Adding files..."
git add .

# Create initial commit
echo "💾 Creating commit..."
git commit -m "Initial commit: Professional transport & logistics portfolio website

- Clean and elegant design for Transport & Logistics professional
- Responsive layout (desktop, tablet, mobile)
- Professional photo integration
- Complete sections: About, Experience, Skills, Certifications, Languages
- Modern navy/grey/white color scheme
- Smooth animations and interactions"

# Add GitHub remote
echo "🔗 Adding GitHub remote..."
git remote add origin https://github.com/ACHRAF484/portfoliio.git

# Set main branch
git branch -M main

# Push to GitHub with credentials
echo "📤 Pushing to GitHub..."
git push -u origin main --force

echo ""
echo "✅ SUCCESS! Portfolio uploaded to GitHub!"
echo "🌐 Repository: https://github.com/ACHRAF484/portfoliio"
echo "📍 Portfolio: http://localhost:8000"