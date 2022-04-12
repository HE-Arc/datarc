<template>
	<div
		class="bg-white cursor-pointer rounded-lg m-4 z-20"
		@click="openModal"
		@keydown.esc="closeModal"
		tabindex="0"
	>
		<div class="w-full h-full relative">
			<svg
				class="text-black"
				xmlns="http://www.w3.org/2000/svg"
				className="h-6 w-6"
				fill="none"
				viewBox="0 0 24 24"
				stroke="currentColor"
				strokeWidth="{2}"
			>
				<path
					strokeLinecap="round"
					strokeLinejoin="round"
					d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"
				/>
			</svg>

			<div
				class="absolute grid content-end top-3/4 h-1/4 w-full bg-surline-yellow bg-opacity-50 rounded-b-lg"
			>
				<div
					class="w-11/12 mx-auto text-black font-bold overflow-hidden overflow-ellipsis whitespace-nowrap"
				>
					{{ name }}
				</div>
			</div>
		</div>
	</div>
	<Modal
		:isShow="isSelected"
		@close-modal="closeModal"
		:name="name"
		:date="date"
		:author="author"
		:url="url"
		:ispublic="text"
	/>
</template>

<script>
	import Modal from "@/components/Modal";

	export default {
		props: {
			name: String,
			date: String,
			author: String,
			url: String,
			ispublic: Boolean,
		},
		created() {
			console.log(this.ispublic);
			this.text = this.ispublic == true ? "public" : "private";
		},
		data() {
			return {
				isSelected: false,
				text: "aa",
			};
		},
		components: {
			Modal,
		},
		methods: {
			openModal() {
				console.log(this);

				this.isSelected = true;
			},
			closeModal() {
				this.isSelected = false;
				this.$parent.updateData();
			},
			keyPressed: function (event) {
				if (this.isSelected) {
					console.log(event.key);
					if (
						event.key === "Escape" ||
						event.key === "Esc" ||
						event.keyCode === 27
					) {
						this.closeModal();
					}
				}
			},
		},
	};
</script>
<style></style>
