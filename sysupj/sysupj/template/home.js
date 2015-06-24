$(document).ready( function(){
	$("#commentForm").hide();
	$("#uploadForm").hide();
	
	$("#commentBtn").click(function(){
		$("#commentForm").show();
		$(this).hide();
	});
	
	$("#uploadBtn").click(function(){
		$("#uploadForm").show();
		$(this).hide();
	});
	
	$("#submitBtn").click(function(){
		console.log($('#commentArea').val());
		$.ajax({
			type:"POST" ,
			url:"/addComment/",
			data:"content=" + $('#commentArea').val(),
            dataType:"json",
			success: function(result){
				if(result == "no login") {
					window.location.href="/login/";
				}
				else {
					var content = result.content;
					var username = result.username;
					$("#commentForm").hide();
					$("#commentBtn").show();
					var newDiv = document.createElement("div");
					newDiv.className = "comment"; 
					newDiv.id = "comment";
					var newIcon = document.createElement("img");
					newIcon.className = "icon";
					newIcon.src= "http://sysupj-pic.stor.sinaapp.com/pic4.jpg";
					var newContent = document.createElement("div");
					newContent.className = "content";
					newContent.innerHTML = "<span>"+username+"</span>"+":"+"<span>"+content+"</span>";
					var newOp = document.createElement("div");
					newOp.className = "operation";
					newOp.innerHTML = "<span>"+"2015-XX-XX"+"</span>"+" <span>"+"回复"+"</span>"+" <span>"+"评论"+"</span>"+" <span>"+"关于我的"+"</span>";
					newDiv.appendChild(newIcon);
					newDiv.appendChild(newContent);
					newDiv.appendChild(newOp);
					var comments = document.getElementById("comments");
					var comment = document.getElementById("comment");
					comments.insertBefore(newDiv,comment);
				}
			}
		})
	});
});