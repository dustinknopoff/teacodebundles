import glob
import json
import os
import subprocess


# Represents a TeaCode Bundle
class Bundle:
    def __init__(self, file):
        """
        Given a .tcbundle file, extract contents.
        :param file: A .tcbundle file.
        """
        self._content = json.load(file)
        self._name: str = self._content['name']
        self._description: str = self._content['description']
        self._expanders = self._content['expanders']

    def to_md(self) -> str:
        """
        Format this bundle for Markdown.
        :return: a markdown formatted string.
        """
        out = ''
        # H1 Header for Bundle name
        out += f'# {self._name}\n\n'
        # H2 header for description
        out += f'## {self._description}\n\n'
        # For every expander in this bundle
        for expander in self.__render_expanders():
            # If the expander is not empty, add formatted too
            if expander is not None:
                out += expander + '\n\n'
        return out

    def __render_expanders(self):
        """
        Convert this Bundle's list of expanders into Expander and convert to md.
        :return: List of markdown formatted Expanders.
        """
        result = []
        for expander in self._expanders:
            expand = Expander(expander)
            result.append(expand.to_md())
        return result


# Represents a TeaCode Expander
class Expander:
    def __init__(self, dictionary):
        self.name: str = dictionary['name']
        self.description: str = dictionary['description']
        self.langs = dictionary['supported_languages']
        self.pattern = dictionary['pattern']
        self.output = dictionary['output_template']
        self.id = dictionary['identifier']

    def __render(self):
        """
        Extract TeaCode expander from description, run and format to Markdown.
        :return: Markdown formatted description field including output of TeaCode expander.
        """
        # Split description on newline
        possibles = self.description.split('\n')
        # Get the first language this Expander works with
        typer = self.langs[0]
        usable = []
        # For all lines in description
        for string in possibles:
            try:
                # Check that it would show output in TeaCode
                if string[0] is '>':
                    # Remove '>' (means something different in md)
                    string = string[1:]
                    # Run TeaCode Expander and add output to string
                    script = "Application('TeaCode').expandAsJson('{text}', {{ 'extension': '{extension}' }})".format(
                        text=string,
                        extension=typer)
                    command = ["osascript", "-l", "JavaScript", "-e", script]
                    session = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                               universal_newlines=True)
                    stdout, stderr = session.communicate()
                    # print(stdout)
                    temp = json.loads(stdout)
                    # Format as code and code blocks
                    usable.append(f'`{string}`' + '\n\n')
                    usable.append(f'```{typer}\n{temp["text"]}\n```')
                else:
                    # If the line is not a expander example, make it a blockquote
                    if string is not '':
                        usable.append(f'> {string}')
            except IndexError:
                continue
        return usable

    def to_md(self):
        """
        Convert this Expander to a markdown formatted string.
        :return: markdown formatted string.
        """
        result = ''
        values = self.__render()
        result += f"### {self.name}\n\nDescription:\n\n"
        for string in values:
            result += string + '\n\n'
        result += f'Languages: {self.langs}\n\n'
        return result


if __name__ == '__main__':
    # For each .tcbundle file in this directory
    for file in glob.glob('*.tcbundle'):
        with open(file, 'r') as f:
            # Make into class Bundle
            bundle = Bundle(f)
            # Get the name and make a markdown file
            with open(os.path.basename(file)[:-9] + '.md', 'w+') as out:
                # Write formatted string to file
                out.write(bundle.to_md())
