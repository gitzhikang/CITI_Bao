<template>
    <div>
        <header>
            <nav>
                <nav-bar></nav-bar>
            </nav>
        </header>
        <article>
            <section>
                <div id="esg-area">
                    <div id="esg-area-current" class="esg-area-item">
                        <h1>时事热门</h1>
                        <ol>
                            <li v-for="(val, index) in heatedNews" :key="index">
                                <a  :href="val.url">{{val.title}}</a>
                            </li>

                        </ol>
                    </div>
                    <div id="esg-area-important" class="esg-area-item">
                        <h1>ESG要闻</h1>
                        
                        <h3><a href="#" @click="toMain($event)">{{main_title}}</a></h3>
                        <p>{{main_vice_title}}</p>
                    </div>
                    <div id="esg-area-inner" class="esg-area-item">
                        <h1>平台动态</h1>
                        <ol>
                            <li><a href="#">习近平：深入分析推进碳达峰碳中和工作面临的形势任务扎扎实实把党中央决策部署落到实处</a></li>
                        </ol>
                    </div>
                </div>
            </section>
            <section>
                <header class="label-header">
                    <ul id="label-select-ul">
                        <li @click="all">全部</li>
                        <li @click="filter_e">E</li>
                        <li @click="filter_s">S</li>
                        <li @click="filter_g">G</li>
                    </ul>
                </header>
                <section>
                    <div id="news-div">
                        <ul id="news-ul">
                            <li v-for="(val, index) in esgNews" :key="index">
                                <a @click="toNews($event)" href="#">{{val.title}}</a>
                                <span id="news-span" :class="val.label">{{val.label}}</span>
                            </li>
                        </ul>
                        <aside>
                            <div id="esgnews-pie">
                                <!-- Pie Chart -->
                                <v-chart :options="pieChart" autoresize />
                            </div>
                            <div id="esgnews-line">
                                <!-- Pie Chart -->
                                <v-chart :options="lineChart" autoresize />
                            </div>
                        </aside>
                    </div>
                    
                </section>
            </section>
        </article>
        <footer>
            <my-footer></my-footer>
        </footer>
    </div>
</template>

<script>
import NavBar from "../components/NavBar.vue"
import Footer from "../components/Footer.vue"
import ECharts from "vue-echarts";
import { pieChart } from "../assets/js/esgnews/data"
import { lineChart } from "../assets/js/esgnews/data"

export default {
    data() {
        return {
            pieChart: pieChart,
            lineChart: lineChart,
            esgNews: [],
            esgNewsCopy: [],
            heatedNews: [],
            main_title: "",
            main_vice_title: "",
        }
    },
    components: { NavBar, "v-chart": ECharts, "my-footer": Footer},
    mounted() {
        let hid = document.getElementById("nav-search")
        hid.style.visibility = "hidden"
        this.getNews()
        this.getViwed()
        this.getHeatedNews()
        this.getMainNews()
    },
    methods: {
        getViwed(){
            const path = '/getnewsviewed';
            this.$axios.get(path)
                .then((res) => {
                    if (res.data.state == "success")
                    {
                        pieChart["series"][0].data = [
                            {value: res.data.e_history[0], name: 'E', itemStyle:{normal:{color:'#45C2E0'}}},
                            {value: res.data.s_history[0], name: 'S', itemStyle:{normal:{color:'#2F4554'}}},
                            {value: res.data.g_history[0], name: 'G', itemStyle:{normal:{color:'#5A5476'}}},].sort(function (a, b) { return a.value - b.value; }
                        );

                        lineChart["series"][0].data = res.data.e_history.reverse();
                        lineChart["series"][1].data = res.data.s_history.reverse();
                        lineChart["series"][2].data = res.data.g_history.reverse();
                    }
                    else{
                        pieChart["title"]["text"] = "数据获取失败"
                        pieChart["series"][0].data = []

                        lineChart["title"]["text"] = "数据获取失败"
                        lineChart["series"][0].data = [0 ,0, 0, 0, 0, 0];
                        lineChart["series"][1].data = [0 ,0, 0, 0, 0, 0];
                        lineChart["series"][2].data = [0 ,0, 0, 0, 0, 0];
                    }

                }
            ).catch((error) => {
                // eslint-disable-next-line
                pieChart["title"]["text"] = "数据获取失败"
                pieChart["series"][0].data = []

                lineChart["title"]["text"] = "数据获取失败"
                lineChart["series"][0].data = [0 ,0, 0, 0, 0, 0];
                lineChart["series"][1].data = [0 ,0, 0, 0, 0, 0];
                lineChart["series"][2].data = [0 ,0, 0, 0, 0, 0];
            });
        },

        getNews(){
            const path = '/newsquery';
            this.$axios.get(path)
                .then((res) => {
                    if (res.data.state == "success")
                    {
                        this.esgNews = []
                        this.esgNewsCopy = []
                        for (let i = 0; i < res.data.e_news.length; i++){
                            this.esgNews.push({
                                "title": res.data.e_news[i][2],
                                "label": res.data.e_news[i][1],
                                "content": res.data.e_news[i][4]
                            })
                        }
                        for (let i = 0; i < res.data.s_news.length; i++){
                            this.esgNews.push({
                                "title": res.data.s_news[i][2],
                                "label": res.data.s_news[i][1],
                                "content": res.data.s_news[i][4]
                            })
                        }
                        for (let i = 0; i < res.data.g_news.length; i++){
                            this.esgNews.push({
                                "title": res.data.g_news[i][2],
                                "label": res.data.g_news[i][1],
                                "content": res.data.g_news[i][4]
                            })
                        }
                        //打乱
                        this.esgNews.sort(function() {
                            return (0.5-Math.random());
                        });
                        this.esgNewsCopy = this.esgNews
                    }
                    else{
                        this.esgNews = []
                    }

                }
            ).catch((error) => {
                // eslint-disable-next-line
                console.error(error);
                });
        },

        getHeatedNews(){
            const path = '/getheatednews';
            this.$axios.get(path)
                .then((res) => {
                    if (res.data.state == "success")
                    {
                        this.heatedNews = []
                        for (let i = 0; i < res.data.result.length; i++){
                            this.heatedNews.push({
                                "title": res.data.result[i][0],
                                "url": res.data.result[i][1],
                            })
                        }
                    }
                    else{
                        this.heatedNews = []
                    }

                }
            ).catch((error) => {
                // eslint-disable-next-line
                console.error(error);
                });
        },

        getMainNews(){
            const path = '/getmainnews';
            this.$axios.get(path)
                .then((res) => {
                    if (res.data.state == "success")
                    {
                        this.main_title = res.data.title
                        this.main_vice_title = res.data.vicetitle
                    }
                    else{
                        
                    }

                }
            ).catch((error) => {
                // eslint-disable-next-line
                console.error(error);
                });
        },

        toNews(e){
            let title = e.target.innerHTML;
            const { href } = this.$router.resolve({
                path: '/news/' + title
            });
            window.open(href, '_blank');
        },

        toMain(e){
            let title = e.target.innerHTML;
            const { href } = this.$router.resolve({
                path: '/mainnews/' + title
            });
            window.open(href, '_blank');
        },

        all(){
            this.esgNews = this.esgNewsCopy
        },

        filter_e(){
            this.esgNews = []
            for (let i = 0; i < this.esgNewsCopy.length; i++){
                if (this.esgNewsCopy[i].label == "E"){
                    this.esgNews.push(this.esgNewsCopy[i])
                }
            }
        },

        filter_s(){
            this.esgNews = []
            for (let i = 0; i < this.esgNewsCopy.length; i++){
                if (this.esgNewsCopy[i].label == "S"){
                    this.esgNews.push(this.esgNewsCopy[i])
                }
            }
        },

        filter_g(){
            this.esgNews = []
            for (let i = 0; i < this.esgNewsCopy.length; i++){
                if (this.esgNewsCopy[i].label == "G"){
                    this.esgNews.push(this.esgNewsCopy[i])
                }
            }
        },
    }
}
</script>

<style scoped>
@import "../assets/css/views/esgnews/esgnews.css";
</style>