import axios from "axios"

export function request(config) {
    const instance = axios.create({
        baseURL: "http://127.0.0.1:5000",
        timeout: 5000
    })
    // http request 拦截器
    instance.interceptors.request.use(
        config => {
            if (sessionStorage.getItem("accessToken")) {
                config.headers.Authorization = sessionStorage.getItem("accessToken")
            }
            return config;
        },
        err => {
            return Promise.reject(err);
        }
    )
    // http response 拦截器
    instance.interceptors.response.use(
        response => {
            return response;
        },
        error => {
            if (error.response) {
                console.log('axios:' + error.response.status);
                switch (error.response.status) {
                    case 403:
                        // 返回403 清除token信息并跳转到登录页面
                        sessionStorage.clear()
                        this.$router.replace({
                            path: '/login'
                        })
                        this.$Message({ showClose: true, message: '未登录，返回登陆界面', type: 'error', duration: 3000 })

                }
            }
            return Promise.reject(error);   // 返回接口的错误信息
        }
    )
    return instance(config)
}


