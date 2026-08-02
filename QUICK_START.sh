#!/bin/bash

# ============================================================
# 3D Portfolio - Quick Setup Script for ihack Audio
# ============================================================
# This script downloads the original repo and applies 
# the customized files automatically
# ============================================================

echo "🚀 Setting up your 3D Portfolio for ihack Audio..."
echo ""

# Step 1: Clone the original repository
echo "📥 Step 1: Downloading original repository..."
if [ -d "3d-portfolio" ]; then
    echo "   Folder '3d-portfolio' already exists. Removing..."
    rm -rf 3d-portfolio
fi

git clone https://github.com/akashrmalhotra/3d-portfolio.git
echo "   ✅ Repository downloaded"
echo ""

# Step 2: Navigate to project
cd 3d-portfolio

# Step 3: Copy customized files
echo "📋 Step 2: Applying customized files..."

# Check if customized files exist in parent directory
if [ -f "../src/components/Landing.tsx" ]; then
    cp ../src/components/Landing.tsx src/components/
    echo "   ✅ Landing.tsx updated"
fi

if [ -f "../src/components/About.tsx" ]; then
    cp ../src/components/About.tsx src/components/
    echo "   ✅ About.tsx updated"
fi

if [ -f "../src/components/Career.tsx" ]; then
    cp ../src/components/Career.tsx src/components/
    echo "   ✅ Career.tsx updated"
fi

if [ -f "../src/components/Work.tsx" ]; then
    cp ../src/components/Work.tsx src/components/
    echo "   ✅ Work.tsx updated"
fi

if [ -f "../src/components/Contact.tsx" ]; then
    cp ../src/components/Contact.tsx src/components/
    echo "   ✅ Contact.tsx updated"
fi

echo ""

# Step 4: Install dependencies
echo "📦 Step 3: Installing dependencies (this may take 2-3 minutes)..."
npm install

if [ $? -eq 0 ]; then
    echo "   ✅ Dependencies installed"
else
    echo "   ❌ Failed to install dependencies"
    exit 1
fi
echo ""

# Step 5: Build project
echo "🔨 Step 4: Building project..."
npm run build

if [ $? -eq 0 ]; then
    echo "   ✅ Build successful!"
else
    echo "   ❌ Build failed"
    exit 1
fi
echo ""

# Step 6: Success message
echo "============================================================"
echo "🎉 SUCCESS! Your 3D Portfolio is ready!"
echo "============================================================"
echo ""
echo "📁 Project folder: $(pwd)"
echo "📦 Build folder: $(pwd)/dist"
echo ""
echo "Next steps:"
echo ""
echo "1️⃣  Test locally:"
echo "   npm run dev"
echo "   Then open: http://localhost:5173"
echo ""
echo "2️⃣  Deploy to Netlify:"
echo "   - Go to: https://app.netlify.com/drop"
echo "   - Drag the 'dist' folder"
echo "   - Your site is live!"
echo ""
echo "3️⃣  Or deploy to Vercel:"
echo "   - Push this folder to GitHub"
echo "   - Connect to vercel.com"
echo "   - Auto-deploy enabled!"
echo ""
echo "============================================================"
