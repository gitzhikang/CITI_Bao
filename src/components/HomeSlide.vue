<template>
<div>
    <el-carousel
    indicator-position="outside"
    height="700px"
    >
        <el-carousel-item v-for="item in bannerList" :key="item.id" >
            
            <img :src="item.ad">
            <div id="mark">{{item.slideLable}}</div>
        </el-carousel-item>
    </el-carousel>
    
</div>
</template>

<script>
import img1 from '../assets/images/slide-1.jpg'
import img2 from '../assets/images/slide-2.jpg'
import img3 from '../assets/images/slide-3.jpg'
import img4 from '../assets/images/slide-4.jpg'
import img5 from '../assets/images/slide-5.jpg'
import SearchBox from './SearchBox.vue'
export default {
    name:'HomeSlide',
    data(){
        return{
            
            bannerList:[
                {id:'001',ad:img1,slideLable:'USINESS CONSULTANCY SERVICES'},
                {id:'002',ad:img2,slideLable:'MONETARY MANAGEMENT SERVICES'},
                {id:'003',ad:img3,slideLable:'TRADING ADVISORY SERVICES'},
                {id:'004',ad:img4,slideLable:'FINANCIAL SECURITY SERVICES'},
                {id:'005',ad:img5,slideLable:'MARKETING STRATEGY SERVICES'}
            ]
    }
    },
    components:{
       
    }
}
</script>

<style scoped>

  #mark {
    color: #ffffff;
    font-size: 50px;
    position: absolute;
    left: 18.5%;
    top: 75%;
    font-weight: bold;
  }

  .el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
    
  }
  
  .el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
   
  }
</style>