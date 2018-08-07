var Gantt_ = require("frappe-gantt").default;
var gantt;

window.change = function ($this) {
    gantt.hide_popup();
    gantt.change_view_mode($this.textContent);
}


document.addEventListener('DOMContentLoaded', function(){
 gantt = new Gantt_( document.querySelector("#gantt"), tasks);
 gantt.change_view_mode();
});

