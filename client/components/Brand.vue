<template>
  <div class="pd-top-20 pd-bt-30">
    <div class="container">
      <div class="head-brand">
        <div class="body-brand">
          <div class="">
            <div class="swiper mySwiper">
              <div class="swiper-wrapper">
                <div class="swiper-slide" v-for="brand in brands" :key="brand.brandname">
                  <a  :href="filterproducts(brand.brandname)">
                    <img class="img-fluid rounded mx-auto d-block" :src="brand.img" />
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
  props: ['brands'],
  methods: {
    getsortname(name) {
      name = name.substring(0, 55)
      return { name }
    },
    getproductsurl(productid) {
      const url = '/products/' + productid
      return url
    },
    async addtocart(ProductName) {
      if (this.$auth.loggedIn) {
        await this.$axios.$post('addtocart/', {
          productname: ProductName,
        })
        this.$nuxt.refresh()
        this.$router.go()
      } else {
        this.$router.push('/login/')
      }
    },
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