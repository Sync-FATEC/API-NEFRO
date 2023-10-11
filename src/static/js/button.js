document.addEventListener('DOMContentLoaded', function() {
    const menuButton = document.getElementById('menu-button');
    const menu = document.getElementById('menu');
    const loginLink = document.querySelector('#menu a[href="/login"]');
    const cadastrarLink = document.querySelector('#menu a[href="/cadastro"]');

    menuButton.addEventListener('click', function() {
        if (menu.style.display === 'block') {
            menu.style.display = 'none';
            cadastrarLink.style.display = 'none';
        } else {
            menu.style.display = 'block';
            cadastrarLink.style.display = 'block';
        }
    });
});
