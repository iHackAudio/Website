# 🚀 3D Portfolio - No-Code Deployment Guide

## Overview

This guide will walk you through deploying your customized 3D portfolio (based on the akashrmalhotra/3d-portfolio template) using **Bolt.new** or **Netlify** - no coding required!

---

## 📁 What You Have

Your customized files are in the `/src/components/` folder:

| File | Purpose | What to Customize |
|------|---------|-------------------|
| `Landing.tsx` | Hero section with your name | YOUR NAME, title |
| `About.tsx` | About me section | Your bio, company description |
| `Career.tsx` | Work experience timeline | Your job history |
| `Work.tsx` | Projects showcase | Your projects |
| `Contact.tsx` | Contact & social links | Your email, social URLs |

---

## 🎯 Quick Customization Guide

### Step 1: Edit Your Name in Landing.tsx

Open `Landing.tsx` and find:
```tsx
<h1>
  YOUR
  <br />
  <span>NAME</span>
</h1>
```

Change to:
```tsx
<h1>
  JOHN
  <br />
  <span>DOE</span>
</h1>
```

### Step 2: Edit Your Title

Find:
```tsx
<h2 className="landing-info-h2">
  <div className="landing-h2-1">Audio</div>
  <div className="landing-h2-2">Engineer</div>
</h2>
```

Change to your title (e.g., "Producer", "Designer", etc.)

### Step 3: Update About.tsx

Replace the placeholder text with your actual bio and company description.

### Step 4: Update Career.tsx

Replace the sample jobs with your actual work experience.

### Step 5: Update Work.tsx

Replace the sample projects with your actual projects and add your project images.

### Step 6: Update Contact.tsx

Replace:
- `yourprofile` with your actual LinkedIn/username
- `hello@ihackaudio.com` with your email
- Social media links with your actual profiles

---

## 🛠️ Option 1: Deploy with Bolt.new (EASIEST - Recommended)

### What is Bolt.new?
Bolt.new is an AI-powered web development platform that lets you deploy websites instantly by simply pasting code.

### Step-by-Step Instructions:

#### Step 1: Get the Original Repository
1. Go to https://github.com/akashrmalhotra/3d-portfolio
2. Click the green **"<> Code"** button
3. Click **"Download ZIP"**
4. Extract the ZIP file on your computer

#### Step 2: Replace the Customized Files
1. Open the extracted folder
2. Navigate to `src/components/`
3. Replace these files with your customized versions:
   - `Landing.tsx`
   - `About.tsx`
   - `Career.tsx`
   - `Work.tsx`
   - `Contact.tsx`

#### Step 3: Go to Bolt.new
1. Open https://bolt.new in your browser
2. Sign up for a free account (if you don't have one)

#### Step 4: Upload Your Project
1. Click **"Import from GitHub"** OR **"Upload Folder"**
2. If uploading folder: Drag and drop your entire project folder
3. Wait for Bolt.new to process the files

#### Step 5: Install Dependencies
Bolt.new will automatically detect the package.json and install dependencies. If prompted, click:
```
npm install
```

#### Step 6: Build & Deploy
1. Bolt.new will automatically build the project
2. Click the **"Deploy"** button
3. Your site will be live in seconds!
4. Copy your URL (e.g., `https://your-site.bolt.new`)

#### Step 7: Custom Domain (Optional)
1. In Bolt.new dashboard, go to **Settings**
2. Click **"Custom Domain"**
3. Enter your domain name
4. Follow DNS instructions

---

## 🌐 Option 2: Deploy with Netlify

### Step-by-Step Instructions:

#### Step 1: Prepare Your Project
1. Download the original repository from https://github.com/akashrmalhotra/3d-portfolio
2. Extract the ZIP file
3. Replace the component files in `src/components/` with your customized versions

#### Step 2: Build the Project Locally (One-Time Setup)

**Option A: Use Netlify CLI (No Local Build Needed)**
Skip to Step 3.

**Option B: Build Locally**
1. Install Node.js from https://nodejs.org (LTS version)
2. Open Terminal/Command Prompt
3. Navigate to your project folder:
   ```bash
   cd path/to/your/3d-portfolio
   ```
4. Install dependencies:
   ```bash
   npm install
   ```
5. Build the project:
   ```bash
   npm run build
   ```
6. You'll see a `dist/` folder created

#### Step 3: Deploy to Netlify

**Method 1: Drag & Drop (Easiest)**
1. Go to https://www.netlify.com
2. Sign up/login with GitHub, GitLab, or email
3. On the dashboard, find the **"Drag and drop your site folder here"** area
4. Drag your `dist/` folder (if built locally) OR entire project folder
5. Your site is live instantly!

**Method 2: Connect Git Repository**
1. Push your customized code to GitHub
2. Go to Netlify dashboard
3. Click **"Add new site"** → **"Import an existing project"**
4. Connect to GitHub
5. Select your repository
6. Build settings:
   - Build command: `npm run build`
   - Publish directory: `dist`
7. Click **"Deploy site"**

**Method 3: Netlify CLI**
1. Install Netlify CLI:
   ```bash
   npm install -g netlify-cli
   ```
2. Login:
   ```bash
   netlify login
   ```
3. Deploy:
   ```bash
   netlify deploy --prod --dir=dist
   ```

#### Step 4: Custom Domain (Optional)
1. In Netlify dashboard, go to **Domain settings**
2. Click **"Add custom domain"**
3. Enter your domain
4. Update DNS records as instructed

---

## 📸 Adding Your Images

### Project Images
1. Add your project screenshots to the `public/images/` folder
2. Update the image paths in `Work.tsx`:
   ```tsx
   image: "/images/your-project-screenshot.png",
   ```

### Recommended Image Sizes:
- Project images: 1200x800px (16:9 ratio)
- Format: PNG or JPG
- Max file size: 500KB per image

---

## 🔧 Troubleshooting

### Issue: Build Fails
**Solution:**
1. Make sure you have the correct Node.js version (18+)
2. Delete `node_modules` folder and `package-lock.json`
3. Run `npm install` again
4. Run `npm run build`

### Issue: 3D Character Not Showing
**Solution:**
- The 3D model files are in `public/models/`
- Don't delete or rename these files
- If missing, re-download from the original repository

### Issue: GSAP Animations Not Working
**Solution:**
- GSAP is included in the dependencies
- Make sure `npm install` completed successfully
- Check browser console for errors

### Issue: Images Not Loading
**Solution:**
- Place images in `public/images/` folder
- Use correct paths: `/images/filename.png`
- Check file extensions match exactly

---

## 🎨 Customization Tips

### Change Colors
Edit `src/index.css` or component CSS files in `src/components/styles/`

### Change Fonts
Edit `src/index.css` and update the font-family

### Add/Remove Sections
1. Edit `src/App.tsx`
2. Import your component
3. Add/remove components from the JSX

### Update 3D Character
The 3D character is controlled by:
- `src/components/Character/` folder
- `src/data/boneData.ts` - bone names for animation

**Note:** Modifying 3D character requires 3D/Three.js knowledge. Keep as-is for best results.

---

## 📱 Testing Your Site

Before deploying, test locally:
```bash
npm install
npm run dev
```
Open http://localhost:5173 in your browser

---

## 🌟 Live Site Checklist

- [ ] Name updated in Landing.tsx
- [ ] About section customized
- [ ] Career/experience updated
- [ ] Projects added with images
- [ ] Contact info updated
- [ ] Social links working
- [ ] Images optimized
- [ ] Site deployed
- [ ] Custom domain connected (optional)

---

## 📞 Need Help?

### Original Repository
https://github.com/akashrmalhotra/3d-portfolio

### Live Demo
https://akashrmalhotra.netlify.app/

### Tech Stack Used
- React 18 + TypeScript
- Vite (build tool)
- Three.js + React Three Fiber (3D)
- GSAP (animations)
- Tailwind CSS (styling)

---

## ✅ You're Done!

Your 3D portfolio with the animated character and smooth GSAP scrolling is now live! The 3D elements and animations will work exactly as in the original template - only your content has been customized.

**Remember:** The 3D character, cursor effects, scroll animations, and all interactive elements are preserved from the original template. You've only changed the text content to match your brand (ihack Audio).

🎉 **Congratulations on your new 3D portfolio!**
