---
author: Tony Fast
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
    import nbconvert, git, yaml, inspect, yaml
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
    except: ...""")
```




    755




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

    <IPython.core.display.HTML object>
    ============================= test session starts =============================
    platform win32 -- Python 3.6.6, pytest-3.5.1, py-1.5.3, pluggy-0.6.0
    Matplotlib: 2.2.2
    Freetype: 2.8.1
    rootdir: C:\Users\deathbeds\Quansight.github.io\_notebooks, inifile:
    plugins: xdist-1.22.5, testmon-0.9.12, remotedata-0.2.1, parallel-0.0.2, openfiles-0.3.0, mpl-0.9, localserver-0.4.1, forked-0.2, doctestplus-0.1.3, arraydiff-0.2, hypothesis-3.66.16, importnb-0.5.0
    collected 2 items
    
    2018-09-13-Making-a-computable-blog.ipynb ..                             [100%]
    
    ========================== 2 passed in 3.39 seconds ===========================



```python

```


```python

```
