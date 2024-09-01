<template>
    <div>
        <!-- search Popup -->
        <div class="body-overlay" id="body-overlay" @click="clickOverlay()"></div>
        <div class="search-popup" id="search-popup">
            <div class="search-form">
                <div class="form-group">
                        <input type="text" class="form-control" placeholder="Search....." id="search-input">
                </div>
                <button class="submit-btn" id="submit-btn" @click="submitSearch()"><i class="fa fa-search"></i></button>
            </div>
        </div>
        <!-- //. search Popup -->
        
        
        <div id="nav-search">
            <nav class="navbar-n navbar-area navbar-expand-lg nav-style-01">
                <div class="container-fluid nav-container-m px-0">
                    <div class="nav-right-content">
                        <ul>
                            <li class="search" id="search" @click="clickSearch()">
                                <i class="fa fa-search"></i>
                            </li>
                        </ul>
                    </div>
                </div>
            </nav>
        </div>        
        <!-- navbar area end -->

        <pre-loader id="preloader"></pre-loader>
    </div>
    
</template>

<script>
import $ from "jquery"
import "../assets/js/searchbox/jquery-2.2.4.min.js"
import "../assets/js/searchbox/bootstrap.min.js"
import PreLoader from "./PreLoader.vue"

export default {
  data() {
    return {
      
    };
  },
  mounted() {
    /*-----------------
            preloader
        ------------------*/
        var preLoder = $("#preloader");
        preLoder.fadeOut(1000);
  },
  methods: {
    clickSearch(){
        let bodyOvrelay =  $('#body-overlay');
        let searchPopup = $('#search-popup');

        $(document).on('click','#search',function(e){
            e.preventDefault();
            searchPopup.addClass('active');
            bodyOvrelay.addClass('active');
            
            
            
        });
    },

    submitSearch(){
        let inputted = document.getElementById("search-input").value;
        console.log('/enterprise/' + inputted)
        this.$router.push({
            path:'/enterprise/' + inputted,
        })
    },

    clickOverlay(){
        let bodyOvrelay =  $('#body-overlay');
        let searchPopup = $('#search-popup');

        $(document).on('click','#body-overlay',function(e){
            e.preventDefault();
            bodyOvrelay.removeClass('active');
            searchPopup.removeClass('active');
        });
    }
  },
  components: { PreLoader },
};
</script>

<style scoped>
@import "../assets/css/components/searchbox/searchbox.css";
@import "../assets/css/components/searchbox/font-awesome.min.css";

</style>