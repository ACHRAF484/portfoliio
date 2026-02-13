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