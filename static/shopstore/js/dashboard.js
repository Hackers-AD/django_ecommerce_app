
function PurchaseItem() {
	var name=document.getElementsByTagName('body');
	var purchase=document.getElementById('purchase');
	var bodyheight=document.body.scrollHeight;
	var windowheight=window.scrollY;
	var cursor=event.clientY;

    name[0].style.overflow="hidden";
	purchase.style.top=windowheight+"px";
	purchase.style.display="block";
}
function ClosePurchase() {
	var name=document.getElementsByTagName('body');
	var purchase=document.getElementById('purchase');

	name[0].style.overflow="scroll";
	purchase.style.display="none";
}