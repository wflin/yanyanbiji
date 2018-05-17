const msgList = () => import(/* webpackChunkName: "mesList" */ '@/views/message/index.vue');
const eachMsg = () => import(/* webpackChunkName: "each" */ '@/views/message/each/');


const Tabbar = () => import(/* webpackChunkName: "Tabbar" */ '@/vue/components/Tabbar/');


export default [{
  path: "/message",
  name: "mesList",
  meta: {
    login: true
  },
  components: {default: msgList, tabbar: Tabbar }
},{
  path: "/message/eachMsg",
  name: "eachMsg",
  meta: {
    login: true
  },
  component: eachMsg
}]
