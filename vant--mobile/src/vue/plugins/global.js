/**
 * Created by root on 2017/12/27.
 **/
import api from './API'
import config from './config'
import rules from './rules'

import Vue from 'vue'
let Hub = new Vue();


global.GLOBAL = {
  api:api,
  config:config,
  hub: Hub,
  rules:rules,
}
