const tab_user = () =>
  import(/* webpackChunkName: "tabbar-user" */ '@/views/user/tabbar-user')
const UserCollect = () =>
  import(/* webpackChunkName: "user-collect" */ '@/views/user/module-collect/')
const UserTeam = () =>
  import(/* webpackChunkName: "user-team" */ '@/views/user/module-team/index')
const queDetail = () =>
  import(/* webpackChunkName: "queDetail" */ '@/views/user/module-team/queDetail')
const UserInvitation = () =>
  import(/* webpackChunkName: "user-invitation" */ '@/views/user/module-invitation/')
const UserAddress = () =>
  import(/* webpackChunkName: "user-address" */ '@/views/user/module-address/')
const UserAddressEdit = () =>
  import(/* webpackChunkName: "user-addressEdit" */ '@/views/user/module-address-edit/')
const UserAutonymEdit = () =>
  import(/* webpackChunkName: "user-autonymEdit" */ '@/views/user/module-autonym-edit/')
const UserServer = () =>
  import(/* webpackChunkName: "user-server" */ '@/views/user/module-server/')

const UserInformation = () =>
  import(/* webpackChunkName: "user-information" */ '@/views/user/user-information-set/')
const UserInfo_SetBg = () =>
  import(/* webpackChunkName: "user-info-setBg" */ '@/views/user/user-information-set/set-bg/')
const UserInfo_SetPassword = () =>
  import(/* webpackChunkName: "user-info-setPassword" */ '@/views/user/user-information-set/set-password/')

const UserOrderEntityList = () =>
  import(/* webpackChunkName: "order-entity-list" */ '@/views/user/order-entity-list/')
const UserOrderEleList = () =>
  import(/* webpackChunkName: "order-ele-list" */ '@/views/user/order-ele-list/')
const UserRefundList = () =>
  import(/* webpackChunkName: "user-refund-list" */ '@/views/user/refund-list/')

const Tabbar = () =>
  import(/* webpackChunkName: "Tabbar" */ '@/vue/components/Tabbar/')

export default [
  {
    path: '/user',
    name: 'user',
    meta: {
      login: true
    },
    components: { default: tab_user, tabbar: Tabbar }
  },
  {
    path: '/user/collect',
    name: 'collect',
    component: UserCollect
  },
  {
    path: '/user/team',
    name: 'team',
    component: UserTeam
  },
  {
    path: '/user/invitation',
    name: 'invitation',
    component: UserInvitation
  },
  {
    path: '/user/queDetail',
    name: 'queDetail',
    component: queDetail
  },
  {
    path: '/user/address',
    name: 'address',
    component: UserAddress
  },
  {
    path: '/user/address/edit/:addressId',
    name: 'address-edit',
    props: true,
    component: UserAddressEdit
  },
  {
    path: '/user/autonym/edit',
    name: 'autonym-edit',
    component: UserAutonymEdit
  },
  {
    path: '/user/server',
    name: 'user-server',
    component: UserServer
  },
  {
    path: '/user/information',
    name: 'user-information',
    meta: {
      login: true
    },
    component: UserInformation
  },
  {
    path: '/user/information/setbg/:questionId',
    name: 'user-info-setbg',
    component: UserInfo_SetBg
  },
  {
    path: '/user/information/setPassword',
    name: 'user-info-setPassword',
    component: UserInfo_SetPassword
  },
  {
    path: '/user/order/list/:active',
    name: 'user-order-list',
    props: true,
    component: UserOrderEntityList
  },
  {
    path: '/user/orderEle/list/:active',
    name: 'user-order-ele-list',
    props: true,
    component: UserOrderEleList
  },
  {
    path: '/user/refund/list',
    name: 'user-refund-list',
    component: UserRefundList
  }
]
