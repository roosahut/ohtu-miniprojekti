*** Settings ***
Library  ../AppLibrary.py

*** Keywords ***
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