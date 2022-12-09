*** Settings ***
Library  AppLibrary.py
Library  SeleniumLibrary

*** Variables ***
${SERVER}  localhost:5000
${BROWSER}  headlesschrome
${DELAY}  0.0 seconds
${HOME URL}  http://${SERVER}
${LOGIN URL}  http://${SERVER}/login
${REGISTER URL}  http://${SERVER}/register

*** Keywords ***
Open And Configure Browser
    Open Browser  browser=${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}

Login Page Should Be Open
    Title Should Be  Login

Error Page Should Be Open
    Title Should Be  Error

Main Page Should Be Open
    Title Should Be  Reference library

Go To Login Page
    Go To  ${LOGIN URL}

Input Add Command
    Input  lisää

Input Read Command
    Input  lue

Input Credentials
    [Arguments]  ${reference}  ${author}  ${name}  ${year}  ${publisher}
    Input  ${reference}
    Input  ${author}
    Input  ${name}
    Input  ${year}
    Input  ${publisher}
    Run Application

