<script>
import Layout from "../../layouts/main";
import PageHeader from "@/components/page-header";

/**
 * Orders Component
 */
export default {
  components: {
    Layout,
    PageHeader
  },
  data() {
    return {
      title: "Orders",
      items: [
        {
          text: "Ecommerce"
        },
        {
          text: "Orders",
          active: true
        }
      ],
      ordersData: [
        {
          orderid: "#NZ1563",
          date: "28 Mar, 2020",
          escore: {
            score:15,
            state:50
          },
          total: {
            score:100,
            state:50
          },
          enstatus: "Great",
          gscore:{
            score:15,
            state:50
          },
          sscore:{
            score:15,
            state:50
          }
        },
        {
          orderid: "#NZ1564",
          date: "28 Mar, 2020",
          escore: {
            score:15,
            state:50
          },
          total: {
            score:100,
            state:50
          },
          enstatus: "Great",
          gscore:{
            score:15,
            state:50
          },
          sscore:{
            score:15,
            state:50
          }
        },
        {
          orderid: "#NZ1565",
          date: "29 Mar, 2020",
          escore: {
            score:15,
            state:50
          },
          total: {
            score:100,
            state:50
          },
          enstatus: "Great",
          gscore:{
            score:15,
            state:50
          },
          sscore:{
            score:15,
            state:50
          }
        },
        {
          orderid: "#NZ1566",
          date: "30 Mar, 2020",
          escore: {
            score:15,
            state:50
          },
          total: {
            score:100,
            state:50
          },
          enstatus: "Great",
          gscore:{
            score:15,
            state:50
          },
          sscore:{
            score:15,
            state:50
          }
        },
        {
          orderid: "#NZ1567",
          date: "31 Mar, 2020",
          escore: {
            score:15,
            state:50
          },
          total: {
            score:100,
            state:50
          },
          enstatus: "Great",
          gscore:{
            score:15,
            state:50
          },
          sscore:{
            score:15,
            state:50
          }
        },
        {
          orderid: "#NZ1568",
          date: "01 Apr, 2020",
          escore: {
            score:15,
            state:50
          },
          total: {
            score:100,
            state:50
          },
          enstatus: "Great",
          gscore:{
            score:15,
            state:50
          },
          sscore:{
            score:15,
            state:50
          }
        },
        {
          orderid: "#NZ1569",
          date: "02 Apr, 2020",
          escore: {
            score:15,
            state:5
          },
          total: {
            score:100,
            state:50
          },
          enstatus: "Great",
          gscore:{
            score:15,
            state:50
          },
          sscore:{
            score:15,
            state:50
          }
        },
        {
          orderid: "#NZ1570",
          date: "03 Apr, 2020",
          escore: {
            score:15,
            state:50
          },
          total: {
            score:100,
            state:50
          },
          enstatus: "Great",
          gscore:{
            score:15,
            state:50
          },
          sscore:{
            score:15,
            state:50
          }
        },
        {
          orderid: "#NZ1571",
          date: "03 Apr, 2020",
          escore: {
            score:15,
            state:50
          },
          total: {
            score:100,
            state:50
          },
          enstatus: "Great",
          gscore:{
            score:15,
            state:50
          },
          sscore:{
            score:15,
            state:50
          }
        },
        {
          orderid: "#NZ1572",
          date: "04 Apr, 2020",
          escore: {
            score:15,
            state:50
          },
          total: {
            score:100,
            state:50
          },
          enstatus: "Great",
          gscore:{
            score:15,
            state:50
          },
          sscore:{
            score:15,
            state:50
          }
        },
        {
          orderid: "#NZ1573",
          date: "06 Apr, 2020",
          escore: {
            score:5,
            state:5
          },
          total: {
            score:100,
            state:50
          },
          enstatus: "Great",
          gscore:{
            score:15,
            state:50
          },
          sscore:{
            score:15,
            state:50
          }
        }
      ],
      totalRows: 1,
      currentPage: 1,
      perPage: 10,
      pageOptions: [10, 25, 50, 100],
      filter: null,
      filterOn: [],
      sortBy: "orderid",
      sortDesc: false,
      fields: [
        { key: "orderid", sortable: true, label: "公司编号" },
        { key: "date", sortable: true ,label: "关注日期"},
        { key: "escore", sortable: true, label: "环境得分" },
        { key: "sscore", sortable: true, label: "社会得分" },
        { key: "gscore", sortable: true, label: "公司治理得分" },
        { key: "total", sortable: true, label: "总分" },
        { key: "enstatus", sortable: true, label: "公司现状" },
        { key: "action" }
      ]
    };
  },
  computed: {
    /**
     * Total no. of records
     */
    rows() {
      return this.ordersData.length;
    }
  },
  mounted() {
    // Set the initial number of items
    this.totalRows = this.ordersData.length;
  },
  methods: {
    /**
     * Search the table data with search input
     */
    onFiltered(filteredItems) {
      // Trigger pagination to update the number of buttons/pages due to filtering
      this.totalRows = filteredItems.length;
      this.currentPage = 1;
    },
    toCertainEn(value){
      this.$router.push({
        name:"enterpriseindex",
        params:{
          targetname:value
        }
      })
    },
    deleteEn(id){
      for(var i = 0; i < this.ordersData.length; i++){
        if(this.ordersData[i].orderid === id){
          console.log(id);
          return;
        }
      }
    }
  }
};
</script>

<template>
  <Layout>
    <PageHeader :title="title" :items="items" />
    <div class="row">
      <div class="col-lg-12">
        <div class="card">
          <div class="card-body pt-0">
            <b-tabs nav-class="nav-tabs-custom">
              <b-tab title-link-class="p-3">
                <template v-slot:title>
                  <a class="font-weight-bold active">我的关注</a>
                </template>
                <div class="row mt-4">
                  <div class="col-sm-12 col-md-6">
                    <div id="tickets-table_length" class="dataTables_length">
                      <label class="d-inline-flex align-items-center">
                        Show&nbsp;
                        <b-form-select v-model="perPage" size="sm" :options="pageOptions"></b-form-select>&nbsp;entries
                      </label>
                    </div>
                  </div>
                  <!-- Search -->
                  <div class="col-sm-12 col-md-6">
                    <div id="tickets-table_filter" class="dataTables_filter text-md-right">
                      <label class="d-inline-flex align-items-center">
                        Search:
                        <b-form-input
                            v-model="filter"
                            type="search"
                            class="form-control form-control-sm ml-2"
                        ></b-form-input>
                      </label>
                    </div>
                  </div>
                  <!-- End search -->
                </div>
                <div class="table-responsive">
                  <b-table
                      class="table-centered"
                      :items="ordersData"
                      :fields="fields"
                      responsive="sm"
                      :per-page="perPage"
                      :current-page="currentPage"
                      :sort-by.sync="sortBy"
                      :sort-desc.sync="sortDesc"
                      :filter="filter"
                      :filter-included-fields="filterOn"
                      @filtered="onFiltered"
                  >
                    <template v-slot:cell(escore)="row">
                      <span class="mr-3">{{ row.value.score}}</span>
                      <div
                          class="badge font-size-12"
                          :class="{'badge-soft-danger': `${row.value.state}` >= 10,
                            'badge-soft-success': `${row.value.state}` <= -10,
                            'badge-soft-warning': `${row.value.state}` > -10 && `${row.value.state}`< 10 }"
                      >{{ row.value.state}}%</div>
                    </template>
                    <template v-slot:cell(sscore)="row">
                      <span class="mr-3">{{ row.value.score}}</span>
                      <div
                          class="badge font-size-12"
                          :class="{'badge-soft-danger': `${row.value.state}` >= 10,
                            'badge-soft-success': `${row.value.state}` <= -10,
                            'badge-soft-warning': `${row.value.state}` > -10 && `${row.value.state}`< 10 }"
                      >{{ row.value.state}}%</div>
                    </template>
                    <template v-slot:cell(gscore)="row">
                      <span class="mr-3">{{ row.value.score}}</span>
                      <div
                          class="badge font-size-12"
                          :class="{'badge-soft-danger': `${row.value.state}` >= 10,
                            'badge-soft-success': `${row.value.state}` <= -10,
                            'badge-soft-warning': `${row.value.state}` > -10 && `${row.value.state}`< 10 }"
                      >{{ row.value.state}}%</div>
                    </template>
                    <template v-slot:cell(total)="row">
                      <span class="mr-3">{{ row.value.score}}</span>
                      <div
                          class="badge font-size-12"
                          :class="{'badge-soft-danger': `${row.value.state}` >= 10,
                            'badge-soft-success': `${row.value.state}` <= -10,
                            'badge-soft-warning': `${row.value.state}` > -10 && `${row.value.state}`< 10 }"
                      >{{ row.value.state}}%</div>
                    </template>
                    <template v-slot:cell(enstatus)="row">
                      <div
                          class="badge font-size-12"
                          :class="{'badge-soft-danger': `${row.value}` === 'Danger',
                            'badge-soft-success': `${row.value}` === 'Great',
                            'badge-soft-warning': `${row.value}` === 'Average'}"
                      >{{ row.value}}</div>
                    </template>
                    <template v-slot:cell(action)="row">
                      <a
                          href="javascript:void(0);"
                          class="mr-3 text-primary"
                          v-b-tooltip.hover
                          @click="toCertainEn(row.item.orderid)"
                      >

                        <i class="el-icon-view font-size-18"></i>
                      </a>
                      <a
                          href="javascript:void(0);"
                          class="text-danger"
                          v-b-tooltip.hover
                          @click="deleteEn(row.item.orderid)"
                      >
                        <i class="mdi mdi-trash-can font-size-18"></i>
                      </a>
                    </template>
                  </b-table>
                </div>
                <div class="row">
                  <div class="col">
                    <div class="dataTables_paginate paging_simple_numbers float-right">
                      <ul class="pagination pagination-rounded mb-0">
                        <!-- pagination -->
                        <b-pagination v-model="currentPage" :total-rows="rows" :per-page="perPage"></b-pagination>
                      </ul>
                    </div>
                  </div>
                </div>
              </b-tab>
            </b-tabs>
          </div>
        </div>
      </div>
    </div>
  </Layout>
</template>