<template>
        <div class="section">
      <div class="container">
        <div class="row">
          <div class="col-12">
            <div class="block__header">
              <h2 class="block-header-title text-center">{{sectiontitle}}</h2>
            </div>
          </div>
          <div
            v-for="product in products"
            :key="product.productcode"
            class="col-lg-3 col-md-4 col-6 items-product mg-bt-30"
          >
            <ProductCard :product="product"></ProductCard>
          </div>
        </div>
      </div>
    </div>
</template>
<script>
export default {
  auth: false,
  props: ['products','sectiontitle' ],
}
</script>
