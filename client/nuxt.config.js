export default {
  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: 'client',
    htmlAttrs: {
      lang: 'en'
    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
      { name: 'format-detection', content: 'telephone=no' }
    ],
    link: [
      { rel: 'stylesheet', href:'https://unpkg.com/swiper/swiper-bundle.min.css'},
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
      { rel: 'stylesheet', href:'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css'},
      { href: "https://cdn.lineicons.com/3.0/lineicons.css", rel:"stylesheet"},
      { rel: 'stylesheet', href:'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.6.1/font/bootstrap-icons.css'},
     ]
  },
  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [
    '@/static/css/style.css',
    '@/static/css/brandstyle.css',
    '@/static/css/loginstyle.css',
  ],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [
  ],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
    // https://go.nuxtjs.dev/eslint
    '@nuxtjs/eslint-module',
  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    'cookie-universal-nuxt',
    ['cookie-universal-nuxt', { alias: 'cookiz' }],
    'bootstrap-vue/nuxt',
    '@nuxtjs/axios',
    '@nuxtjs/auth-next'
  ],
  

  // Axios module configuration: https://go.nuxtjs.dev/config-axios
  axios: {
    baseURL: "http://127.0.0.1:8000/",
    Credentials: true
  },
  auth: {
    strategies: {
      local: {
        scheme: 'refresh',
        localStorage: {
          prefix: 'auth.'
        },
        username: {
          prefix: 'username.',
          property: 'username',
          maxAge: 60 * 60 
        },
        token: {
          prefix: 'access.',
          property: 'access',
          maxAge: 60*5,
          type: 'Bearer'
        },
        refreshToken: {
          prefix: 'refresh.',
          property: 'refresh',
          data: 'refresh',
          maxAge: 60 * 60
        },
        user: {
          property: 'user',
          autoFetch: true,
        },
        endpoints: {
          login: { url: '/login/', method: 'post'},
          refresh: { url: 'api/token/refresh/', method: 'post' },
          user: { url: '/user/', method: 'get' },
          logout: { url: '/logout/', method: 'post'}
        },
        Credentials: true
      }
    }
  },

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {
  },

  router: {
    middleware: ['auth']
  }
}
