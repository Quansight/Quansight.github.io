---
author: tonyfast
layout: post
modified_date: September 14, 2018
name: 2018-09-14-Computable-posts-from-quansight
path: _notebooks
---

At [Quansight](https://www.quansight.com/), we frequently use [Jupyter notebooks](jupyter.org) to communicate our on going contributions to [sustainable open source software](https://www.quansight.com/sos-partnership).  We thought it would be appropriate to compose blog posts with notebooks so they may be read as blog posts with [Jekyll](https://jekyllrb.com) and reused as demos on [Binder](https://mybinder.org/).

## Convert and deploy notebooks

In this notebook, we will build the tools required to convert a notebook to a valid [Jekyll post](https://jekyllrb.com/docs/posts/).  This process requires:
    
1. Converting notebooks to markdown with [`nbconvert`](http://nbconvert.readthedocs.io/).
2. Prepending [yaml front matter](https://jekyllrb.com/docs/front-matter/) to the markdown.
3. Setting up the [Travis Pages Deployment](https://docs.travis-ci.com/user/deployment/pages/).

`collect_last_input` is a utility to function to extract pieces of the last code cell that way run.


```python
    def collect_last_input(stop=-1):
        try: return '\n'.join(In[-1].splitlines()[:stop])
        except: return 
```

### Dependencies

* [`nbconvert`](http://nbconvert.readthedocs.io/) will convert notebooks into other file formats.
* [`git`/__GitPython__](https://gitpython.readthedocs.io/en/stable/) allows us to introspect the revision history to discover metadata about a post.
* [`yaml`/__PyYAML__](https://pyyaml.org/) will compose the [YAML Front Matter](https://jekyllrb.com/docs/front-matter/) that Jekyll uses to create posts.


```python
    import nbconvert, git, yaml, inspect; from pathlib import Path
    _imports = collect_last_input()
```

[__jupyter_nbconvert_config.py__](https://nbconvert.readthedocs.io/en/latest/config_options.html) is a special file name recognized by the `nbconvert` `configuration` system.  A goal of this notebook build the correct configuration file to create our posts.


```python
    configuration = Path('..', 'jupyter_nbconvert_config.py')
```

`FrontMatters` converts a notebook to Markdown and preprends the `yaml` front matter.


```python
    class FrontMatters(nbconvert.exporters.MarkdownExporter):
        def from_notebook_node(self, nb, resources=None, **kw):
            nb, resources = super().from_notebook_node(nb, resources, **kw)
            md = dict(resources['metadata'])
            md['author'] = author_from_repo(Path(md['path'], f"{md['name']}.ipynb"))
            md['layout'] = 'post'
            return '---\n'.join((
                '', yaml.safe_dump(md, default_flow_style=False), nb)), resources
    _front_matter_source = collect_last_input()
```

`author_from_repo` extracts the authors of a notebook from the `git` revision history.


```python
    def author_from_repo(file, dir='.'):
        repo = git.Repo(dir)
        return repo.blame('HEAD~0', file)[0][0].author.name
```

## Formatting __jupyter_nbconvert_config.py__

The components above are combined to create our `configuration` file.


```python
    collect_last_input() and configuration.write_text (F"""{_imports}

    {_front_matter_source}

    {inspect.getsource(author_from_repo)}
    try:
        c.NbConvertApp.export_format = f"jupyter_nbconvert_config.FrontMatters"
        c.FilesWriter.build_directory = "_posts"
    except: ...""");
```

## Travis

The __.travis.yml__ runs `nbconvert` on the ___notebooks__ folder.  After the scripts have completed the [Travis Pages Deployment](https://docs.travis-ci.com/user/deployment/pages/) pushes the changes to __master__ branch that hosts [__http://quansight.github.io/__](http://quansight.github.io/).

## Tests

Below we test that our `configuration` exports the correct features to convert our notebook to a post.


```python
    def test_author():
        assert author_from_repo('_notebooks/2018-09-14-Computable-posts-from-quansight.ipynb', dir='..') in ('Tony Fast', 'tonyfast')
        
    def test_convert():
        from IPython import get_ipython
        import io
        !pushd .. && jupyter nbconvert _notebooks/2018-09-14-Computable-posts-from-quansight.ipynb
        post = Path('../_posts/2018-09-14-Computable-posts-from-quansight.md')
        assert post.exists()
        *_, fm, md = post.read_text().split('---', 2)
        fm = yaml.safe_load(io.StringIO(fm))
        assert isinstance(fm, dict)
        assert 'layout' in fm, "The blog post won't show with Jekyll."

    if __name__ == '__main__':
        !ipython -m pytest -- 2018-09-14-Computable-posts-from-quansight.ipynb
```

    ]0;IPython: Quansight.github.io/_notebooks[1m============================= test session starts ==============================[0m
    platform darwin -- Python 3.6.3, pytest-3.5.0, py-1.5.3, pluggy-0.6.0
    benchmark: 3.1.1 (defaults: timer=time.perf_counter disable_gc=False min_rounds=5 min_time=0.000005 max_time=1.0 calibration_precision=10 warmup=False warmup_iterations=100000)
    rootdir: /Users/tonyfast/Quansight.github.io/_notebooks, inifile:
    plugins: xdist-1.22.2, forked-0.2, cov-2.5.1, benchmark-3.1.1, hypothesis-3.56.5, nbval-0.9.1, importnb-0.5.0
    collected 2 items                                                              [0m
    
    2018-09-14-Computable-posts-from-quansight.ipynb ..[36m                      [100%][0m
    
    [32m[1m=========================== 2 passed in 2.06 seconds ===========================[0m



```python

```


```python

```
