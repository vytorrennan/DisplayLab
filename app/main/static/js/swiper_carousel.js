const swiperGaming = new Swiper(".swiperGaming", {

    slidesPerView: 1,
    spaceBetween: 20,

    loop: true,

    autoplay: {
        delay: 3000,
        disableOnInteraction: false,
        pauseOnMouseEnter: true,
    },

    pagination: {
        el: ".swiperGaming .swiper-pagination",
        clickable: true,
    },
    navigation: {
        nextEl: ".swiper-btn-gaming-next",
        prevEl: ".swiper-btn-gaming-prev",
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

const swiperPesquisa = new Swiper(".swiperPesquisa", {

    slidesPerView: 1,
    spaceBetween: 20,

    loop: true,

    autoplay: {
        delay: 3000,
        disableOnInteraction: false,
        pauseOnMouseEnter: true,
    },

    pagination: {
        el: ".swiperPesquisa .swiper-pagination",
        clickable: true,
    },
    navigation: {
        nextEl: ".swiper-btn-pesquisa-next",
        prevEl: ".swiper-btn-pesquisa-prev",
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