const sideMenu = document.querySelector('.sideMenu')
const sideOption = document.querySelector('.sideOption')

sideMenu.addEventListener('click', () => {
    sideOption.classList.toggle('off')
})