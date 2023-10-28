const menuButton = document.getElementById('menu-button');
const menu = document.getElementById('menu');
const arrow = document.querySelector('.arrow');

menuButton.addEventListener('click', function() {
    if (menu.style.display === 'block') {
        menu.style.display = 'none';
    } else {
        menu.style.display = 'block';
    }
    arrow.classList.toggle('arrow_rotate');
});