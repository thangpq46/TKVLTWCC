<template>
  <div>
    <div class="section pd-top-10">
      <div class="container">
        <div class="row justify-content-center">
          <div class="col-lg-8 col-md-8 col-12 banner-left">
            <div>
              <b-carousel
                id="carousel-fade"
                fade
                indicators
                img-width="800"
                img-height="200"
                style="max-width: 800px; max-height: 200px;"
              >
                <b-carousel-slide
                  img-src="/images/banner/bn-left-1.png"
                ></b-carousel-slide>
                <b-carousel-slide
                  img-src="/images/banner/bn-left-2.png"
                ></b-carousel-slide>
                <b-carousel-slide
                  img-src="/images/banner/bn-left-3.png"
                ></b-carousel-slide>
                <b-carousel-slide
                  img-src="/images/banner/bn-left-4.png"
                ></b-carousel-slide>
                <b-carousel-slide
                  img-src="/images/banner/bn-left-5.png"
                ></b-carousel-slide>
              </b-carousel>
            </div>
          </div>
          <div class="col-lg-4 col-md-4 col-12 banner-right">
            <div class="">
              <img
                src="/images/banner/bn-right-1.png"
                class="img-fluid"
                alt=""
              />
            </div>
            <div class="pd-top-10">
              <img
                src="/images/banner/bn-right-2.png"
                class="img-fluid"
                alt=""
              />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>