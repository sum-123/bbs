<template>
  <div id="app">
    <el-menu
      :default-active="activeIndex"
      class="el-menu-demo"
      mode="horizontal"
      style="dispaly: flex; position: relative"
      @select="handleSelect"
      
    >
      <el-menu-item><i class="el-icon-notebook-2"></i></el-menu-item>
      <el-menu-item index="1" @click="indexClick">首页</el-menu-item>
      <el-menu-item index="2" @click="searchClick">搜索</el-menu-item>

      <div style="position: absolute; right: 10px; display: inline-block">
        <el-button plain  type="primary" @click="loginClick" v-if="state == 0">登录</el-button>
        <el-button plain  type="primary" @click="registerClick" v-if="state == 0">注册</el-button>

        <el-button plain  type="primary"  style="padding:5px"  @click="createMessage" v-if="state == 1">发布留言</el-button>
        <el-dropdown  style="margin:" @command="handleCommand">
          <div class="demo-type">
            <div class="el-dropdown-link">
              <img :src="imgUrl" alt="" style="height:48px" v-if="state == 1">
            </div>
          </div>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item command="personal">个人中心</el-dropdown-item>
            <el-dropdown-item command="myMessage2">我的留言</el-dropdown-item>
            <el-dropdown-item command="logout" divided>注销</el-dropdown-item>
          </el-dropdown-menu>
        </el-dropdown>
      </div>
    </el-menu>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  data() {
    return {
      activeIndex: "1",
      activeIndex2: "1",
      state: localStorage.state,
      url:localStorage.avatar
      // url:'cat.jpg'
    };
  },

  computed: {
        imgUrl () {
            return require('./assets/'+this.url)
        }
  },


  methods: {
    handleSelect(key, keyPath) {
      console.log(key, keyPath);
    },
    indexClick() {
      this.$router.push({
        path: "index",
      });
    },
    loginClick() {
      this.$router.push({
        path: "login",
      });
    },
    registerClick() {
      this.$router.push({
        path: "register",
      });
    },

    handleCommand(command) {
      if (command == "personal") {
        // localStorage.avatar = this.imgUrl;
        this.$router.push({
          path: "personal",
        });
      }

      if (command == "myMessage2") {
        this.$router.push({
          path: "myMessage2",
        });
      }

      if (command == "logout") {
        localStorage.state = 0;

        sessionStorage.clear();
        this.$router.push({
          path: "index",
        });
        location.reload();
      }
    },

    searchClick() {
      this.$router.push({
        path: "search",
      });
    },
    createMessage(){
      this.$router.push({
        path: "createMessage",
      });
    }
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.el-dropdown-link {
  cursor: pointer;
  color: #409eff;
}

.el-icon-arrow-down {
  font-size: 12px;
}
</style>
