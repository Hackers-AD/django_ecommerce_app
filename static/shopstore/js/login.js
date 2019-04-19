function Register() {
	var name=document.getElementById('name');
	var np=document.getElementById('np');
	var rp=document.getElementById('rp');
	var info=document.getElementById('info');
    
    if (np.value.length<8) {
		info.style.color="crimson";
		info.innerHTML="* Password length must be 8 or greater."
		return false;
	}
	if (np.value!=rp.value) {
		info.style.color="crimson";
		info.innerHTML="* Password doesn't matched."
		return false;
	}
	if (!(/\S/.test(name.value)) || !(/\S/.test(np.value)) ) {
        return false;
    }
}