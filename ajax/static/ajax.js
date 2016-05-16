
// console.log("value of csrfmiddlewaretoken is" + );


$('#post_submit').on('submit',function(event) {
	event.preventDefault();
	console.log("Working fine.");

	// start ajax

	$.ajax({


// using this for csrf handling




		// alert(" i am in ajax");
		// console.log(" iam ");
		url : "/apply/",
		type : "POST",
		data : 
		{
			csrfmiddlewaretoken:document.getElementsByName('csrfmiddlewaretoken')[0].value,
			name : $('#id_name').val(),
			email : $('#id_email').val(),
			password : $('#id_password').val(),
			repeat_password : $('#id_repeat_password').val(),
		},
		success: function(json) {
			alert("Congratulations! You scored: " + json['errors'][0]);

		},

		// error




	})

	
});
