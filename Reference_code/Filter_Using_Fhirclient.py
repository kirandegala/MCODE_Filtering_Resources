from fhirclient.models.patient import Patient
import json
import os 
for file in os.listdir("./Sample_FHIR_Data"):
    if '.json' in file:
        # Step 1: Load the JSON file
        with open("./Sample_FHIR_Data/" + file, 'r') as file:
            data = json.load(file)
        data = data['entry']
        patient_data = {}

        for i in range(len(data)):
            if data[i]['resource']['resourceType'] == "Patient":
                patient_data = data[i]['resource']
                break

        patient = Patient(patient_data)

        race = None
        for ext in patient.extension or []:
            if ext.url == 'http://hl7.org/fhir/us/core/StructureDefinition/us-core-race':
                race = ext.extension[0].valueCoding.display
                break

        # print(patient.birthDate.isostring)
        # print(race)
        # print(patient.gender)

        if race == 'White' and patient.gender == "female":
            print(file)