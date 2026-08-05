/**
 * VAKS Global Trading Co. (VGTC) - Main Application Script
 * Features: Sticky Navbar, Mobile Menu Drawer, FAQ Accordion, Fun Facts Counter (IntersectionObserver),
 * Quote Modal Handler, Scrollspy, and AOS Init.
 */

document.addEventListener('DOMContentLoaded', () => {
    // 1. Initialize AOS (Animate On Scroll)
    if (typeof AOS !== 'undefined') {
        AOS.init({
            duration: 800,
            easing: 'ease-in-out',
            once: true,
            offset: 80
        });
    }

    // 2. Sticky Navbar & Scroll Effects
    const mainHeader = document.getElementById('main-header');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 40) {
            mainHeader.classList.add('shadow-md', 'py-1');
            mainHeader.classList.remove('py-0');
        } else {
            mainHeader.classList.remove('shadow-md', 'py-1');
        }
    });

    // 3. Mobile Hamburger Menu Toggle
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');
    const menuIcon = document.getElementById('menu-icon');

    if (mobileMenuBtn && mobileMenu) {
        mobileMenuBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            const isHidden = mobileMenu.classList.contains('hidden');
            if (isHidden) {
                mobileMenu.classList.remove('hidden');
                menuIcon.classList.remove('fa-bars');
                menuIcon.classList.add('fa-xmark');
            } else {
                mobileMenu.classList.add('hidden');
                menuIcon.classList.remove('fa-xmark');
                menuIcon.classList.add('fa-bars');
            }
        });

        // Close mobile menu when clicking any nav link
        document.querySelectorAll('.mobile-nav-link').forEach(link => {
            link.addEventListener('click', () => {
                mobileMenu.classList.add('hidden');
                menuIcon.classList.remove('fa-xmark');
                menuIcon.classList.add('fa-bars');
            });
        });

        // Close mobile menu when clicking outside
        document.addEventListener('click', (e) => {
            if (!mobileMenu.contains(e.target) && !mobileMenuBtn.contains(e.target)) {
                mobileMenu.classList.add('hidden');
                if (menuIcon) {
                    menuIcon.classList.remove('fa-xmark');
                    menuIcon.classList.add('fa-bars');
                }
            }
        });
    }

    // 4. FAQ Accordion Handler
    const accordionHeaders = document.querySelectorAll('.accordion-header');
    accordionHeaders.forEach(header => {
        header.addEventListener('click', () => {
            const content = header.nextElementSibling;
            const icon = header.querySelector('.accordion-icon');
            const isOpen = content.classList.contains('open');

            // Close all open accordions first (Single-expand mode)
            document.querySelectorAll('.accordion-content').forEach(item => {
                item.classList.remove('open');
                item.style.maxHeight = null;
            });
            document.querySelectorAll('.accordion-icon').forEach(ic => {
                ic.classList.remove('rotate-180');
            });
            document.querySelectorAll('.accordion-header').forEach(hdr => {
                hdr.setAttribute('aria-expanded', 'false');
            });

            // Toggle current accordion if it wasn't open
            if (!isOpen) {
                content.classList.add('open');
                content.style.maxHeight = content.scrollHeight + 'px';
                if (icon) icon.classList.add('rotate-180');
                header.setAttribute('aria-expanded', 'true');
            }
        });
    });

    // 5. Fun Facts Animated Counter (IntersectionObserver)
    const counters = document.querySelectorAll('.stat-counter');
    let animated = false;

    const startCounters = () => {
        counters.forEach(counter => {
            const target = parseInt(counter.getAttribute('data-target'), 10) || 0;
            const duration = 2000; // 2 seconds animation
            const stepTime = 30;
            const totalSteps = duration / stepTime;
            const increment = target / totalSteps;
            let current = 0;

            const timer = setInterval(() => {
                current += increment;
                if (current >= target) {
                    counter.innerText = target.toLocaleString();
                    clearInterval(timer);
                } else {
                    counter.innerText = Math.floor(current).toLocaleString();
                }
            }, stepTime);
        });
    };

    const counterObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting && !animated) {
                animated = true;
                startCounters();
                observer.disconnect(); // Only run once
            }
        });
    }, { threshold: 0.3 });

    const funFactsSection = document.querySelector('.stat-counter')?.closest('section');
    if (funFactsSection) {
        counterObserver.observe(funFactsSection);
    }

    // 6. Active Link Highlighting (Multi-Page)
    const navLinks = document.querySelectorAll('.nav-link');
    const currentPath = window.location.pathname.split('/').pop() || 'index.html';

    navLinks.forEach(link => {
        const linkPath = link.getAttribute('href');
        if (linkPath === currentPath) {
            link.classList.add('text-[#8BC34A]', 'font-semibold');
            if (link.classList.contains('border-b-2')) {
                link.classList.remove('border-transparent');
                link.classList.add('border-vaks-lime');
            }
        }
    });

    // 8. HTML5 Canvas Hero Image Sequence Player (Scroll-Driven)
    const initScrollHeroCanvas = () => {
        const canvas = document.getElementById('hero-canvas');
        if (!canvas) return;
        const ctx = canvas.getContext('2d');
        const heroSection = document.querySelector('.hero-section-wrapper') || canvas.parentElement;

        const frameCount = 150; // Total frames in hero-section folder
        const images = [];
        let imagesLoaded = 0;

        const drawFrame = (index) => {
            const img = images[index];
            if (!img || !img.complete) return;
            canvas.width = img.naturalWidth || 1920;
            canvas.height = img.naturalHeight || 1080;
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
        };

        // Preload frames
        for (let i = 1; i <= frameCount; i++) {
            const img = new Image();
            const frameNumber = i.toString().padStart(3, '0');
            img.src = `hero-section/ezgif-frame-${frameNumber}.jpg`;
            img.onload = () => {
                imagesLoaded++;
                if (imagesLoaded === 1) drawFrame(0);
            };
            images.push(img);
        }

        // Update frame index based on window scroll position within hero section
        const updateScrollFrame = () => {
            const rect = heroSection.getBoundingClientRect();
            const windowHeight = window.innerHeight;
            
            // Calculate scroll progress percentage (0 to 1) relative to Hero viewport
            const totalScrollableHeight = heroSection.offsetHeight + windowHeight;
            const currentScroll = Math.max(0, windowHeight - rect.top);
            const scrollFraction = Math.min(1, Math.max(0, currentScroll / totalScrollableHeight));

            const frameIndex = Math.min(
                frameCount - 1,
                Math.floor(scrollFraction * frameCount)
            );

            requestAnimationFrame(() => drawFrame(frameIndex));
        };

        window.addEventListener('scroll', updateScrollFrame, { passive: true });
        window.addEventListener('resize', () => {
            updateScrollFrame();
        });
    };

    initScrollHeroCanvas();
});

// 7. Global Quote Modal Logic
function openQuoteModal() {
    const modal = document.getElementById('quote-modal');
    const form = document.getElementById('quote-form');
    const successMsg = document.getElementById('form-success');
    if (modal) {
        modal.classList.remove('hidden');
        document.body.style.overflow = 'hidden';
        if (form) form.classList.remove('hidden');
        if (successMsg) successMsg.classList.add('hidden');
    }
}

function closeQuoteModal() {
    const modal = document.getElementById('quote-modal');
    if (modal) {
        modal.classList.add('hidden');
        document.body.style.overflow = 'auto';
    }
}

function inquireProduct(productName) {
    openQuoteModal();
    const select = document.getElementById('modal-product');
    if (select) {
        select.value = productName;
    }
}

function handleQuoteSubmit(e) {
    e.preventDefault();
    const form = document.getElementById('quote-form');
    const successMsg = document.getElementById('form-success');

    // Simulate submission delay for realistic feel
    const submitBtn = form.querySelector('button[type="submit"]');
    const originalText = submitBtn.innerHTML;
    submitBtn.disabled = true;
    submitBtn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Submitting...';

    setTimeout(() => {
        submitBtn.disabled = false;
        submitBtn.innerHTML = originalText;
        form.reset();
        form.classList.add('hidden');
        successMsg.classList.remove('hidden');
    }, 1000);
}

// Close modal on Escape key
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
        closeQuoteModal();
    }
});

// Close modal on clicking backdrop
document.addEventListener('click', (e) => {
    const modal = document.getElementById('quote-modal');
    if (e.target === modal) {
        closeQuoteModal();
    }
});
