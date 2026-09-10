const swipers = document.querySelectorAll('.sobreSwiper');
swipers.forEach(function(element) {
    new Swiper(element, {
        slidesPerView: 1,
        spaceBetween: 24,
        navigation: {
            nextEl: element.parentElement.querySelector(".swiper-button-next"),
            prevEl: element.parentElement.querySelector(".swiper-button-prev"),
        },
        pagination: {
            el: element.parentElement.querySelector(".swiper-pagination"),
            clickable: true,
        },
        breakpoints: {
            768: {
                slidesPerView: 2,
            },
            992: {
                slidesPerView: 3,
            }
        }
    });
});