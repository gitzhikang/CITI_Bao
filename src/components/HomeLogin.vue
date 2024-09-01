<template>
<foo name="user-login" transition="pop-out" :width="modalWidth" :focus-trap="true" :height="400">
  <div class="box">
    <div class="box-part" id="bp-left">
      <div class="partition" id="partition-register">
        <div class="partition-title">LOGIN ACCOUNT</div>
        <div class="partition-form">
          <form autocomplete="false">

            <div class="autocomplete-fix">
              <input disabled type="password">
            </div>

            <input id="n-email" type="text" placeholder="Email address or Username">
            
            <input id="n-password2" type="password" placeholder="Password">
          </form>
            <div id="forgetpassword">
              <router-link to="/forgot-password"><span>忘记密码</span></router-link>
            </div>
          <div style="margin-top: 42px">
          </div>

          

          <button class="large-btn github-btn" @click="login"><span>登陆</span></button>
          <button class="large-btn facebook-btn" @click="userRegister"><span>用户注册</span></button>
        </div>
      </div>
    </div>
    <div class="box-part" id="bp-right">
      <div class="box-messages">
          <!-- 右侧内容 -->
          <img src="../assets/images/img/login/login.jpg" alt="">
      </div>
    </div>
  </div>
</foo>
</template>
<script>
import {authMethods} from '../state/helpers'
import api from "@/views/pages/account/api";
const MODAL_WIDTH = 656

export default {
  name: 'HomeLogin',
  data() {
    return {
      modalWidth: MODAL_WIDTH,
      form:{
        name:'',
        password:''
      }

    }
  },
  created() {
    this.modalWidth =
      window.innerWidth < MODAL_WIDTH ? MODAL_WIDTH / 2 : MODAL_WIDTH
  },
  methods: {
     userRegister(){
      this.$router.push({
        name:'registeruser'
      })
    },
    login(){
      let data = {
        name: this.form.name,
        password: this.form.password
      }
      api.login(data).then(res => {
        if (res.data.code == 1) {
          this.$notify.success({
            title: '提示',
            message: "登陆成功",
          })
        } else {
        }
      })
    }
  }
}
</script>
<style scoped>
img{
  width: 100%;
}

.box {
  background: white;
  overflow: hidden;
  width: 656px;
  height: 400px;
  border-radius: 2px;
  box-sizing: border-box;
  box-shadow: 0 0 40px black;
  color: #8b8c8d;
  font-size: 0;
}
.box .box-part {
  display: inline-block;
  position: relative;
  vertical-align: top;
  box-sizing: border-box;
  height: 100%;
  width: 50%;
}
.box .box-part #bp-right {
  background: url("/static/panorama.jpg") no-repeat top left;
  border-left: 1px solid #eee;
}
.box .box-messages {
  position: absolute;
  left: 0;
  bottom: 98px;
  width: 100%;
}
.box .box-error-message {
  position: relative;
  overflow: hidden;
  box-sizing: border-box;
  height: 0;
  line-height: 32px;
  padding: 0 12px;
  text-align: center;
  width: 100%;
  font-size: 11px;
  color: white;
  background: #f38181;
}
.box .partition {
  width: 100%;
  height: 100%;
}
.box .partition .partition-title {
  box-sizing: border-box;
  padding: 40px;
  width: 100%;
  text-align: center;
  letter-spacing: 1px;
  font-size: 20px;
  font-weight: 300;
}
.box .partition .partition-form {
  padding: 15px 20px;
  box-sizing: border-box;
}
.box input[type='password'],
.box input[type='text'] {
  display: block;
  box-sizing: border-box;
  margin-bottom: 4px;
  width: 100%;
  font-size: 12px;
  line-height: 2;
  border: 0;
  border-bottom: 1px solid #dddedf;
  padding: 4px 8px;
  font-family: inherit;
  transition: 0.5s all;
}
.box button {
  background: white;
  border-radius: 4px;
  box-sizing: border-box;
  padding: 10px;
  letter-spacing: 1px;
  font-family: 'Open Sans', sans-serif;
  font-weight: 400;
  min-width: 140px;
  margin-top: 8px;
  color: #8b8c8d;
  cursor: pointer;
  border: 1px solid #dddedf;
  text-transform: uppercase;
  transition: 0.1s all;
  font-size: 10px;
}
.box button:hover {
  border-color: #c7c8c9;
  color: #6f7071;
}
.box .large-btn {
  width: 100%;
  background: white;
}
.box .large-btn span {
  font-weight: 600;
}
.box .large-btn:hover {
  color: white !important;
}
.box .button-set {
  margin-bottom: 8px;
}
.box #register-btn,
.box #signin-btn {
  margin-left: 8px;
}
.box .facebook-btn {
  border-color: #3880ff;
  color: #3880ff;
}
.box .facebook-btn:hover {
  border-color: #3880ff;
  background: #3880ff;
}
.box .enterprise-btn {
  border-color: #2faa66;
  color: #2faa66;
}
.box .enterprise-btn:hover {
  border-color: #2faa66;
  background: #2faa66;
}
.box .github-btn {
  border-color: #dba226;
  color: #dba226;
}
.box .github-btn:hover {
  border-color: #dba226;
  background: #dba226;
}
.box .autocomplete-fix {
  position: absolute;
  visibility: hidden;
  overflow: hidden;
  opacity: 0;
  width: 0;
  height: 0;
  left: 0;
  top: 0;
}


.pop-out-enter-active,
.pop-out-leave-active {
  transition: all 0.5s;
}

.pop-out-enter,
.pop-out-leave-active {
  opacity: 0;
  transform: translateY(24px);
}
.box-messages{
    position: absolute;
}
#forgetpassword{
    position: absolute;
    width: 100px;
    height: 40px;
    font-size: 10px;
    right: 5px;
    top: 200px;
    color: red;
}
</style>