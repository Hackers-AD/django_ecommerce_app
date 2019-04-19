function CheckUserAuth(argument) {
	var decision;

	if (argument!="True") {
		decision=window.confirm("You must login to make transactions.\n\nProceed ?");
		if (decision) {
			window.open('/accounts/login/','_self');
		}
		return false;
	}
	return true;
}
function BuyItem(argument) {
	var name=document.getElementsByTagName('body');
	var purchase=document.getElementById('purchase');
	var bodyheight=document.body.scrollHeight;
	var windowheight=window.scrollY;
	var cursor=event.clientY;

	if (argument!="True") {
		
	}
	else{
		name[0].style.overflow="hidden";
	    purchase.style.top=windowheight+"px";
	    purchase.style.display="block";
	}
}
function CloseBuy() {
	var name=document.getElementsByTagName('body');
	var purchase=document.getElementById('purchase');

	name[0].style.overflow="scroll";
	purchase.style.display="none";
}