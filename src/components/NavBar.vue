<template>
    <!-- Navbar -->
	<nav class="navbar-m navbar-default w3layouts agileits hover-effect-m">
		<p @click="toIndex">
			ESG Platfrom
		</p>
		<div class="container-m">

			<div id="navbar-m" class="navbar-collapse-m w3layouts agileits navbar-right-m collapse">
				
				<ul id ="nav-list" class="nav-m  navbar-nav">
					<li><a @click="search()">企业搜索</a></li>
					<li><a @click="news()">ESG资讯</a></li>
					
					<li><a href="#team">TEAM</a></li>
					<li><a href="#contact">CONTACT</a></li>
					<li><a @click="my()">我的</a></li>
				</ul>
			</div>
			<div id="searchbox">
				<search-box></search-box>
			</div>
			
		</div>
	</nav>
	<!-- //Navbar -->
</template>

<script>
import SearchBox from "../components/SearchBox.vue"

export default {
  data() {
    return {
      
    };
  },
  mounted() {
    
  },
  methods: {
    toIndex(){
		this.$router.push({
            path:'/index',

        })
	},
	search(){
		this.$router.push('/SX')
	},
	news(){
		this.$router.push('/news')
	},
	my(){
		const { href } = this.$router.resolve({
                path: '/ecommerce/orders'
            });
            window.open(href, '_blank');
	},
  },
  components: { SearchBox },
};
</script>

<style scoped>
@import "../assets/css/components/navbar/bootstrap.min.css";
@import "../assets/css/components/navbar/chocolat.css";
@import "../assets/css/components/navbar/font-awesome.min.css";
@import "../assets/css/components/navbar/navbar.css";

</style>
