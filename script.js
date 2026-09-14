/**
 * VAKS Global Trading Co. (VGTC) - Main Application Script
 * Features: Sticky Navbar, Mobile Menu Drawer, FAQ Accordion, Fun Facts Counter (IntersectionObserver),
 * Quote/Contact Modal Handler, WhatsApp & Phone Direct Integration, and AOS Init.
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
    if (mainHeader) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 40) {
                mainHeader.classList.add('shadow-md', 'py-1');
                mainHeader.classList.remove('py-0');
            } else {
                mainHeader.classList.remove('shadow-md', 'py-1');
            }
        });
    }

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
                if (menuIcon) {
                    menuIcon.classList.remove('fa-bars');
                    menuIcon.classList.add('fa-xmark');
                }
            } else {
                mobileMenu.classList.add('hidden');
                if (menuIcon) {
                    menuIcon.classList.remove('fa-xmark');
                    menuIcon.classList.add('fa-bars');
                }
            }
        });

        // Close mobile menu when clicking any nav link
        document.querySelectorAll('.mobile-nav-link').forEach(link => {
            link.addEventListener('click', () => {
                mobileMenu.classList.add('hidden');
                if (menuIcon) {
                    menuIcon.classList.remove('fa-xmark');
                    menuIcon.classList.add('fa-bars');
                }
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
});

// 7. Direct Contact Modal Logic (No Form Fields)
function openQuoteModal(productName) {
    const modal = document.getElementById('quote-modal');
    if (modal) {
        modal.classList.remove('hidden');
        document.body.style.overflow = 'hidden';
    }

    const subtitle = document.getElementById('modal-product-subtitle');
    const waUae = document.getElementById('modal-wa-uae');
    const waPk = document.getElementById('modal-wa-pk');

    if (productName) {
        if (subtitle) subtitle.textContent = `Inquiring for: ${productName}`;
        const msg = encodeURIComponent(`Hello VGTC! I would like to inquire about ${productName}.`);
        if (waUae) waUae.href = `https://wa.me/971503908597?text=${msg}`;
        if (waPk) waPk.href = `https://wa.me/923218988421?text=${msg}`;
    } else {
        if (subtitle) subtitle.textContent = `Connect directly with our export desk for pricing & specs.`;
        const defaultMsg = encodeURIComponent(`Hello VGTC! I would like to request a B2B export quote.`);
        if (waUae) waUae.href = `https://wa.me/971503908597?text=${defaultMsg}`;
        if (waPk) waPk.href = `https://wa.me/923218988421?text=${defaultMsg}`;
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
    openQuoteModal(productName);
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
