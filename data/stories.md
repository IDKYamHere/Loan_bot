## Story 01
* greet
	-utter_greet

## Story 02
* goodbye
	-utter_goodbye

## Story 03
* weather
    - utter_weather

## interactive_story_1
* greet
	- utter_greet
	- action_face_rec
    - utter_askloan
* affirm
    - utter_what_loan
* loan_type{"loantype": "car"}
    - slot{"loantype": "car"}
    - utter_loan_amt
* loan_amt{"l_amt": "1000000"}
    - slot{"l_amt": "1000000"}
    - utter_monthly_pay
* monthlypay{"monthly_pay": "20000"}
    - slot{"monthly_pay": "20000"}
    - action_loanoffer
    - slot{"loantype": "car"}
    - utter_check_eligibility
* affirm
    - utter_give_info
* affirm
    - utter_name
* affirm{"name": "Sidd"}
    - slot{"name": "Sidd"}
    - utter_spelling
* affirm
    - utter_dob
* dateofbirth{"dob": "10-July-1999"}
    - slot{"dob": "10-July-1999"}
    - utter_what_doc
* document_type{"doc_type": "Driving License"}
    - slot{"doc_type": "Driving License"}
    - utter_holdup
    - action_card_scan
    - utter_thankyou
    - utter_emporbusi
* cus_work{"work": "employed"}
    - utter_whichcompany
* company_name{"company": "Nucleus Software Exports ltd"}
    - slot{"company": "Nucleus Software Exports ltd"}
    - action_validate_company
    - slot{"company": "Nucleus Software Exports ltd"}
    - utter_salary
* cus_salary{"salary": "100000"}
    - slot{"salary": "100000"}
    - utter_have_payslip
* affirm
    - utter_holdup
    - action_click_photo
    - utter_cibil_wait
* affirm
    - utter_congrats
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
	- utter_greet
	- action_face_rec
    - utter_askloan
* affirm
    - utter_what_loan
* loan_type{"loantype": "car"}
    - slot{"loantype": "car"}
    - utter_loan_amt
* loan_amt{"l_amt": "4000000"}
    - slot{"l_amt": "4000000"}
    - utter_monthly_pay
* monthlypay{"monthly_pay": "20000"}
    - slot{"monthly_pay": "20000"}
    - action_loanoffer
    - slot{"loantype": "car"}
    - utter_check_eligibility
* affirm
    - utter_give_info
* affirm
    - utter_name
* affirm{"name": "Sanjay"}
    - slot{"name": "Sanjay"}
    - utter_spelling
* affirm
    - utter_dob
* dateofbirth{"dob": "20-March-1995"}
    - slot{"dob": "20-March-1995"}
    - utter_what_doc
* document_type{"doc_type": "Driving License"}
    - slot{"doc_type": "Driving License"}
    - utter_holdup
    - action_card_scan
    - utter_thankyou
    - utter_emporbusi
* cus_work{"work": "employed"}
    - utter_whichcompany
* company_name{"company": "Nucleus Software Exports ltd"}
    - slot{"company": "Nucleus Software Exports ltd"}
    - action_validate_company
    - slot{"company": "Nucleus Software Exports ltd"}
    - utter_salary
* cus_salary{"salary": "300000"}
    - slot{"salary": "300000"}
    - utter_have_payslip
* affirm
    - utter_holdup
    - action_click_photo
    - utter_cibil_wait
* affirm
    - utter_congrats
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
	- utter_greet
	- action_face_rec
    - utter_askloan
* affirm
    - utter_what_loan
* loan_type{"loantype": "marriage"}
    - slot{"loantype": "marriage"}
    - utter_loan_amt
* loan_amt{"l_amt": "500000"}
    - slot{"l_amt": "500000"}
    - utter_monthly_pay
* loan_amt{"monthly_pay": "20000"}
    - slot{"monthly_pay": "20000"}
    - action_loanoffer
    - slot{"loantype": "marriage"}
    - utter_check_eligibility
* affirm
    - utter_give_info
* affirm
    - utter_name
* need_loan{"name": "Arjun"}
    - slot{"name": "Arjun"}
    - utter_spelling
* affirm
    - utter_dob
* dateofbirth{"dob": "25-April-2005"}
    - slot{"dob": "25-April-2005"}
    - utter_what_doc
* document_type{"doc_type": "Driving License"}
    - slot{"doc_type": "Driving License"}
    - utter_holdup
    - action_card_scan
    - utter_thankyou
    - utter_emporbusi
* cus_work{"work": "employed"}
    - utter_whichcompany
* company_name{"company": "Nucleus Software Exports ltd"}
    - slot{"company": "Nucleus Software Exports ltd"}
    - action_validate_company
    - slot{"company": "Nucleus Software Exports ltd"}
    - utter_salary
* cus_salary{"salary": "75000"}
    - slot{"salary": "75000"}
    - utter_have_payslip
* affirm
    - utter_holdup
    - action_click_photo
    - utter_cibil_wait
* affirm
    - utter_congrats
* goodbye
    - utter_goodbye
* goodbye

## interactive_story_1
* greet
	- utter_greet
	- action_face_rec
* need_loan
    - utter_what_loan
* loan_type{"loantype": "house"}
    - slot{"loantype": "house"}
    - utter_loan_amt
* loan_amt{"l_amt": "700000"}
    - slot{"l_amt": "700000"}
    - utter_monthly_pay
* monthlypay{"monthly_pay": "40000"}
    - slot{"monthly_pay": "40000"}
    - action_loanoffer
    - slot{"loantype": "house"}
    - utter_check_eligibility
* affirm
    - utter_give_info
* affirm
    - utter_name
* cusname{"name": "Rahul"}
    - slot{"name": "Rahul"}
    - utter_spelling
* affirm
    - utter_dob
* dateofbirth{"dob": "12-June-1997"}
    - slot{"dob": "12-June-1997"}
    - utter_what_doc
* document_type{"doc_type": "Passport"}
    - slot{"doc_type": "Passport"}
    - utter_holdup
    - action_card_scan
    - utter_thankyou
    - utter_emporbusi
* cus_work{"work": "employed"}
    - utter_whichcompany
* company_name{"company": "Nucleus Software Exports ltd"}
    - slot{"company": "Nucleus Software Exports ltd"}
    - action_validate_company
    - slot{"company": "Nucleus Software Exports ltd"}
    - utter_salary
* cus_salary{"salary": "2000000"}
    - slot{"salary": "2000000"}
    - utter_have_payslip
* affirm
    - utter_holdup
    - action_click_photo
    - utter_cibil_wait
* affirm
    - utter_congrats
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
	- utter_greet
	- action_face_rec
* need_loan
    - utter_what_loan
* loan_type{"loantype": "house"}
    - slot{"loantype": "house"}
    - utter_loan_amt
* loan_amt{"l_amt": "600000"}
    - slot{"l_amt": "600000"}
    - utter_monthly_pay
* loan_amt{"monthly_pay": "5000"}
    - slot{"monthly_pay": "5000"}
    - action_loanoffer
    - slot{"loantype": "house"}
    - utter_check_eligibility
* affirm
    - utter_give_info
* affirm
    - utter_name
* loan_type{"name": "Kumar"}
    - slot{"name": "Kumar"}
    - utter_spelling
* affirm
    - utter_dob
* dateofbirth{"dob": "13-October-1997"}
    - slot{"dob": "13-October-1997"}
    - utter_what_doc
* document_type{"doc_type": "Aadhar Card"}
    - slot{"doc_type": "Aadhar Card"}
    - utter_holdup
    - action_card_scan
    - utter_thankyou
    - utter_emporbusi
* cus_work{"work": "employed"}
    - utter_whichcompany
* company_name{"company": "google"}
    - slot{"company": "google"}
    - action_validate_company
    - slot{"company": "google"}
    - utter_salary
* cus_salary{"salary": "4000000"}
    - slot{"salary": "4000000"}
    - utter_have_payslip
* affirm
    - utter_holdup
    - action_click_photo
    - utter_cibil_wait
* affirm
    - utter_congrats
* goodbye
    - utter_goodbye
* goodbye

## interactive_story_1
* greet
    - utter_greet
	- action_face_rec
* need_loan
    - utter_what_loan
* loan_type{"loantype": "electronics"}
    - slot{"loantype": "electronics"}
    - utter_loan_amt
* loan_amt{"l_amt": "800000"}
    - slot{"l_amt": "800000"}
    - utter_monthly_pay
* loan_amt{"monthly_pay": "6000"}
    - slot{"monthly_pay": "6000"}
    - action_loanoffer
    - slot{"loantype": "electronics"}
    - utter_check_eligibility
* affirm
    - utter_give_info
* affirm
    - utter_name
* cusname{"name": "Parag"}
    - slot{"name": "Parag"}
    - utter_spelling
* affirm
    - utter_dob
* dateofbirth{"dob": "14-December-1965"}
    - slot{"dob": "14-December-1965"}
    - utter_what_doc
* document_type{"doc_type": "Driving License"}
    - slot{"doc_type": "Driving License"}
    - utter_holdup
    - action_card_scan
    - utter_thankyou
    - utter_emporbusi
* cus_work{"work": "employed"}
    - utter_whichcompany
* company_name{"company": "Microsoft"}
    - slot{"company": "Microsoft"}
    - action_validate_company
    - slot{"company": "Microsoft"}
    - utter_salary
* cus_salary{"salary": "5000000"}
    - slot{"salary": "5000000"}
    - utter_have_payslip
* affirm
    - utter_holdup
    - action_click_photo
    - utter_cibil_wait
* affirm
    - utter_congrats
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
	- action_face_rec
* need_loan
    - utter_what_loan
* loan_type{"loantype": "marriage"}
    - slot{"loantype": "marriage"}
    - utter_loan_amt
* loan_amt{"l_amt": "4000000"}
    - slot{"l_amt": "4000000"}
    - utter_monthly_pay
* loan_amt{"monthly_pay": "70000"}
    - slot{"monthly_pay": "70000"}
    - action_loanoffer
    - slot{"loantype": "marriage"}
    - utter_check_eligibility
* affirm
    - utter_give_info
* affirm
    - utter_name
* cusname{"name": "Prakash"}
    - slot{"name": "Prakash"}
    - utter_spelling
* affirm
    - utter_dob
* dateofbirth{"dob": "26-March-1990"}
    - slot{"dob": "26-March-1990"}
    - utter_what_doc
* document_type{"doc_type": "Passport"}
    - slot{"doc_type": "Passport"}
    - utter_holdup
    - action_card_scan
    - utter_thankyou
    - utter_emporbusi
* cus_work{"work": "employed"}
    - utter_whichcompany
* company_name{"company": "Nucleus Software Exports ltd"}
    - slot{"company": "Nucleus Software Exports ltd"}
    - action_validate_company
    - slot{"company": "Nucleus Software Exports ltd"}
    - utter_salary
* cus_salary{"salary": "400000"}
    - slot{"salary": "400000"}
    - utter_have_payslip
* affirm
    - utter_holdup
    - action_click_photo
    - utter_cibil_wait
* affirm
    - utter_congrats
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
    - action_face_rec
* need_loan
    - utter_what_loan
* loan_type{"loantype": "house"}
    - slot{"loantype": "house"}
    - utter_loan_amt
* loan_amt{"l_amt": "100000"}
    - slot{"l_amt": "100000"}
    - utter_monthly_pay
* loan_amt{"monthly_pay": "30000"}
    - slot{"monthly_pay": "30000"}
    - action_loanoffer
    - slot{"loantype": "house"}
    - utter_check_eligibility
* affirm
    - utter_give_info
* affirm
    - utter_name
* cusname{"name": "Om"}
    - slot{"name": "Om"}
    - utter_spelling
* affirm
    - utter_dob
* dateofbirth{"dob": "16-November-1985"}
    - slot{"dob": "16-November-1985"}
    - utter_what_doc
* document_type{"doc_type": "Driving License"}
    - slot{"doc_type": "Driving License"}
    - utter_holdup
    - action_card_scan
    - utter_thankyou
    - utter_emporbusi
* cus_work{"work": "employed"}
    - utter_whichcompany
* company_name{"company": "Nucleus Software Exports ltd"}
    - slot{"company": "Nucleus Software Exports ltd"}
    - action_validate_company
    - slot{"company": "Nucleus Software Exports ltd"}
    - utter_salary
* cus_salary{"salary": "7000000"}
    - slot{"salary": "7000000"}
    - utter_have_payslip
* affirm
    - utter_holdup
    - action_click_photo
    - utter_cibil_wait
* affirm
    - utter_congrats
* goodbye
    - utter_goodbye
