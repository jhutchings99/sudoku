const app = new Vue({
    el: '#app',
    data: {
        board: [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
    },
    methods: {
        checkInput: function (event, rowIndex, columnIndex) {
            if (event.target.value > 9 || event.target.value < 1) {
                this.board[rowIndex][columnIndex] = 0;
            }
        },

        editCell: function (event, rowIndex, columnIndex) {
            this.board[rowIndex][columnIndex] = event.target.value;
        }
    }
});
