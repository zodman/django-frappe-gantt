var Gantt_ = require("frappe-gantt").default;
var gantt;


toggle_class = function($this){
// toggle class
    var elemtns = document.querySelectorAll(".change")
    for(i=0; i<elemtns.length; i++){
    	elemtns[i].classList.remove("is-active")
    }
    
    $this.parentNode.classList.add("is-active")

}

window.change = function ($this) {
	//$this.preventDefault();
    gantt.hide_popup();
    gantt.change_view_mode($this.textContent);
	toggle_class($this);

}


document.addEventListener('DOMContentLoaded', function(){
 gantt = new Gantt_( document.querySelector("#gantt"), tasks);
 gantt.change_view_mode();
 var e = document.querySelector(".change a")
 toggle_class(e);
});


