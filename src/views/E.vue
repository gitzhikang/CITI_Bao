<template>
    <div id="E">
        <header>
            <nav-bar></nav-bar>
        </header>
        <section>
            <article>
                <v-chart :options="lineChart" autoresize />
            </article>
        </section>
        <footer>
            <my-footer></my-footer>
        </footer>
    </div>
</template>

<script>
import ECharts from "vue-echarts";
import "v-charts/lib/pie";

export default {
    
}
</script>