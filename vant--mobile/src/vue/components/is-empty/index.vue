<template>
	<div class="is_empty" v-show="value">
		<div>
			<img src="../../../assets/images/is_empty.png" alt="无商品" width="20%">
		</div>
		<div>
			<slot></slot>
		</div>
	</div>
</template>

<script>
	export default {
		name: "is-empty",
		props: {value: Boolean}
	}
</script>


<style lang="scss" scoped>
	@import "../../../assets/scss/var";
	.is_empty{
		text-align: center;
		color: $font-color-gray;
		padding-top: 100px;
		>div{
			margin-bottom: 20px;
		}
    img{
      margin:0 auto;
    }
	}
</style>
