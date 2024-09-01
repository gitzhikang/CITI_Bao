<template>
  <!-- About -->
  <div class="about w3layouts agileits" id="about">
    <div class="container">
      <div class="about-grids w3layouts agileits">
        <div
          class="col-md-6 col-sm-6 about-grid w3layouts agileits about-grid-1"
        >
          <img src="../assets/images/about.jpg" alt="Affiliation" />
        </div>
        <div
          class="col-md-6 col-sm-6 about-grid w3layouts agileits about-grid-2"
        >
          <h1>ABOUT US</h1>
          <p>
            Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do
            eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim
            ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
            aliquip exea.
          </p>

          <!-- Modal -->
          <button
            class="btn btn-primary w3layouts agileits hvr-underline-from-left"
            @click="show"
          >
            了解更多<span
              class="glyphicon glyphicon-arrow-right"
              aria-hidden="true"
            ></span>
          </button>
          <!-- 弹窗内容 -->
          <foo name="my-first-modal" 
            classes="cute-dog-profile-photo"
            :width="1000"
            :height="600"
            :adaptive="true"
            :focusTrap="true"
          >
             <div 
      slot="top-right"
      class="ct-top-right"
      @click="$modal.hide('my-first-modal')"
    >
      Close
    </div> 
        <img src="../assets/images/about.jpg" class="aboutPhoto" />
            This is my first modal!!!
          </foo>
          <!-- //Modal -->
        </div>
        <div class="clearfix"></div>
      </div>
    </div>
  </div>
  <!-- //About -->
</template>

<script>
export default {
  name: "HomeAbout",
   methods: {
        show () {
            this.$modal.show('my-first-modal');
        },
        hide () {
            this.$modal.hide('my-first-modal');
        }
    },
    

};
</script>

<style scoped>

@import "../assets/css/views/index/about.css";
.cute-dog-profile-photo {
  background-color: rgb(198, 197, 197);
  border-radius: 50px;
  box-shadow: 0 2px 20px 0 rgba(0, 0, 0, 0.4);
  border: 1px solid rgba(255, 255, 255, 0.65);
}
.aboutPhoto{
    width:500px;
    
    margin: 100px 0;
}
    .ct-top-right {
  cursor: pointer;
  margin: 20px;
  padding: 10px 20px;
  font-weight: 600;
  color: white;
  text-shadow: 0 0px 20px black;
  background: #555;
  border-radius: 100px;
}
.about, .mission, .expertise, .portfolio, .feedback, .team, .newsletter, .news, .contact {
	padding: 100px 0;
}

</style>