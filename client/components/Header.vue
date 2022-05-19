<template>
  <div>
    <div
      class="section navbar-area"
      style="background-color: #081828; padding: 5px 0px"
    >
      <div class="container">
        <div class="row justify-content-center top-bar">
          <div
            class="
              col-lg-3 col-md-6 col-sm-5 col-6
              justify-content-start
              margin-top-bottom
            "
          >
            <a
              href="tel:1900 1234"
              class="no-decoration dp-flex tuvan align-items-center"
            >
              <div class="item-top align-items-center">
                <i class="fas fa-phone-alt"></i>
                <p>Tư vấn bán hàng</p>
              </div>
            </a>
          </div>
          <div
            class="
              justify-content-center
              col-lg-4 col-md-6 col-sm-7 col-6
              dp-flex
              margin-left margin-top-bottom
            "
          >
            <a
              href="tel:1900 1234"
              class="no-decoration dp-flex tuvan align-items-center"
            >
              <div class="item-top align-items-center">
                <p>Contact</p>
              </div>
            </a>
            <a
              href="tel:1900 1234"
              class="d-min-none no-decoration dp-flex tuvan align-items-center"
            >
              <div class="item-top align-items-center">
                <p>24/24</p>
              </div>
            </a>
            <a
              href="tel:1900 1234"
              class="no-decoration dp-flex tuvan align-items-center"
            >
              <div class="item-top align-items-center">
                <p>1900 1234</p>
              </div>
            </a>
          </div>

          <div
            class="
              d-max-992-none
              col-lg-4 col-md-3 col-sm-7 col-6
              dp-flex
              margin-left margin-top-bottom
            "
            style="justify-content: flex-end"
          >
            <a
              href="tel:1900 1234"
              class="no-decoration dp-flex tuvan align-items-center"
            >
              <div class="item-top align-items-center">
                <p>Yêu cầu báo giá</p>
              </div>
            </a>
            <a
              href="tel:1900 1234"
              class="no-decoration tuvan align-items-center"
            >
              <div class="item-top align-items-center">
                <p>Khuyến mãi</p>
              </div>
            </a>
          </div>
        </div>
      </div>
    </div>
    <div class="section" style="background-color: #1a4388">
      <div class="container">
        <div class="row align-items-center" style="height: 100px">
          <div class="col-lg-3 col-md-5 col-sm-5 col-5">
            <div class="head-logo">
              <NuxtLink to="/">
                <img
                  src="/images/banner/logo_ankhang.png"
                  alt=""
                />
              </NuxtLink>
            </div>
          </div>
          <div class="col-lg-4 col-md-0 col-sm-0 col-0 d-max-992-none">
            <form>
              <div class="search-head dp-flex">
                <input
                  v-model="searchinput"
                  type="text"
                  placeholder="Tìm kiếm sản phẩm"
                  class="form-control"
                />
                <button type="button">
                  <a :href="filterproducts(searchinput)"
                    ><i class="fas fa-search"></i
                  ></a>
                </button>
              </div>
            </form>
          </div>
          <div class="col-lg-5 col-md-7 col-sm-7 col-7 dp-flex no-decoration">
            <div class="item-hotline dp-flex d-max-1200-none">
              <a href="tel:1900 1234">
                <i class="fas fa-phone-alt"></i>
              </a>
              <h5>Hotline: <span>1900 1234</span></h5>
            </div>
            <div class="item-account dp-flex">
              <img v-if="$auth.loggedIn" class="preview-img" :src="$auth.user.img" width="40px" height="40" />
              <i v-else class="fas fa-user-circle"></i>
              <h5 v-if="$auth.loggedIn">
                <NuxtLink to="/user" class="no-decoration" style="color: #fff"
                  >TÀI KHOẢN</NuxtLink
                >
                <div class="dn-dk">
                  <div class="cart-items" style="margin-top: 2.2px">
                    <a href="javascript:void(0)" class="no-decoration"
                      ><span>
                        {{ $auth.user.first_name }}
                        {{ $auth.user.last_name }}</span
                      ></a
                    >
                    <div class="shopping-item">
                      <div class="dropdown-cart-header">
                        <span>
                          <NuxtLink
                            to="/user/orders"
                            style="float: left; no-decoration; font-size: 16px; font-weight: 700"
                            class="no-decoration"
                            >Lịch sử đơn hàng</NuxtLink
                          >
                        </span>
                      </div>
                    </div>
                  </div>

                  <span> | </span>
                  <a class="no-decoration" style="margin-top: 2.2px"
                    ><span class="cursor-poin" @click="logout">
                      Đăng xuất</span
                    ></a
                  >
                </div>
              </h5>
              <h5 v-else>
                <a class="no-decoration" style="color: #fff">TÀI KHOẢN</a>
                <div class="dn-dk">
                  <div class="cart-items" style="margin-top: 2.2px">
                    <a href="/login" class="no-decoration"
                      ><span> Đăng nhập</span></a
                    >
                  </div>
                  <span> | </span>
                  <a
                    href="/register"
                    class="no-decoration"
                    style="margin-top: 2.2px"
                    ><span> Đăng ký</span></a
                  >
                </div>
              </h5>
            </div>
            <div
              v-if="$auth.loggedIn"
              class="item-account dp-flex"
              style="padding-right: 10px"
            >
              <a href="/cart">
                <i class="fas fa-cart-arrow-down" style="position: relative">
                  <span class="countproductincart"
                    >{{ $auth.user.numofproducts }}
                  </span>
                </i>
              </a>
              <div class="d-xs-none">
                <h5 style="line-height: 40px">Giỏ hàng</h5>
              </div>
            </div>
            <!-- Chư đăng nhập -->
            <div
              v-else
              class="item-account dp-flex"
              style="padding-right: 10px"
            >
              <a @click="nologin()">
                <i class="fas fa-cart-arrow-down" style="position: relative">
                </i>
              </a>
              <div class="d-xs-none">
                <h5 style="line-height: 40px">Giỏ hàng</h5>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="section" style="border-bottom: 1px solid #eee">
      <div class="container">
        <div class="row align-items-center">
          <div class="col-lg-9 col-md-6 col-4">
            <div class="nav-inner">
              <!-- Start Mega Category Menu -->
              <div class="mega-category-menu">
                <span class="cat-button"
                  ><i class="lni lni-menu"></i>Danh mục sản phẩm</span
                >
                <ul class="sub-category">
                  <li v-for="brand in brands" :key="brand.brandname">
                    <a :href="filterproducts(brand.brandname)">{{
                      brand.brandname
                    }}</a>
                  </li>
                </ul>
              </div>
              <!-- End Mega Category Menu -->
              <!-- Start Navbar -->
              <nav class="navbar navbar-expand-lg">
                <button
                  class="navbar-toggler mobile-menu-btn"
                  type="button"
                  data-bs-toggle="collapse"
                  data-bs-target="#navbarSupportedContent"
                  aria-controls="navbarSupportedContent"
                  aria-expanded="false"
                  aria-label="Toggle navigation"
                >
                  <span class="toggler-icon"></span>
                  <span class="toggler-icon"></span>
                  <span class="toggler-icon"></span>
                </button>
                <div
                  class="collapse navbar-collapse sub-menu-bar"
                  id="navbarSupportedContent"
                >
                  <ul id="nav" class="navbar-nav ms-auto">
                    <li class="nav-item">
                      <NuxtLink
                        to="/"
                        class="active"
                        aria-label="Toggle navigation"
                        >Trang chủ</NuxtLink
                      >
                    </li>
                    <li class="nav-item">
                      <NuxtLink to="/introduction" aria-label="Toggle navigation">Giới thiệu</NuxtLink>
                    </li>
                    <li class="nav-item">
                      <NuxtLink class="dd-menu collapsed" to="/"
                        >Sản phẩm</NuxtLink
                      >
                    </li>
                    <li class="nav-item">
                      <a href="#" aria-label="Toggle navigation">Blog</a>
                    </li>
                    <li class="nav-item">
                      <NuxtLink to="/feedback" aria-label="Toggle navigation">Liên hệ</NuxtLink>
                    </li>
                  </ul>
                </div>
                <!-- navbar collapse -->
              </nav>
              <!-- End Navbar -->
            </div>
          </div>
          <div class="col-lg-3 col-md-6 col-8">
            <!-- Start Nav Social -->
            <div class="nav-social">
              <ul>
                <li>
                  <a href="javascript:void(0)"
                    ><i class="lni lni-facebook-filled"></i
                  ></a>
                </li>
                <li>
                  <a href="javascript:void(0)"
                    ><i class="lni lni-twitter-original"></i
                  ></a>
                </li>
                <li>
                  <a href="javascript:void(0)"
                    ><i class="lni lni-instagram"></i
                  ></a>
                </li>
                <li>
                  <a href="javascript:void(0)"><i class="lni lni-skype"></i></a>
                </li>
              </ul>
            </div>
            <!-- End Nav Social -->
          </div>
        </div>
      </div>
    </div>
    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p"
      crossorigin="anonymous"
    ></script>
  </div>
</template>
<script>
export default {
  auth: 'guest ',
    async asyncData({ $axios }) {
    const brands = await $axios.$get('/brand/')
    return { brands }
  },
  props: ['brands' ],
  data() {
    return {
      searchinput: '',
    }
  },
  methods: {
    filterproducts(searchinput) {
      if (searchinput === '') {
        return '/products'
      } else {
        return '/products/filter/' + searchinput
      }
    },
    async logout() {
      await this.$auth.logout(/* .... */)
      window.localStorage.clear()
    },
    nologin() {
      alert('Bạn hiện tại chưa đăng nhập!')
      this.$router.push('/login/')
    },
  },
}
</script>
