#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Script pour améliorer la version mobile du portfolio

# 1. Mettre à jour le HTML avec le bouton hamburger
with open('/Users/achrafberouih/Desktop/portfolio/index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Ajouter le bouton hamburger
old_nav = '''    <nav class="navbar">
        <div class="container">
            <div class="nav-brand">ACHRAF BEROUIH</div>
            <ul class="nav-menu">'''

new_nav = '''    <nav class="navbar">
        <div class="container">
            <div class="nav-brand">ACHRAF BEROUIH</div>
            <button class="mobile-menu-toggle" aria-label="Toggle menu">
                <span></span>
                <span></span>
                <span></span>
            </button>
            <ul class="nav-menu">'''

html_content = html_content.replace(old_nav, new_nav)

with open('/Users/achrafberouih/Desktop/portfolio/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("✅ HTML mis à jour avec bouton hamburger")

# 2. Mettre à jour le CSS pour le mobile
with open('/Users/achrafberouih/Desktop/portfolio/style.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

# Ajouter les styles pour le menu hamburger mobile
mobile_styles = '''
/* Bouton Hamburger - Caché sur desktop */
.mobile-menu-toggle {
    display: none;
    flex-direction: column;
    justify-content: space-around;
    width: 30px;
    height: 25px;
    background: transparent;
    border: none;
    cursor: pointer;
    padding: 0;
    z-index: 1000;
}

.mobile-menu-toggle span {
    width: 100%;
    height: 3px;
    background-color: var(--color-accent);
    transition: all 0.3s ease;
    border-radius: 2px;
}

.mobile-menu-toggle.active span:nth-child(1) {
    transform: rotate(45deg) translate(8px, 8px);
}

.mobile-menu-toggle.active span:nth-child(2) {
    opacity: 0;
}

.mobile-menu-toggle.active span:nth-child(3) {
    transform: rotate(-45deg) translate(7px, -7px);
}

'''

# Trouver où insérer (avant les media queries)
media_query_pos = css_content.find('@media (max-width: 1024px)')

if media_query_pos > 0:
    css_content = css_content[:media_query_pos] + mobile_styles + css_content[media_query_pos:]

# Remplacer les styles mobile existants
old_mobile_768 = '''@media (max-width: 768px) {
    .navbar .container {
        padding: var(--spacing-sm) var(--spacing-md);
        gap: var(--spacing-sm);
    }

    .nav-brand {
        font-size: 14px;
    }

    .nav-menu {
        gap: var(--spacing-sm);
    }

    .nav-menu a {
        font-size: 0.85rem;
    }

    .lang-toggle {
        transform: scale(0.9);
    }'''

new_mobile_768 = '''@media (max-width: 768px) {
    .navbar .container {
        padding: var(--spacing-sm) var(--spacing-md);
        position: relative;
    }

    .mobile-menu-toggle {
        display: flex;
    }

    .nav-menu {
        position: fixed;
        top: 60px;
        right: -100%;
        width: 250px;
        height: calc(100vh - 60px);
        background-color: var(--color-bg-light);
        flex-direction: column;
        padding: var(--spacing-2xl) var(--spacing-lg);
        box-shadow: -2px 0 10px rgba(0, 0, 0, 0.1);
        transition: right 0.3s ease;
        z-index: 999;
        gap: var(--spacing-lg);
    }

    .nav-menu.active {
        right: 0;
    }

    .nav-menu li {
        width: 100%;
    }

    .nav-menu a {
        font-size: 16px;
        padding: var(--spacing-sm) 0;
        display: block;
    }

    .lang-toggle {
        position: absolute;
        top: 50%;
        right: 60px;
        transform: translateY(-50%);
    }'''

css_content = css_content.replace(old_mobile_768, new_mobile_768)

# Simplifier encore plus pour 480px
old_mobile_480 = '''@media (max-width: 480px) {
    .navbar .container {
        padding: 4px 8px;
    }

    .nav-brand {
        font-size: 12px;
    }

    .nav-menu {
        gap: 2px;
        font-size: 0.65rem;
    }

    .nav-menu a {
        font-size: 0.65rem;
        padding: 2px 4px;
    }

    .lang-toggle {
        transform: scale(0.7);
    }

    .lang-btn {
        padding: 2px 5px;
        font-size: 9px;
    }'''

new_mobile_480 = '''@media (max-width: 480px) {
    .navbar .container {
        padding: var(--spacing-sm);
    }

    .nav-brand {
        font-size: 13px;
    }

    .mobile-menu-toggle {
        width: 28px;
        height: 22px;
    }

    .nav-menu {
        top: 55px;
        width: 200px;
    }

    .lang-toggle {
        right: 50px;
        transform: translateY(-50%) scale(0.85);
    }

    .lang-btn {
        padding: 4px 8px;
        font-size: 11px;
    }'''

css_content = css_content.replace(old_mobile_480, new_mobile_480)

with open('/Users/achrafberouih/Desktop/portfolio/style.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

print("✅ CSS mis à jour pour version mobile améliorée")

# 3. Mettre à jour le JavaScript
with open('/Users/achrafberouih/Desktop/portfolio/script.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

# Ajouter la fonctionnalité du menu hamburger avant la fermeture
hamburger_js = '''
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
'''

# Ajouter avant le dernier });
js_content = js_content.replace('});', hamburger_js + '\n});')

with open('/Users/achrafberouih/Desktop/portfolio/script.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print("✅ JavaScript mis à jour avec menu hamburger fonctionnel")
print("\n🎉 Tous les fichiers ont été mis à jour pour une meilleure compatibilité mobile!")
