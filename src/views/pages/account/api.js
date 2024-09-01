import axios from 'axios'

let apiserver = 'http://127.0.0.1:8888';

const appapi = axios.create({
  //headers: {'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'},
  baseURL:apiserver
});

let apppost = (url,params) =>{
  return appapi.post(url,params)
};

export default {
  //用户相关
  register : params =>{
    return apppost('/user/register',params);
  },
  login:params =>{
    return apppost('/user/login',params);
  },
  nameIsExist:params =>{
    return apppost('/user/isExist',params);
  }
}



