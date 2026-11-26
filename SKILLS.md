# Skills

Twelve skills. Each big skill runs a full workflow and loads its mini skills (modules) only when it needs them.

| Command | Skill | What it does |
|---|---|---|
| `/design` | Super Design | The main design skill. |
| `/landing-page` | Landing Page | Web design for pages that sell: one offer, one audience, one primary action. |
| `/prototype` | Prototype | Turns one site into many. |
| `/scroll-site` | Scroll Site | Cinematic, scroll-driven websites where scrolling moves the story: smooth scroll, pinned scenes, scrubbed image sequences and word-by-word reveals. |
| `/animate` | Animate | All motion that isn't scroll storytelling. |
| `/image` | Image | Gets the images a page needs. |
| `/brand` | Brand | Brand identity and the system under every page. |
| `/review` | Review | A graded report on any page or site, with no changes made. |
| `/demo` | Demo | Shows the product, and shows the work. |
| `/marketing` | Marketing | Plans, writes and measures marketing for your business or your clients: campaign briefs, competitor positioning, blog, social, email and launch copy, SEO audits, brand-voice checks and performance reports. |
| `/interview` | Interview | Interviews you in depth about a feature or project, asking questions that aren't obvious, until the picture is complete. |
| `/agentation` | Agentation | Adds the Agentation visual feedback toolbar to a Next.js app, so you can click on the page and leave notes your coding agent can read. |

## /design: Super Design

The main design skill. It works out what a page or screen is for, sets one clear art direction, builds or redesigns it, then hands it to a judge AI. The judge never sees the builder's reasoning: it scores the page from screenshots against a 10-point rubric and writes a full critique. The builder fixes the worst issues and the loop repeats until the page scores 8/10 with no dimension below 7.

**Use it when**

- An app screen, dashboard or component looks generic or unfinished
- A page "looks AI-generated" and you want it fixed, not just flagged
- An honest critique of a design before you show it to anyone
- UX copy, a developer handoff spec, or a user research plan
- Award-winning references before you choose a direction

**Try**

- `/design Redesign the settings page so it stops looking AI-generated`
- `/design Critique this dashboard and fix it until it scores 8/10`
- `/design Write the empty states and error messages for the signup flow`

<details><summary>40 mini skills inside</summary>

**Art direction and taste**

- `tastemaker`: Generate genuinely beautiful, on-brand UI instead of generic "AI slop" — use whenever the user asks to build, design, style, or improve a UI, landing page, dashboard…
- `design-taste-frontend`: tasteskill v2, the anti-slop frontend skill.
- `design-taste-frontend-v1`: The original v1 taste-skill, preserved for projects depending on its exact behavior.
- `design-taste-frontend-v2-experimental`: Old v2 (experimental) of taste-skill, the single-file dial-driven version, preserved for projects depending on its exact behavior.
- `high-end-visual-design`: Teaches the AI to design like a high-end agency.
- `gpt-taste`: Elite UX/UI & Advanced GSAP Motion Engineer.
- `emil-design-eng`: This skill encodes Emil Kowalski's philosophy on UI polish, component design, animation decisions, and the invisible details that make software feel great.

**Build and redesign**

- `redesign-existing-projects`: Upgrades existing websites and apps to premium quality.
- `unslop`: Turns vibecoded, AI-looking UI into a designed interface with its own character.
- `design-first-ui-prompting`: Use when you need design-first, spec-driven, skimmable prompts for UI generation.
- `mobile-native`: Make a web app feel native on a phone — the small CSS and meta-tag fixes that separate "a website in a browser" from something that feels installed.
- `full-output-enforcement`: Overrides default LLM truncation behavior.

**Details and CSS**

- `beautiful-shadows`: Apply exact Tailwind arbitrary shadow utilities for polished, layered neutral elevation.
- `container-lines`: Add vertical container-size guide lines with mini corner squares for precise, structured web layouts.
- `corner-diagonals`: Apply diagonal-cut corners and chamfered edges to buttons, cards, panels, and container shells.
- `corner-lasers`: Create a corner-anchored laser composition with thin beams, a bright emitter node, bloom, and atmospheric glow or fog.
- `css-alpha-masking`: Apply CSS alpha masking with linear-gradient for horizontal or vertical edge fades (mask-image and -webkit-mask-image).
- `css-border-gradient`: Apply subtle gradient-border treatments for premium web surfaces.
- `number-details`: Add decorative 01, 02, 03 numeric detail markers.
- `progressive-blur`: Create a layered CSS progressive blur (top or bottom) using multiple backdrop-filter masks for depth and softness.
- `tailwindcss`: Use when designing/implementing UI with Tailwind CSS (layout, typography, responsive, theming, component patterns).
- `ask-sonner`: Guide to Sonner, the React toast library — install and wire up the Toaster, pick the right toast() call, promise and loading toasts, updating, dismissing and persisting…
- `better-ui`: Polishes surfaces, icons and motion with exact values for border radius, optical alignment, shadows, icon states and animation.

**Illustration**

- `illustration-framed-panel`: Draws original design-and-coding scenes as SVG cards (480x360) in a framed-panel cartoon style.
- `illustration-grainy-gouache`: Draws original cosy animal scenes as hand-authored SVG cards (480x360) in a grainy gouache, risograph-like style.
- `illustration-halftone-line`: Draws hand-authored SVG spot illustrations in a halftone line style for design and coding scenes.
- `illustration-ink-sketch`: Draws hand-inked cartoon critters and living objects as SVG cards (480x360), each acting out a coding or design idea.
- `illustration-line-interior`: Draws original hand-written SVG spot scenes in the Line interior style, wide airy rooms or terraces where slim, realistic people do design and coding work.
- `illustration-one-line`: Draws original hand-written SVG spot illustrations in the One-line style, joyful action figures doing design and coding work.

**References and inspiration**

- `awwwards-inspiration`: Use when building a site that needs design references (e.g.
- `awwwards-setup`: Use when the awwwards MCP server or its skills are invoked for the first time in a session or on a new machine — when no awwwards preferences exist yet, or the user asks…
- `awwwards-doctor`: Use when awwwards-mcp scraping or tools stop working — BlockedError, "layout may have changed" parser errors, empty results, failed captures, stale searches — or when…
- `web-technique-to-skill`: Turn a visual or interaction technique you already built into a reusable web-design skill, by isolating the one mechanism that makes it work while reproducing its…
- `article-prompts-to-skills`: Convert an article, tutorial, or prompt pack into focused reusable AgentSkills, one independent capability per skill, with portable instructions, example prompts…

**Loops and verification**

- `iterate-until-verified`: Apply a prompt-agnostic execution and verification loop to any substantial task while preserving the original request.

**Critique and research**

- `design-critique`: Get structured design feedback on usability, hierarchy, and consistency.
- `user-research`: Plan, conduct, and synthesize user research.
- `research-synthesis`: Synthesize user research into themes, insights, and recommendations.
- `ux-copy`: Write or review UX copy — microcopy, error messages, empty states, CTAs.
- `design-handoff`: Generate developer handoff specs from a design.

</details>

## /landing-page: Landing Page

Web design for pages that sell: one offer, one audience, one primary action. It runs intake questions, picks the structure and layout, writes the conversion copy and SEO, applies a strict visual system, then finishes with the Super Design judge loop.

**Use it when**

- A new landing page for a product, client or launch
- Rewriting a homepage that tries to do too much
- A pricing page
- A premium, award-style marketing site
- Rebuilding a page inspired by a reference site without copying it

**Try**

- `/landing-page Build a landing page for my app that gets people to join the waitlist`
- `/landing-page Rewrite this homepage hero so the offer is obvious`
- `/landing-page Make a pricing page with three plans`

<details><summary>8 mini skills inside</summary>

**Landing page system**

- `landing-page-design`: Complete system for high-converting landing pages: intake, page structure, layout, conversion copy, SEO, and strict visual rules for type, spacing, radius, backgrounds, hero, icons and motion.
- `landing-page`: Use when designing or rewriting a high-converting landing page (single-offer page) for SaaS/apps/services.
- `pricing-page`: Use when designing or rewriting a high-converting SaaS pricing page (structure, plan design, copywriting, SEO/AEO, FAQs, layout patterns, experiments).

**Web design craft**

- `web-design-engineer`: Build or redesign polished browser-rendered visual artifacts with HTML/CSS/JavaScript/React: pages, dashboards, prototypes, slide decks, animations, UI mockups, and data…
- `build-awwwards-quality-sites`: Art-direct and implement distinctive, motion-rich marketing, editorial, portfolio, and landing websites with original reference-inspired imagery, standout heroes, GSAP…

**Rebuild from a reference site**

- `recreate`: Recreate a website from a link — evidence-driven reconstruction with the awwwards MCP.
- `awwwards-section-loop`: Use when recreating or rebuilding a multi-section page from a reference site — build section by section instead of all at once.
- `stitched-full-page-capture`: Capture or repair reliable full-page screenshots for lazy-loaded, scroll-animated, Framer, WebGL/canvas, or reveal-heavy web pages.

</details>

## /prototype: Prototype

Turns one site into many. It pulls your real content, builds several complete versions in different themes, and puts them on one gallery page. Open any version full size or full screen, flip through with the arrow keys, then take the winner into Super Design. Themes come from 36 visual styles in 8 families, plus brand-inspired style recipes.

**Use it when**

- Showing a client several directions before committing
- Choosing between dark, light, editorial or brutalist looks
- Turning a day's inspiration references into five original builds
- Seeing how the same copy feels in different styles

**Try**

- `/prototype Prototype my site in six different themes`
- `/prototype Show me an editorial, a brutalist and a dark glass version of this page`

<details><summary>39 mini skills inside</summary>

**Prototype engines**

- `prototype`: Build multiple genuinely different versions of a UI piece you describe, rendered behind a visual picker so you can flip through them live and promote the one that feels…
- `build-daily-inspiration-sites`: Turn a completed daily UI inspiration capture into exactly five original landing-page builds, one per separate Codex task, using Sites.
- `daily-ui-inspiration-capture`: Create a recurring daily UI inspiration capture.

**Dark glass and tech**

- `blue-laser-clean-glass-layout`: Create a clean dark glass layout system with a thin blue laser atmosphere, frosted premium shells, and polished dashboard structure.
- `dark-glass-clean-layout`: Create a dark glass layout system with frosted premium shells, clean multi-column workspace structure, floating data cards, and restrained atmospheric depth.
- `glass-dark-ui`: Build dark-mode glassmorphism interfaces with readable contrast, frosted surfaces, and gradient borders using a pseudo-element mask.
- `glass-dark-mode-clock`: Create a dark glass design system with frosted shells, soft beam grids, circular clock-like calibration dials, and precise sci-fi instrument framing.
- `framed-tech-dark-border-gradient`: Create a framed dark technical design system with border-gradient shells, asymmetrical grid panels, mono utility labeling, and restrained monochrome atmosphere.
- `tech-green-dark-mode-modern`: Create a modern dark-mode technical design system with matte-black surfaces, emerald signal accents, mono system labeling, framed dashboard cards, and restrained glow.
- `bright-green-tech-system-webgl`: Create a bright-green technical design system with structured split layouts, hard-framed dark surfaces, mono utility labels, and a prominent WebGL visualization zone.
- `funky-purple-container-tech`: Create a dark container-led technical design system with fuchsia-purple accents, layered rounded shells, crisp frame lines, and playful futuristic focal objects.

**Atmospheric dark**

- `atmosphere-background`: Create a dark atmospheric background with drifting vertical light folds, screen-blended glow, and a concentrated luminous corner or lower-edge bloom.
- `dither-background`: Create a dark monochrome procedural background with enlarged square pixels and visible Bayer-style ordered dithering.
- `dither-laser-dark-mode`: Create a dark premium design system that combines near-black surfaces, subtle ordered-dither texture, and a thin accent-colored laser atmosphere.
- `mesh-gradient-dark-blue-clean`: Create a futuristic, premium, clean dark-blue mesh-gradient design system across background rendering, hero shell, navigation, floating nodes, framed sections, CTAs, and…
- `dark-blue-contrasting-clean`: Create a dark-blue clean design system with strong contrast, cobalt gradient feature blocks, crisp framed structure, and restrained premium glow.

**Clean light and paper**

- `clean-minimal-beige-light-mode`: Create a clean minimal beige light-mode design system with warm neutral shells, quiet process grids, restrained accent color, and elegant low-contrast structure.
- `light-mode-paper-technical`: Create a light-mode technical design system with warm paper surfaces, dark outer framing, subtle diagonal texture, precise bracketed geometry, and restrained accent…
- `orange-clean-paper-saas`: Create a clean paper-toned SaaS design system with warm neutrals, orange accent signals, rounded premium forms, and polished product illustration surfaces.
- `blue-cloudy-clean-modern`: Create a clean modern design system with a luminous blue sky atmosphere, soft drifting cloud light, minimal white framing, and serene premium typography.
- `minimalist-ui`: Clean editorial-style interfaces. Warm monochrome palette, typographic contrast, flat bento grids, muted pastels.

**Editorial**

- `editorial-tech`: Blend editorial magazine composition with precision product-tech detailing using asymmetrical grids, cinematic media bands, mono utility labels, and restrained accent…
- `editorial-portfolio-chapters`: Create or redesign creative-studio, agency, photographer, artist, and portfolio websites where project work leads the story.
- `book-serif-index`: Create an archival book-reader design system with serif-led pages, mono index navigation, aged paper surfaces, margin notes, and a premium catalog frame.
- `editorial-service-booking`: Create or redesign appointment-based service websites for salons, barbers, spas, wellness studios, clinics, and hospitality brands.
- `image-first-grid-layout`: Create an image-led grid design system with full-bleed photography, structural guide lines, anchored content blocks, and restrained technical overlays.

**Agency grids and frames**

- `agency-grid-layout-minimal`: Create a minimal agency design system with a disciplined editorial grid, oversized typography, quiet uppercase utility labels, restrained image blocks, and subtle…
- `framed-grid-layout`: Create minimal framed grid layouts with thin visible boundary lines, L-shaped corner brackets, subtle diagonal line texture, and strict section alignment.
- `nested-container-clean-agency`: Create a clean agency design system built from nested containers, with an outer editorial shell, inset dark feature blocks, rounded premium cards, and restrained accent…
- `nested-container-frames`: Create a container-in-container layout system using nested frames.
- `split-layout-technical`: Create a technical split-screen design system with dual panels, fine frame lines, mono metadata, quiet editorial typography, and premium inset surfaces.
- `technical-wireframe-info-layout`: Create a monochrome technical wireframe design system with exploded 3D structure, connector annotations, sparse information labels, and precise dark diagnostic framing.

**Brutalist**

- `documentary-brutalist-agency`: Create or redesign creative agency, production studio, architecture, culture, and portfolio websites with billboard typography, hard black-and-white chapters, exposed…
- `industrial-brutalist-ui`: Raw mechanical interfaces fusing Swiss typographic print with military terminal aesthetics.

**Skeuomorphic and tactile**

- `skeuomorphic-ui`: Create skeuomorphic web UI surfaces with layered gradients, stacked inner and outer shadows, reflective gradient borders, micro texture, and embossed text or icon details.
- `high-contrast-skeuomorphic-clean`: Create a high-contrast clean skeuomorphic design system with molded dark surfaces, crisp light separation, tactile inset depth, and restrained signal accents.

**SaaS and product**

- `product-proof-saas`: Create or redesign SaaS and AI product landing pages where a real workflow, interface, or deterministic demo is the central proof.
- `operational-enterprise-ai`: Create or redesign enterprise AI, automation, security, and operations product pages that explain system boundaries, approvals, auditability, exceptions, and rollback.
- `solar-duotone-bold`: Use Iconify Solar Duotone Bold icon style.

</details>

## /scroll-site: Scroll Site

Cinematic, scroll-driven websites where scrolling moves the story: smooth scroll, pinned scenes, scrubbed image sequences and word-by-word reveals. It plans the story in chapters, then builds one chapter at a time with one scroll engine.

**Use it when**

- An Awwwards-style launch or portfolio site
- Scrubbing a video or image sequence as you scroll
- Pinned sections, horizontal chapters, progress timelines
- Copying how a reference site's scroll motion works
- Debugging GSAP or ScrollTrigger

**Try**

- `/scroll-site Turn this product story into a cinematic scroll site`
- `/scroll-site Pin the features section and scrub the phone mockup on scroll`

<details><summary>14 mini skills inside</summary>

**Scroll engines and storytelling**

- `cinematic-gsap-lenis-motion-system`: Create premium cinematic web motion systems with GSAP, ScrollTrigger, and Lenis.
- `cinematic-scroll-storytelling`: Create cinematic scroll-driven landing pages with Lenis smooth scrolling, GSAP ScrollTrigger, scroll-linked progression, staggered text reveals, sticky card stacks…
- `gsap-scrolltrigger-storytelling`: Build cinematic sticky product storytelling with GSAP ScrollTrigger, progressive UI reveals, scroll-synced animation, smooth interpolation, and immersive section…
- `scroll-world-storytelling`: Turn an article, case study, brand narrative, product journey, or long-form story into a cinematic scroll-driven landing page using one of three renderers: scrubbed…
- `gsap`: Use when you need to add or debug professional web animations with GSAP (timelines, ScrollTrigger, stagger, transforms) in HTML/CSS/JS/React.
- `motion-authoring`: Use when a converted project (build_project --authored) needs its motion authored — turning motion.manifest.json + inert skeletons into real per-section/page motion with…

**Scroll effects**

- `animation-on-scroll`: Create an on-scroll animation trigger using IntersectionObserver with Tailwind-friendly animation classes and keyframes.
- `horizontal-scroll-scenes`: Build scene-by-scene chapters that advance left to right on one fixed stage while the user scrolls vertically, with native scroll as the only input.
- `scroll-progress-timeline`: Turn any ordered process into a data-driven vertical or horizontal scroll story with a base line, progress fill, active step states, responsive collapse, semantic…
- `scroll-scrubbed-visual-sequence`: Build reversible scroll-controlled visual transformations with a pinned or sticky stage, normalized progress, and video, image-sequence, canvas, SVG, or DOM renderers.
- `scroll-scrubbed-word-reveal`: Reveal marked-up text word by word as scroll progress advances, while preserving semantic inline links, emphasis, responsive line wrapping, and reduced-motion readability.
- `masked-reveal`: Create masked staggered word reveals on scroll with GSAP ScrollTrigger.
- `webgl-landing-steering`: Use when creating or refining WebGL-heavy landing pages and you need to steer toward a specific visual outcome (premium, technical, playful, cinematic) while balancing…

**Study and copy reference motion**

- `awwwards-motion-study`: Use when building a site whose reference has animation — before writing any motion code, and again when verifying a build.

</details>

## /animate: Animate

All motion that isn't scroll storytelling. It decides whether something should move at all, then picks the purpose, tool, properties, easing and duration, and makes sure it's interruptible and smooth. Covers micro-interactions, cursor effects, particles, shaders, globes and React Native motion, and audits motion that already exists.

**Use it when**

- Button, hover and page-transition polish
- A cursor trail, particles or a shader background
- A globe or 3D accent on a landing page
- Motion that feels janky or drops frames
- Recreating an interaction you saw in a video
- Naming an effect you can only describe

**Try**

- `/animate Make these buttons and cards feel alive`
- `/animate Add a subtle particle background to the hero`
- `/animate Why does this animation stutter on my phone?`

<details><summary>37 mini skills inside</summary>

**Principles and building**

- `animate`: Build an animation from scratch, making the decisions in the order that determines whether it feels right — should it animate at all, what purpose, which tool, which…
- `animation-vocabulary`: Reverse-lookup glossary that turns a vague description of a web animation or motion effect into its exact term ("the bouncy thing when a popover opens" → Pop in;
- `apple-design`: Apple's approach to interface design and fluid, physical motion, translated for the web.
- `animation-systems`: Use when designing or implementing product-grade web motion like Stripe, Linear, Apple, and Vercel.
- `animate-expo`: Build animations in React Native and Expo, making the decisions in the order that determines whether they feel right — should it animate, which thread it runs on, which…

**Micro-interactions and transitions**

- `reveal-hover-effect`: Build cursor-following spotlight reveals that expose a second aligned image through a soft radial mask.
- `staggered-word-reveal`: Create subtle editorial word-by-word text reveal animations where each word fades and rises into place once it enters the viewport.
- `marquee-loop`: Apply seamless infinite marquee loops using duplicated items.
- `fire-paper-loader`: Build a burning-paper ring loader whose GLSL flame is drawn by a Worker on an OffscreenCanvas started from the head, so a main thread blocked by the page build cannot…
- `paper-cinder-transition`: Change between pages, chapters or scenes with a paper-burn transition, a ragged ember line that sweeps across the frame, chars the old page ahead of it and reveals the…
- `beam-glow-states`: Create React loading, processing, selected, current, focus, and pressed states with the border-beam package's animated edge glow.
- `liquid-metal-border`: Add and tune animated liquid-metal WebGL borders with the React `metal-fx` package.
- `thinking-orbs`: Add accessible animated AI loading and agent-status indicators with the React thinking-orbs library.
- `gooey-blob-system`: Create a gooey blob system using SVG filters where multiple shapes merge into a single fluid form.

**Cursor and particles**

- `add-shader-cursor-trail`: Add the Shaders WebGPU mouse effect used for the Tidal Commons hero: a white twinkling halftone cursor trail driven by ChromaFlow, masked through a DotGrid, finished…
- `shaders-cursor-ripples`: Add cursor-following fluid WebGPU distortion over an existing image with the Shaders library's ImageTexture and CursorRipples components.
- `pointer-trail-emitter`: Build a cursor trail whose spacing stays constant at any hand speed, by emitting motes per unit of distance travelled rather than on a timer, so a flick draws the same…
- `build-interactive-particle-trail`: Build a cursor or touch particle interaction that emits by distance along the traveled segment into a recycled GPU point pool, with optional keyboard-triggered bursts.
- `ambient-section-particles`: Add a restrained particle atmosphere inside one section with configurable shapes, density, gravity, wind, sway, rotation, recycling or settling, pointer disturbance…
- `falling-leaves`: Build falling leaves that read as leaves, with each one tumbling on its own axis so it presents a face, thins to an edge, and opens out again, and with its sideways slip…
- `matterjs`: Use when implementing 2D physics interactions with Matter.js, including Engine/World setup, Render/Runner configuration, adding bodies and constraints, and…

**Shaders, WebGL and 3D accents**

- `background-grid-webgl`: Create a perspective WebGL background grid with fading lines, subtle particle haze, slow forward drift, and gentle camera parallax.
- `webgl-laser`: Create a fixed full-screen WebGL laser background effect with a thin white-hot vertical core, restrained brand-colored halo, and soft smoky fog around the beam.
- `globe-gl`: Use when implementing globe.gl (Globe.GL) for 3D globe data visualization with WebGL/ThreeJS, including setup, data layers (points, arcs, polygons, labels), and…
- `globe-particles`: Create a globe-like 3D particle visualization with a dense luminous spherical core and thinner orbital ring or flattened disc.
- `cobejs`: Use when adding a lightweight interactive globe with cobe (canvas setup, markers, interaction, performance, integration with React/Next.js).
- `unicorn-studio`: Use when embedding and customizing Unicorn Studio interactive animations on the web (embed, responsive sizing, performance, layering with UI, fallbacks).
- `vantajs`: Use when adding animated WebGL background effects with Vanta.js (setup, parameters, resizing, performance, integration in React/Next.js).
- `hairline-create`: Use when someone asks for a new Hairline figure, or runs /hairline-create with an idea.
- `hairline-adopt`: Use when someone has an SVG (an icon, a logo, an illustration) and wants it as a Hairline figure, or runs /hairline-adopt with a file.

**Motion review and performance**

- `review-animations`: Reviews animation and motion code against a high craft bar derived from Emil Kowalski's design engineering philosophy.
- `improve-animations`: Survey a codebase's animation and motion code as a senior motion advisor, then produce a prioritized audit and self-contained implementation plans for other agents (or…
- `find-animation-opportunities`: Search a codebase or UI for places that don't animate but should, and reject everything that shouldn't.
- `animation-performance`: Keep web animations inside the frame budget — animate composite-only properties, keep motion off the main thread when the page is busy, and find the cause when an…
- `optimize-web-animations`: Profile, audit, and optimize frontend page performance with emphasis on animation work, memory-leak risks, long-session slowdowns, CSS animations, canvas/WebGL…

**Copy an interaction**

- `video-to-superprompt`: Turn a reference video into a super detailed recreation or inspiration prompt.
- `html-to-interaction-prompts`: Convert a supplied HTML page or generated HTML reference into a screenshot-backed article containing multiple reusable interaction prompts.

</details>

## /image: Image

Gets the images a page needs. It generates art-directed hero images, section comps, app screen concepts and transparent assets when an image tool is available, and sources real photos and real company logos when that's the honest choice.

**Use it when**

- A hero or section visual that matches the art direction
- Real stock photos for people and places
- Company or tool logos for a "used by" row
- Transparent PNG ornaments, icons or sprites

**Try**

- `/image Generate a hero image for this page`
- `/image Find real photos for the team section and add proper alt text`

<details><summary>7 mini skills inside</summary>

**Generate**

- `imagegen-frontend-web`: Elite frontend image-direction skill for generating premium, conversion-aware website design references.
- `imagegen-frontend-mobile`: Elite mobile app image-generation skill for creating premium, app-native screen concepts and flows.
- `codex-gpt-image-2-5-flare`: Generate or edit artwork with built-in Codex image gen, especially transparent PNG ornaments, game sprites, emblems, and UI graphics.
- `image-to-code`: Elite website image-to-code skill for Codex.

**Source**

- `aura-asset-images`: Use when you need high-quality stock-style images from Aura Assets (aura.build/assets) similar to Unsplash for design mockups and marketing: backgrounds, abstract…
- `unsplash-asset-images`: Use when you need to pick high-quality Unsplash images for product/design assets (avatars, headshots, portraits, large website backgrounds, and abstract wallpapers) and…
- `company-logos`: Use Iconify Simple Icons logos (64x64) instead of text logos.

</details>

## /brand: Brand

Brand identity and the system under every page. It makes brand kits and logo systems, and builds, audits, documents or migrates a design system: tokens, components, states and docs.

**Use it when**

- A new brand or a refresh
- Logo concepts and guideline boards
- Hardcoded colors everywhere and inconsistent UI
- Extracting tokens from an existing app
- Documenting a component, or picking a component library

**Try**

- `/brand Make a brand kit for my coffee shop`
- `/brand Our UI is a mess: build us a design system from what's there`

<details><summary>10 mini skills inside</summary>

**Brand identity**

- `brandkit`: Premium brand-kit image generation skill for creating high-end brand-guidelines boards, logo systems, identity decks, and visual-world presentations.
- `generate-reference-inspired-brand-worlds`: Generate multiple original brand campaign worlds from a supplied visual reference while controlling how close the new work feels without copying protected signature…

**Design systems**

- `design-system-boss`: Use for vague whole-app design system asks on an app that already ships UI, like "our UI is a mess, fix it", "we need a design system", "we hardcode colors everywhere"…
- `build-design-system`: Use when an ask names one phase of design system work, such as "extract tokens from the app" or "add states and specs to our Button", or for an empty repo, such as…
- `migrate-design-system`: Use when an app has to move onto a design system that already exists, such as "migrate the app to our design system", "move every screen onto the new components", a…
- `token-mapping`: Reports how hardcoded style values on a page, file or diff map onto a project's existing design tokens, purpose first, then value.
- `component-docs`: Writes one component's documentation entry from its code, stories and real call sites, in a Geist-style page order.
- `stitch-design-taste`: Semantic Design System Skill for Google Stitch.
- `pick-ui-library`: Pick the right library for a given frontend task from a curated, opinionated list — numbers, OTP inputs, charts, command menus, virtualization, drag and drop, toasts…
- `design-system`: Audit, document, or extend your design system.

</details>

## /review: Review

A graded report on any page or site, with no changes made. It uses the same rubric and independent judge as Super Design, so a review score and a design score mean the same thing. Full mode adds audits for AI-design slop, accessibility, performance, motion, originality and worst-case data.

**Use it when**

- "Is this ready to ship?"
- Grading a site before a pitch
- Finding out why something looks AI-generated
- Accessibility evidence (WCAG 2.1 AA)
- Stress-testing a screen with long names and empty states

**Try**

- `/review Review my site and grade it`
- `/review Do a full audit of this page before launch`

<details><summary>10 mini skills inside</summary>

**Design review**

- `ui-review`: Critiques a screen, flow, prototype or running build against agreed criteria, accessibility included, and ranks findings by severity.
- `audit-ai-design-slop`: Audit websites, apps, screenshots, mockups, and design code for harmful AI-design clichés, generic generated defaults, and established UI defects.
- `no-ai-design-slop`: Prevent and remove generic AI-generated design defaults, incoherent visual choices, and established UI defects while creating, revising, or reviewing websites, apps…
- `workflow-score-to-target`: Score work out of 10 against a clear rubric, then improve it round by round until every item reaches the target score the user named (for example "get it to 8 out of…

**Originality, performance and reporting**

- `audit-reference-originality`: Audit a website or digital experience against its supplied source references for originality and plagiarism risk.
- `performance-profiling`: Guide performance profiling for Apple platform apps with Instruments, Xcode diagnostics, and MetricKit.
- `audit-verify-explain-grade-5`: Audit work, verify claims with concrete evidence, and explain the result in simple grade-5 language.

**Stress tests and status**

- `break-ui`: Try to break a piece of UI by feeding it worst-case data — long names, unbreakable emails, one-letter names, missing fields, huge counts, zero items, long labels…
- `workflow-threads-manager`: Oversee the other Claude threads (sessions) working on the same project.

**Accessibility**

- `accessibility-review`: Run a WCAG 2.1 AA accessibility audit on a design or page.

</details>

## /demo: Demo

Shows the product, and shows the work. It builds realistic fake product UI for hero shots and feature cards, records polished browser walkthroughs, turns pages into short videos with voiceover, sends progress screenshots as you build, and publishes finished projects to GitHub with a proper README and preview.

**Use it when**

- A product shot for a hero or feature card
- A short walkthrough video of a feature
- Before-and-after pictures for an update
- Publishing a finished project with a GitHub Pages link

**Try**

- `/demo Make an animated product shot of our dashboard for the hero`
- `/demo Record a 20-second walkthrough of the checkout flow`

<details><summary>8 mini skills inside</summary>

**Product UI and demos**

- `stageshow`: Build faux product UI that looks like a real product, as a still illustration or an animated demo with a cursor.
- `html-demo`: Show an app working on a web page by drawing it live in HTML instead of recording it.

**Video and voice**

- `html-reel`: Turn a tweet, a video, a YouTube video or a landing page into a 9:16 reel (Instagram Reels, TikTok, Shorts) that says what the source says and looks like it, with every…
- `browser-video-recording`: Create polished 60 fps 4:3 4K browser screen-recording style videos from Codex in-app browser captures, with browser-only crop, natural macOS cursor styling, deliberate…
- `elevenlabs-tts`: Generate ElevenLabs text-to-speech audio from scripts or inline text using local voice profiles.

**Show and ship work**

- `workflow-progress-screenshots`: Show the user real screenshots of the work as it progresses, without being asked.
- `workflow-ship-change`: Ship every change the way the user requires, with the guardrails.
- `publish-project-to-github`: Package a finished local project into an intentional GitHub repository, create a strong README and visual preview, push it safely, configure a public GitHub Pages URL…

</details>

## /marketing: Marketing

Plans, writes and measures marketing for your business or your clients: campaign briefs, competitor positioning, blog, social, email and launch copy, SEO audits, brand-voice checks and performance reports. Pulls live numbers from tools like HubSpot or Ahrefs when those are connected.

**Use it when**

- A launch or campaign plan
- A week of social posts or a newsletter
- An onboarding or win-back email sequence
- An SEO audit with an action plan
- Checking copy against a brand voice
- A monthly marketing report

**Try**

- `/marketing Plan the launch campaign for our new feature`
- `/marketing Write a five-email onboarding sequence`

<details><summary>10 mini skills inside</summary>

**Plan**

- `campaign-plan`: Generate a full campaign brief with objectives, audience, messaging, channel strategy, content calendar, and success metrics.
- `competitive-brief`: Research competitors and generate a positioning and messaging comparison with content gaps, opportunities, and threats.

**Write**

- `content-creation`: Draft marketing content across channels — blog posts, social media, email newsletters, landing pages, press releases, and case studies.
- `draft-content`: Draft blog posts, social media, email newsletters, landing pages, press releases, and case studies with channel-specific formatting and SEO recommendations.
- `email-sequence`: Design and draft multi-email sequences with full copy, timing, branching logic, exit conditions, and performance benchmarks.

**Grow and measure**

- `seo-audit`: Run a comprehensive SEO audit — keyword research, on-page analysis, content gaps, technical checks, and competitor comparison.
- `brand-review`: Review content against your brand voice, style guide, and messaging pillars, flagging deviations by severity with specific before/after fixes.
- `performance-report`: Build a marketing performance report with key metrics, trend analysis, wins and misses, and prioritized optimization recommendations.

**Social posts on X**

- `write-like-meng-on-x`: Write, rewrite, review, or continuously refine X/Twitter posts in Meng To's current voice using his deduplicated authored-post corpus, personal and product context…
- `x-bookmark-quote-posts`: Check a user's latest X/Twitter bookmarks and turn recent saved posts into source-backed quote-post drafts calibrated against the user's latest 100 authored posts.

</details>

## /interview: Interview

Interviews you in depth about a feature or project, asking questions that aren't obvious, until the picture is complete. Then it writes a detailed spec into the project's .plans folder.

**Use it when**

- Before building something big
- Turning a vague idea into a buildable spec
- Surfacing tradeoffs and edge cases early

**Try**

- `/interview Interview me about the new onboarding flow`

## /agentation: Agentation

Adds the Agentation visual feedback toolbar to a Next.js app, so you can click on the page and leave notes your coding agent can read. It verifies the whole loop, not just that the toolbar appears.

**Use it when**

- Giving visual feedback on a running app straight to your agent
- Setting up a review loop for a client build

**Try**

- `/agentation Set up Agentation in this Next.js app and connect it to you`

## Not included: REA

REA (Reverse Engineer Anything) pairs well with these skills but ships separately with its own MCP server. Get it from https://github.com/morluto/rea, or run `npx rea-agents setup`.
