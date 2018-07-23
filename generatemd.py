import json
import subprocess
import os, glob


class Bundle:
    def __init__(self, file):
        self._content = json.load(file)
        self._name = self._content['name']
        self._description = self._content['description']
        self._expanders = self._content['expanders']

    def to_md(self):
        out = ''
        out += f'# {self._name}\n\n'
        out += f'## {self._description}\n\n'
        for expander in self.__render_expanders():
            if expander is not None:
                out += expander + '\n\n'
        return out

    def __render_expanders(self):
        result = []
        for expander in self._expanders:
            expand = Expander(expander)
            result.append(expand.to_md())
        return result


class Expander:
    def __init__(self, dictionary):
        self.name = dictionary['name']
        self.description = dictionary['description']
        self.langs = dictionary['supported_languages']
        self.pattern = dictionary['pattern']
        self.output = dictionary['output_template']
        self.id = dictionary['identifier']

    def __render(self):
        possibles = self.description.split('\n')
        typer = self.langs[0]
        usable = []
        for string in possibles:
            try:
                if string[0] is '>':
                    string = string[1:]
                    script = "Application('TeaCode').expandAsJson('{text}', {{ 'extension': '{extension}' }})".format(
                        text=string,
                        extension=typer)
                    command = ["osascript", "-l", "JavaScript", "-e", script]
                    session = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                               universal_newlines=True)
                    stdout, stderr = session.communicate()
                    # print(stdout)
                    temp = json.loads(stdout)
                    usable.append(f'`{string}`' + '\n\n')
                    usable.append(f'```\n{temp["text"]}\n```')
                else:
                    if string is not '':
                        usable.append(f'> {string}')
            except IndexError:
                continue
        return usable

    def to_md(self):
        result = ''
        values = self.__render()
        result += f"### {self.name}\n\nDescription:\n\n"
        for string in values:
            result += string + '\n\n'
        result += f'Languages: {self.langs}\n\n'
        return result


if __name__ == '__main__':
    for file in glob.glob('*.tcbundle'):
        with open(file, 'r') as f:
            bundle = Bundle(f)
            with open(os.path.basename(file)[:-9] + '.md', 'w+') as out:
                out.write(bundle.to_md())
