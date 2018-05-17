<template>
	<div class="user_collect" v-waterfall-lower="loadMore" waterfall-disabled="disabled" waterfall-offset="100">
		<is-empty v-model="isEmpty">暂无商品收藏</is-empty>
	</div>
</template>

<script>
import IsEmpty from "@/vue/components/is-empty/";
import loadMore from '@/vue/mixin/load-more';

export default {

	mixins: [loadMore],

	data() {
		return {
			isEmpty: true
		}
	},

	components: {
		[IsEmpty.name]: IsEmpty,
	}
}

</script>

<style lang="scss" scoped>
@import '../../../assets/scss/var';
.clear_invalid {
  width: 120px;
  color: $font-color-gray;
  border: 1px solid $font-color-gray;
  margin: 0 auto;
  text-align: center;
  padding: 5px 3px;
  margin-top: 20px;
  border-radius: 3px;
}
</style>
