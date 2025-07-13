**Prompt for Gemini:**

You're a senior frontend developer with an eye for design and UX. Your task is to create a stunning, modern landing page for a product named **Wally** — an AI shopping assistant that allows users to shop using voice or natural language commands.

Use **Next.js** with **TypeScript** and **Tailwind CSS**, and structure the project with clean, modular, reusable components. Animate the elements using **Framer Motion** for smooth transitions. Follow the exact instructions below and use your own design sense to make the UI **extremely beautiful and aesthetic.**

---

### 🗂 Folder Structure & Component Files

There is a folder called `frontend/components/` and inside it, generate **three separate `.tsx` files**:

1. `Navbar.tsx`
2. `Hero.tsx`
3. `Products.tsx`

Each should be a **full-screen** section.

---

### ✨ General Style Guidelines

* **Font**: Use `Segoe UI` (system font if unavailable)
* **Theme**: Light mode only
* **Colors**:

  * Background: White or off-white (`#f9fafb`)
  * Primary accents: Soft **blue** and **purple** gradients (`#6366f1`, `#8b5cf6`, `#60a5fa`)
  * Shadows and soft borders to give a clean, premium feel
* **Animations**: Use `framer-motion` to animate:

  * Component fade-ins
  * Button hover effects
  * Card hover/entry animations
* **Responsiveness**: Mobile-first design; all components should scale beautifully on smaller devices
* **Layout**: Use Tailwind grid or flex utilities for alignment, centering, and spacing

---

### 🔗 `Navbar.tsx` Instructions

* Transparent/light background, sticky at top
* Contains logo: `Wally` (styled with gradient text)
* Navigation links: "Home", "Features", "Products", "Contact"
* Add a subtle hover animation to links using `framer-motion`
* Keep padding generous, and use flex for layout

---

### 🎯 `Hero.tsx` Instructions

* Fullscreen section (100vh)

* Center-aligned content

* Large bold title:

  > **"Shopping has never been easier. Use your voice or natural language to buy your favourite products."**

* Below the title, include a **short description**:

  > "Meet Wally – your personal AI shopping assistant. Just say what you need, and we’ll handle the rest."

* CTA button: `Get Started`

  * Styled with a blue/purple gradient background
  * On hover: scale slightly, pulse animation

* Add entrance animation for each element using `framer-motion`

---

### 🛍️ `Products.tsx` Instructions

* Fullscreen section with a **light grid layout** of product cards
* Create 6 **dummy product cards** using a map function over a static array
* Each card should include:

  * Product image (use placeholder from `https://source.unsplash.com`)
  * Product title (e.g., "Wireless Headphones")
  * Short description
  * Price (e.g., \$99.99)
  * "Add to Cart" button with gradient background
* Animate cards on load (fade/scale in), and scale on hover using `framer-motion`
* Responsive layout: 1-column on mobile, 2 on tablet, 3 on desktop

---

### Additional details

In Next.js 13+, follow best practices with `Server Components` and `Client Components` when needed.

Add subtle gradient backgrounds, pastel shadow cards, and rounded corners (`rounded-2xl`) for a soft, elegant design. Keep spacing generous with padding and margin (`p-8`, `gap-6` etc.).

---

> Remember: the goal is to create a **visually impressive, smooth, and minimal** landing page experience for Wally that could be shown off in a startup pitch or investor demo.