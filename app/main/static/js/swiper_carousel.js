const swiperGaming = new Swiper(".swiperGaming", {

    slidesPerView: 1,
    spaceBetween: 20,

    loop: true,

    autoplay: {
        delay: 3000,
        disableOnInteraction: false,
    },


    pagination: {
        el: ".swiperGaming .swiper-pagination",
        clickable: true,
    },
    navigation: {
        nextEl: ".swiperGaming .swiper-button-next",
        prevEl: ".swiperGaming .swiper-button-prev",
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
    },


    pagination: {
        el: ".swiperPesquisa .swiper-pagination",
        clickable: true,
    },
    navigation: {
        nextEl: ".swiperPesquisa .swiper-button-next",
        prevEl: ".swiperPesquisa .swiper-button-prev",
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