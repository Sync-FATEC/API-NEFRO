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

let btnMenu = document.querySelector('.menuMobile')
let menuMobileBox = document.querySelector('.menuMobileBox')

btnMenu.addEventListener('click', () => {
    if (menuMobileBox.classList.contains('ativo')) {
        menuMobileBox.classList.remove('ativo')
        menuMobileBox.classList.add('desativado')
        btnMenu.classList.remove('ativo')
        btnMenu.classList.add('desativado')
    } else {
        menuMobileBox.classList.remove('desativado')
        menuMobileBox.classList.add('ativo')
        btnMenu.classList.remove('desativado')
        btnMenu.classList.add('ativo')
    }
})