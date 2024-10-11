# Hello Anemos Developer

## Build

```python
pip install twine
pip install wheel

python setup.py sdist
python setup.py bdist_wheel
```

## Upload

### testpypi

```bash
twine upload --repository testpypi dist/* --config-file .pypirc
```

If you failed upload to test-pypi. You can execute `twine check dist/*` and try fix!

### pypi

```bash
twine upload --repository testpypi dist/* --config-file .pypirc
```
