*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Resource  reference_resource.robot
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

