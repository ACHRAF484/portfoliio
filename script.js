document.addEventListener('DOMContentLoaded', function() {
    const langButtons = document.querySelectorAll('.lang-btn');
    const translatableElements = document.querySelectorAll('[data-fr][data-en]');
    
    const setLanguage = (lang) => {
        translatableElements.forEach(element => {
            const value = element.getAttribute(`data-${lang}`);
            if (value !== null) {
                element.innerHTML = value;
            }
        });

        langButtons.forEach(button => {
            button.classList.toggle('active', button.getAttribute('data-lang') === lang);
        });

        document.documentElement.lang = lang;
        localStorage.setItem('lang', lang);
    };

    const savedLanguage = localStorage.getItem('lang') || 'fr';
    setLanguage(savedLanguage);

    langButtons.forEach(button => {
        button.addEventListener('click', () => setLanguage(button.getAttribute('data-lang')));
    });

    // Menu Hamburger Mobile
    const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
    const navMenu = document.querySelector('.nav-menu');

    if (mobileMenuToggle) {
        mobileMenuToggle.addEventListener('click', function() {
            this.classList.toggle('active');
            navMenu.classList.toggle('active');
        });

        // Fermer le menu quand on clique sur un lien
        document.querySelectorAll('.nav-menu a').forEach(link => {
            link.addEventListener('click', function() {
                mobileMenuToggle.classList.remove('active');
                navMenu.classList.remove('active');
            });
        });

        // Fermer le menu si on clique en dehors
        document.addEventListener('click', function(event) {
            if (!event.target.closest('.navbar')) {
                mobileMenuToggle.classList.remove('active');
                navMenu.classList.remove('active');
            }
        });
    }

    // Navigation smooth scroll
    const navLinks = document.querySelectorAll('.nav-menu a');
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href.startsWith('#')) {
                e.preventDefault();
                const target = document.querySelector(href);
                if (target) {
                    const offsetTop = target.offsetTop - 70;
                    window.scrollTo({
                        top: offsetTop,
                        behavior: 'smooth'
                    });
                }
            }
        });
    });

    // Nettoyage du DOM
    const footer = document.querySelector('footer.footer');
    if (footer && footer.parentElement) {
        let node = footer.nextSibling;
        while (node) {
            const next = node.nextSibling;
            node.remove();
            node = next;
        }
    }
});
