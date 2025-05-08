def expert_system():
    print(" Welcome to the Medical Diagnosis Expert System")
    print("Answer the following questions with 'yes' or 'no'.\n")

    fever = input("Do you have a fever? ").lower()
    cough = input("Do you have a cough? ").lower()
    headache = input("Do you have a headache? ").lower()
    fatigue = input("Are you feeling tired? ").lower()
    rash = input("Do you have a skin rash? ").lower()

    print("\n Diagnosis Result:")
    if fever == 'yes' and cough == 'yes' and fatigue == 'yes':
        print(" You might have the Flu.")
    elif fever == 'yes' and rash == 'yes':
        print(" You might have Measles.")
    elif headache == 'yes' and fatigue == 'yes':
        print(" You might be experiencing Migraine.")
    elif fever == 'no' and cough == 'no' and rash == 'no':
        print(" You seem to be healthy!")
    else:
        print(" Cannot determine the condition. Please consult a doctor.")

# Run the expert system
expert_system()


o/p

 Welcome to the Medical Diagnosis Expert System  
Answer the following questions with 'yes' or 'no'.  

Do you have a fever? yes  
Do you have a cough? yes  
Do you have a headache? no  
Are you feeling tired? yes  
Do you have a skin rash? no  

 Diagnosis Result:  
 You might have the Flu.


Do you have a fever? yes  
Do you have a cough? no  
Do you have a headache? no  
Are you feeling tired? no  
Do you have a skin rash? yes  

🔍 Diagnosis Result:  
😷 You might have Measles.



Do you have a fever? no  
Do you have a cough? no  
Do you have a headache? yes  
Are you feeling tired? yes  
Do you have a skin rash? no  

🔍 Diagnosis Result:  
🧠 You might be experiencing Migraine.




Do you have a fever? no  
Do you have a cough? no  
Do you have a headache? no  
Are you feeling tired? no  
Do you have a skin rash? no  

🔍 Diagnosis Result:  
🙂 You seem to be healthy!



Do you have a fever? yes  
Do you have a cough? no  
Do you have a headache? yes  
Are you feeling tired? no  
Do you have a skin rash? no  

🔍 Diagnosis Result:  
🩺 Cannot determine the condition. Please consult a doctor.


