const mobileBtn = document.querySelector('.mobile-btn')

mobileBtn.addEventListener('click', () => {
    const mobileMenu = document.querySelector('.mobile-menu')
    if(mobileMenu.classList.contains('active')){
        mobileMenu.classList.remove('active')
    } else {
        mobileMenu.classList.add('active')
    }
})