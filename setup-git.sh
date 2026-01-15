#!/bin/bash

# Portfolio Git Setup Script
# This script initializes git and pushes to GitHub

cd /tmp/portfolio

echo "🔧 Setting up Git repository..."

# Initialize git
git init

# Configure git
git config user.name "Achraf Berouih"
git config user.email "achraf.berouih@gmail.com"

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: Professional transport & logistics portfolio"

# Add remote
git remote add origin https://github.com/ACHRAF484/portfoliio.git

# Set main branch
git branch -M main

# Push to GitHub
echo "📤 Pushing to GitHub..."
git push -u origin main

echo "✅ Portfolio pushed to GitHub successfully!"
echo "🌐 Your portfolio is live at: https://github.com/ACHRAF484/portfoliio"