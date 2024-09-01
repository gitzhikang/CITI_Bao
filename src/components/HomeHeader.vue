<template>
  <div class="header w3layouts agileits" id="home">

	<!-- Navbar -->
	<nav class="navbar-index navbar-default w3layouts agileits hover-effect" id="nav-index">
		<div class="container">

			<div class="navbar-header w3layouts agileits">
				<button type="button" class="navbar-toggle w3layouts agileits collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false">
					<span class="sr-only w3ls agileits">Toggle navigation</span>
					<span class="icon-bar aits w3layouts"></span>
					<span class="icon-bar w3ls w3layouts"></span>
					<span class="icon-bar aits agileits"></span>
				</button>
				<a class="navbar-brand w3layouts agileits" href="#">ESG PLATFORM</a>
			</div>

			<div id="navbar" class="navbar-collapse w3layouts agileits navbar-right collapse">
				<ul class="nav w3layouts agileits navbar-nav" id="list">
					<li><a @click="search()">企业搜索</a></li>
					<li><a @click="news()">ESG资讯</a></li>
					<li><a @click="my()">我的</a></li>
					<li>
					
					<a href="#about" class="el-dropdown-link">
						关于ESG
					</a>
					
					</li>
					<li v-if="!$store.state.login"><a @click="choseIdentification">登陆</a></li>
					<el-dropdown class="dropdown" v-if="$store.state.login">
					<a class="el-dropdown-link" id="dropdown-logout">
						<i class="el-icon-more-outline"></i>
					</a>
					<el-dropdown-menu slot="dropdown">
						<el-dropdown-item icon="el-icon-star-off"><el-button type="text" @click="foucusEnterprise" id="focusEnter">我的关注企业</el-button></el-dropdown-item>
						<el-dropdown-item icon="el-icon-s-opportunity"><el-button type="text" @click="personalRecommand" id="PersonalRe">我的账户</el-button></el-dropdown-item>
						<el-dropdown-item icon="el-icon-remove"><el-button type="text" @click="open">登出账户</el-button></el-dropdown-item>
						
					</el-dropdown-menu>
					</el-dropdown>
				</ul>
				<home-login/>
        <home-en-login/>
			</div>

		</div>
	</nav>
	<!-- //Navbar -->



	<!-- Slider -->
	
	<!-- //Slider -->

</div>
<!-- //Header -->
<!-- //Navbar -->
</template>

<script>
import HomeLogin from './HomeLogin.vue';
import HomeEnLogin from "@/components/HomeEnLogin";

export default {
  components: {
    HomeLogin,
    HomeEnLogin
  },
    name:'HomeHeader',
  mounted() {

  this.$bus.$on('showlogin',this.choseIdentification)
    this.$bus.$on('showlogin2',this.choseIdentification)
  },
  methods: {
		search(){
			this.$router.push('/SX')
		},
		news(){
			this.$router.push('/news')
		},

		my(){
			if(this.$store.state.auth.ifLogin){
				this.$router.push('/ecommerce/orders')
			}
			else{
				 this.$confirm('请先登陆账户', '提示', {
          confirmButtonText: '登陆',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
			   this.showUser();
        }).catch(() => {
                 
        });
		
		}
			
		},
    choseIdentification(){

      this.$confirm('请选择登陆身份', '提示', {
        distinguishCancelAndClose: true,
        confirmButtonText: '个人',
        cancelButtonText: '企业',
        type: 'warning'
      }).then(() => {
        this.showUser();
      }).catch(action => {
        if(action === 'cancel') {
          this.showEn();
        }
      });
    },
		showUser () {
            this.$modal.show('user-login');

        },
    showEn(){
      this.$modal.show('en-login');
    },
    hide () {
      this.$modal.hide('user-login');
    },
		ifLogin(){
			if(!this.$store.state.login){
				alert('请先登陆账户！')
			}
		},
		logout(){
			console.log(this);
		},
		
      open() {
		
        this.$confirm('确认登出账户?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
		this.$store.commit('USERLOGOUT',false);
          this.$message({
            type: 'success',
            message: '登出成功!'
          });
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '已取消登出'
          });          
        });
      },
	  foucusEnterprise() {
		if(!this.$store.state.login){
        this.$alert('请先登陆账户！', '提示消息', {
          confirmButtonText: '确定',
          
        });
      }
	  },
	  personalRecommand(){
		  if(!this.$store.state.login){
			   this.$alert('请先登陆账户！', '提示消息', {
          		confirmButtonText: '确定',
          
        	});
		  }
	  }

	},
}
</script>
<style src="../assets/css/views/index/bootstrap.min.css"  scoped></style>
<style scoped>




/*-- Navbar --*/

.navbar-index {
  position: absolute;
  z-index: 99999;
  width: 100%;
  background-color: transparent !important;
  border: none;
  border-radius: 0;
  margin: 0;
  padding-top: 30px;
}

.navbar-nav{
  display: inline-block !important;
}

.navbar-default .navbar-brand {
  color: #FFF;
  font-size: 50px;
  font-weight: 700;
  height: 0;
  padding: 0;
  line-height: 0;
  margin-top: 20px;
  font-family: 'Raleway', sans-serif;

}

.navbar-header{
  /*  ------------     */
  display: block !important;
  color: white !important;
}

.navbar-header:hover{
  color: rgb(70, 70, 70) !important;
}

.navbar-default .navbar-brand:hover, .navbar-default .navbar-brand:focus {
  color: #FFF;
  font-weight: 700;
}

.navbar-default .navbar-nav>li>a {
  color: #FFF;
  padding: 10px 20px;
}

.navbar-default .navbar-nav>li>a:hover, .navbar-default .navbar-nav>li>a:focus {
  color: #000;
}

.hover-effect ul{
  margin:0;
  padding:0;
  text-align:center;
}

.hover-effect li{
  list-style:none;
  display:inline-block;
  margin: 0;
}

.hover-effect li a {
  font-size: 16px;
}

.hover-effect a:hover, .hover-effect a:focus {
  outline: none;
}

.hover-effect ul{
  -webkit-transform: translateZ(0);
  transform: translateZ(0);
}

.hover-effect li {
  overflow: hidden;
  position: relative;
}

.hover-effect li:before, .hover-effect li:after {
  display: block;
  -webkit-transform: translateY(100%);
  transform: translateY(100%);
}

.hover-effect li:before {
  left: 0%;
}

.hover-effect li:after {
  left: 50%;
}

.hover-effect a {
  backface-visibility: hidden;
  display: block;
  position: relative;
  text-align: center;
  text-decoration: none;
}

.hover-effect a:before, .hover-effect a:after {
  -webkit-transform: translateY(-100%);
  transform: translateY(-100%);
}

.hover-effect a:before {
  left: 25%;
}

.hover-effect a:after {
  left: 75%;
}

.hover-effect a:hover {
  color: #000;
  font-weight: 500;
}

.hover-effect li:before, .hover-effect li:after, .hover-effect a:before, .hover-effect a:after {
  background-color: #FFF;
  position: absolute;
  height: 100%;
  width: 26%;
  top: 0;
  content: '';
  z-index: -1;
  opacity: 0;
  -webkit-transition: all 0.2s ease;
  transition: all 0.2s ease;
  /*--w3layouts--*/
  /*--agileits--*/
}

.hover-effect li:before {
  -webkit-transition-delay: 0s;
  transition-delay: 0s;
}

.hover-effect li:after {
  -webkit-transition-delay: 0.1s;
  transition-delay: 0.1s;
}

.hover-effect a:before {
  -webkit-transition-delay: 0.05s;
  transition-delay: 0.05s;
}

.hover-effect a:after {
  -webkit-transition-delay: 0.15s;
  transition-delay: 0.15s;
}

.hover-effect li:hover:before, .hover-effect li.current:before, .hover-effect li:hover:after, .hover-effect li.current:after, .hover-effect li:hover a:before, .hover-effect li.current a:before, .hover-effect li:hover a:after, .hover-effect li.current a:after {
  opacity: 1;
  -webkit-transform: translateY(0);
  transform: translateY(0);
}

.hover-effect li:hover:before, .hover-effect li.current:before {
  -webkit-transition-delay: 0s;
  transition-delay: 0s;
}

.hover-effect li:hover:after, .hover-effect li.current:after {
  -webkit-transition-delay: 0.15s;
  transition-delay: 0.15s;
}

.hover-effect li:hover a:before, .hover-effect li.current a:before {
  -webkit-transition-delay: 0.075s;
  transition-delay: 0.075s;
}

.hover-effect li:hover a:after, .hover-effect li.current a:after {
  -webkit-transition-delay: 0.225s;
  transition-delay: 0.225s;
}

#esg-news header{
  text-align: center;
}

#esg-news-header{
  width: 200px;
  border-bottom: black solid 1px;
  margin-left: 44%;
}

/*--w3layouts--*/
/*--agileits--*/
/*-- //Navbar --*/

	/deep/ .el-dropdown-link{
		color: #FFF;
		padding: 9px 20px;
		
	}
	.el-dropdown-link:hover{
		color: rgb(0, 0, 0);
		font-weight: 500;
	}
	.about, .mission, .expertise, .portfolio, .feedback, .team, .newsletter, .news, .contact {
	padding: 100px 0;
	}
	#focusEnter,#PersonalRe{
		text-decoration:none;
		color:#606266
	}
	.el-icon-more-outline{
		font-size: 25px;
		color: #ffffff;
	}
	#dropdown-logout{
		padding: 5px 20px;
	}
</style>