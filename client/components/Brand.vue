<template>
  <div class="pd-top-20 pd-bt-30">
    <div class="container">
      <div class="head-brand">
        <div class="body-brand">
          <div class="">
            <div class="swiper mySwiper">
              <div class="swiper-wrapper">
                <div
                  class="swiper-slide"
                  v-for="brand in brands"
                  :key="brand.brandname"
                >
                  <a :href="filterproducts(brand.brandname)">
                    <img
                      class="img-fluid rounded mx-auto d-block"
                      :src="brand.img"
                    />
                  </a>
                </div>
              </div>
              <div class="swiper-button-next"></div>
              <div class="swiper-button-prev"></div>
            </div>
          </div>
          <script src="https://unpkg.com/swiper/swiper-bundle.min.js"></script>

          <!-- Initialize Swiper -->
          <script>
            var swiper = new Swiper('.mySwiper', {
              slidesPerView: 6,
              spaceBetween: 10,
              loop: true,
              loopFillGroupWithBlank: true,
              pagination: {
                el: '.swiper-pagination',
                clickable: true,
              },
              navigation: {
                nextEl: '.swiper-button-next',
                prevEl: '.swiper-button-prev',
              },
            })
          </script>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  auth: 'guest',
  props: ['brands' ],
  methods: {
    filterproducts(searchinput) {
      if (searchinput === '') {
        return '/products'
      } else {
        return '/products/filter/' + searchinput
      }
    },
  },
}
</script>
