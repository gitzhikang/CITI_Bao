<template>
<div>
    <header>
        <nav>
            <nav-bar></nav-bar>
        </nav>
    </header>
    <article>
        <header>
            <h1 id="mainnews-title">{{title}}</h1>
        </header>
        <p>
            {{content}}
        </p>
        <footer>
            
        </footer>
    </article>
    <footer>
            <my-footer></my-footer>
        </footer>
</div>
    
</template>

<script>
import NavBar from "../components/NavBar.vue"
import Footer from "../components/Footer.vue"

export default {
    data() {
        return {
            title: "",
            content: "",
            url: "",
            label: ""
        }
    },
    created(){
        this.title = this.$route.params.title;
        this.getData();
    },
    components: { NavBar, "my-footer": Footer},
    mounted() {
        let hid = document.getElementById("nav-search")
        hid.style.visibility = "hidden"
    },
    methods:{
        getData() {
            const path = '/getmainnews';
            this.$axios.get(path)
                .then((res) => {
                    if (res.data.state != "failed")
                    {
                        this.content = res.data.content;
                    }
                    else{
                        this.$router.push({
                            path: "/500"
                        })
                    }
                    
                })
                .catch((error) => {
                    // eslint-disable-next-line
                    console.error(error);
                });
        },
    }
    
}
</script>

<style scoped>
header{
    text-align: center;
    margin-top: 40px;
}

#mainnews-title{
    width: 80vw !important;
    margin-left: 10vw !important;
}

p{
    margin-top: 50px;
    text-indent: 2em;
    width: 80vw;
    margin-left: 10vw;
    margin-bottom: 50px;
}

footer p{
    font-size: 13px;
}
</style>