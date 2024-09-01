<template>
<body>
    <div id="fof-div">
    <aside id="fof-as"><img src="../assets/images/maintenance-bg.png" alt="404 Image">
    </aside>
    <main id="fof-main">
        <h1>Sorry!</h1>
        <p>
        服务器错误<em>. . . 网络攻城狮正在加急维修.</em>
        </p>
        <a href="/index"><button @click="toIndex()">返回主页！</button></a>
    </main>
    </div>
</body>

</template>


<script>


export default({
    data() {
        return{
            smgHtmlPath: "../../public/3-404/index.html"
        }
    },
    methods: {
        toIndex(){
            this.$router.push({
                path: "/index"
            })
        }
    },
})
</script>


<style scoped>
@import "../assets/css/views/404/style.css";
</style>