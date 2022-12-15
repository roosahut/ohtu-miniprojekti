*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Login Page

*** Test Cases ***
Login With Correct Credentials
    Set Username  mikko
    Set Password  mikko6969
    Submit Credentials
    Login Should Succeed

Login With Incorrect Password
    Set Username  mikko
    Set Password  mikko4200
    Submit Credentials
    Login Should Fail With Message  Wrong username or password

Login With Nonexistent Username
    Set Username  koira
    Set Password  kalle456
    Submit Credentials
    Login Should Fail With Message  Wrong username or password

*** Keywords ***
Create User And Go To Login Page
    Create User  mikko  mikko6969
    Go To Login Page
    Login Page Should Be Open