<template>
  <div>
    <Header />
    <section class="container g-0 bg-light">
      <div
        id="myCarousel"
        class="carousel carousel-dark slide"
        data-bs-ride="carousel"
      >
        <div class="carousel-indicators">
          <button
            type="button"
            data-bs-target="#myCarousel"
            data-bs-slide-to="0"
            class=""
            aria-label="Slide 1"
          ></button>
          <button
            type="button"
            data-bs-target="#myCarousel"
            data-bs-slide-to="1"
            aria-label="Slide 2"
            class=""
          ></button>
          <button
            type="button"
            data-bs-target="#myCarousel"
            data-bs-slide-to="2"
            aria-label="Slide 3"
            class="active"
            aria-current="true"
          ></button>
        </div>
        <div class="carousel-inner">
          <div class="carousel-item">
            <img src="@/assets/images/banner/banner1.jpg" class="img-fluid" />
          </div>
          <div class="carousel-item">
            <img src="@/assets/images/banner/banner2.jpg" class="img-fluid" />
          </div>
          <div class="carousel-item active">
            <img src="@/assets/images/banner/banner1.jpg" class="img-fluid" />
          </div>
        </div>
        <button
          class="carousel-control-prev"
          type="button"
          data-bs-target="#myCarousel"
          data-bs-slide="prev"
        >
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Previous</span>
        </button>
        <button
          class="carousel-control-next"
          type="button"
          data-bs-target="#myCarousel"
          data-bs-slide="next"
        >
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Next</span>
        </button>
      </div>
    </section>
    <section class="container g-0 bg-light">
      <h2 class="block-header-title">Danh Mục Laptop</h2>
      <div class="row list-item">
        <div v-for="brand in brands" :key="brand.brandname" class="col-4 col-lg-2">
          <a :href="filterproducts(brand.brandname)">
          <img
            class="img-fluid"
            :src="brand.img"
          />
          </a>
        </div>
      </div>
    </section>
    <section class="container g-0 bg-light">
      <h2 class="block-header-title text-center">Sản Phẩm Mới Về</h2>
      <div class="row g-0">
        <div
          v-for="product in newproducts"
          :key="product.productcode"
          class="col-6 col-lg-3"
        >
          <div class="product">
            <div class="img-thumbnail">
              <img class="img-fluid" :src="product.img" />
            </div>
            <div class="product_title">
              <a :href="getproductsurl(product.productcode)"
                >{{ getsortname(product.name).name }}...</a
              >
            </div>
            <div class="product_price">
              <span>{{ product.price }}$</span>
            </div>
            <div>
              <button type="button" class="btn btn-primary add-to-cart col-12" @click="addtocart(product.name)">
                Mua Ngay
              </button>
            </div>
          </div>
        </div>
      </div>
    </section>
    <section class="container g-0 bg-light">
      <h2 class="block-header-title text-center">Sản Phẩm Nổi Bật</h2>
      <div class="row g-0">
        <div
          v-for="product in instockproducts"
          :key="product.productcode"
          class="col-6 col-lg-3"
        >
          <div class="product">
            <div class="img-thumbnail">
              <img class="img-fluid" :src="product.img" />
            </div>
            <div class="product_title">
              <a :href="getproductsurl(product.productcode)"
                >{{ getsortname(product.name).name }}...</a
              >
            </div>
            <div class="product_price">
              <span>{{ product.price }}$</span>
            </div>
            <div>
              <button type="button" class="btn btn-primary add-to-cart col-12" @click="addtocart(product.name)">
                Mua Ngay
              </button>
            </div>
          </div>
        </div>
      </div>
    </section>
    <section class="container g-0 bg-light">
      <h2 class="block-header-title text-center">Sản Phẩm Bán Chạy</h2>
      <div class="row g-0">
        <div
          v-for="product in hotproducts"
          :key="product.productcode"
          class="col-6 col-lg-3"
        >
          <div class="product">
            <div class="img-thumbnail">
              <img class="img-fluid" :src="product.img" />
            </div>
            <div class="product_title">
              <a :href="getproductsurl(product.productcode)"
                >{{ getsortname(product.name).name }}...</a
              >
            </div>
            <div class="product_price">
              <span>{{ product.price }}$</span>
            </div>
            <div>
              <button type="button" class="btn btn-primary add-to-cart col-12" @click="addtocart(product.name)">
                Mua Ngay
              </button>
            </div>
          </div>
        </div>
      </div>
    </section>
    <Footer />
  </div>
</template>

<script>
export default {
  auth: 'guest',
  async asyncData({ $axios }) {
    const brands = await $axios.$get('/brand/')
    const newproducts = await $axios.$get('/newproducts/')
    const instockproducts = await $axios.$get('/instockproducts/')
    const hotproducts = await $axios.$get('/hotproducts/')
    return { newproducts, instockproducts, hotproducts, brands }
  },
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
      if(this.$auth.loggedIn){
        await this.$axios.$post('addtocart/', {
        productname: ProductName,
      })
      this.$nuxt.refresh();
      this.$router.go()
      }
      else{
        this.$router.push('/login/');
      }
    },
    filterproducts(searchinput){
      if (searchinput === '') {
        return "/products"
      }
      else {
        return"/products/filter/"+ searchinput
      }
    }
  },
}
</script>
