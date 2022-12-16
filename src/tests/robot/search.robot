*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Resource  reference_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Login


*** Test Cases ***
Search Reference
    Add Book Reference
    Add Article Reference
    Go To References Page
    Search  Kissat
    Page Should Contain  Kissat
    Page Should Not Contain  Koirat


*** Keywords ***
Create User And Login
    Create User  mikko  mikko6969
    Go To Login Page
    Set Username  mikko
    Set Password  mikko6969
    Submit Credentials

Add Book Reference
    Go To Book Page
    Set Refkey  cats2022  
    Set Author  Katti K 
    Set Title  Kissat  
    Set Publisher  Otava
    Set Year  2022
    Submit Data

Add Article Reference
    Go To Article Page
    Set Refkey  dogs2222
    Set Author  Katti K 
    Set Title  Koirat  
    Set Journal  Lehti
    Set Year  2222
    Set Volume  4
    Submit Data

Search
    [Arguments]  ${search}
    Input Text  search  ${search}
    Click Button  Search
