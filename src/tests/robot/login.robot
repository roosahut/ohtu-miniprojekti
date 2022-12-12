*** Settings ***
Resource  resource.robot
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

*** Keywords ***
Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Error Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Create User And Go To Login Page
    Create User  jaakko  jaakko6969
    Go To Login Page
    Login Page Should Be Open