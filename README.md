## General info
Test automation framework based on python and selenium webdriver.
This project tries to automate basic functionalities of cloathing shop website (http://automationpractice.com).

## Project structure
* base - this folder contains classes enabling the creation of selectors for the elements on the page, assertions and support methods,
* config - contains tests configuration,
* pages - in the page catalogue are stored classes related to the usage of concrete application pages,
* tests - contains modules storing tests for given fields of the application,

## ToDo
* Test data transferred in the form of a yaml file,
* Browser closes after the test is done or if an error occurs,
* Pytest implementation,
* Logging infrastructure implementation,
* Improve page_elements section,
* Explicit wait (instead of implicit wait),
* More descriptions,
