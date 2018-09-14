import nbconvert, git, yaml, inspect; from pathlib import Path

class FrontMatters(nbconvert.exporters.MarkdownExporter):
    def from_notebook_node(self, nb, resources=None, **kw):
        nb, resources = super().from_notebook_node(nb, resources, **kw)
        md = dict(resources['metadata'])
        md['author'] = author_from_repo(Path(md['path'], f"{md['name']}.ipynb"))
        md['layout'] = 'post'
        return '---\n'.join((
            '', yaml.safe_dump(md, default_flow_style=False), nb)), resources

def author_from_repo(file, dir='.'):
    repo = git.Repo(dir)
    return repo.blame('HEAD~0', file)[0][0].author.name

try:
    c.NbConvertApp.export_format = f"jupyter_nbconvert_config.FrontMatters"
    c.FilesWriter.build_directory = "_posts"
except: ...