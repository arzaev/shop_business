function askQuestion() {
    var name = document.getElementById("nameForm").value;
    var email = document.getElementById("emailForm").value;
    var phone = document.getElementById("phoneForm").value;
    var message = document.getElementById("messageForm").value;

    var jsonText = JSON.stringify({'name': name, 'email': email, 'phone': phone, 'message': message});
    var csrf_token = document.getElementById('csrf').value;
    console.log(jsonText);
	$.ajax({
	  type: 'POST',
	  traditional: true,
	  headers: {'X-CSRFToken': csrf_token},
	  dataType: 'html',
	  data: jsonText,
	  url: '/question/',
	  success: function(data){
		alert("Ваше сообщение отправлено менеджеру и будет обработано в ближайшее время!");
		location.reload();
	  }
  })
}