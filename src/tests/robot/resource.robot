*** Settings ***
Library  AppLibrary.py
Library  SeleniumLibrary
Library  OperatingSystem

*** Variables ***
${SERVER}  localhost:5000
${BROWSER}  headlesschrome
${DELAY}  0.0 seconds
${HOME URL}  http://${SERVER}
${LOGIN URL}  http://${SERVER}/login
${REGISTER URL}  http://${SERVER}/register
${ARTICLE URL}  http://${SERVER}/add_reference?add_reference=article
${INPROCEEDINGS URL}  http://${SERVER}/add_reference?add_reference=inproceedings
${BOOK URL}  http://${SERVER}/add_reference?add_reference=book
${MASTERS URL}  http://${SERVER}/add_reference?add_reference=master_thesis
${REFERENCES URL}  http://${SERVER}/view_references


*** Keywords ***
Open And Configure Browser
    Open Browser  browser=${BROWSER}
    #Maximize Browser Window
    Set Selenium Speed  ${DELAY}

Login Page Should Be Open
    Title Should Be  Login

Register Page Should Be Open
    Title Should Be  Register

Error Page Should Be Open
    Title Should Be  Error

Main Page Should Be Open
    Title Should Be  Reference library

Go To Home Page
    Go To  ${HOME URL}

Go To Login Page
    Go To  ${LOGIN URL}

Go To Register Page
    Go To  ${REGISTER URL}

Go To Article Page
    Go To  ${ARTICLE URL}

Go To Masters Page
    Go To  ${MASTERS URL}

Go To Book Page
    Go To  ${BOOK URL}

Go To Inproceedings Page
    Go To  ${INPROCEEDINGS URL}

Go To References Page
    Go To  ${REFERENCES URL}

# Input Book
#     [Arguments]  ${reference}  ${author}  ${name}  ${publisher}  ${year}  
#     Input  ${reference}
#     Input  ${author}
#     Input  ${name}
#     Input  ${publisher}
#     Input  ${year}
#     Run Application

