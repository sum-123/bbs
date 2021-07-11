<template>
  <div class="about">
    <div class="content-box">
      <img src="../assets/login-header.png" alt="" class="bgimg" />
      <div class="phone-user">
        <h3 class="phone-user-title">用户登录</h3>
        <div class="phone-user-input">
          <span>
            <i class="el-icon-user-solid"></i>
            <input type="text" v-model="username" placeholder="请输入用户名" />
          </span>
        </div>
        <div class="phone-user-input">
          <span>
            <i class="el-icon-lock"></i>
            <input
              type="password"
              v-model="password"
              placeholder="请输入密码"
            />
          </span>
        </div>
        <div class="phone-user-button">
          <el-button type="primary" style="width: 100%" @click="submitForm"
            >登录</el-button
          >
        </div>
        <div class="right">
          <el-link href="/register">还没有账号？注册一个</el-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Crypto from "@/crypto/index.js";
export default {
  data() {
    return {
      username: "",
      password: "",
      userList: JSON.parse(localStorage.getItem("userList")),
    };
  },
  methods: {
    submitForm() {
      console.log(localStorage.avatar)
      var that = this
      this.$axios({
        method: "post",
        url: "http://127.0.0.1:5000/login",
        data: {
          username: that.username,
          // password:this.password,
          password: Crypto.set(that.password),
        },
      })
        .then(function (res) {
          console.log(res);
          if (res.data == "success") {
            alert("登陆成功！");
            localStorage.state = 1;
            localStorage.avatar = 'monster.jpg';
            localStorage.username = that.username;
            localStorage.password = Crypto.set(that.password);
            that.$router.push({
              path: "index",
            });
            location.reload();
          } else if (res.data == "fail") {
            alert("密码错误！");
          } else if (res.data == "invalid") {
            alert("用户名不存在！");
          }
          
        })
        .catch(function (err) {
          console.log(err);
        });
    },
  },
};
</script>
<style scoped>
span {
  border: none;
  padding: 10px 4px 10px 4px;
  border-bottom: 1px solid #dcdfe6;
}
span:hover {
  border-bottom: 1px solid #66afe9;
  outline: 0;
}
input {
  width: 80%;
  border: none;
  padding: 2px;
  font-size: 15px;
}
input:focus {
  outline: 0;
}
.content-box {
  width: 500px;
  height: 500px;
  position: relative;
  top: 150px;
  left: 50%;
  transform: translateX(-50%);
  border-radius: 15px;
  box-shadow: 0 0 28px #dee9fe, 0 0 15px rgba(0, 0, 0, 0.04);
}
.bgimg {
  height: 113px;
  width: 288px;
  top: -80px;
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  background-size: 100%;
}
.phone-user {
  margin: auto;
  position: relative;
  top: 50px;
  font-size: 20px;
  text-align: center;
  width: 80%;
  height: 100%;
}

.phone-user-title {
  color: #000;
  font-weight: bold;
}

.phone-user-input {
  margin: auto;

  margin-top: 50px;
  position: relative;
  text-align: center;
}
.phone-user-button {
  margin: auto;
  width: 100%;
  margin-top: 50px;
}
.phone-user-line {
  border-bottom: 1px solid #dedede;
}
.right {
  margin-top: 30px;
  float: right;
}
</style>
