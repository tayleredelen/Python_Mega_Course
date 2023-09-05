contents = ['blah blah blah',
            'whatever cheddar',
            'woah momma']

filenames = ['one.txt',
             'two.txt',
             'three.txt']

for content, filename in zip(contents, filenames):
    file = open(f"files/{filename}", 'w')
    file.write(content)