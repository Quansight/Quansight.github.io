---
author: Tony Fast
layout: post
modified_date: September 14, 2018
name: 2018-09-13-Making-a-computable-blog
path: _notebooks
---




```python
    def collect_last_input(stop=-1):
        try: return '\n'.join(In[-1].splitlines()[:stop])
        except: return 
```


```python
    import nbconvert, git, yaml, inspect
    from pathlib import Path
    _imports = collect_last_input(-2)
    config = Path('..', 'jupyter_nbconvert_config.py')
```


```python
    def author_from_repo(file, dir='.'):
        repo = git.Repo(dir)
        return repo.blame('HEAD~0', file)[0][0].author.name
```


```python
    class FrontMatters(nbconvert.exporters.MarkdownExporter):
        def from_notebook_node(self, nb, resources=None, **kw):
            nb, resources = super().from_notebook_node(nb, resources, **kw)
            md = dict(resources['metadata'])
            md['author'] = author_from_repo(Path(md['path'], f"{md['name']}.ipynb"))
            md['layout'] = 'post'
            return '---\n'.join((
                '', yaml.safe_dump(md, default_flow_style=False), nb
            )), resources
    _front_matter_source = collect_last_input()
```


```python
    collect_last_input() and config.write_text (F"""{_imports}

    {_front_matter_source}

    {inspect.getsource(author_from_repo)}
    try:
        c.NbConvertApp.export_format = f"jupyter_nbconvert_config.FrontMatters"
        c.FilesWriter.build_directory = "_posts"
    except: ...""");
```


```python
    def test_author():
        assert author_from_repo('_notebooks/2018-09-13-Making-a-computable-blog.ipynb', dir='..') == 'Tony Fast'
        
    def test_convert():
        from IPython import get_ipython
        import io
        !pushd .. && jupyter nbconvert _notebooks/2018-09-13-Making-a-computable-blog.ipynb
        post = Path('../_posts/2018-09-13-Making-a-computable-blog.md')
        assert post.exists()
        *_, fm, md = post.read_text().split('---', 2)
        assert isinstance(yaml.safe_load(io.StringIO(fm)), dict)
```


```python
    if __name__ == '__main__':
        !ipython -m pytest -- 2018-09-13-Making-a-computable-blog.ipynb
```
