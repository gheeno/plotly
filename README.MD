Plotly Dash 2.0 practice.

### INSTALLATION ###
1. Install pip requirements : 
    ```commandline
    ~ pip install -r requirements.txt 
    ```
    ```commandline
    ~ pip install -e .
    ```

### STEPS ###
1. Run the web app. 
- `python src/apps/sample_app.py`

2. Execute pytest.
- `pytest -v`

### NOTES During development ###
1. To pause the debugger in chrome due to dynamic objects : 
    - Chrome Dev Tools : console 
    - `setTimeout(()=>{debugger;},5000);`

2. To Pause test : 
    ```import pdb```
    ```pdb.set_trace() #add to line```

3. SVG xpath sample : `//*[name()="samplesvgname"]`
