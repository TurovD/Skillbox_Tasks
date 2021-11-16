site = {
	'html': {
		'head': {
			'title': 'Мой сайт'
		},
		'body': {
			'h2': 'Здесь будет мой заголовок',
			'div': 'Тут, наверное, какой-то блок',
			'p': 'А вот здесь новый абзац'
		}
	}
}

def find_key(text, key, deep):
    if key in text:
        return text[key]
    if deep > 1:
        for sub_struct in text.values():
            if isinstance(sub_struct, dict):
                result = find_key(sub_struct, key, deep - 1)
                if result:
                    break
        else:
            result = None
        return result

print(find_key(site, 'p',1))