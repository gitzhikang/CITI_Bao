<template>
    <div>
        <HomeHeader/>
        
        <home-slide/>
        <HomeAbout/>
        <my-footer/>
    </div>

</template>

<script>
import HomeHeader from '../components/HomeHeader.vue'
import HomeSlide from '../components/HomeSlide.vue'
import HomeAbout from '../components/HomeAbout.vue' 
import Footer from '../components/Footer.vue'

export default {

  name: 'App',
  components: {
    HomeHeader,
    HomeSlide,
	HomeAbout,
	"my-footer": Footer
  }
}
</script>

<style scoped>

@import "../assets/css/views/index/reset.css";
@import "../assets/css/views/index/bootstrap.min.css";
@import "../assets/css/views/index/chocolat.css";
@import "../assets/css/views/index/font-awesome.min.css";
@import "../assets/css/views/index/index.css";
</style>