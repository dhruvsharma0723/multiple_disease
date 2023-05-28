import os
import openai


# openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = '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'

def get_suggestions(age,pregnancies_num,skin_thickness,diab_pedig,insulin,bloodpressure,bmi,glucose):

    response = openai.Completion.create(
                model="text-davinci-002",
                prompt=f"Summarize the data in a report format and give me the food and lifestyle suggestions separately point wise for someone who has the following parameters and has been diagnosed with diabetes:\nage: {age}, \npregnancies: {pregnancies_num}\nskin thickness value: {skin_thickness}\nDiabetes Pedigree Function value: {diab_pedig}\ninsulin: {insulin}\nbp: {bloodpressure}\nbmi: {bmi}\nglucose: {glucose}\nsuggestions: ",

                temperature=0.65,
                max_tokens=1000,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
                )

    generated_text = response.choices[0].text.strip()

    return generated_text



#openai.api_key = os.getenv("OPENAI_API_KEY")
def get_suggestions1(age,sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal):

  response = openai.Completion.create(
  model="text-davinci-003",
  prompt=f"Summarize the data in the report format and give me the food and lifestyle suggestions separately for someone who has the following parameters and has been diagnosed with heart disease:\nage: {age},\ngender:{sex},\nChest Pain Types:{cp},\nResting Blood Pressure:{trestbps}, \nSerum Cholesterol in mg/dl: {chol},\nFasting Blood Sugar: {fbs},\nResting Electrocardiographic results: {restecg},\nMaximum Heart Rate achieved:{thalach},\nExercise Induced Angina:{exang},\nST depression induced by exercise:{oldpeak},\nSlope of the peak exercise ST segment:{slope},\nMajor vessels colored by flourosopy:{ca},\nthal: 0 = normal; 1 = fixed defect; 2 = reversable defect:{thal}\nsuggestions:\n",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

  generated_text = response.choices[0].text.strip()

  return generated_text