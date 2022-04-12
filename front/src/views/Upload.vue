<template>
	<div>Upload</div>
	<div class="w-32 h-32">
		<UploadWindow />
	</div>
</template>

<script>
	import UploadWindow from "../components/UploadWindow.vue";

	export default {
		name: "Upload",
		components: { UploadWindow },
		method: {},
	};
</script>
