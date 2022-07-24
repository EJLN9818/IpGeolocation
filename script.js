const $ = selector => document.querySelector(selector);

const OPTIONS = {
	method: 'GET',
	headers: {
		'X-RapidAPI-Key': 'c77531be5dmsh8192cafd6775cd7p14fea0jsnc0784ab75f08',
		'X-RapidAPI-Host': 'ip-geolocation-and-threat-detection.p.rapidapi.com'
	}
};

const fetchIpInfo = ip => {
	return fetch(`https://ip-geolocation-and-threat-detection.p.rapidapi.com/${ip}`, OPTIONS)
	.then(response => response.json())
	.catch(err => console.error(err));
};

const $form = $('#form');
const $input = $('#input');	
const $submit = $('#submit');
const $results = $('#results');

const validateIp = ip => {
	const regex = /^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/;
	return regex.test(ip);
}

const setInvalidClass = () => {
	$input.setAttribute('aria-invalid', 'true');
	$input.setAttribute('aria-invalid', 'true');
	$submit.removeAttribute('disabled');
	$submit.removeAttribute('aria-busy');
}


$form.addEventListener('submit', async (event) => {
	event.preventDefault();
	const { value } = $input;
	if (!value) {
		setInvalidClass();
		$results.innerHTML = 'Por favor, inserta una dirección IP.';
		return;
	}
	
	$submit.setAttribute('disabled', '');
	$submit.setAttribute('aria-busy', 'true');

	if (!validateIp(value)) {
		setInvalidClass();
		$results.innerHTML = 'Por favor, inserta una dirección IP válida.';
		return;
	}

	const ipInfo = await fetchIpInfo(value);
	console.log(ipInfo);
	if (ipInfo) {
		$results.innerHTML = JSON.stringify(ipInfo, null, 2);
		$input.setAttribute('aria-invalid', 'false');
	}

	setInvalidClass();
});
