var swiper = new Swiper(".mySwiper", {

    slidesPerView: 1,
    spaceBetween: 20,

    loop: true,

    autoplay: {
        delay: 3000,
        disableOnInteraction: false,
    },


    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },

    breakpoints: {
        640: {
            slidesPerView: 2,
            spaceBetween: 20,
        },
        1024: {
            slidesPerView: 3,
            spaceBetween: 30,
        },
    },
});