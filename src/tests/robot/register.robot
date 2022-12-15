*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Open Register Page


*** Test Cases ***
Register With Valid Username And Password
    Set Username  nimi
    Set Password In Registration  kalle123
    Set Password Confirmation  kalle123
    Register User
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password In Registration  kalle123
    Set Password Confirmation  kalle123
    Register User
    Register Should Fail With Message  Username is too short, it should be at least 4 characters long

Register With Valid Username And Too Short Password
    Set Username  koira
    Set Password In Registration  ka123
    Set Password Confirmation  ka123
    Register User
    Register Should Fail With Message  Password is too short

Register With Nonmatching Password And Password Confirmation
    Set Username  kissa
    Set Password In Registration  kalle123
    Set Password Confirmation  kalle12
    Register User
    Register Should Fail With Message  The passwords are not the same

Login After Successful Registration
    Open Login Page
    Set Username  nimi
    Set Password  kalle123
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
    Open Login Page
    Set Username  ka
    Set Password  kalle456
    Submit Credentials
    Login Should Fail With Message  Wrong username or password


*** Keywords ***
Register Should Succeed
    Main Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Page Should Contain  ${message}

Register User
    Click Button  Create an account

Set Password In Registration
    [Arguments]  ${password}
    Input Password  password1  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password2  ${password}

Open Register Page
    Go To Register Page
    Register Page Should Be Open

Open Login Page
    Go To Login Page
    Login Page Should Be Open