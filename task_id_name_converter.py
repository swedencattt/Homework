def camel_to_snake(name):
	newname = []
	for i in name:
		if i.isapper():
			newname.append('_' + i.lower())
	return newname


def snake_to_camel(name):
	name = name.title().replace('_', '')
	return name

