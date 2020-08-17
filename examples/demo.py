#
# #topicNames = ["AllergyIntolerance","Appointment","Claim","ConceptMapElement","Condition","Consent","Coverage","DataBufferLog","DiagnosticReport","Encounter","EpisodeOfCare","ExplanationOfBenefit","FamilyMemberHistory","Immunization","Location","Medication","MedicationAdministration","MedicationDispense","MedicationOrder","MedicationPrescription","MedicationStatement","Observation","Organization","Patient","PatientExclude","Practitioner","Procedure","ProcedureRequest","Questionnaire","QuestionnaireResponse","ReferralRequest","RelatedPerson","Specimen","_confluent-monitoring","mt-event-dp","reindex","sv5-event","telemetry","test"]
#
# topicNames = ["AllergyIntolerance","Appointment","Claim","ConceptMapElement","Condition","Consent","Coverage","DataBufferLog","DiagnosticReport","Encounter","EpisodeOfCare","ExplanationOfBenefit","FamilyMemberHistory","Immunization","Location","Medication","MedicationAdministration","MedicationDispense","MedicationOrder","MedicationPrescription","MedicationStatement","Observation","Organization","Patient","PatientExclude","Practitioner","Procedure","ProcedureRequest","Questionnaire","QuestionnaireResponse","ReferralRequest","RelatedPerson","Specimen","_confluent-monitoring", "reindex","sv5-event","telemetry","test"]
#
# print(len(topicNames))
#
# for topic in topicNames:
#     #print(i)
#     print('{{"topic":"{}","partition": 0,"replicas":[0,1,2]}},'.format(topic))
#



enter_number = int(input("enter number "))
is_prod_or_sum = int(input("Enter 1 for product or 2 for sum "))

counter = 1
sum = 0
product = 1

while counter <= enter_number:
    if is_prod_or_sum == 2:
        sum = counter + sum
        print(sum)
    elif is_prod_or_sum == 1:
        product = counter * product
        print(product)
    else:
        print("Please run again and provide 1 for product or 2 for sum!")
        break

    counter = counter + 1