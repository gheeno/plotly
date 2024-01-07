Plotly - challenge

### INSTALLATION ###

1. Install Python 3.11.X

2. Install pip requirements : 
    ```commandline
    ~ pip install -r requirements.txt 
    ```
    ```commandline
    ~ pip install -e .
    ```

3. Install Google Chrome

4. Clone the repo 

### STEPS ###

Cypress IO:

1. Execute Pytest with report.html.
- `~ pytest -v --html=report.html ./src/tests/pagetests/test_cypress_navigation.py`

2. To view the report
- `In the root folder ./plotly/ , there should be a report.html file after a pytest run ( following the command above ), open it via VSCode Extension or a browser.`

Dash App :

1. Run the web app. 
- `~ python src/dash_app/sample_app.py`

2. Execute pytest.
- `~ pytest -v ./src/tests/pagetests/test_sample_app.py`

3. Additional : Execute Robotframework
- `~ robot -d ./results ./src/tests/robot/test_sample_app.robot `

### NOTES During development ###
1. To pause the debugger in chrome due to dynamic objects : 
    - Chrome Dev Tools : console 
    - `setTimeout(()=>{debugger;},5000);`

2. To Pause test : 
    ```import pdb```
    ```pdb.set_trace() #add to line```

3. SVG xpath sample : `//*[name()="samplesvgname"]`
