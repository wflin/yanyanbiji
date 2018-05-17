const tab_cart = () =>
  import(/* webpackChunkName: "tabbar-cart" */ '@/views/order/tabbar-cart.vue')
const PlaceOrderEntity = () =>
  import(/* webpackChunkName: "placerder-entity" */ '@/views/order/place-order-entity/')
const Payment = () =>
  import(/* webpackChunkName: "payment" */ '@/views/order/payment/')
const PaymentStatus = () =>
  import(/* webpackChunkName: "payment-status" */ '@/views/order/payment-status/')

const Tabbar = () =>
  import(/* webpackChunkName: "Tabbar" */ '@/vue/components/Tabbar/')

export default [
  {
    path: '/order',
    name: 'cart',
    meta: {
      login: true
    },
    components: { default: tab_cart, tabbar: Tabbar }
  },
  {
    path: '/order/placeOrderEntity',
    name: 'placeOrderEntity',
    component: PlaceOrderEntity
  },
  {
    path: '/order/payment',
    name: 'payment',
    component: Payment
  },
  {
    path: '/order/payment/:status',
    name: 'paymentStatus',
    component: PaymentStatus,
    props: true
  }
]
