<template>
    <div>
        <div v-for="order in orders" :key="order.orderdate">
            <div>
                <span>Mã Đơn :</span> <span>{{order.orderid}}</span>
                <span>Địa Chỉ :</span><span>{{order.orderaddress}}</span>
                <span>Ngày đặt :</span><span>{{order.orderdate}}</span>
                <span>Tổng Tiền đơn hàng :</span><span>{{order.total}}</span>
                <span v-if="order.orderstatus ==='pending'">Trạng thái đơn hàng : Đang chờ xử lí</span>
                <span v-else-if="order.orderstatus ==='confirmed'">Trạng thái đơn hàng : Đã Xác Nhận</span>
                <span v-else-if="order.orderstatus ==='done'">Trạng thái đơn hàng : Đã Hoàn Tất</span>
                <span v-else>Trạng thái đơn hàng : Đã Hủy</span>
                <button v-if="order.orderstatus ==='pending'" type="button" @click="cancelorder(order.orderid)">Hủy đơn</button>
            </div>
            <div v-for="detail in order.details" :key="detail.productname">
                {{detail}}
                <span>{{detail.productname}}</span>
                <img :src="detail.img">
                <span>{{detail.quantity}}</span>
                <span>{{detail.price}}</span>
            </div>
        </div>
    </div>
</template>
<script>

export default {
    async asyncData({ $axios}){
        const orders = await $axios.$get('/userorders/')
        return {orders}
    },
    methods: {
        async cancelorder(id){
            const response= await this.$axios.$post('/userorders/',{
                orderid: id,
            })
            console.log(response)
        }
    }
}
</script>
