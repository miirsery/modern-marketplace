<template>
    <svg class="c-icon"
      :class="iconClass"
      :width="width"
      :height="height"
      aria-hidden="true">
        <use xmlns:xlink="http://www.w3.org/1999/xlink" :xlink:href="href"></use>
    </svg>
</template>

<script>
    export default {
        name: 'Icon',

        props: {
            name: {
                type: String,
                required: true
            },
            width: {
                type: [Number, String]
            },
            height: {
                type: [Number, String]
            }
        },

        computed: {
            href() {
                return `#${this.name}`;
            },

            iconClass() {
                return `c-icon--${this.name}`;
            }
        }
    };
</script>