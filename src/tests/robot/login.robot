*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Login Page

*** Test Cases ***
Login With Correct Credentials
    Set Username  jaakko
    Set Password  jaakko6969
    Submit Credentials
    Login Should Succeed

Login With Incorrect Password
    Set Username  jaakko
    Set Password  jaakko4200
    Submit Credentials
    Login Should Fail With Message  Wrong username or password

Login With Nonexistent Username
    Set Username  koira
    Set Password  kalle456
    Submit Credentials
    Login Should Fail With Message  Wrong username or password

*** Keywords ***
Create User And Go To Login Page
    Create User  jaakko  jaakko6969
    Go To Login Page
    Login Page Should Be Open