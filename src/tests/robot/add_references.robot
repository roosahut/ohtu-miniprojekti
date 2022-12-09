*** Settings ***
Resource  resource.robot

*** Test Cases ***

Add Adds One Reference To References
    Add Reference  cats1  Katti K  Kissat  2222  Koira k
    References Should Contain  cats1  Katti K  Kissat  2222  Koira k