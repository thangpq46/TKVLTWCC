<template>
  <div>
    <Header  :brands="brands"></Header>
    <div class="section pd-top-20">
		<div class="container">
			<div class="row ">
				<div class=" col-md-6 col-12">
			  	<img class="item img-fluid" :src="product.img" :alt="product.productid"/>
		    </div>
		    <div class=" col-md-6 col-12 info-product-right align-items-center">
			    <h4>{{ product.name }}</h4>
		      <div>
			      	<span class="price">{{ product.price}}$</span>
                  
		      </div>
		    	<ul class="review">
                <li><i class="lni lni-star-filled"></i></li>
                <li><i class="lni lni-star-filled"></i></li>
                <li><i class="lni lni-star-filled"></i></li>
                <li><i class="lni lni-star-filled"></i></li>
                <li><i class="lni lni-star-filled"></i></li>
                <li><span>5.0</span></li>
            </ul>		
		        <hr/>
            <div class="product-info-items">
              <p v-for="detail in details" :key="detail">{{ detail }}</p>
              <p v-if="product.stock > 1"><b>Còn Hàng</b></p>
              <p v-else> <b>Hết Hàng</b> </p>
              <button class="btn btn-danger" @click="addtocart(product.name)">MUA HÀNG</button>
            </div>
      </div>
      </div>
		</div>
	</div>
    <div class="section">
      <div class="container">
        <div class="row">
          <div class="col-12">
            <div class="block__header">
              <h2 class="block-header-title text-center">SẢN PHẨM TƯƠNG TỰ</h2>
            </div>
          </div>
          <div
            v-for="product in products"
            :key="product.productcode"
            class="col-lg-3 col-md-4 col-6 items-product mg-bt-30"
          >
            <div class="product-img">
              <a :href="getproductsurl(product.productcode)">
                <img
                  :src="product.img"
                  alt=""
                  class="img-fluid rounded mx-auto d-block pd-10"
                />
              </a>
            </div>
            <div class="product-info">
              <a :href="getproductsurl(product.productcode)">
                <h6>{{ getsortname(product.name).name }}...</h6>
              </a>
              <span>{{ product.price }}$</span>
              <button
                type="button"
                class="btn btn-danger add-to-cart col-12"
                @click="addtocart(product.name)"
              >
                Mua Ngay
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
    <Top-footer />
    <Footer />
  </div>
</template>
<script>
export default {
  auth: 'guest auth',
  async asyncData({ $axios, params }) {
    const product = await $axios.$get(`/products/${params.id}`)
    const products = await $axios.$get(`/products`)
    const details = product.description.split('- ')
    const brands = await $axios.$get('/brand/')
    return { product, products, details, brands }
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
    filterproducts(searchinput){
      if (searchinput === '') {
        return "/products"
      }
      else {
        return"/products/filter/"+ searchinput
      }
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
  },
}
</script>
