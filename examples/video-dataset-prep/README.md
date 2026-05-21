# Video Dataset Prep Example

A small example showing the test-driven assistant workflow.

It extracts frames from videos into:

```text
dataset/images/
```

Setup:

```bash
conda create -n cv-detect python=3.11 -y
conda activate cv-detect
conda install -c conda-forge opencv numpy pytest -y
```

Run tests:

```bash
python -m pytest -q
```
