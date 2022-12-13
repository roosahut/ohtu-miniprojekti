*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Login

*** Test Cases ***

Add Adds One Book Reference To References
    Go To Book Page
    Set Refkey  cats1  
    Set Author  Katti K  
    Set Title  Kissat  
    Set Year  2222  
    Set Publisher  Koira k
    Submit Credentials
    Go To References Page
    Page Should Contain  cats1

*** Keywords ***
Create User And Login
    Create User  mikko  mikko6969
    Go To Login Page
    Set Username  mikko
    Set Password  mikko6969
    Submit Login Credentials


Set Refkey
    [Arguments]  ${ref_key}
    Input Text  ref_key  ${ref_key}

Set Author
    [Arguments]  ${author}
    Input Text  author  ${author}

Set Title
    [Arguments]  ${title}
    Input Text  title  ${title}

Set Publisher
    [Arguments]  ${publisher}
    Input Text  publisher  ${publisher}

Set Year
    [Arguments]  ${year}
    Input Text  year  ${year}

Submit Credentials
    Click Button  Add reference

Submit Login Credentials
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}