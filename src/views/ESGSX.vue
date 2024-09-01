<template>
  <div id="enterprise">
    <header>
      <div id="nav">
        <nav-bar>
        </nav-bar>
        
      </div>

    </header>
    <!-- 内容 -->
    <el-row class="mains">
      <el-col :span="5">
        <div style="opacity: 0;">1</div>
      </el-col>
      <el-col :span="12">
        <div style="width: 100%;">
          <el-carousel height="350px">
                <el-carousel-item v-for="(v,i) in banner" :key="i">
                  <img style="width: 100%;" :src='v.img'>
                </el-carousel-item>
              </el-carousel>
        </div>
        <div class="flex zhongbu" style="padding: 20px 0;">
          <!-- <div class="flex align_center">
            <span>成立年份：</span>
            <el-date-picker v-model="value1" type="datetimerange" range-separator="至" start-placeholder="开始日期"
              end-placeholder="结束日期">
            </el-date-picker>
          </div> -->
          <div class="flex align_center">
            <span>ESG评级：</span>
            <el-select v-model="pingji" placeholder="请选择">
              <el-option v-for="item in pingjiList" :key="item.value" :label="item.label" :value="item.value">
              </el-option>
            </el-select>
          </div>
          <div class="flex align_center" style="margin-left: 50px;">
            <span>行业：</span>
            <el-select v-model="hangye" placeholder="请选择">
              <el-option v-for="item in hangyeList" :key="item.value" :label="item.label" :value="item.value">
              </el-option>
            </el-select>
          </div>
        </div>
        <!-- 列表 -->
        <div class="zhongbu" style="padding-top: 20px;">
          <div class="flex align_center align_center">
            <span style="margin-right: 10px;">E：</span>
            <el-radio class="flex align_center" v-model="radio" label="x">能源与气候变化</el-radio>
             <el-radio class="flex align_center" v-model="radio" label="1">原材料与废弃物</el-radio>
              <el-radio class="flex align_center" v-model="radio" label="2">废水</el-radio>
                <!-- <el-radio class="flex align_center" v-model="radio" label="3">环保清洁</el-radio>
                <el-radio class="flex align_center" v-model="radio" label="4">环保处罚和突发环境事件</el-radio>
                <el-radio class="flex align_center" v-model="radio" label="5">测试数据</el-radio> -->
          </div>
          <div class="flex align_center align_center" style="padding: 10px 0;">
            <span style="margin-right: 10px;">S：</span>
            <el-radio class="flex align_center" v-model="radio" label="q">雇佣</el-radio>
              <el-radio class="flex align_center" v-model="radio" label="w">职业健康与安全生产</el-radio>
              <el-radio class="flex align_center" v-model="radio" label="e">产品质量</el-radio>
                <el-radio class="flex align_center" v-model="radio" label="r">发展与培训</el-radio>
                <el-radio class="flex align_center" v-model="radio" label="t">研发与创新</el-radio>
                <el-radio class="flex align_center" v-model="radio" label="y">供应链</el-radio>
                  <el-radio class="flex align_center" v-model="radio" label="u">信息安全与隐私保护</el-radio>
                  <el-radio class="flex align_center" v-model="radio" label="i">客户</el-radio>
          </div>
          <div class="flex align_center align_center">
            <span style="margin-right: 10px;">G：</span>
            <el-radio class="flex align_center" v-model="radio" label="a">公司治理</el-radio>
             <el-radio class="flex align_center" v-model="radio" label="b">商业道德</el-radio>
              <!-- <el-radio class="flex align_center" v-model="radio" label="s">环境污染</el-radio>
              <el-radio class="flex align_center" v-model="radio" label="d">风险管理</el-radio> -->
          </div>
          <div>
            <el-table :data="tableData" style="width: 100%" :default-sort="{prop: 'date', order: 'descending'}">
              <el-table-column prop="xuhao" label="序号" sortable width="180">
              </el-table-column>
              <el-table-column prop="title" label="名称">
              </el-table-column>
              <el-table-column prop="type" label="所属行业">
              </el-table-column>
              <el-table-column prop="level" label="ESG评级">
              </el-table-column>
            </el-table>
          </div>
        </div>
      </el-col>
    </el-row>
    <my-footer></my-footer>
  </div>
</template>

<script>
  import NavBar from "../components/NavBar.vue"
  import SearchBox from "../components/SearchBox.vue"
  import Footer from "../components/Footer.vue"
  import {
    pieChart
  } from "../assets/js/enterprise/data"
  import {
    lineChart
  } from "../assets/js/enterprise/data"
  import ECharts from "vue-echarts";
  import "v-charts/lib/pie";

  export default {
    data() {
      return {
        radio:'x',
        banner:[
          {
            img:require('../assets/images/img/news-1.jpg')
          },
          {
            img:require('../assets/images/img/news-2.jpg')
          },
          {
            img:require('../assets/images/img/news-3.jpg')
          }
        ],
        tableData: [{
          xuhao: '1',
          title: '移城房产',
          type: '房地产',
          level: 'AAA'
        },{
          xuhao: '2',
          title: '移城房产',
          type: '房地产',
          level: 'AAA'
        },{
          xuhao: '3',
          title: '移城房产',
          type: '房地产',
          level: 'AAA'
        },{
          xuhao: '4',
          title: '移城房产',
          type: '房地产',
          level: 'BB '
        }],
        pingjiList: [{
            value: 'all',
            label: '全部'
          }, {
            value: 'AAA',
            label: 'AAA'
          }, {
            value: 'AA',
            label: 'AA'
          }, {
            value: 'A',
            label: 'A'
          }, {
            value: 'BBB',
            label: 'BBB'
          },
          {
            value: 'BB',
            label: 'BB'
          },
          {
            value: 'B',
            label: 'B'
          },
          {
            value: 'C',
            label: 'C'
          }
        ],
        hangyeList: [{
          value: '选项1',
          label: '工业'
        }, {
          value: '选项2',
          label: '材料'
        }, {
          value: '选项3',
          label: '医疗保健'
        }, {
          value: '选项4',
          label: '金融'
        }, {
          value: '选项5',
          label: '房地产'
        }],
        pingji: 'all',
        hangye: '',
        value1: [new Date(2000, 10, 10, 10, 10), new Date(2000, 10, 11, 10, 10)],
        pieChart: pieChart,
        lineChart: lineChart,
      };
    },
    components: {
      NavBar,
      "my-footer": Footer
    },
    mounted() {

    },
    methods: {
      formatter(row, column) {
        return row.address;
      },
      route(name){
        this.$router.push({
            path:'/tuijian',
            query:{
                entername: inputted,
            }
            // path:'/tuijian',

        })
      }
    }
  };
</script>

<style scoped>
  .mains {
    padding: 40px;
    min-height: 500px;
  }

  .zhongbu {
    /* padding-left: 40px; */
  }

  #nav{
    
  }

  #searchbox{
    
  }
</style>
