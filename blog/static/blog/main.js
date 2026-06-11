/* ================================================
   TECHBLOG — Comportamientos del frontend
   ================================================ */

/* ── Funciones globales de filtrado (accesibles desde HTML) ── */

/**
 * Filtra posts por categoría manteniendo búsqueda activa y orden.
 * @param {string} categoria - Nombre de la categoría o cadena vacía para "Todas".
 */
function filtrarCategoria(categoria) {
    const url = new URL(window.location.href);
    if (categoria) {
        url.searchParams.set('categoria', categoria);
    } else {
        url.searchParams.delete('categoria');
    }
    window.location.href = url.toString();
}

/**
 * Cambia el orden de los posts manteniendo búsqueda y categoría activa.
 * @param {string} orden - 'reciente' o 'antiguo'.
 */
function ordenarPosts(orden) {
    const url = new URL(window.location.href);
    url.searchParams.set('orden', orden);
    window.location.href = url.toString();
}

/* ── Comportamientos al cargar el DOM ── */
document.addEventListener('DOMContentLoaded', () => {

    /* Menú hamburguesa (navegación móvil) */
    const btnHamburguesa = document.getElementById('btnHamburguesa');
    const menuNav        = document.getElementById('menuNav');

    if (btnHamburguesa && menuNav) {
        btnHamburguesa.addEventListener('click', () => {
            const estaAbierto = menuNav.classList.toggle('abierto');
            btnHamburguesa.classList.toggle('activo');
            btnHamburguesa.setAttribute('aria-expanded', String(estaAbierto));
        });

        document.addEventListener('click', (e) => {
            if (!e.target.closest('.nav-principal') && menuNav.classList.contains('abierto')) {
                menuNav.classList.remove('abierto');
                btnHamburguesa.classList.remove('activo');
                btnHamburguesa.setAttribute('aria-expanded', 'false');
            }
        });

        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && menuNav.classList.contains('abierto')) {
                menuNav.classList.remove('abierto');
                btnHamburguesa.classList.remove('activo');
                btnHamburguesa.setAttribute('aria-expanded', 'false');
                btnHamburguesa.focus();
            }
        });
    }

    /* Botones de filtro de categoría (delegación de eventos) */
    document.querySelectorAll('.btn-filtro').forEach((btn) => {
        btn.addEventListener('click', () => {
            filtrarCategoria(btn.dataset.categoria || '');
        });
    });

    /* Breadcrumb: botón de categoría en página de detalle */
    document.querySelectorAll('.breadcrumb-btn-cat').forEach((btn) => {
        btn.addEventListener('click', () => {
            const url = new URL(window.location.origin + '/');
            url.searchParams.set('categoria', btn.dataset.categoria);
            window.location.href = url.toString();
        });
    });

    /* Cierre automático de alertas del sistema (5 segundos) */
    document.querySelectorAll('.alerta').forEach((alerta) => {
        setTimeout(() => {
            alerta.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
            alerta.style.opacity    = '0';
            alerta.style.transform  = 'translateY(-10px)';
            setTimeout(() => alerta.remove(), 400);
        }, 5000);
    });

    /* Sombra en la cabecera al hacer scroll */
    const cabecera = document.querySelector('.cabecera');
    if (cabecera) {
        window.addEventListener('scroll', () => {
            cabecera.classList.toggle('cabecera-scroll', window.scrollY > 20);
        }, { passive: true });
    }

    /* Cerrar menú móvil al hacer clic en un enlace de navegación */
    document.querySelectorAll('.enlace-nav').forEach((enlace) => {
        enlace.addEventListener('click', () => {
            if (menuNav && menuNav.classList.contains('abierto')) {
                menuNav.classList.remove('abierto');
                if (btnHamburguesa) {
                    btnHamburguesa.classList.remove('activo');
                    btnHamburguesa.setAttribute('aria-expanded', 'false');
                }
            }
        });
    });

});