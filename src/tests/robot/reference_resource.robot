*** Settings ***
Library  SeleniumLibrary
Library  AppLibrary.py
Resource  resource.robot
Resource  login_resource.robot


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