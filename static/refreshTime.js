function refreshTime() {
  $.ajax({
    url: '{% url time %}',
    success: function (data) {
      console.log("success function called");
      $('#test').html(data);
    }
  });
}


$( document ).ready(function () {
  console.log("setting interval");
      setTimeout(refreshTime,1000);
});