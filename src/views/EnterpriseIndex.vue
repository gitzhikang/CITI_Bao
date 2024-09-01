<template>
    <div id="enterprise">
        <header style="border-top: 0px">
            <nav-bar></nav-bar>
        </header>
        <section>
            <header>
                <h1 id="title">{{name}}</h1>
                <function-bar id="func" :followed = 'followed'></function-bar>
                
            </header>
            <article id="main">
                <section>
                    <section id="esg-sec">
                        <header>
                            <h2>
                                ESG评级
                            </h2>
                        </header>
                        <div id="charts">
                            
                            <div id="esg-total">
                                <ul id="esg-total-ul">
                                    <li>
                                        <h3 style="color: #45C2E0">E</h3>
                                        <p>{{E}}</p>
                                    </li>
                                    <li>
                                        <h3 style="color: #2F4554">S</h3>
                                        <p>{{S}}</p>
                                    </li>
                                    <li>
                                        <h3 style="color: #5A5476">G</h3>
                                        <p>{{G}}</p>
                                    </li>
                                </ul>
                            </div>
                            <div id="pie">
                                <!-- Pie Chart -->
                                <v-chart :options="pieChart" autoresize />
                            </div>
                        </div>
                        <div id="esg-detail">
                            <h3>ESG详情</h3>
                            <div id="esg-table">
                                <button @click="resetDateFilter" class="esg-table-btn">清除日期过滤器</button>
                                <button @click="clearFilter" class="esg-table-btn">清除所有过滤器</button>
                                <el-table
                                    ref="filterTable"
                                    :data="tableData"
                                    height="350"
                                    style="width: 100%"
                                    :header-cell-style="HeaderCellStyle"
                                    :cell-style="{'background-color':'#2F4554','color':'white'}">
                                    <el-table-column
                                    prop="pro"
                                    label="项目"
                                    width="180">
                                    </el-table-column>
                                    <el-table-column
                                    prop="val"
                                    label="值">
                                    </el-table-column>
                                    <el-table-column
                                    prop="tag"
                                    label="标签"
                                    width="100"
                                    :filters="[{ text: 'E', value: 'E' }, { text: 'S', value: 'S' }, { text: 'G', value: 'G' }]"
                                    :filter-method="filterTag"
                                    filter-placement="bottom-end">
                                    </el-table-column>
                                </el-table>
                            </div>
                        </div>
                    </section>
                    <section id="assess-sec">
                        <header>
                            <h2>
                                相关舆情
                            </h2>
                        </header>
                        <div id="assess">
                           <div id="coll-div">
                                <el-collapse v-model="activeNames" @change="handleChange" id="collap" :cell-style="{'background-color':'#2F4554','color':'white'}">
                                    <el-collapse-item title="一致性 Consistency" name="1" class="el-title" style="font-weight:bold;">
                                        <ul style="padding-top: 10px">
                                            <li>
                                                <a href="#" class="assess-a" style="color: rgb(4, 231, 235)">企业碳排放增长过多</a>
                                            </li>
                                            <li>
                                                <a href="#" class="assess-a" style="color: rgb(4, 231, 235)">企业碳排放量逐年递减</a>
                                            </li>
                                        </ul>
                                    </el-collapse-item>
                                    <el-collapse-item title="反馈 Feedback" name="2" class="el-title">
                                        <ul style="padding-top: 10px">
                                            <li>
                                                <a href="#" class="assess-a" style="color: rgb(4, 231, 235)">企业碳排放增长过多</a>
                                            </li>
                                            <li>
                                                <a href="#" class="assess-a" style="color: rgb(4, 231, 235)">企业碳排放量逐年递减</a>
                                            </li>
                                        </ul>
                                    </el-collapse-item>
                                    <el-collapse-item title="效率 Efficiency" name="3" class="el-title">
                                        <ul style="padding-top: 10px">
                                            <li>
                                                <a href="#" class="assess-a" style="color: rgb(4, 231, 235)">企业碳排放增长过多</a>
                                            </li>
                                            <li>
                                                <a href="#" class="assess-a" style="color: rgb(4, 231, 235)">企业碳排放量逐年递减</a>
                                            </li>
                                        </ul>
                                    </el-collapse-item>
                                </el-collapse>
                           </div>
                           <div>

                           </div>
                        </div>
                    </section>
                    <section id="buy-sec">
                        <header>
                            <h2>
                                近期股价
                            </h2>
                        </header>
                        <p>
                            <img :src=stock alt="">
                        </p>
                    </section>
                </section>
                
                <section>
                    <aside  id="detail">
                        <div>
                            <div>
                                <h2>企业详情</h2>
                            </div>
                            <div id="detail-ul">
                                <ul>
                                    <li v-for="(value,key) in detail_list" :key="key">
                                        <i>{{key}} : </i><span>{{value}}</span>
                                    </li>
                                    
                                        
                                </ul>
                            </div>
                        </div>
                    </aside>
                    <aside id="message">
                        <div>
                            <h2>企业资讯</h2>
                            <div id="message-ul">
                                <ul>
                                    <li v-for="(value,key) in message_list" :key="key">
                                        <a :href="value.url">{{value.content}}</a>
                                    </li>
                                    
                                </ul>
                            </div>
                            
                        </div>
                    </aside>
                    
                </section>

            </article>
        </section>
        <footer>
            <my-footer></my-footer>
        </footer>
        
    </div>
    
	<!-- //Slider -->
</template>

<script>
import NavBar from "../components/NavBar.vue"
import Footer from "../components/Footer.vue"
import FunctionBar from "../components/FunctionBar.vue"

import { pieChart } from "../assets/js/enterprise/data"
import { lineChart } from "../assets/js/enterprise/data"
import ECharts from "vue-echarts";
import "v-charts/lib/pie";

export default {
    data() {
        return {
            pieChart: pieChart,
            activeNames: ['1'],
            lineChart: lineChart,
            name: "ESG Ananysis Platform",
            detail_list: {
                "公司全称": "ESG Ananysis Platform",
                "注册日期": "2021-12-12",
                "注册资金": "1000万元",
            },
            message_list: {
                "国家": "#",
                "国家出台政策": "#",
                "国家出台": "#",
                "国家出台政策导致股市跳水": "#",
                "国家出台政策导致": "#",
                "国家出台政策导致股市": "#",
            },
            introduction:"墨刀是一款在线设计编辑原型的工具，特点短平快，适合一些APP，小型pc工程，以及一些频繁迭代的产品，\
                        优点协同办公效率比较高，目前国内个别大公司以及中小企业都有用到，个人版本免费，但是使用页面数量有限，\
                        编辑后产品都是保存直接保存在云上，很方便。",
            E: 0,
            S: 0,
            G: 0,
            E_history: [],
            S_history: [],
            G_history: [],
            stock: "http://image.sinajs.cn/newchart/daily/n/sh601006.gif",
            tableData:  [],
            followed: false
        };
    },
    components: { NavBar, "v-chart": ECharts, "my-footer": Footer, FunctionBar},
    mounted() {
        this.getData();
        
        // let hid = document.getElementById("nav-search")
        // hid.style.visibility = "hidden"

    },
    methods: {
        handleChange(val) {
            console.log(val);
        },

        getData() {
            const path = '/esgquery';
            this.$axios.post(path, {"name": this.name})
                .then((res) => {
                    if (res.data.state != "failed")
                    {
                        this.name = res.data.name;
                        this.detail_list = {
                            "公司名称": res.data.name,
                            "法人代表": res.data.legalrepresentative,
                            "统一社会信用代码": res.data.cc,
                            "电话": res.data.tel,
                            "官网": res.data.net,
                            "邮箱": res.data.email,
                            "地址": res.data.addr,
                            "简介": res.data.brief,
                        }
                        this.message_list = [
                            {"content":  res.data.msg1, "url":  res.data.msg1href},
                            {"content":  res.data.msg2, "url":  res.data.msg2href},
                            {"content":  res.data.msg3, "url":  res.data.msg3href},
                            {"content":  res.data.msg4, "url":  res.data.msg4href},
                            {"content":  res.data.msg5, "url":  res.data.msg5href},
                        ]
                        this.E = res.data.E;
                        this.S = res.data.S;
                        this.G = res.data.G;
                        console.log(this.E);
                        pieChart["series"][0].data = [
                            {value: this.E, name: 'E', itemStyle:{normal:{color:'#45C2E0'}}},
                            {value: this.S, name: 'S', itemStyle:{normal:{color:'#2F4554'}}},
                            {value: this.G, name: 'G', itemStyle:{normal:{color:'#5A5476'}}},].sort(function (a, b) { return a.value - b.value; }
                        );
                        this.E_history = res.data.E_history;
                        this.S_history = res.data.S_history;
                        this.G_history = res.data.G_history;
                        lineChart["series"][0].data = this.E_history;
                        lineChart["series"][1].data = this.S_history;
                        lineChart["series"][2].data = this.G_history;
                        
                        for (let i = 0; i < res.data.table_e.length; i++){
                            this.tableData.push({
                                pro: res.data.table_e[i].pro,
                                val: res.data.table_e[i].value,
                                tag: res.data.table_e[i].tag
                            })
                        }
                        for (let j = 0; j < res.data.table_s.length; j++){
                            this.tableData.push({
                                pro: res.data.table_s[j].pro,
                                val: res.data.table_s[j].value,
                                tag: res.data.table_s[j].tag
                            })
                        }
                        for (let k = 0; k < res.data.table_g.length; k++){
                            this.tableData.push({
                                pro: res.data.table_g[k].pro,
                                val: res.data.table_g[k].value,
                                tag: res.data.table_g[k].tag
                            })
                        }
                        console.log("E", this.E);
                        console.log("S", this.S);
                        console.log("G", this.G);
                    }
                    else{
                        this.$router.push({
                            path: "/404"
                        })
                    }
                    
                })
                .catch((error) => {
                    // eslint-disable-next-line
                    console.error(error);
                });
        },

        getfFollowed(){
            const path = '/getfollow';
            this.$axios.post(path, {"follower": 'zx', 'followed': '万达电影'})
                .then((res) => {
                    if (res.data.state == "success")
                    {
                        if(res.data.len > 0){
                            this.followed = true
                            console.log("yhtdyt")
                        }
                    }
                    else{
                        this.followed = false
                    }

                }
            ).catch((error) => {
                // eslint-disable-next-line
                console.error(error);
            });
        },

        resetDateFilter() {
            this.$refs.filterTable.clearFilter('date');
        },
        clearFilter() {
            this.$refs.filterTable.clearFilter();
        },
        formatter(row, column) {
            return row.address;
        },
        filterTag(value, row) {
            return row.tag === value;
        },
        filterHandler(value, row, column) {
            const property = column['property'];
            return row[property] === value;
        },
        HeaderCellStyle(row,column,rowIndex,columnIndex){
            return 'background-color:#61A0A8;font-size: 16px;margin-left:10px;color:white'
        }
    },
    created(){
        // pieChart["series"][0].data = [{value: 335, name: 'E'},
        //         {value: 301, name: 'S'},
        //         {value: 274, name: 'G'},].sort(function (a, b) { return a.value - b.value; })
        // this.name = this.$router.params.name
        this.name = this.$route.params.targetname
        this.getfFollowed();

    }
};
</script>

<style scoped>
@import "../assets/css/views/enterpriseindex/enterpriseindex.css";
/deep/ .el-collapse-item__header{
    font-weight: bold;
    font-size: 18px;
    background-color: rgb(80, 80, 80);
    padding-left: 20px;
    color: rgb(0, 0, 0);
}

/deep/ .el-collapse-item__content{
    background-color: rgb(139, 139, 139);
    margin: 0px;
    padding-left: 20px;
    color: darkturquoise;
}


/deep/ .el-collapse{
    background-color: rgb(109, 109, 109);
    
}
</style>