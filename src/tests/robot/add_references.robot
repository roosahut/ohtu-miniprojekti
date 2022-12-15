*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Login

*** Test Cases ***
Add Book Reference
    Go To Book Page
    Set Refkey  cats1  
    Set Author  Katti K  
    Set Title  Kissat  
    Set Publisher  Koira k
    Set Year  2222
    Submit Data
    Go To References Page
    Page Should Contain  cats1

Add Article Reference
    Go To Article Page
    Set Refkey  cats2
    Set Author  Katti K  
    Set Title  Kissat  
    Set Journal  Koira k
    Set Year  2222
    Set Volume  4
    Submit Data
    Go To References Page
    Page Should Contain  cats2

Add Inproceedings Reference
    Go To Inproceedings Page
    Set Refkey  cats3
    Set Author  Katti K  
    Set Title  Kissat  
    Set Booktitle  Koira k
    Set Year  2222
    Submit Data
    Go To References Page
    Page Should Contain  cats3

Add Mastersthesis Reference
    Go To Masters Page
    Set Refkey  cats4
    Set Author  Katti K  
    Set Title  Kissat  
    Set School  Koulu k
    Set Year  2222
    Submit Data
    Go To References Page
    Page Should Contain  cats4

Add Reference With Empty Fields
    Go To Masters Page
    Set Refkey  cats4
    Set Author  Katti K 
    Submit Data
    Page Should Contain  Reference adding failed, try again

Add Refkey That Already Exists
    Go To Book Page
    Set Refkey  cats1  
    Set Author  Katti K  
    Set Title  Kissat  
    Set Publisher  Koira k
    Set Year  2222
    Submit Data

    Go To Article Page
    Set Refkey  cats1
    Set Author  Katti K  
    Set Title  Kissat  
    Set Journal  Koira k
    Set Year  2222
    Set Volume  4
    Submit Data
    Page Should Contain  You already have a reference with this key

*** Keywords ***
Create User And Login
    Create User  mikko  mikko6969
    Go To Login Page
    Set Username  mikko
    Set Password  mikko6969
    Submit Credentials

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

Set Journal
    [Arguments]  ${journal}
    Input Text  journal  ${journal}

Set Volume
    [Arguments]  ${volume}
    Input Text  volume  ${volume}

Set Booktitle
    [Arguments]  ${booktitle}
    Input Text  booktitle  ${booktitle}

Set School
    [Arguments]  ${school}
    Input Text  school  ${school}

Submit Data
    Click Button  Add reference

Submit Credentials
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}