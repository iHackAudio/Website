# 🎵 ihack Audio - 3D Portfolio

A stunning 3D portfolio website built with React, TypeScript, Three.js, React Three Fiber, and GSAP animations.

![3D Portfolio Preview](https://akashrmalhotra.netlify.app/preview.jpg)

## ✨ Features

- 🎭 **Interactive 3D Character** - Animated avatar that responds to user interactions
- 🎨 **GSAP Animations** - Smooth scroll-triggered animations and transitions
- 🖱️ **Custom Cursor** - Unique cursor effects throughout the site
- 📱 **Responsive Design** - Works on desktop, tablet, and mobile
- ⚡ **Fast Performance** - Built with Vite for lightning-fast loading
- 🎯 **One-Page Layout** - Smooth scrolling between sections

## 🛠️ Tech Stack

- **React 18** - UI library
- **TypeScript** - Type safety
- **Vite** - Build tool
- **Three.js** - 3D graphics
- **React Three Fiber** - React renderer for Three.js
- **GSAP** - Animation library
- **Tailwind CSS** - Styling

## 📁 Customized Files

This portfolio has been customized for **ihack Audio**:

| File | Description |
|------|-------------|
| `Landing.tsx` | Hero section with name and title |
| `About.tsx` | Company and personal bio |
| `Career.tsx` | Work experience timeline |
| `Work.tsx` | Featured projects showcase |
| `Contact.tsx` | Contact info and social links |

## 🚀 Quick Start

### Prerequisites
- Node.js 18+ installed
- npm or yarn

### Installation

1. **Clone or download the original repository:**
   ```bash
   git clone https://github.com/akashrmalhotra/3d-portfolio.git
   cd 3d-portfolio
   ```

2. **Replace customized files:**
   Copy the files from `src/components/` in this folder to the same location in the project.

3. **Install dependencies:**
   ```bash
   npm install
   ```

4. **Run development server:**
   ```bash
   npm run dev
   ```

5. **Open in browser:**
   Navigate to `http://localhost:5173`

## 📦 Build for Production

```bash
npm run build
```

The built files will be in the `dist/` folder.

## 🌐 Deployment

### Option 1: Netlify (Recommended)
1. Build the project: `npm run build`
2. Drag the `dist/` folder to Netlify
3. Your site is live!

### Option 2: Bolt.new
1. Go to https://bolt.new
2. Upload your project folder
3. Click Deploy

### Option 3: Vercel
1. Connect your GitHub repository
2. Vercel will auto-deploy on every push

## 🎨 Customization Guide

### Update Your Name
Edit `src/components/Landing.tsx`:
```tsx
<h1>
  YOUR
  <br />
  <span>NAME</span>
</h1>
```

### Update Projects
Edit `src/components/Work.tsx` and modify the `projects` array:
```tsx
const projects = [
  {
    title: "Your Project",
    category: "Project Category",
    tools: "Technologies used",
    image: "/images/your-image.png",
    link: "https://your-project.com",
  },
];
```

### Update Contact Info
Edit `src/components/Contact.tsx` with your:
- Email address
- Social media links
- Location

### Add Project Images
1. Place images in `public/images/`
2. Reference them in Work.tsx as `/images/filename.png`
3. Recommended size: 1200x800px

## 🎯 Project Structure

```
3d-portfolio/
├── public/
│   ├── images/          # Project screenshots
│   └── models/          # 3D character files
├── src/
│   ├── components/      # React components
│   │   ├── Character/   # 3D character components
│   │   ├── styles/      # CSS files
│   │   └── utils/       # Utility functions
│   ├── data/            # Data files (boneData.ts)
│   ├── types/           # TypeScript types
│   ├── App.tsx          # Main app component
│   └── main.tsx         # Entry point
├── index.html
├── package.json
├── tsconfig.json
└── vite.config.ts
```

## 🔧 Key Components

### 3D Character (`src/components/Character/`)
- `Character.tsx` - Main character component
- `CharacterScene.tsx` - 3D scene setup
- `TypingAnimation.tsx` - Typing animation logic

### Sections
- `Landing.tsx` - Hero section
- `About.tsx` - About me
- `Career.tsx` - Experience timeline
- `Work.tsx` - Projects slider
- `WhatIDo.tsx` - Services/skills
- `Contact.tsx` - Contact form & socials
- `TechStack.tsx` - Technology stack

### Utilities
- `Cursor.tsx` - Custom cursor
- `Navbar.tsx` - Navigation
- `SocialIcons.tsx` - Social media icons
- `HoverLinks.tsx` - Hover effects

## 🐛 Troubleshooting

### 3D Character not showing?
- Check that model files exist in `public/models/`
- Ensure WebGL is enabled in your browser

### Build errors?
- Delete `node_modules` and `package-lock.json`
- Run `npm install` again

### Images not loading?
- Verify images are in `public/images/`
- Check file paths match exactly (case-sensitive)

## 📄 License

This project is based on the [3d-portfolio](https://github.com/akashrmalhotra/3d-portfolio) template by Akash Malhotra, licensed under MIT.

## 🙏 Credits

- Original template: [akashrmalhotra](https://github.com/akashrmalhotra)
- 3D character: Mixamo
- Icons: React Icons
- Fonts: Google Fonts

---

**Made with ❤️ for ihack Audio**
