<!-- 登陆页面   -->
<template>
  <div id="app">
    <el-row :gutter="20">
      <!-- gutter 栅格间距 -->
      <el-col :span="8" :offset="8">
        <!-- span 栅格占的列数，offset是偏移列数 -->
        <div class="grid-content"></div>
      </el-col>
    </el-row>

    <el-row :gutter="20" style="padding: 25px">
      <!-- gutter 栅格间距 -->

      <el-col :span="8" :offset="8">
        <!-- span 栅格占的列数，offset是偏移列数 -->
        <el-card shadow="always">
          <h1>用户注册</h1>
          <el-divider></el-divider>

          <el-form
            :model="ruleForm"
            status-icon
            :rules="rules"
            ref="ruleForm"
            label-width="100px"
            class="demo-ruleForm"
          >
            <!-- 用户名 -->
            <el-form-item label="用户名" prop="username">
              <el-input
                placeholder="请输入10字符以内的用户名"
                v-model="ruleForm.username"
              ></el-input>
            </el-form-item>

            <!-- 密码 -->
            <el-form-item label="密码" prop="pass">
              <el-input
                type="password"
                placeholder="请输入密码"
                v-model="ruleForm.pass"
                autocomplete="off"
              ></el-input>
            </el-form-item>
            <!-- 确认密码 -->
            <el-form-item label="确认密码" prop="checkPass">
              <el-input
                type="password"
                placeholder="请再次输入密码"
                v-model="ruleForm.checkPass"
                autocomplete="off"
              ></el-input>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="submitForm('ruleForm')"
                >提交</el-button
              >
              <el-button @click="resetForm('ruleForm')">重置</el-button>
            </el-form-item>
          </el-form>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>



<script>
import {request} from '../network/request'
import Crypto from "@/crypto/index.js";
export default {

  data() {
    var checkUsername = (rule, value, callback) => {
      if (!value) {
        return callback(new Error("用户名不能为空"));
      }
      setTimeout(() => {
        if (value.length > 10) {
          callback(new Error("请输入输入10字符以内的用户名"));
        } else {
          callback();
        }
      }, 1000);
    };
    var validatePass = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请输入密码"));
      } else {
        if (this.ruleForm.checkPass !== "") {
          this.$refs.ruleForm.validateField("checkPass");
        }
        callback();
      }
    };
    var validatePass2 = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请再次输入密码"));
      } else if (value !== this.ruleForm.pass) {
        callback(new Error("两次输入密码不一致!"));
      } else {
        callback();
      }
    };
    return {
      userId: parseInt(localStorage.userId),
      userList: [],
      ruleForm: {
        pass: "",
        checkPass: "",
        username: "",
      },
      rules: {
        pass: [{ validator: validatePass, trigger: "blur" }],
        checkPass: [{ validator: validatePass2, trigger: "blur" }],
        username: [{ validator: checkUsername, trigger: "blur" }],
      },
    };
  },

  methods: {
    submitForm() {
      
      if(this.ruleForm.pass.length < 8){
        alert("密码不能小于8位！")
      }else{
        //发送post请求
      var that = this;
      request({
        method: "post", //请求方式，默认是get请求
        url: "/register", //地址
        data: {
          //这里是发送给后台的数据
          username: this.ruleForm.username,
          password: Crypto.set(this.ruleForm.pass),
          avatar:
            "monster.jpg",
        },
      }).then(function (res) {
        if (res.data == "success") {
          alert("注册成功！")
          that.ruleForm.username = "";
          that.ruleForm.pass = "";
          that.ruleForm.checkPass = "";
        } else if (res.data == "repetition") {
          alert("用户名重复！")
        }
      });
      
      }
      
    },
    resetForm(formName) {
      this.$refs[formName].resetFields();
    },
  },
};
</script>

<style>
.content {
  margin: 0 auto;
}
.el-card {
  border-radius: 30px;
  /* box-shadow: 0 2px 12px 0 rgb(243, 102, 102); */
  /* box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04); */
}
.grid-content {
  /* background: rgb(14, 214, 131); */
  border-radius: 4px;
  min-height: 80px;
}
.el-row {
  margin-bottom: 20px;
}
</style>
