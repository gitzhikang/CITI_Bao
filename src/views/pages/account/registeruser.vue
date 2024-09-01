<template>
  <div>
    <el-row>
      <el-col :span="24">

      </el-col>
    </el-row>
    <el-row class="form_main">

      <el-col :span="8" :offset="8">
        <el-card class="box-card">
          <div>
            <div class="text-center">
              <div>
                <a href="/" class="logo">
                  <img src="@/assets/images/logo-dark.png" height="45px" alt="logo" />
                </a>
              </div>

              <h4 class="font-size-18 mt-4">Register account</h4>
              <p class="text-muted">Get your free Nazox account now.</p>
            </div>
          </div>
          <div class="card_main">
            <el-form ref="form" :model="form" :rules="rules" label-width="90px">
              <el-form-item label="用户名" prop="name" >
                <el-input v-model="form.name"></el-input>
              </el-form-item>
              <el-form-item label="电子邮箱" prop="email">
                <el-input v-model="form.email"></el-input>
              </el-form-item>
              <el-form-item label="个人电话" prop="phone">
                <el-input v-model="form.phone"></el-input>
              </el-form-item>
              <el-form-item label="密码" prop="password">
                <el-input type="password" v-model="form.password"></el-input>
              </el-form-item>
              <el-form-item label="确认密码" prop="checkpassword">
                <el-input type="password" v-model="form.checkpassword"></el-input>
              </el-form-item>

              <el-form-item>
                <el-row>
                  <el-col :span="12"><div class="grid-content bg-purple"><el-button type="primary" @click="register('form')" :disabled="isDisable">注册</el-button></div></el-col>
                  <el-col :span="12"><div class="grid-content bg-purple-light"><el-button @click="resetForm('form')">重置</el-button></div></el-col>
                </el-row>


              </el-form-item>
            </el-form>
            <div class="mt-5 text-center">
              <p>
                Already have an account ?
                <a
                    tag="a"

                    class="font-weight-medium text-primary"
                    @click="showLogin"
                >Login</a>
              </p>
              <p>
                © 2020 Nazox. Crafted with
                <i class="mdi mdi-heart text-danger"></i> by Themesdesign
              </p>
            </div>
          </div>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import api from "./api.js";

export default {
  name: "registeruser",
  data() {
    var checkname = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('用户名不能为空'));
      }
      let data = {
        name: this.form.name,
        password: this.form.password,
        email:this.form.email,
        phone:this.form.phone,
      }
      api.nameIsExist(data).then(res => {
        let code = res.data.code;
        let msg = res.data.msg;
        if (code == 0) {
          callback(new Error(msg));
        } else {
          callback();
        }
      })
    };

    var checkPass = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入密码'));
      } else {
        callback();
      }
    };
    var checkPass2 = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请再次输入密码'));
      } else if (value !== this.form.password) {
        callback(new Error('两次输入密码不一致!'));
      } else {
        callback();
        this.isDisable = false;
      }
    };
    var checkemail = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入邮箱'));
      } else {
        callback();
      }
    };
    var checkphone = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入手机号'));
      } else {
        callback();
      }
    };
    return {
      isDisable: false,
      form: {
        name: '',
        password: '',
        checkpassword: '',
        email:'',
        phone:''
      },
      rules: {
        name: [
          {validator: checkname, trigger: 'blur'},
        ],
        password: [
          {validator: checkPass, trigger: 'blur'}
        ],
        checkpassword: [
          {validator: checkPass2, trigger: 'blur'}
        ],
        email:[
          { validator: checkemail, trigger: 'blur' },
          { type: 'email', message: '请输入正确的邮箱地址', trigger: ['blur', 'change'] }
        ],
        phone: [
          {validator: checkphone, trigger: 'blur'}
        ]
      }
    }
  },

  methods: {
    register(form) {
      this.$refs[form].validate((valid) => {
        if (valid) {
          let data = {
            name: this.form.name,
            password: this.form.password
          }
          api.register(data).then(res => {
            if (res.data.code == 1) {
              this.$notify.success({
                title: '注册成功',
                message: "即将跳转到登录页",
                onClose: this.gologin
              })
            } else {
            }
          })
        } else {
          this.$notify.error({
            title: '注册失败',
            message: "请按要求输入",
            position: 'top-left'
          });
          return false;
        }
      });
    },
    showLogin(){

      this.$bus.$emit('showlogin2',true);
      this.$router.push('/index')
    },
    gologin() {
      this.$router.push("/user/login")
    },
    resetForm(formName) {
      this.$refs[formName].resetFields();
    }
  }

}
</script>

<style scoped>

.card_main {
  margin-top: 30px;
  margin-right: 20px;
}
</style>
