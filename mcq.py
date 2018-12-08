#!python3
# mcq.py
import random

capitals = {
        "Andra Pradesh":"Hyderabad",
        "Arunachal Pradesh":"Itangar",
        "Assam": "Dispur",
        "Bihar": "Patna",
        "Chhattisgarh": "Raipur",
        "Goa": "Panaji",
        "Gujarat": "Gandhinagar",
        "Haryana": "Chandigarh",
        "Himachal Pradesh": "Shimla",
        "Jammu and Kashmir": "Srinagar and Jammu",
        "Jharkhand": "Ranchi",
        "Karnataka": "Bangalore",
        "Kerala": "Thiruvananthapuram",
        "Madya Pradesh": "Bhopal",
        "Maharashtra": "Mumbai",
        "Manipur": "Imphal",
        "Meghalaya": "Shillong",
        "Mizoram": "Aizawi",
        "Nagaland": "Kohima",
        "Orissa": "Bhubaneshwar",
        "Punjab": "Chandigarh",
        "Rajasthan": "Jaipur",
        "Sikkim": "Gangtok",
        "Tamil Nadu": "Chennai",
        "Telangana": "Hyderabad",
        "Tripura": "Agartala",
        "Uttarakhand": "Dehradun",
        "Uttar Pradesh": "Lucknow",
        "West Bengal": "Kolkata",
        "Union Territories": "Capital",
        "Andaman and Nicobar Islands": "Port Blair",
        "Chandigarh": "Chandigarh",
        "Dadar and Nagar Haveli": "Silvassa",
        "Daman and Diu": "Daman",
        "Delhi": "Delhi",
        "Lakshadweep": "Kavaratti",
        "Pondicherry": "Pondicherry"
}

for i in range (10):                                                                # Loop to set question paper serial number.
    question_file = open('quiz_questionset%s.txt'%(i+1),'w+')                        #Creating questions file. 
    answer_file = open('quiz_answerset%s.txt'%(i+1),'w+')                            #Creating answer file.

    question_file.write('Name:\n\nDate:\n\nPeriod:\n\n')
    question_file.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (i + 1))     #Header for question_file.
    question_file.write('\n\n')

    ques_list=list(capitals.keys())                                                 #Created list of states.
    random.shuffle(ques_list)                                                       #Shuffling the elements of list.

    for j in range(37):                                                             #Looping through all 50 states, making a question for each.
        correct = capitals[ques_list[j]]
        wrong = list(capitals.values())
        del wrong[wrong.index(correct)]
        wrong=random.sample(wrong,3) 
        answer_options=wrong+[correct] 
        random.shuffle(answer_options)  


        question_file.write('%s. What is the capital of %s?\n' % (j + 1,ques_list[j]))

        for k in range(4):                                                          #Writing the question and the answer options to the quiz file.
            question_file.write('%s. %s\n' % ('ABCD'[k], answer_options[k]))
            question_file.write('\n')
            answer_file.write('%s. %s\n' % (j + 1, 'ABCD'[answer_options.index(correct)]))

test = open("test.txt", "w+")
test.write("test")
test.close()
question_file.close()
answer_file.close()



