Basically I'm trying to add these:
`pip install openai==0.28 config==0.5.1 langchain==0.0.297 pydantic==1.10.9 tiktoken==0.5.1 faiss-cpu transformers==4.47.1 torch==2.5.1 datasets==3.2.0 evaluate==0.4.3 accelerate==1.2.1 ipywidgets==8.1.5 matplotlib==3.10.0 seaborn==0.13.2 clean-text==0.6.0 scikit-learn==1.6.0 sentencepiece==0.2.0 pandas==2.0.0`

And I'm trying to do so using `uv add ... ; uv sync; uv lock` - is that appropriate? shall I remove the `==` from all?
## fixed via uv 

```bash

uv python pin 3.13 # pin the version (defaulting to 3.14 is not ideal, too new)

uv add openai==0.28 config==0.5.1 langchain==0.0.297 pydantic==1.10.9 tiktoken==0.5.1 faiss-cpu transformers==4.47.1 torch==2.5.1 datasets==3.2.0 evaluate==0.4.3 accelerate==1.2.1 ipywidgets==8.1.5 matplotlib==3.10.0 seaborn==0.13.2 clean-text==0.6.0 scikit-learn==1.6.0 sentencepiece pandas==2.0.0

uv sync 
uv lock
```
