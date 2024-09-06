# Python-PytestBdd-Selenium-Docker
Using Python, pytest-bdd, Selenium, and Docker, this is an automation framework for web UI testing.

## pytest-bdd info

```
# Cucumber Report
pytest .\tests\steps\test_contact.py --cucumberjson=./target/cucumber.json
```

```
# conftest.py
# Place inside the tests folder.
# File is a global place to store fixtures.
@pytest.fixture
def my_global_fixture():
    return { }
```

```
# pytest.ini
# Place this file at the root of the project.
# Register annotations here.
[pytest]
markers = 
    contact: Run the contact feature
    fuzzy: Run the fuzzy feature
```

```
# Before Step and After Step
@pytest.fixture
def before_and_after_each_step():
    print('before step')
    yield
    print('after step')
```

```
# Parallel (pytest-xdist)
pytest .\tests\steps\test* -n 10
```

```
# Print
pytest .\tests\steps\test* -s
```

```
# Link features
scenarios('../features/name_of.feature')
```

```
# Scenario Context
@pytest.fixture
def scenario_context():
    return { }

@given('scenario context is used')
def _(scenario_context):
    pass
```

```
# Pass variable from step to step definition
@when(parsers.parse('the number is less than {some_number:d}))
def _(context, some_number):
    pass
```

## Automation Framework
###### The ConfigProvider class (configprovider folder) reads the configuration file, automation_config.ini, and provides those settings elsewhere in the automation.
###### The DriverProvider class (driverprovider folder) provides a local or remote driver to each thread of execution based on settings in automation_config.ini.
###### Page Object Model (pagemodels folder) is a design pattern for UI automation. There is a class for each page or subsection of a page.	Methods of the class are actions that can occur on the page. Private class data holds the elemenet location strategy (css, id, etc.).
###### Test data (testdata/json folder) is stored as JSON in the repository. Test models (testdata/model folder) provide typing for the test data. Test data providers (testdata/provider folder) read the JSON and convert test data to a list of typed objects. This could be adapted to work with a database in a similar manner.
###### Feature files (tests/features folder) define the behavior of the application. Cucumber is software that executes a feature file.	Step definitions (tests/steps folder) contain code behind each step of the scenarios found in the feature files.
###### conftest.py contains shared fixtures and shared steps. By convention in pytest-bdd, if a step definition is to be used by more than one feature file, the step definition must go in conftest.py. Within conftest.py, scenario_context yields a dictionary for each thread of test execution. Test data/state to be passed to the next step of the scenario is stored in the dictionary. By convention in Cucumber, the dictionary is called "scenario context".
###### Docker Compose YAML is configured to run a containerized Selenium Grid. Versions of the Selenium Grid are available that run all Chrome, all Edge, all Firefox, and a mix of these browsers. There is a corresponding video capture version of each that is currently only configured to work in Windows.
###### pytest.ini markers are used to annotate feature files for execution.
