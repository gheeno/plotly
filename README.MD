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

Cypress IO:

1. TODO

Dash App :
1. Run the web app. 
- `~ python src/dash/apps/sample_app.py`

2. Execute pytest.
- `~ pytest -v`

3. Additional : Execute Robotframework
- `~ robot -d ./results ./src/dash/tests/robot/test_sample_app.robot `

### NOTES During development ###
1. To pause the debugger in chrome due to dynamic objects : 
    - Chrome Dev Tools : console 
    - `setTimeout(()=>{debugger;},5000);`

2. To Pause test : 
    ```import pdb```
    ```pdb.set_trace() #add to line```

3. SVG xpath sample : `//*[name()="samplesvgname"]`
