function addCart() {
    var id_product = document.getElementById('idProduct').value;
    var count_product = document.getElementById('countProduct').value;
    var jsonText = JSON.stringify({'id_product': id_product, 'count_product': count_product});
    var csrf_token = document.getElementById('csrf').value;
    console.log(jsonText);
    console.log(csrf_token);
	$.ajax({
	  type: 'POST',
	  traditional: true,
	  headers: {'X-CSRFToken': csrf_token},
	  dataType: 'html',
	  data: jsonText,
	  url: '/add_product/',
	  success: function(data){
		location.reload();
	  }
  })
}

function removeCart(id_product) {
    var jsonText = JSON.stringify({'id_product': id_product});
    var csrf_token = document.getElementById('csrf').value;
    console.log(jsonText);
    console.log(csrf_token);
	$.ajax({
	  type: 'POST',
	  traditional: true,
	  headers: {'X-CSRFToken': csrf_token},
	  dataType: 'html',
	  data: jsonText,
	  url: '/remove_product/',
	  success: function(data){
		location.reload();
	  }
  })
}

function updateProductInCart(id_product, count_product) {
    var nc = "newCount" + id_product;
    var new_count = document.getElementById(nc).value;
    var jsonText = JSON.stringify({'id_product': id_product, 'count_product': count_product, 'new_count': new_count});
    var csrf_token = document.getElementById('csrf').value;
    console.log(jsonText);
    console.log(csrf_token);
	$.ajax({
	  type: 'POST',
	  traditional: true,
	  headers: {'X-CSRFToken': csrf_token},
	  dataType: 'html',
	  data: jsonText,
	  url: '/update_product/',
	  success: function(data){
		location.reload();
	  }
  })
}